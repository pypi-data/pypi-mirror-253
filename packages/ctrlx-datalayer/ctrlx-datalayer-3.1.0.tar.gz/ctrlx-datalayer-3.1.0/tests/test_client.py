import faulthandler
import typing
import unittest
from unittest import mock

import ctrlxdatalayer.clib_system
import ctrlxdatalayer.converter
from ctrlxdatalayer.client import Client, ResponseCallback, TimeoutSetting
from ctrlxdatalayer.variant import Result, Variant

faulthandler.enable()


class TestClientBase(unittest.TestCase):
    """
    TestClientBase
    """

    def setUp(self):
        """ setUp """
        self.patcher_client_delete = mock.patch(
            'ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientDelete', return_value=None)
        self.patcher_client_delete.start()

    def tearDown(self):
        """  """
        self.patcher_client_delete.stop()


class TestClient(TestClientBase):
    """ TestClient """

    def test_factory_create_client(self):
        """ test_factory_create_client """
        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_systemDelete', return_value=None), \
                mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_systemCreate', return_value=123), \
                mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_systemFactory', return_value=111222), \
                mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_systemStop', return_value=None):
            with ctrlxdatalayer.system.System("") as system:
                self.assertIsNotNone(system)
                self.assertTrue(system.get_handle() != 0)
                factory = system.factory()
                self.assertIsNotNone(factory)
                with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_factoryCreateClient', return_value=33334444):
                    client = factory.create_client("")
                    self.assertIsNotNone(client)

    def test_close(self):
        """ test_close """
        with Client(112233) as client:
            client.close()

    def test_set_timeout(self):
        """ test_set_timeout """
        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientSetTimeout', return_value=Result.OK):
            with Client(112233) as client:
                result = client.set_timeout(TimeoutSetting.PING, 1000)
            self.assertTrue(result == Result.OK)
        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientSetTimeout', return_value=Result.FAILED):
            with Client(112233) as client:
                result = client.set_timeout(TimeoutSetting.PING, 1000)
            self.assertTrue(result == Result.FAILED)
        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientSetTimeout', return_value=Result.OK):
            with Client(112233) as client:
                result = client.set_timeout(TimeoutSetting.IDLE, 1000)
            self.assertTrue(result == Result.OK)
        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientSetTimeout', return_value=Result.FAILED):
            with Client(112233) as client:
                result = client.set_timeout(TimeoutSetting.IDLE, 1000)
            self.assertTrue(result == Result.FAILED)

    def test_is_connected(self):
        """ test_is_connected """
        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientIsConnected', return_value=True):
            with Client(112233) as client:
                val = client.is_connected()
            self.assertTrue(val)
        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientIsConnected', return_value=False):
            with Client(112233) as client:
                val = client.is_connected()
            self.assertFalse(val)

    def test_set_auth_token(self):
        """ test_set_auth_token """
        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientSetAuthToken', return_value=None):
            with Client(112233) as client:
                client.set_auth_token("geheimer tocken")
        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientSetAuthToken', return_value=None):
            with Client(112233) as client:
                client.set_auth_token("")
        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientSetAuthToken', return_value=None):
            with Client(112233) as client:
                self.assertRaises(TypeError, client.set_auth_token, None)

    def test_get_auth_token(self):
        """ test_get_auth_token """
        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientGetAuthToken', return_value="streng geheimer token".encode('utf-8')):
            with Client(112233) as client:
                val = client.get_auth_token()
            self.assertTrue(val == "streng geheimer token")

    def test_ping_sync(self):
        """ test_ping_sync """
        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientPingSync', return_value=Result.OK):
            client = Client(112233)
            res = client.ping_sync()
            self.assertTrue(res == Result.OK)
        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientPingSync', return_value=Result.FAILED):
            with Client(112233) as client:
                res = client.ping_sync()
            self.assertTrue(res == Result.FAILED)

    def test_create_sync(self):
        """ test_create_sync """
        with Variant() as wdata:
            with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientCreateSync', return_value=Result.OK):
                with Client(112233) as client:
                    res, data = client.create_sync("address/ok", wdata)
                self.assertTrue(res == Result.OK)
                self.assertIsNotNone(data)
                data.close()
            with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientCreateSync', return_value=Result.FAILED):
                with Client(112233) as client:
                    res, data = client.create_sync("address/bad", wdata)
                self.assertTrue(res == Result.FAILED)
                self.assertIsNotNone(data)
                data.close()

    def test_remove_sync(self):
        """ test_remove_sync """
        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientRemoveSync', return_value=Result.OK):
            with Client(112233) as client:
                res = client.remove_sync("address/ok")
            self.assertTrue(res == Result.OK)
        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientRemoveSync', return_value=Result.FAILED):
            with Client(112233) as client:
                res = client.remove_sync("address/bad")
            self.assertTrue(res == Result.FAILED)

    def test_browse_sync(self):
        """ test_browse_sync """
        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientBrowseSync', return_value=Result.OK):
            with Client(112233) as client:
                res, data = client.browse_sync("address/ok")
            self.assertTrue(res == Result.OK)
            self.assertIsNotNone(data)
            data.close()
        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientBrowseSync', return_value=Result.FAILED):
            with Client(112233) as client:
                res, data = client.browse_sync("address/bad")
            self.assertTrue(res == Result.FAILED)
            self.assertIsNotNone(data)
            data.close()

    def test_read_sync(self):
        """ test_read_sync """
        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientReadSync', return_value=Result.OK):
            with Client(112233) as client:
                res, data = client.read_sync("address/ok")
            self.assertTrue(res == Result.OK)
            self.assertIsNotNone(data)
            data.close()
        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientReadSync', return_value=Result.FAILED):
            with Client(112233) as client:
                res, data = client.read_sync("address/bad")
            self.assertTrue(res == Result.FAILED)
            self.assertIsNotNone(data)
            data.close()

    def test_read_sync_args(self):
        """ test_read_sync_args """
        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientReadSync', return_value=Result.OK):
            with Client(112233) as client:
                with Variant() as data:
                    res, data = client.read_sync_args("address/ok", data)
            self.assertTrue(res == Result.OK)
            self.assertIsNotNone(data)
        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientReadSync', return_value=Result.FAILED):
            with Client(112233) as client:
                with Variant() as data:
                    res, data = client.read_sync_args("address/bad", data)
            self.assertTrue(res == Result.FAILED)
            self.assertIsNotNone(data)

    def test_write_sync(self):
        """ test_write_sync """
        wdata = Variant()
        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientWriteSync', return_value=Result.OK):
            with Client(112233) as client:
                res, data = client.write_sync("address/ok", wdata)
            self.assertTrue(res == Result.OK)
            self.assertIsNotNone(data)
            data.close()
        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientWriteSync', return_value=Result.FAILED):
            with Client(112233) as client:
                res, data = client.write_sync("address/bad", wdata)
            self.assertTrue(res == Result.FAILED)
            self.assertIsNotNone(data)
            data.close()

    def test_metadata_sync(self):
        """ test_metadata_sync """
        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientMetadataSync', return_value=Result.OK):
            with Client(112233) as client:
                res, data = client.metadata_sync("address/ok")
            self.assertTrue(res == Result.OK)
            self.assertIsNotNone(data)
            data.close()
        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientMetadataSync', return_value=Result.FAILED):
            with Client(112233) as client:
                res, data = client.metadata_sync("address/bad")
            self.assertTrue(res == Result.FAILED)
            self.assertIsNotNone(data)
            data.close()

    def test_read_json_sync(self):
        """ test_read_json """
        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientReadJsonSync', return_value=Result.OK):
            with Client(112233) as client:
                conv = ctrlxdatalayer.converter.Converter(1234)
                json = Variant()
                json.set_string('testdata')
                res, data = client.read_json_sync(conv, "address/ok", 2, json)
            self.assertTrue(res == Result.OK)
            self.assertIsNotNone(data)
            data.close()
        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientReadJsonSync', return_value=Result.FAILED):
            with Client(112233) as client:
                res, data = client.read_json_sync(conv, "address/bad", 2)
            self.assertTrue(res == Result.FAILED)
            self.assertIsNotNone(data)
            data.close()

    def test_write_json_sync(self):
        """ test_write_json """
        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientWriteJsonSync', return_value=Result.OK):
            with Client(112233) as client:
                conv = ctrlxdatalayer.converter.Converter(1234)
                res, data = client.write_json_sync(conv, "address/ok", "{1:1}")
            self.assertTrue(res == Result.OK)
            self.assertIsNotNone(data)
            data.close()
        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientWriteJsonSync', return_value=Result.FAILED):
            with Client(112233) as client:
                conv = ctrlxdatalayer.converter.Converter(1234)
                res, data = client.write_json_sync(
                    conv, "address/bad", "{1:1}")
            self.assertTrue(res == Result.FAILED)
            self.assertIsNotNone(data)
            data.close()


class TestClientAsync(TestClient):
    """ TestClientAsync """

    def test_ping_async(self):
        """ test_create_async """
        with Variant() as d:
            with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientPingASync', return_value=Result.OK):
                with Client(112233) as client:
                    res = client.ping_async(None)
                self.assertTrue(res == Result.OK)
            with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientPingASync', return_value=Result.FAILED):
                with Client(112233) as client:
                    res = client.ping_async(None)
                self.assertTrue(res == Result.FAILED)

    def test_create_async(self):
        """ test_create_async """
        with Variant() as d:
            with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientCreateASync', return_value=Result.OK):
                with Client(112233) as client:
                    res = client.create_async("address/ok", d, None)
                self.assertTrue(res == Result.OK)
            with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientCreateASync', return_value=Result.FAILED):
                with Client(112233) as client:
                    res = client.create_async("address/bad", d, None)
                self.assertTrue(res == Result.FAILED)

    def test_remove_async(self):
        """ test_remove_async """
        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientRemoveASync', return_value=Result.OK):
            with Client(112233) as client:
                res = client.remove_async("address/ok", None)
            self.assertTrue(res == Result.OK)
        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientRemoveASync', return_value=Result.FAILED):
            with Client(112233) as client:
                res = client.remove_async("address/bad", None)
            self.assertTrue(res == Result.FAILED)

    def test_browse_async(self):
        """ test_browse_async """
        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientBrowseASync', return_value=Result.OK):
            with Client(112233) as client:
                res = client.browse_async("address/ok", None)
            self.assertTrue(res == Result.OK)
        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientBrowseASync', return_value=Result.FAILED):
            with Client(112233) as client:
                res = client.browse_async("address/bad", None)
            self.assertTrue(res == Result.FAILED)

    def test_read_async(self):
        """ test_read_async """
        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientReadASync', return_value=Result.OK):
            with Client(112233) as client:
                res = client.read_async("address/ok", None)
            self.assertTrue(res == Result.OK)
        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientReadASync', return_value=Result.FAILED):
            with Client(112233) as client:
                res = client.read_async("address/bad", None)
            self.assertTrue(res == Result.FAILED)

    def test_read_async_args(self):
        """ test_read_async """
        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientReadASync', return_value=Result.OK):
            with Client(112233) as client:
                with Variant() as args:
                    res = client.read_async_args("address/ok", args, None)
            self.assertTrue(res == Result.OK)
        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientReadASync', return_value=Result.FAILED):
            with Client(112233) as client:
                with Variant() as args:
                    res = client.read_async_args("address/bad", args, None)
            self.assertTrue(res == Result.FAILED)

    def test_write_async(self):
        """ test_write_async """
        with Variant() as d:
            with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientWriteASync', return_value=Result.OK):
                with Client(112233) as client:
                    res = client.write_async("address/ok", d, None)
                self.assertTrue(res == Result.OK)
            with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientWriteASync', return_value=Result.FAILED):
                with Client(112233) as client:
                    res = client.write_async("address/bad", d, None)
                self.assertTrue(res == Result.FAILED)

    def test_metadata_async(self):
        """ test_metadata_async """
        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientMetadataASync', return_value=Result.OK):
            with Client(112233) as client:
                res = client.metadata_async("address/ok", None)
            self.assertTrue(res == Result.OK)
        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientMetadataASync', return_value=Result.FAILED):
            with Client(112233) as client:
                res = client.metadata_async("address/bad", None)
            self.assertTrue(res == Result.FAILED)


class _CallbackClient(Client):
    """
    _CallbackClient
    """

    def create_cb(self, cb: ResponseCallback):
        """ create_cb """
        return self._test_callback(cb)


class TestClientCallback(TestClientBase):
    """
    TestClientCallback
    """

    def test_callback_ok(self):
        """ test_callback_ok """
        with _CallbackClient(112233) as client:

            def cb(result: Result, data: typing.Optional[Variant], userdata: ctrlxdatalayer.clib.userData_c_void_p):
                if result == Result.OK:
                    self.check = True
                print("Async callback in Python: ", result)

            call_back = client.create_cb(cb)
            self.check = False
            call_back(Result.OK.value, None, None)
            self.assertTrue(self.check == True)

    def test_callback_fail(self):
        """ test_callback_fail """
        with _CallbackClient(112233) as client:

            def cb(result: Result, data: typing.Optional[Variant], userdata: ctrlxdatalayer.clib.userData_c_void_p):
                if result == Result.FAILED:
                    self.check = True
                print("Async callback in Python: ", result)

            call_back = client.create_cb(cb)
            self.assertIsNotNone(call_back)
            self.check = False
            call_back(Result.FAILED.value, None, None)
            self.assertTrue(self.check == True)

    def test_callback_data(self):
        """ test_callback_data """
        with _CallbackClient(112233) as client:

            def cb(result: Result, data: typing.Optional[Variant], userdata: ctrlxdatalayer.clib.userData_c_void_p):
                self.check = True
                print("Async callback in Python: result={}, data={} ".format(
                    result, ["no", data.get_int16()][data is not None]))

            self.check = False
            call_back = client.create_cb(cb)
            self.assertIsNotNone(call_back)
            with Variant() as v:
                v.set_int16(1701)
                call_back(Result.OK.value, v.get_handle(), None)
                self.assertTrue(self.check == True)

    def test_callback_userdata(self):
        """ test_callback_userdata """
        with _CallbackClient(112233) as client:

            def cb(result: Result, data: typing.Optional[Variant], userdata: ctrlxdatalayer.clib.userData_c_void_p):
                self.check = True
                print("Async callback in Python: result={}, data={}, userdata={} ".format(
                    result,
                    ["no", data.get_int16()][data is not None],
                    ["no", userdata][userdata is not None]))

            self.check = False
            call_back = client.create_cb(cb)
            self.assertIsNotNone(call_back)
            with Variant() as v:
                v.set_int16(1701)
                call_back(Result.OK.value, v.get_handle(), 123)
                self.assertTrue(self.check == True)


if __name__ == '__main__':
    unittest.main()
