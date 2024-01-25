import ctypes
import faulthandler
import typing
import unittest
from unittest import mock

import ctrlxdatalayer
from ctrlxdatalayer.bulk import Response, BulkReadRequest, BulkWriteRequest, BulkCreateRequest
from ctrlxdatalayer.clib_bulk import C_BulkResponse, C_VecBulkResponse
from ctrlxdatalayer.client import Client
from ctrlxdatalayer.variant import Result, Variant
from tests.test_bulk import TestBulkBase

faulthandler.enable()


class TestBulkAsync(TestBulkBase):
    """
    TestBulkAsync
    """

    def test_read_async_error(self):
        """ test_read_async_error """
        def cb(resps: typing.List[Response], userdata: ctrlxdatalayer.clib.userData_c_void_p):
            pass

        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientReadBulkASync', return_value=Result.FAILED):
            with Client(112233) as client:
                bulk = client.create_bulk()
                with bulk:
                    req = [BulkReadRequest(
                        '/framework/metrics/system/cpu-utilisation-percent'),
                        BulkReadRequest(
                        '/motion/axs/AxisA/state/values/actual/pos')]
                    result = bulk.read(req, cb)
                    self.assertTrue(result == Result.FAILED)

    def test_read_async(self):
        """ test_read_async """
        def cb(resps: typing.List[Response], userdata: ctrlxdatalayer.clib.userData_c_void_p):
            pass

        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientReadBulkASync', return_value=Result.OK):
            with Client(112233) as client:
                bulk = client.create_bulk()
                with bulk:
                    req = [BulkReadRequest(
                        '/framework/metrics/system/cpu-utilisation-percent'),
                        BulkReadRequest(
                        '/motion/axs/AxisA/state/values/actual/pos')]
                    result = bulk.read(req, cb)
                    self.assertTrue(result == Result.OK)

    def test_read_async_cb(self):
        """ test_read_async_cb """
        def cb(resps: typing.List[Response], userdata: ctrlxdatalayer.clib.userData_c_void_p):
            print("callback")
            self.assertTrue(len(resps) == 1)
            self.assertEqual(resps[0].get_address(
            ), '/framework/metrics/system/cpu-utilisation-percent')

        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientReadBulkASync', return_value=Result.OK):
            with Client(112233) as client:
                bulk = client.create_bulk()
                with bulk:
                    req = [BulkReadRequest(
                        '/framework/metrics/system/cpu-utilisation-percent')]
                    result = bulk.read(req, cb)
                    self.assertTrue(result == Result.OK)
                    with Variant() as v:
                        v.set_bool8(True)
                        call_back = bulk._test_callback(cb)

                        bulk_resp = C_BulkResponse()
                        bulk_resp.address = '/framework/metrics/system/cpu-utilisation-percent'.encode(
                            'utf-8')
                        bulk_resp.result = Result.OK.value
                        bulk_resp.timestamp = ctypes.c_uint64(
                            116444736000000000)
                        bulk_resp.data = v.get_handle()

                        pr = (C_BulkResponse * 1)(bulk_resp)
                        bulk_vec_resp = C_VecBulkResponse()
                        bulk_vec_resp.count = 1
                        bulk_vec_resp.response = pr
                        call_back(bulk_vec_resp, 0)

    def test_write_async_cb(self):
        """ test_write_async_cb """
        def cb(resps: typing.List[Response], userdata: ctrlxdatalayer.clib.userData_c_void_p):
            print("callback")
            self.assertTrue(len(resps) == 1)
            self.assertEqual(resps[0].get_address(
            ), '/framework/metrics/system/cpu-utilisation-percent')

        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientWriteBulkASync', return_value=Result.OK):
            with Client(112233) as client, Variant() as v:
                v.set_bool8(True)
                bulk = client.create_bulk()
                with bulk:
                    req = [BulkWriteRequest(
                        '/framework/metrics/system/cpu-utilisation-percent', v)]
                    result = bulk.write(req, cb)
                    self.assertTrue(result == Result.OK)
                    v.set_bool8(True)
                    call_back = bulk._test_callback(cb)

                    bulk_resp = C_BulkResponse()
                    bulk_resp.address = '/framework/metrics/system/cpu-utilisation-percent'.encode(
                        'utf-8')
                    bulk_resp.result = Result.OK.value
                    bulk_resp.timestamp = ctypes.c_uint64(
                        116444736000000000)
                    bulk_resp.data = v.get_handle()

                    pr = (C_BulkResponse * 1)(bulk_resp)
                    bulk_vec_resp = C_VecBulkResponse()
                    bulk_vec_resp.count = 1
                    bulk_vec_resp.response = pr
                    call_back(bulk_vec_resp, 0)

    def test_browse_async_cb(self):
        """ test_browse_async_cb """
        def cb(resps: typing.List[Response], userdata: ctrlxdatalayer.clib.userData_c_void_p):
            print("callback")
            self.assertTrue(len(resps) == 1)
            self.assertEqual(resps[0].get_address(
            ), '/framework/metrics/system/cpu-utilisation-percent')

        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientBrowseBulkASync', return_value=Result.OK):
            with Client(112233) as client:
                bulk = client.create_bulk()
                with bulk:
                    result = bulk.browse(
                        ['/framework/metrics/system/cpu-utilisation-percent'], cb)
                    self.assertTrue(result == Result.OK)
                    with Variant() as v:
                        v.set_bool8(True)
                        call_back = bulk._test_callback(cb)

                        bulk_resp = C_BulkResponse()
                        bulk_resp.address = '/framework/metrics/system/cpu-utilisation-percent'.encode(
                            'utf-8')
                        bulk_resp.result = Result.OK.value
                        bulk_resp.timestamp = ctypes.c_uint64(
                            116444736000000000)
                        bulk_resp.data = v.get_handle()

                        pr = (C_BulkResponse * 1)(bulk_resp)
                        bulk_vec_resp = C_VecBulkResponse()
                        bulk_vec_resp.count = 1
                        bulk_vec_resp.response = pr
                        call_back(bulk_vec_resp, 0)

    def test_metadata_async_cb(self):
        """ test_metadata_async_cb """
        def cb(resps: typing.List[Response], userdata: ctrlxdatalayer.clib.userData_c_void_p):
            print("callback")
            self.assertTrue(len(resps) == 1)
            self.assertEqual(resps[0].get_address(
            ), '/framework/metrics/system/cpu-utilisation-percent')

        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientMetadataBulkASync', return_value=Result.OK):
            with Client(112233) as client:
                bulk = client.create_bulk()
                with bulk:
                    result = bulk.metadata(
                        ['/framework/metrics/system/cpu-utilisation-percent'], cb)
                    self.assertTrue(result == Result.OK)
                    with Variant() as v:
                        v.set_bool8(True)
                        call_back = bulk._test_callback(cb)

                        bulk_resp = C_BulkResponse()
                        bulk_resp.address = '/framework/metrics/system/cpu-utilisation-percent'.encode(
                            'utf-8')
                        bulk_resp.result = Result.OK.value
                        bulk_resp.timestamp = ctypes.c_uint64(
                            116444736000000000)
                        bulk_resp.data = v.get_handle()

                        pr = (C_BulkResponse * 1)(bulk_resp)
                        bulk_vec_resp = C_VecBulkResponse()
                        bulk_vec_resp.count = 1
                        bulk_vec_resp.response = pr
                        call_back(bulk_vec_resp, 0)

    def test_create_async_cb(self):
        """ test_metadata_async_cb """
        def cb(resps: typing.List[Response], userdata: ctrlxdatalayer.clib.userData_c_void_p):
            print("callback")
            self.assertTrue(len(resps) == 1)
            self.assertEqual(resps[0].get_address(
            ), '/framework/metrics/system/cpu-utilisation-percent')

        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientCreateBulkASync', return_value=Result.OK):
            with Client(112233) as client:
                bulk = client.create_bulk()
                with bulk:
                    result = bulk.create(
                        [BulkCreateRequest('framework/metrics/system/cpu-utilisation-percent')], cb)
                    self.assertTrue(result == Result.OK)
                    with Variant() as v:
                        v.set_bool8(True)
                        call_back = bulk._test_callback(cb)

                        bulk_resp = C_BulkResponse()
                        bulk_resp.address = '/framework/metrics/system/cpu-utilisation-percent'.encode(
                            'utf-8')
                        bulk_resp.result = Result.OK.value
                        bulk_resp.timestamp = ctypes.c_uint64(
                            116444736000000000)
                        bulk_resp.data = v.get_handle()

                        pr = (C_BulkResponse * 1)(bulk_resp)
                        bulk_vec_resp = C_VecBulkResponse()
                        bulk_vec_resp.count = 1
                        bulk_vec_resp.response = pr
                        call_back(bulk_vec_resp, 0)

    def test_delete_async_cb(self):
        """ test_metadata_async_cb """
        def cb(resps: typing.List[Response], userdata: ctrlxdatalayer.clib.userData_c_void_p):
            print("callback")
            self.assertTrue(len(resps) == 1)
            self.assertEqual(resps[0].get_address(
            ), '/framework/metrics/system/cpu-utilisation-percent')

        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientDeleteBulkASync', return_value=Result.OK):
            with Client(112233) as client:
                bulk = client.create_bulk()
                with bulk:
                    result = bulk.delete(
                        ['/framework/metrics/system/cpu-utilisation-percent'], cb)
                    self.assertTrue(result == Result.OK)
                    with Variant() as v:
                        v.set_bool8(True)
                        call_back = bulk._test_callback(cb)

                        bulk_resp = C_BulkResponse()
                        bulk_resp.address = '/framework/metrics/system/cpu-utilisation-percent'.encode(
                            'utf-8')
                        bulk_resp.result = Result.OK.value
                        bulk_resp.timestamp = ctypes.c_uint64(
                            116444736000000000)
                        bulk_resp.data = v.get_handle()

                        pr = (C_BulkResponse * 1)(bulk_resp)
                        bulk_vec_resp = C_VecBulkResponse()
                        bulk_vec_resp.count = 1
                        bulk_vec_resp.response = pr
                        call_back(bulk_vec_resp, 0)


if __name__ == '__main__':
    unittest.main()
