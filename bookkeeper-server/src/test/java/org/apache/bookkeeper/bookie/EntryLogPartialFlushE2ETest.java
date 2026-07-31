/*
 *
 * Licensed to the Apache Software Foundation (ASF) under one
 * or more contributor license agreements.  See the NOTICE file
 * distributed with this work for additional information
 * regarding copyright ownership.  The ASF licenses this file
 * to you under the Apache License, Version 2.0 (the
 * "License"); you may not use this file except in compliance
 * with the License.  You may obtain a copy of the License at
 *
 *   http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing,
 * software distributed under the License is distributed on an
 * "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 * KIND, either express or implied.  See the License for the
 * specific language governing permissions and limitations
 * under the License.
 *
 */
package org.apache.bookkeeper.bookie;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertTrue;
import static org.junit.Assert.fail;

import io.netty.buffer.ByteBuf;
import io.netty.util.ReferenceCountUtil;
import java.io.File;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.StandardCopyOption;
import java.util.Arrays;
import org.apache.bookkeeper.bookie.storage.ldb.DbLedgerStorage;
import org.apache.bookkeeper.client.BookKeeper.DigestType;
import org.apache.bookkeeper.client.LedgerHandle;
import org.apache.bookkeeper.test.BookKeeperClusterTestCase;
import org.junit.After;
import org.junit.Test;

/**
 * End-to-end reproducer for a stale entrylog position after an injected entrylog flush failure.
 *
 * <p>This is intentionally a reproducer for the current bad state, not the desired fixed behavior.
 */
public class EntryLogPartialFlushE2ETest extends BookKeeperClusterTestCase {
    private static final byte[] PASSWD = new byte[0];
    private final int writeBufferBytes;
    private final int entryPayloadBytes;
    private final int initialEntries;
    private final int postFailureEntries;
    private final int candidateOffset;
    private final long entryLogSizeLimit;
    private final String runId;
    private final Path artifactsDir;

    public EntryLogPartialFlushE2ETest() {
        super(3, 180);
        this.writeBufferBytes = intProperty("bk.e2e.partialFlush.writeBufferBytes", 64 * 1024);
        this.entryPayloadBytes = intProperty("bk.e2e.partialFlush.entryPayloadBytes", 512);
        this.initialEntries = intProperty("bk.e2e.partialFlush.initialEntries", 200);
        this.postFailureEntries = intProperty("bk.e2e.partialFlush.postFailureEntries", 220);
        this.candidateOffset = intProperty("bk.e2e.partialFlush.candidateOffset", 100);
        this.entryLogSizeLimit = longProperty("bk.e2e.partialFlush.entryLogSizeLimit", 128 * 1024L);
        this.runId = System.getProperty("bk.e2e.partialFlush.runId", Long.toString(System.currentTimeMillis()));
        this.artifactsDir = Paths.get(System.getProperty("bk.e2e.partialFlush.artifactsDir",
                "target/entrylog-partial-flush-e2e"));

        baseConf.setLedgerStorageClass(DbLedgerStorage.class.getName());
        baseConf.setProperty(DbLedgerStorage.DIRECT_IO_ENTRYLOGGER, false);
        baseConf.setEntryLogPerLedgerEnabled(false);
        baseConf.setWriteBufferBytes(writeBufferBytes);
        baseConf.setReadBufferBytes(writeBufferBytes);
        baseConf.setFlushInterval(600000);
        baseConf.setFlushIntervalInBytes(0);
        baseConf.setEntryLogSizeLimit(entryLogSizeLimit);
        baseConf.setMinUsableSizeForEntryLogCreation(1);
        baseConf.setGcWaitTime(600000);
    }

    @After
    public void resetFault() {
        DefaultEntryLogger.BufferedLogChannel.PartialFlushFault.reset();
    }

    @Test
    public void testEntryLogWriterReusesStalePositionAfterInjectedFlushFailure() throws Exception {
        Bookie targetBookie = serverByIndex(0).getBookie();
        Bookie healthyBookie = serverByIndex(1).getBookie();
        File targetLedgerDir = confByIndex(0).getLedgerDirs()[0];
        File healthyLedgerDir = confByIndex(1).getLedgerDirs()[0];

        LedgerHandle lh = bkc.createLedger(3, 3, 2, DigestType.CRC32, PASSWD);

        for (int i = 0; i < initialEntries; i++) {
            lh.addEntry(payload(i));
        }

        DefaultEntryLogger.BufferedLogChannel.PartialFlushFault
                .enableOnceForLogPathContaining(targetLedgerDir.getAbsolutePath());

        try {
            targetBookie.getLedgerStorage().flush();
            fail("The injected entrylog flush failure should have failed the first target-bookie flush");
        } catch (Exception expected) {
            assertTrue("Unexpected exception: " + expected,
                    expected.getMessage().contains("Injected entrylog partial flush failure"));
        }

        assertTrue(DefaultEntryLogger.BufferedLogChannel.PartialFlushFault.hasFired());
        long delta = DefaultEntryLogger.BufferedLogChannel.PartialFlushFault.getInjectedPhysicalPosition()
                - DefaultEntryLogger.BufferedLogChannel.PartialFlushFault.getInjectedLogicalPosition();
        assertTrue("The injected failure should make physical position advance beyond logical position: " + delta,
                delta > 0);

        long candidateEntryId = -1;
        long candidatePayloadIndex = initialEntries + candidateOffset;
        for (int i = initialEntries; i < initialEntries + postFailureEntries; i++) {
            long entryId = lh.addEntry(payload(i));
            if (i == candidatePayloadIndex) {
                candidateEntryId = entryId;
            }
        }
        assertTrue("candidateOffset must point to a post-failure entry", candidateEntryId >= 0);

        targetBookie.getLedgerStorage().flush();
        healthyBookie.getLedgerStorage().flush();
        long targetIndexedLocation = ((DbLedgerStorage) targetBookie.getLedgerStorage()).getLocation(
                lh.getId(), candidateEntryId);
        long healthyIndexedLocation = ((DbLedgerStorage) healthyBookie.getLedgerStorage()).getLocation(
                lh.getId(), candidateEntryId);
        writeArtifacts(lh.getId(), candidateEntryId, targetIndexedLocation, healthyIndexedLocation,
                targetLedgerDir, healthyLedgerDir);

        ByteBuf healthyEntry = healthyBookie.readEntry(lh.getId(), candidateEntryId);
        try {
            assertEquals(lh.getId(), healthyEntry.getLong(0));
            assertEquals(candidateEntryId, healthyEntry.getLong(8));
        } finally {
            ReferenceCountUtil.release(healthyEntry);
        }

        try {
            ByteBuf targetEntry = targetBookie.readEntry(lh.getId(), candidateEntryId);
            try {
                if (targetEntry.getLong(0) == lh.getId() && targetEntry.getLong(8) == candidateEntryId) {
                    fail("Target bookie unexpectedly read the post-failure entry from a correct location");
                }
            } finally {
                ReferenceCountUtil.release(targetEntry);
            }
        } catch (Exception expected) {
            // Expected on the pre-fix code: the target bookie persisted a stale location for this entry.
        }
    }

    private void writeArtifacts(long ledgerId, long candidateEntryId, long targetIndexedLocation,
            long healthyIndexedLocation, File targetLedgerDir, File healthyLedgerDir) throws Exception {
        Files.createDirectories(artifactsDir);

        File injectedLogFile = DefaultEntryLogger.BufferedLogChannel.PartialFlushFault.getInjectedLogFile();
        long targetIndexedLogId = targetIndexedLocation >>> 32L;
        long targetIndexedPosition = targetIndexedLocation & 0xffffffffL;
        long healthyIndexedLogId = healthyIndexedLocation >>> 32L;
        long healthyIndexedPosition = healthyIndexedLocation & 0xffffffffL;
        Path copiedTargetLog = copyEntryLog(logFile(targetLedgerDir, targetIndexedLogId), "target");
        Path copiedHealthyLog = copyEntryLog(logFile(healthyLedgerDir, healthyIndexedLogId), "healthy");
        String copiedTargetLogs = copyAllEntryLogs(targetLedgerDir, "target");
        String copiedHealthyLogs = copyAllEntryLogs(healthyLedgerDir, "healthy");

        long injectedLogicalPosition = DefaultEntryLogger.BufferedLogChannel.PartialFlushFault
                .getInjectedLogicalPosition();
        long injectedPhysicalPosition = DefaultEntryLogger.BufferedLogChannel.PartialFlushFault
                .getInjectedPhysicalPosition();
        StringBuilder summary = new StringBuilder();
        summary.append("runId=").append(runId).append('\n');
        summary.append("writeBufferBytes=").append(writeBufferBytes).append('\n');
        summary.append("entryPayloadBytes=").append(entryPayloadBytes).append('\n');
        summary.append("initialEntries=").append(initialEntries).append('\n');
        summary.append("postFailureEntries=").append(postFailureEntries).append('\n');
        summary.append("candidateOffset=").append(candidateOffset).append('\n');
        summary.append("entryLogSizeLimit=").append(entryLogSizeLimit).append('\n');
        summary.append("ledgerId=").append(ledgerId).append('\n');
        summary.append("candidateEntryId=").append(candidateEntryId).append('\n');
        summary.append("indexedLocation=").append(targetIndexedLocation).append('\n');
        summary.append("indexedLogId=").append(targetIndexedLogId).append('\n');
        summary.append("indexedPosition=").append(targetIndexedPosition).append('\n');
        summary.append("targetIndexedLocation=").append(targetIndexedLocation).append('\n');
        summary.append("targetIndexedLogId=").append(targetIndexedLogId).append('\n');
        summary.append("targetIndexedPosition=").append(targetIndexedPosition).append('\n');
        summary.append("healthyIndexedLocation=").append(healthyIndexedLocation).append('\n');
        summary.append("healthyIndexedLogId=").append(healthyIndexedLogId).append('\n');
        summary.append("healthyIndexedPosition=").append(healthyIndexedPosition).append('\n');
        summary.append("injectedLogFile=").append(injectedLogFile.getAbsolutePath()).append('\n');
        summary.append("targetLedgerDir=").append(targetLedgerDir.getAbsolutePath()).append('\n');
        summary.append("healthyLedgerDir=").append(healthyLedgerDir.getAbsolutePath()).append('\n');
        summary.append("copiedLogFile=").append(copiedTargetLog.toAbsolutePath()).append('\n');
        summary.append("copiedTargetLogFile=").append(copiedTargetLog.toAbsolutePath()).append('\n');
        summary.append("copiedHealthyLogFile=").append(copiedHealthyLog.toAbsolutePath()).append('\n');
        summary.append("copiedTargetLogs=").append(copiedTargetLogs).append('\n');
        summary.append("copiedHealthyLogs=").append(copiedHealthyLogs).append('\n');
        summary.append("injectedLogicalPosition=").append(injectedLogicalPosition).append('\n');
        summary.append("injectedPhysicalPosition=").append(injectedPhysicalPosition).append('\n');
        summary.append("injectedDelta=").append(injectedPhysicalPosition - injectedLogicalPosition).append('\n');
        summary.append("injectedBytes=").append(DefaultEntryLogger.BufferedLogChannel.PartialFlushFault
                .getInjectedBytes()).append('\n');
        Files.write(artifactsDir.resolve(runId + ".properties"), summary.toString().getBytes(StandardCharsets.UTF_8));
    }

    private Path copyEntryLog(File sourceLog, String role) throws Exception {
        Path copiedLog = artifactsDir.resolve(runId + "-" + role + "-" + sourceLog.getName());
        Files.copy(sourceLog.toPath(), copiedLog, StandardCopyOption.REPLACE_EXISTING);
        return copiedLog;
    }

    private String copyAllEntryLogs(File ledgerDir, String role) throws Exception {
        File currentDir = new File(ledgerDir, "current");
        File[] logs = currentDir.listFiles((dir, name) -> name.endsWith(".log"));
        if (logs == null) {
            return "";
        }
        Arrays.sort(logs);
        StringBuilder copied = new StringBuilder();
        for (File log : logs) {
            Path copiedLog = copyEntryLog(log, role);
            if (copied.length() > 0) {
                copied.append(',');
            }
            copied.append(copiedLog.toAbsolutePath());
        }
        return copied.toString();
    }

    private static File logFile(File ledgerDir, long logId) {
        return new File(new File(ledgerDir, "current"), Long.toHexString(logId) + ".log");
    }

    private byte[] payload(long entryId) {
        byte[] payload = new byte[entryPayloadBytes];
        Arrays.fill(payload, (byte) 'x');
        byte[] marker = ("entry-" + entryId).getBytes(StandardCharsets.UTF_8);
        System.arraycopy(marker, 0, payload, 0, Math.min(marker.length, payload.length));
        return payload;
    }

    private static int intProperty(String name, int defaultValue) {
        return Integer.parseInt(System.getProperty(name, Integer.toString(defaultValue)));
    }

    private static long longProperty(String name, long defaultValue) {
        return Long.parseLong(System.getProperty(name, Long.toString(defaultValue)));
    }
}
