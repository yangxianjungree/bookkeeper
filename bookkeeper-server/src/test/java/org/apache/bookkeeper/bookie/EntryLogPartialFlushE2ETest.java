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
    private static final int WRITE_BUFFER_BYTES = 64 * 1024;
    private static final int ENTRY_PAYLOAD_BYTES = 512;
    private static final byte[] PASSWD = new byte[0];

    public EntryLogPartialFlushE2ETest() {
        super(3, 180);
        baseConf.setLedgerStorageClass(DbLedgerStorage.class.getName());
        baseConf.setProperty(DbLedgerStorage.DIRECT_IO_ENTRYLOGGER, false);
        baseConf.setEntryLogPerLedgerEnabled(false);
        baseConf.setWriteBufferBytes(WRITE_BUFFER_BYTES);
        baseConf.setReadBufferBytes(WRITE_BUFFER_BYTES);
        baseConf.setFlushInterval(600000);
        baseConf.setFlushIntervalInBytes(0);
        baseConf.setEntryLogSizeLimit(128 * 1024L);
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

        LedgerHandle lh = bkc.createLedger(3, 3, 2, DigestType.CRC32, PASSWD);

        for (int i = 0; i < 200; i++) {
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
        for (int i = 200; i < 420; i++) {
            long entryId = lh.addEntry(payload(i));
            if (i == 300) {
                candidateEntryId = entryId;
            }
        }

        targetBookie.getLedgerStorage().flush();

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

    private static byte[] payload(long entryId) {
        byte[] payload = new byte[ENTRY_PAYLOAD_BYTES];
        Arrays.fill(payload, (byte) 'x');
        byte[] marker = ("entry-" + entryId).getBytes(StandardCharsets.UTF_8);
        System.arraycopy(marker, 0, payload, 0, marker.length);
        return payload;
    }
}
