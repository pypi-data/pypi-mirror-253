import threading
import unittest
import typing
from ctrlxdatalayer.bulk import Response, BulkReadRequest, BulkWriteRequest, BulkCreateRequest
import ctrlxdatalayer
import ctrlxdatalayer.system
from ctrlxdatalayer.client import Result
from ctrlxdatalayer.variant import Variant
from tests.test_integration_client import TestClientBase
from tests.test_utils import client_timeout, is_integration_test, root_node_alldata_provider

# port 443 is needed
_timeout = client_timeout()

# export INTEGRATION=1
# unset INTEGRATION

b = is_integration_test()


@unittest.skipIf(is_integration_test() == False, "no integration test")
class TestAsyncBulk(TestClientBase):
    """ TestAsyncBulk """

    def __init__(self, *args, **kwargs):  # Accept all unrecognized args for delegation
        """ __init__ """
        # Delegate to parent initializer
        super().__init__(*args, **kwargs)
        self.ev = threading.Event()

    def wait(self):
        """ wait """
        self.ev.wait(10)

    def setUp(self):
        """ setUp """
        self.ev.clear()

    def test_is_connected(self):
        """ test_is_connected """
        print("test_is_connected")
        self.client.set_timeout(
            ctrlxdatalayer.client.TimeoutSetting.PING, _timeout)
        b = self.client.is_connected()
        self.assertTrue(b)

    def test_read_async(self):
        """ test_read_async """
        print("test_read_async")

        def cb(resps: typing.List[Response], userdata: ctrlxdatalayer.clib.userData_c_void_p):
            self.assertTrue(len(resps) == 1)
            self.ev.set()
            print("async test_read_async")

        with self.client.create_bulk() as bulk:
            self.assertIsNotNone(bulk)
            r = bulk.read(
                [BulkReadRequest("/framework/metrics/system/cpu-utilisation-percent")], cb)
            print(f"read result {Result(r)}")
            self.assertTrue(r == Result.OK)
            self.wait()
            self.assertTrue(self.ev.is_set())
            self.assertTrue(
                len(bulk.get_response()) == 1)
            r = bulk.get_response()[0].get_result()
            self.assertEqual(r, Result.OK)

    def test_browse_async(self):
        """ test_browse_async """
        print("test_browse_async")

        def cb(resps: typing.List[Response], userdata: ctrlxdatalayer.clib.userData_c_void_p):
            self.assertTrue(len(resps) == 1)
            self.ev.set()
            print("async test_browse_async")

        with self.client.create_bulk() as bulk:
            self.assertIsNotNone(bulk)
            r = bulk.browse(["/framework/metrics/system/"], cb)
            print(f"browse result {Result(r)}")
            self.assertTrue(r == Result.OK)
            self.wait()
            self.assertTrue(self.ev.is_set())
            self.assertTrue(
                len(bulk.get_response()) == 1)
            r = bulk.get_response()[0].get_result()
            self.assertEqual(r, Result.OK)

    def test_metadata_async(self):
        """ test_metadata_async """
        print("test_metadata_async")

        def cb(resps: typing.List[Response], userdata: ctrlxdatalayer.clib.userData_c_void_p):
            self.assertTrue(len(resps) == 1)
            self.ev.set()
            print("async test_metadata_async")

        with self.client.create_bulk() as bulk:
            self.assertIsNotNone(bulk)
            r = bulk.metadata(
                ["/framework/metrics/system/cpu-utilisation-percent"], cb)
            print(f"metadata result {Result(r)}")
            self.assertTrue(r == Result.OK)
            self.wait()
            self.assertTrue(self.ev.is_set())
            self.assertTrue(
                len(bulk.get_response()) == 1)
            r = bulk.get_response()[0].get_result()
            self.assertEqual(r, Result.OK)

    def test_write_async(self):
        """ test_write_async """
        print("test_write_async")

        def cb(resps: typing.List[Response], userdata: ctrlxdatalayer.clib.userData_c_void_p):
            self.assertTrue(len(resps) == 1)
            self.ev.set()
            print("async test_write_async")

        with Variant() as v:
            v.set_bool8(True)
            with self.client.create_bulk() as bulk:
                self.assertIsNotNone(bulk)
                r = bulk.write(
                    [BulkWriteRequest("/diagnosis/cfg/realtime/numbers", v)], cb)
                print(f"write result {Result(r)}")
                self.assertTrue(r == Result.OK)
                self.wait()
                self.assertTrue(self.ev.is_set())
                self.assertTrue(
                    len(bulk.get_response()) == 1)
                r = bulk.get_response()[0].get_result()
                self.assertEqual(r, Result.OK)

    @unittest.skipIf(is_integration_test() == False or root_node_alldata_provider() == "", "no integration test")
    def test_create_delete_async(self):
        """ test_create_delete_async """
        print("test_create_delete_async")

        def cb(resps: typing.List[Response], userdata: ctrlxdatalayer.clib.userData_c_void_p):
            self.assertTrue(len(resps) == 1)
            self.ev.set()
            print("async test_create_delete_async")

        with self.client.create_bulk() as bulk:
            self.assertIsNotNone(bulk)
            r = bulk.create(
                [BulkCreateRequest(root_node_alldata_provider() + "/dynamic/_py/")], cb)
            print(f"create result {Result(r)}")
            self.assertTrue(r == Result.OK)
            self.wait()
            self.assertTrue(self.ev.is_set())
            self.assertTrue(
                len(bulk.get_response()) == 1)
            r = bulk.get_response()[0].get_result()
            self.assertEqual(r, Result.OK)

            self.setUp()
            r = bulk.delete(
                [root_node_alldata_provider() + "/dynamic/_py/"], cb)
            print(f"delete result {Result(r)}")
            self.assertTrue(r == Result.OK)
            self.wait()
            self.assertTrue(self.ev.is_set())
            self.assertTrue(
                len(bulk.get_response()) == 1)
            r = bulk.get_response()[0].get_result()
            self.assertEqual(r, Result.OK)


if __name__ == '__main__':
    unittest.main()
