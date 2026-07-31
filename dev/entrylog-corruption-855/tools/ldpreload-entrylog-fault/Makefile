CC ?= gcc
CFLAGS ?= -O2 -g
CFLAGS += -Wall -Wextra -fPIC
LDFLAGS += -shared -ldl -pthread

TARGET := libbk_entrylog_fault.so
SRC := entrylog_fault.c

.PHONY: all clean

all: $(TARGET)

$(TARGET): $(SRC)
	$(CC) $(CFLAGS) -o $@ $< $(LDFLAGS)

clean:
	rm -f $(TARGET)
