#!/usr/bin/env bash

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck source=common.sh
. "${SCRIPT_DIR}/common.sh"

detect_java

if [[ "${RESET_RUNTIME:-0}" == "1" ]]; then
  rm -rf "${RUNTIME_DIR}"
fi

mkdir -p "${RUNTIME_DIR}/downloads" "${CONF_DIR}" "${DATA_DIR}" "${LOG_DIR}" "${PIDS_DIR}" "${REPORT_DIR}"

if [[ ! -f "${PULSAR_ARCHIVE}" && -f "${PULSAR_ARCHIVE_SEED}" ]]; then
  cp "${PULSAR_ARCHIVE_SEED}" "${PULSAR_ARCHIVE}"
fi

if [[ ! -f "${PULSAR_SHA512}" && -f "${PULSAR_SHA512_SEED}" ]]; then
  cp "${PULSAR_SHA512_SEED}" "${PULSAR_SHA512}"
fi

if [[ ! -f "${PULSAR_ARCHIVE}" ]]; then
  curl -L --retry 3 --retry-delay 5 -C - -o "${PULSAR_ARCHIVE}" "${PULSAR_URL}"
fi

if [[ ! -f "${PULSAR_SHA512}" ]]; then
  curl -L --retry 3 --retry-delay 5 -o "${PULSAR_SHA512}" "${PULSAR_SHA512_URL}"
fi

(
  cd "$(dirname "${PULSAR_ARCHIVE}")"
  sha512sum -c "$(basename "${PULSAR_SHA512}")"
)

if [[ ! -x "${PULSAR_HOME}/bin/pulsar" ]]; then
  tar -xzf "${PULSAR_ARCHIVE}" -C "${RUNTIME_DIR}"
fi

if [[ ! -f "${BK_ARCHIVE}" ]]; then
  if [[ ! -f "${BK_DIST_TARBALL}" ]]; then
    echo "Missing BookKeeper ${BK_VERSION} distribution: ${BK_DIST_TARBALL}" >&2
    exit 1
  fi
  cp "${BK_DIST_TARBALL}" "${BK_ARCHIVE}"
fi

if [[ ! -x "${BK_HOME}/bin/bookkeeper" ]]; then
  mkdir -p "${RUNTIME_DIR}/bookkeeper"
  tar -xzf "${BK_ARCHIVE}" -C "${RUNTIME_DIR}/bookkeeper"
fi

bk_server_jar="${BK_HOME}/lib/org.apache.bookkeeper-bookkeeper-server-${BK_VERSION}.jar"
if [[ ! -f "${bk_server_jar}" ]]; then
  echo "Missing expected BookKeeper server jar: ${bk_server_jar}" >&2
  exit 1
fi

jar_cmd="${JAVA_HOME:-}/bin/jar"
if [[ ! -x "${jar_cmd}" ]]; then
  jar_cmd="$(command -v jar || true)"
fi
if [[ -z "${jar_cmd}" ]]; then
  echo "Cannot find jar command to inspect ${bk_server_jar}" >&2
  exit 1
fi

failpoint_class='org/apache/bookkeeper/bookie/DefaultEntryLogger$BufferedLogChannel$PartialFlushFault.class'
if ! "${jar_cmd}" tf "${bk_server_jar}" | grep -Fxq "${failpoint_class}"; then
  echo "BookKeeper ${BK_VERSION} jar does not contain failpoint class: ${failpoint_class}" >&2
  exit 1
fi

cp "${PULSAR_HOME}/conf/zookeeper.conf" "${CONF_DIR}/zookeeper.conf"
cat >> "${CONF_DIR}/zookeeper.conf" <<EOF

# entrylog partial flush 4.16.7 bookie harness overrides
dataDir=${DATA_DIR}/zk
clientPort=2181
admin.enableServer=false
metricsProvider.httpPort=7000
forceSync=no
EOF

generate_bookie_conf() {
  local name="$1"
  local port="$2"
  local metrics_port="$3"
  mkdir -p "${DATA_DIR}/${name}/journal" "${DATA_DIR}/${name}/ledgers" "${DATA_DIR}/${name}/rocksdb" "${LOG_DIR}/${name}"
  cat > "${CONF_DIR}/${name}.conf" <<EOF
# Minimal BookKeeper ${BK_VERSION} bookie config for the entrylog partial flush harness.
bookiePort=${port}
advertisedAddress=127.0.0.1
allowLoopback=true
journalDirectories=${DATA_DIR}/${name}/journal
ledgerDirectories=${DATA_DIR}/${name}/ledgers
indexDirectories=${DATA_DIR}/${name}/ledgers
metadataServiceUri=zk+hierarchical://127.0.0.1:2181/ledgers
zkServers=127.0.0.1:2181
ledgerStorageClass=org.apache.bookkeeper.bookie.storage.ldb.DbLedgerStorage
dbStorage_directIOEntryLogger=false
dbStorage_rocksDBPath=${DATA_DIR}/${name}/rocksdb
entryLogPerLedgerEnabled=false
entryLogFilePreallocationEnabled=false
writeBufferSizeBytes=65536
readBufferSizeBytes=65536
flushInterval=1000
flushEntrylogBytes=0
logSizeLimit=131072
gcWaitTime=600000
minorCompactionThreshold=0
majorCompactionThreshold=0
minorCompactionInterval=0
majorCompactionInterval=0
entryLocationCompactionInterval=0
numAddWorkerThreads=4
statsProviderClass=org.apache.bookkeeper.stats.NullStatsProvider
prometheusStatsHttpPort=${metrics_port}
httpServerEnabled=false
minUsableSizeForEntryLogCreation=0
minUsableSizeForHighPriorityWrites=0
entryLocationRocksdbConf=${BK_HOME}/conf/entry_location_rocksdb.conf
ledgerMetadataRocksdbConf=${BK_HOME}/conf/ledger_metadata_rocksdb.conf
defaultRocksdbConf=${BK_HOME}/conf/default_rocksdb.conf
EOF
}

generate_bookie_conf bk1 3181 8001
generate_bookie_conf bk2 3182 8002
generate_bookie_conf bk3 3183 8003

mkdir -p "${LOG_DIR}/broker"
cp "${PULSAR_HOME}/conf/broker.conf" "${CONF_DIR}/broker.conf"
cat >> "${CONF_DIR}/broker.conf" <<EOF

# entrylog partial flush 4.16.7 bookie harness overrides
metadataStoreUrl=zk:127.0.0.1:2181
configurationMetadataStoreUrl=zk:127.0.0.1:2181
clusterName=test
advertisedAddress=127.0.0.1
brokerServicePort=6650
webServicePort=8080
bookkeeperMetadataServiceUri=zk+hierarchical://127.0.0.1:2181/ledgers
managedLedgerDefaultEnsembleSize=3
managedLedgerDefaultWriteQuorum=3
managedLedgerDefaultAckQuorum=2
functionsWorkerEnabled=false
webSocketServiceEnabled=false
brokerDeleteInactiveTopicsEnabled=false
transactionCoordinatorEnabled=false
systemTopicEnabled=false
numOrderedExecutorThreads=4
numIOThreads=2
numHttpServerThreads=8
bookkeeperClientNumWorkerThreads=2
bookkeeperClientNumIoThreads=2
EOF

mkdir -p "${DATA_DIR}/zk" "${LOG_DIR}/zk" "${LOG_DIR}/init" "${LOG_DIR}/client"

cat > "${RUNTIME_DIR}/versions.properties" <<EOF
pulsarVersion=${PULSAR_VERSION}
bookieVersion=${BK_VERSION}
bookieDistribution=${BK_ARCHIVE}
bookieServerJar=${bk_server_jar}
failpointClass=${failpoint_class}
EOF

echo "Prepared Pulsar ${PULSAR_VERSION} with external BookKeeper ${BK_VERSION} bookies under ${RUNTIME_DIR}"
echo "Verified failpoint class in ${bk_server_jar}"
