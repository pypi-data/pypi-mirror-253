import unittest

import ctrlxdatalayer
import ctrlxdatalayer.system
from ctrlxdatalayer.client import Result
from ctrlxdatalayer.variant import Variant
from ctrlxdatalayer.bulk import BulkReadRequest, BulkWriteRequest, BulkCreateRequest
from tests.test_integration_client import TestClientBase
from tests.test_utils import client_timeout, is_integration_test, root_node_alldata_provider

# port 443 is needed
_timeout = client_timeout()

# export INTEGRATION=1
# unset INTEGRATION

b = is_integration_test()


@unittest.skipIf(is_integration_test() == False, "no integration test")
class TestBulk(TestClientBase):
    """ TestBulk """

    def test_is_connected(self):
        """ test_is_connected """
        print("test_is_connected")
        self.client.set_timeout(
            ctrlxdatalayer.client.TimeoutSetting.PING, _timeout)
        b = self.client.is_connected()
        self.assertTrue(b)

    def test_read_sync(self):
        """ test_read_sync """
        print("test_read_sync")
        with Variant() as v:
            with self.client.create_bulk() as bulk:
                self.assertIsNotNone(bulk)
                r = bulk.read([BulkReadRequest("/framework/metrics/system/cpu-utilisation-percent"),
                              BulkReadRequest("/diagnosis/cfg/realtime/numbers", v)])
                print(f"read result {Result(r)}")
                self.assertTrue(r == Result.OK)
                self.assertEqual(len(bulk.get_response()), 2)
                self.assertTrue(len(bulk.get_response()[0].get_address()) != 0)
                self.assertEqual(bulk.get_response()[
                                 0].get_result(), Result.OK)
                self.assertEqual(bulk.get_response()[
                                 1].get_result(), Result.OK)

    def test_browse_sync(self):
        """ test_browse_sync """
        print("test_browse_sync")
        with self.client.create_bulk() as bulk:
            self.assertIsNotNone(bulk)
            r = bulk.browse(["/framework/metrics/system/",
                            "/diagnosis/cfg/realtime/"])
            print(f"browse result {Result(r)}")
            self.assertTrue(r == Result.OK)
            self.assertEqual(len(bulk.get_response()), 2)
            self.assertTrue(len(bulk.get_response()[0].get_address()) != 0)
            self.assertEqual(bulk.get_response()[
                0].get_result(), Result.OK)
            self.assertEqual(bulk.get_response()[
                1].get_result(), Result.OK)

    def test_write_sync(self):
        """ test_write_sync """
        print("test_write_sync")
        with Variant() as v:
            v.set_bool8(True)
            with self.client.create_bulk() as bulk:
                self.assertIsNotNone(bulk)
                r = bulk.write(
                    [BulkWriteRequest("/diagnosis/cfg/realtime/numbers", v)])
                self.assertTrue(r == Result.OK)
                self.assertEqual(len(bulk.get_response()), 1)
                self.assertTrue(len(bulk.get_response()[0].get_address()) != 0)
                self.assertEqual(bulk.get_response()[
                    0].get_result(), Result.OK)

    def test_metadata_sync(self):
        """ test_metadata_sync """
        print("test_metadata_sync")
        with self.client.create_bulk() as bulk:
            self.assertIsNotNone(bulk)
            r = bulk.metadata(
                ["/framework/metrics/system/cpu-utilisation-percent", "/diagnosis/cfg/realtime/numbers"])
            print(f"browse result {Result(r)}")
            self.assertTrue(r == Result.OK)
            self.assertEqual(len(bulk.get_response()), 2)
            self.assertTrue(len(bulk.get_response()[0].get_address()) != 0)
            self.assertEqual(bulk.get_response()[
                0].get_result(), Result.OK)
            self.assertEqual(bulk.get_response()[
                1].get_result(), Result.OK)

    @unittest.skipIf(is_integration_test() == False or root_node_alldata_provider() == "", "no integration test")
    def test_create_delete_sync(self):
        """ test_create_delete_sync """
        print("test_create_delete_sync")
        with self.client.create_bulk() as bulk:
            self.assertIsNotNone(bulk)
            r = bulk.create(
                [BulkCreateRequest(root_node_alldata_provider() + "/dynamic/_py/")])
            self.assertTrue(r == Result.OK)
            self.assertEqual(len(bulk.get_response()), 1)
            self.assertTrue(len(bulk.get_response()[0].get_address()) != 0)
            self.assertEqual(bulk.get_response()[
                0].get_result(), Result.OK)

            r = bulk.delete([root_node_alldata_provider() + "/dynamic/_py/"])
            self.assertTrue(r == Result.OK)
            self.assertEqual(len(bulk.get_response()), 1)
            self.assertTrue(len(bulk.get_response()[0].get_address()) != 0)
            self.assertEqual(bulk.get_response()[
                0].get_result(), Result.OK)


if __name__ == '__main__':
    unittest.main()
