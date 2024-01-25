import ctypes
import threading
import typing
import unittest

import ctrlxdatalayer
import ctrlxdatalayer.system
from ctrlxdatalayer.client import Result
from ctrlxdatalayer.variant import Variant, VariantType
from tests.test_utils import (client_connection, client_timeout,
                              is_integration_test, root_node_alldata_provider)

# port 443 is needed
_connectionClient = client_connection()
_timeout = client_timeout()

# export INTEGRATION=1
# unset INTEGRATION

b = is_integration_test()


@unittest.skipIf(is_integration_test() == False, "no integration test")
class TestClientBase(unittest.TestCase):
    """ TestClientBase """

    @classmethod
    def setUpClass(cls):
        """ setUpClass """
        print("Using ctrlX CORE as client: ", _connectionClient)
        cls.system = ctrlxdatalayer.system.System("")
        cls.system.start(False)
        cls.client = cls.system.factory().create_client(_connectionClient)
        bc = cls.client.is_connected()
        print("cls connect={}".format(bc))

    @classmethod
    def tearDownClass(cls):
        """ tearDownClass """
        print("tearDownClass")
        cls.client.close()
        cls.system.stop(True)
        cls.system.close()


@unittest.skipIf(is_integration_test() == False, "no integration test")
class TestClient(TestClientBase):
    """ TestClient """

    def test_is_connected(self):
        """ test_is_connected """
        print("test_is_connected")
        self.client.set_timeout(ctrlxdatalayer.client.TimeoutSetting.PING, _timeout)
        b = self.client.is_connected()
        self.assertTrue(b)

    def test_set_timeout(self):
        """ test_set_timeout """
        print("test_set_timeout")
        r = self.client.set_timeout(
            ctrlxdatalayer.client.TimeoutSetting.PING, _timeout)
        self.assertTrue(r == Result.OK)

    def test_ping_sync(self):
        """ test_ping_sync """
        print("test_ping_sync")
        b = self.client.is_connected()
        self.assertTrue(b)
        r = self.client.ping_sync()
        self.assertTrue(r == Result.OK)

    def test_get_auth_token(self):
        """ test_get_auth_token """
        print("test_get_auth_token")
        r = self.client.get_auth_token()
        self.assertIsNotNone(r)

    def test_set_auth_token(self):
        """ test_set_auth_token """
        print("test_set_auth_token")
        self.client.set_auth_token("streng geheim")
        r = self.client.get_auth_token()
        self.assertIsNotNone(r)

    def test_browse_sync(self):
        """ test_browse_sync """
        print("test_browse_sync")
        r, v = self.client.browse_sync("")
        self.assertTrue(r == Result.OK)
        self.assertIsNotNone(v)
        self.assertTrue(v.get_type() == VariantType.ARRAY_STRING)
        v.close()

    def test_read_sync(self):
        """ test_read_sync """
        print("test_read_sync")
        r, v = self.client.read_sync("/diagnosis/cfg/realtime/numbers")
        self.assertTrue(r == Result.OK)
        self.assertIsNotNone(v)
        self.assertTrue(v.get_type() == VariantType.BOOL8)
        v.close()

    def test_read_sync_args(self):
        """ test_read_sync """
        print("test_read_sync")
        with Variant() as v:
            r, v = self.client.read_sync_args(
                "/diagnosis/cfg/realtime/numbers", v)
            self.assertTrue(r == Result.OK)
            self.assertIsNotNone(v)
            self.assertTrue(v.get_type() == VariantType.BOOL8)

    def test_write_sync(self):
        """ test_write_sync """
        print("test_write_sync")
        v = Variant()
        v.set_bool8(True)
        r, v = self.client.write_sync("/diagnosis/cfg/realtime/numbers", v)
        self.assertTrue(r == Result.OK)
        self.assertIsNotNone(v)
        self.assertTrue(v.get_type() == VariantType.UNKNON)
        v.close()

    def test_metadata_sync(self):
        """ test_metadata_sync """
        print("test_metadata_sync")
        r, v = self.client.metadata_sync("/diagnosis/cfg/realtime/numbers")
        self.assertTrue(r == Result.OK)
        self.assertIsNotNone(v)
        self.assertTrue(v.get_type() == VariantType.FLATBUFFERS)
        v.close()


@unittest.skipIf(is_integration_test() == False, "no integration test")
class TestClientAsyn(TestClientBase):
    """ TestClientAsyn """

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

    def test_ping_async(self):
        """ test_ping_async """
        print("test ping_async")

        def cb(result: Result, data: typing.Optional[Variant], userdata: ctrlxdatalayer.clib.userData_c_void_p):
            """ cb """
            if data is None:
                print("Async callback in Python (no data): {}, userdata={} ".format(
                    result, ["no", userdata][userdata is not None]))  # ? : from C
            else:
                print("Async callback in Python: ", result)
            self.ev.set()

        r = self.client.ping_async(cb)
        self.assertTrue(r == Result.OK)
        self.wait()
        self.assertTrue(self.ev.is_set())

    def test_ping_async_user(self):
        """ test_ping_async_user """
        print("test ping_async")

        def cb(result: Result, data: typing.Optional[Variant], userdata: ctrlxdatalayer.clib.userData_c_void_p):
            """ cb """
            if data is None:
                print("Async callback in Python (no data): {}, userdata={} ".format(
                    result, ["", userdata][userdata is not None]))
            else:
                print("Async callback in Python: ", result)
            self.ev.set()

        r = self.client.ping_async(cb, 123)
        self.assertTrue(r == Result.OK)
        self.wait()
        self.assertTrue(self.ev.is_set())

    def test_write_async_user(self):
        """ test_write_async_user """
        print("test write_async")

        def cb(result: Result, data: typing.Optional[Variant], userdata: ctrlxdatalayer.clib.userData_c_void_p):
            """ cb """
            if data is None:
                print("Async callback in Python (no data): {}, userdata={} ".format(
                    result, ["", userdata][userdata is not None]))
            else:
                print("Async callback in Python: result={}, userdata={}".format(
                    result, ["", userdata][userdata is not None]))
            self.ev.set()

        with Variant() as v:
            v.set_bool8(True)
            r = self.client.write_async(
                "/diagnosis/cfg/realtime/numbers", v, cb, 321)
            self.assertTrue(r == Result.OK)
            self.wait()
            self.assertTrue(self.ev.is_set())

    def test_read_async_user(self):
        """ test_read_async_user """
        print("test_read_async_user")

        def cb(result: Result, data: typing.Optional[Variant], userdata: ctrlxdatalayer.clib.userData_c_void_p):
            """ cb """
            if data is None:
                print("Async callback in Python (no data): {}, userdata={} ".format(
                    result, ["", userdata][userdata is not None]))
            else:
                r, v = data.clone()
                print("Async callback in Python: result={}, userdata={}, data={}".format(
                    result, ["", userdata][userdata is not None], ["", v.get_string()][r == Result.OK]))
                v.close()
            self.ev.set()

        r = self.client.read_async(
            "/diagnosis/cfg/realtime/numbers", cb, 321)
        self.assertTrue(r == Result.OK)
        self.wait()
        self.assertTrue(self.ev.is_set())

    def test_read_async_args_user(self):
        """ test_read_async_args_user """
        print("test_read_async_args_user")

        def cb(result: Result, data: typing.Optional[Variant], userdata: ctrlxdatalayer.clib.userData_c_void_p):
            """ cb """
            if data is None:
                print("Async callback in Python (no data): {}, userdata={} ".format(
                    result, ["", userdata][userdata is not None]))
            else:
                r, v = data.clone()
                print("Async callback in Python: result={}, userdata={}, data={}".format(
                    result, ["", userdata][userdata is not None], ["", v.get_string()][r == Result.OK]))
                v.close()
            self.ev.set()
        with Variant() as args:
            r = self.client.read_async_args(
                "/diagnosis/cfg/realtime/numbers", args, cb, 654)
            self.assertTrue(r == Result.OK)
            self.wait()
            self.assertTrue(self.ev.is_set())

    def test_metadata_async_user(self):
        """ test_metadata_async_user """
        print("test_metadata_async_user")

        def cb(result: Result, data: typing.Optional[Variant], userdata: ctrlxdatalayer.clib.userData_c_void_p):
            """ cb """
            if data is None:
                print("Async callback in Python (no data): {}, userdata={} ".format(
                    result, ["", userdata][userdata is not None]))
            else:
                r, v = data.clone()
                print("Async callback in Python: result={}, userdata={}, data={}".format(
                    result, ["", userdata][userdata is not None], ["", v.get_string()][r == Result.OK]))
                v.close()
            self.ev.set()

        r = self.client.metadata_async(
            "/diagnosis/cfg/realtime/numbers", cb, 456)
        self.assertTrue(r == Result.OK)
        self.wait()
        self.assertTrue(self.ev.is_set())

    def test_browse_async_user(self):
        """ test_browse_async_user """
        print("test_browse_async_user")

        def cb(result: Result, data: typing.Optional[Variant], userdata: ctrlxdatalayer.clib.userData_c_void_p):
            """ cb """
            if data is None:
                print("Async callback in Python (no data): {}, userdata={} ".format(
                    result, ["", userdata][userdata is not None]))
            else:
                r, v = data.clone()
                print("Async callback in Python: result={}, userdata={}, data={}".format(
                    result, ["", userdata][userdata is not None], ["", v.get_array_string()][r == Result.OK]))
                v.close()
            self.ev.set()

        r = self.client.browse_async("", cb, 789)
        self.assertTrue(r == Result.OK)
        self.wait()
        self.assertTrue(self.ev.is_set())

    def test_browse_async_user_obj(self):
        """ test_browse_async_user_obj """
        print("test_browse_async_user_obj")

        def cb(result: Result, data: typing.Optional[Variant], userdata: ctrlxdatalayer.clib.userData_c_void_p):
            """ cb """
            if data is None:
                print("Async callback in Python (no data): {}".format(
                    result))
            else:
                print("Async callback in Python: result={},".format(
                    result))
            pyUserdata = ctypes.cast(userdata, ctypes.POINTER(
                ctypes.py_object)).contents.value
            pyUserdata.ev.set()

        cUserdata = ctypes.cast(ctypes.pointer(
            ctypes.py_object(self)), ctypes.c_void_p)
        r = self.client.browse_async("", cb, cUserdata)
        self.assertTrue(r == Result.OK)
        self.wait()
        self.assertTrue(self.ev.is_set())

    @staticmethod
    def cb_ext(result: Result, data: typing.Optional[Variant], userdata: ctrlxdatalayer.clib.userData_c_void_p):
        """ cb_ext """
        if data is None:
            print("Async callback in Python (no data): {}".format(
                result))
        else:
            print("Async callback in Python: result={},".format(
                result))
        pyUserdata = ctypes.cast(userdata, ctypes.POINTER(
            ctypes.py_object)).contents.value
        pyUserdata.ev.set()

    def test_browse_async_user_ext_obj(self):
        """ test_browse_async_user_ext_obj """
        print("test_browse_async_user_ext_obj")

        cUserdata = ctypes.cast(ctypes.pointer(
            ctypes.py_object(self)), ctypes.c_void_p)
        r = self.client.browse_async("", TestClientAsyn.cb_ext, cUserdata)
        self.assertTrue(r == Result.OK)
        self.wait()
        self.assertTrue(self.ev.is_set())

    def test_read_json_sync(self):
        """ test_read_json_sync """
        print("test_read_json_sync")
        converter = self.system.json_converter()
        with Variant() as v:
            r, v = self.client.read_json_sync(converter, "scheduler/admin/state", 2)
            self.assertTrue(r == Result.OK)
            self.assertIsNotNone(v)
            self.assertTrue(v.get_type() == VariantType.STRING)
            self.assertTrue(len(v.get_string()) != 0)


@unittest.skipIf(is_integration_test() == False or root_node_alldata_provider() == "", "no integration test")
class TestClientCreateSync(TestClientBase):
    """ TestClientCreateSync """

    def __init__(self, *args, **kwargs):  # Accept all unrecognized args for delegation
        """ __init__ """
        # Delegate to parent initializer
        super().__init__(*args, **kwargs)
        self.addressBase = root_node_alldata_provider() + "/dynamic/_py/"

    def create_sync(self, node: str, data: Variant):
        address = self.addressBase + node
        # Remove node so that create will succeed
        result = self.client.remove_sync(address)  # Ignore error

        result, dataReturned = self.client.create_sync(address, data)
        return result, dataReturned

    def check_create_sync(self, node: str, data: Variant):
        r, v = self.create_sync(node, data)
        # !!! data == v, v is reference on data
        self.assertTrue(r == Result.OK)
        self.assertIsNotNone(v)
        self.assertTrue(v.get_type() == VariantType.UNKNON)

    def test_create_sync_simple(self):
        """ test_create_sync_simple """
        print("test_create_sync_simple")
        with Variant() as data:
            data.set_bool8(True)
            self.check_create_sync("bool8", data)

            data.set_int8(-127)
            self.check_create_sync("int8", data)

    def test_create_sync_array(self):
        """ test_create_sync_array """
        print("test_create_sync_array")
        with Variant() as data:
            data.set_array_bool8([False, True, False])
            self.check_create_sync("array-of-bool8", data)

            data.set_array_int8([-127, -1, 0, 127])
            self.check_create_sync("array-of-int8", data)


if __name__ == '__main__':
    unittest.main()
