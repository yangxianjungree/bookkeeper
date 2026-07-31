#define _GNU_SOURCE
#define _LARGEFILE64_SOURCE

#include <dlfcn.h>
#include <errno.h>
#include <fcntl.h>
#include <limits.h>
#include <pthread.h>
#include <stdbool.h>
#include <stdarg.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>
#include <sys/uio.h>
#include <unistd.h>

typedef ssize_t (*write_fn)(int, const void *, size_t);
typedef ssize_t (*pwrite_fn)(int, const void *, size_t, off_t);
typedef ssize_t (*pwrite64_fn)(int, const void *, size_t, off64_t);
typedef ssize_t (*writev_fn)(int, const struct iovec *, int);

static write_fn real_write;
static pwrite_fn real_pwrite;
static pwrite64_fn real_pwrite64;
static writev_fn real_writev;

static pthread_once_t init_once = PTHREAD_ONCE_INIT;
static pthread_mutex_t state_lock = PTHREAD_MUTEX_INITIALIZER;
static __thread int in_hook;

static int enabled;
static int dry_run;
static long min_write_bytes = 32768;
static long after_matches = 1;
static long max_triggers = 1;
static long matches_seen;
static long triggers_seen;
static int log_fd = -1;
static char path_contains[PATH_MAX] = "/current/";
static char file_suffix[64] = ".log";

static int env_flag(const char *name, int default_value) {
    const char *value = getenv(name);
    if (value == NULL || value[0] == '\0') {
        return default_value;
    }
    return strcmp(value, "1") == 0
            || strcasecmp(value, "true") == 0
            || strcasecmp(value, "yes") == 0
            || strcasecmp(value, "on") == 0;
}

static long env_long(const char *name, long default_value) {
    const char *value = getenv(name);
    char *end = NULL;
    long parsed;

    if (value == NULL || value[0] == '\0') {
        return default_value;
    }

    errno = 0;
    parsed = strtol(value, &end, 10);
    if (errno != 0 || end == value || parsed < 0) {
        return default_value;
    }
    return parsed;
}

static void copy_env_string(const char *name, char *dest, size_t dest_size) {
    const char *value = getenv(name);
    if (value == NULL || value[0] == '\0') {
        return;
    }
    snprintf(dest, dest_size, "%s", value);
}

static void load_real_symbols(void) {
    real_write = (write_fn) dlsym(RTLD_NEXT, "write");
    real_pwrite = (pwrite_fn) dlsym(RTLD_NEXT, "pwrite");
    real_pwrite64 = (pwrite64_fn) dlsym(RTLD_NEXT, "pwrite64");
    real_writev = (writev_fn) dlsym(RTLD_NEXT, "writev");
}

static void fault_log(const char *format, ...) {
    char message[2048];
    va_list args;
    int len;

    if (real_write == NULL) {
        return;
    }

    va_start(args, format);
    len = vsnprintf(message, sizeof(message), format, args);
    va_end(args);

    if (len <= 0) {
        return;
    }
    if ((size_t) len >= sizeof(message)) {
        len = (int) sizeof(message) - 1;
        message[len] = '\0';
    }

    if (log_fd >= 0) {
        (void) real_write(log_fd, message, (size_t) len);
    } else {
        (void) real_write(STDERR_FILENO, message, (size_t) len);
    }
}

static void init_config(void) {
    const char *log_path;

    load_real_symbols();

    enabled = env_flag("BK_ENTRYLOG_FAULT_ENABLED", 0);
    dry_run = env_flag("BK_ENTRYLOG_FAULT_DRY_RUN", 0);
    min_write_bytes = env_long("BK_ENTRYLOG_FAULT_MIN_WRITE_BYTES", min_write_bytes);
    after_matches = env_long("BK_ENTRYLOG_FAULT_AFTER_MATCHES", after_matches);
    max_triggers = env_long("BK_ENTRYLOG_FAULT_MAX_TRIGGERS", max_triggers);
    copy_env_string("BK_ENTRYLOG_FAULT_PATH_CONTAINS", path_contains, sizeof(path_contains));
    copy_env_string("BK_ENTRYLOG_FAULT_FILE_SUFFIX", file_suffix, sizeof(file_suffix));

    log_path = getenv("BK_ENTRYLOG_FAULT_LOG");
    if (log_path != NULL && log_path[0] != '\0') {
        log_fd = open(log_path, O_CREAT | O_WRONLY | O_APPEND, 0644);
    }

    fault_log("bk-entrylog-fault: init enabled=%d dry_run=%d path_contains=%s suffix=%s "
              "min_write_bytes=%ld after_matches=%ld max_triggers=%ld\n",
              enabled, dry_run, path_contains, file_suffix, min_write_bytes, after_matches, max_triggers);
}

static bool ends_with(const char *value, const char *suffix) {
    size_t value_len;
    size_t suffix_len;

    if (suffix == NULL || suffix[0] == '\0') {
        return true;
    }
    value_len = strlen(value);
    suffix_len = strlen(suffix);
    return value_len >= suffix_len && strcmp(value + value_len - suffix_len, suffix) == 0;
}

static bool fd_path(int fd, char *path, size_t path_size) {
    char proc_path[64];
    ssize_t len;

    snprintf(proc_path, sizeof(proc_path), "/proc/self/fd/%d", fd);
    len = readlink(proc_path, path, path_size - 1);
    if (len < 0) {
        return false;
    }
    path[len] = '\0';
    return true;
}

static bool path_matches(const char *path) {
    if (strstr(path, path_contains) == NULL) {
        return false;
    }
    return ends_with(path, file_suffix);
}

static bool select_fault(const char *op, int fd, size_t count, char *path, size_t path_size,
                         long long offset, long *match_number) {
    bool selected = false;

    *match_number = 0;
    if (!enabled || count < (size_t) min_write_bytes) {
        return false;
    }
    if (!fd_path(fd, path, path_size) || !path_matches(path)) {
        return false;
    }

    pthread_mutex_lock(&state_lock);
    matches_seen++;
    *match_number = matches_seen;
    if (matches_seen >= after_matches && triggers_seen < max_triggers) {
        selected = true;
    }
    pthread_mutex_unlock(&state_lock);

    fault_log("bk-entrylog-fault: matched op=%s fd=%d path=%s count=%zu offset=%lld match=%ld selected=%d\n",
              op, fd, path, count, offset, *match_number, selected ? 1 : 0);
    return selected;
}

static bool record_trigger_after_success(const char *op, int fd, const char *path, size_t count,
                                         long long offset, ssize_t real_rc, long match_number) {
    bool trigger = false;

    if (real_rc != (ssize_t) count) {
        fault_log("bk-entrylog-fault: not-triggering op=%s fd=%d path=%s count=%zu offset=%lld "
                  "real_rc=%zd match=%ld reason=real-write-not-full\n",
                  op, fd, path, count, offset, real_rc, match_number);
        return false;
    }

    pthread_mutex_lock(&state_lock);
    if (triggers_seen < max_triggers) {
        triggers_seen++;
        trigger = true;
    }
    pthread_mutex_unlock(&state_lock);

    if (trigger) {
        fault_log("bk-entrylog-fault: %s op=%s fd=%d path=%s count=%zu offset=%lld "
                  "real_rc=%zd match=%ld trigger=%ld errno=EIO\n",
                  dry_run ? "dry-run-would-trigger" : "triggering",
                  op, fd, path, count, offset, real_rc, match_number, triggers_seen);
    }
    return trigger && !dry_run;
}

ssize_t write(int fd, const void *buf, size_t count) {
    char path[PATH_MAX] = "";
    long match_number = 0;
    bool selected;
    ssize_t rc;

    pthread_once(&init_once, init_config);
    if (in_hook || real_write == NULL) {
        return real_write == NULL ? -1 : real_write(fd, buf, count);
    }

    in_hook = 1;
    selected = select_fault("write", fd, count, path, sizeof(path), -1, &match_number);
    rc = real_write(fd, buf, count);
    if (selected && record_trigger_after_success("write", fd, path, count, -1, rc, match_number)) {
        errno = EIO;
        in_hook = 0;
        return -1;
    }
    in_hook = 0;
    return rc;
}

ssize_t pwrite(int fd, const void *buf, size_t count, off_t offset) {
    char path[PATH_MAX] = "";
    long match_number = 0;
    bool selected;
    ssize_t rc;

    pthread_once(&init_once, init_config);
    if (in_hook || real_pwrite == NULL) {
        return real_pwrite == NULL ? -1 : real_pwrite(fd, buf, count, offset);
    }

    in_hook = 1;
    selected = select_fault("pwrite", fd, count, path, sizeof(path), (long long) offset, &match_number);
    rc = real_pwrite(fd, buf, count, offset);
    if (selected && record_trigger_after_success("pwrite", fd, path, count, (long long) offset, rc, match_number)) {
        errno = EIO;
        in_hook = 0;
        return -1;
    }
    in_hook = 0;
    return rc;
}

ssize_t pwrite64(int fd, const void *buf, size_t count, off64_t offset) {
    char path[PATH_MAX] = "";
    long match_number = 0;
    bool selected;
    ssize_t rc;

    pthread_once(&init_once, init_config);
    if (in_hook || real_pwrite64 == NULL) {
        return real_pwrite64 == NULL ? -1 : real_pwrite64(fd, buf, count, offset);
    }

    in_hook = 1;
    selected = select_fault("pwrite64", fd, count, path, sizeof(path), (long long) offset, &match_number);
    rc = real_pwrite64(fd, buf, count, offset);
    if (selected && record_trigger_after_success("pwrite64", fd, path, count, (long long) offset, rc, match_number)) {
        errno = EIO;
        in_hook = 0;
        return -1;
    }
    in_hook = 0;
    return rc;
}

ssize_t writev(int fd, const struct iovec *iov, int iovcnt) {
    char path[PATH_MAX] = "";
    long match_number = 0;
    bool selected;
    ssize_t rc;
    size_t count = 0;
    int i;

    pthread_once(&init_once, init_config);
    if (in_hook || real_writev == NULL) {
        return real_writev == NULL ? -1 : real_writev(fd, iov, iovcnt);
    }

    for (i = 0; i < iovcnt; i++) {
        count += iov[i].iov_len;
    }

    in_hook = 1;
    selected = select_fault("writev", fd, count, path, sizeof(path), -1, &match_number);
    rc = real_writev(fd, iov, iovcnt);
    if (selected && record_trigger_after_success("writev", fd, path, count, -1, rc, match_number)) {
        errno = EIO;
        in_hook = 0;
        return -1;
    }
    in_hook = 0;
    return rc;
}
