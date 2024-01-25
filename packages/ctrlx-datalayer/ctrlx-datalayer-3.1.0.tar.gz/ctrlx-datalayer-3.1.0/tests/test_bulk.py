import ctypes
import datetime
import faulthandler
import unittest
from unittest import mock

from ctrlxdatalayer.client import Client
from ctrlxdatalayer.variant import Result, Variant
from ctrlxdatalayer.bulk import BulkReadRequest, BulkWriteRequest, BulkCreateRequest

faulthandler.enable()


class TestBulkBase(unittest.TestCase):
    """
    TestBulkBase
    """

    def setUp(self):
        """ setUp """
        self.patcher_client_delete = mock.patch(
            'ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientDelete', return_value=None)
        self.patcher_client_delete.start()

    def tearDown(self):
        """  """
        self.patcher_client_delete.stop()


class TestBulkSync(TestBulkBase):
    """
    TestBulkSync
    """

    def test_close(self):
        """ test_close """
        with Client(112233) as client:
            client.close()

    def test_read_sync_error(self):
        """ test_read_sync """
        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientBulkReadSync', return_value=Result.FAILED):
            with Client(112233) as client:
                bulk = client.create_bulk()
                with bulk:
                    req = [BulkReadRequest(
                        '/framework/metrics/system/cpu-utilisation-percent'),
                        BulkReadRequest(
                        '/motion/axs/AxisA/state/values/actual/pos')]
                    result = bulk.read(req)
                    self.assertTrue(result == Result.FAILED)

    def test_read_sync(self):
        """ test_read_sync """
        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientBulkReadSync', return_value=Result.OK):
            with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_bulkGetResponseAddress', return_value='/framework/metrics/system/cpu-utilisation-percent'.encode('utf-8')):
                with Variant() as v:
                    v.set_bool8(False)
                    with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_bulkGetResponseData', return_value=v.get_handle()):
                        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_bulkGetResponseTimestamp', return_value=ctypes.c_uint64(116444736000000000)):
                            with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_bulkGetResponseResult', return_value=Result.OK):
                                with Client(112233) as client:
                                    bulk = client.create_bulk()
                                    with bulk:
                                        req = [BulkReadRequest(
                                            '/framework/metrics/system/cpu-utilisation-percent')]
                                        result = bulk.read(req)
                                        self.assertTrue(result == Result.OK)
                                        self.assertTrue(
                                            len(bulk.get_response()) == 1)
                                        self.assertEqual(bulk.get_response()[0].get_address(
                                        ), '/framework/metrics/system/cpu-utilisation-percent')
                                        self.assertEqual(bulk.get_response()[
                                                         0].get_result(), Result.OK)
                                        self.assertEqual(bulk.get_response()[
                                                         0].get_data().get_bool8(), False)
                                        self.assertEqual(bulk.get_response()[
                                                         0].get_data().get_bool8(), False)
                                        self.assertEqual(bulk.get_response()[
                                                         0].get_datetime(), datetime.datetime(1970, 1, 1))

    def test_read_sync_error2(self):
        """ test_read_sync_error2 """
        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientBulkReadSync', return_value=Result.OK):
            with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_bulkGetResponseAddress', return_value='/framework/metrics/system/cpu-utilisation-percent'.encode('utf-8')):
                with Variant() as v:
                    v.set_bool8(False)
                    with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_bulkGetResponseData', return_value=v.get_handle()):
                        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_bulkGetResponseTimestamp', return_value=ctypes.c_uint64(116444736000000000)):
                            with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_bulkGetResponseResult', return_value=Result.FAILED):
                                with Client(112233) as client:
                                    bulk = client.create_bulk()
                                    with bulk:
                                        req = [BulkReadRequest(
                                            '/framework/metrics/system/cpu-utilisation-percent')]
                                        result = bulk.read(req)
                                        self.assertTrue(result == Result.OK)
                                        self.assertTrue(
                                            len(bulk.get_response()) == 1)
                                        self.assertEqual(bulk.get_response()[
                                                         0].get_result(), Result.FAILED)

    def test_read_args_sync(self):
        """ test_read_args_sync """
        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientBulkReadSync', return_value=Result.OK):
            with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_bulkGetResponseAddress', return_value='/read/value/1/with/arg'.encode('utf-8')):
                with Variant() as v:
                    v.set_bool8(False)
                    with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_bulkGetResponseData', return_value=v.get_handle()):
                        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_bulkGetResponseTimestamp', return_value=ctypes.c_uint64(116444736000000000)):
                            with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_bulkGetResponseResult', return_value=Result.OK):
                                with Client(112233) as client:
                                    with Variant() as arg:
                                        bulk = client.create_bulk()
                                        with bulk:
                                            arg.set_bool8(True)
                                            req = [BulkReadRequest(
                                                '/read/value/1/with/arg', arg),
                                                BulkReadRequest(
                                                '/read/value/2/with/arg', arg)]
                                            result = bulk.read(req)
                                            self.assertTrue(
                                                result == Result.OK)
                                            self.assertEqual(
                                                len(bulk.get_response()), 2)
                                            self.assertEqual(bulk.get_response()[0].get_address(
                                            ), '/read/value/1/with/arg')
                                            self.assertEqual(bulk.get_response()[
                                                             0].get_result(), Result.OK)
                                            self.assertEqual(bulk.get_response()[
                                                0].get_datetime(), datetime.datetime(1970, 1, 1))

    def test_write_sync_error(self):
        """ test_write_sync """
        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientBulkWriteSync', return_value=Result.FAILED):
            with Client(112233) as client:
                with Variant() as data:
                    bulk = client.create_bulk()
                    with bulk:
                        data.set_bool8(True)
                        req = [BulkWriteRequest(
                            '/write/value/1', data)]
                        data.set_string('write_value')
                        req.append(BulkWriteRequest(
                            '/write/value/2', data))
                        result = bulk.write(req)
                        self.assertTrue(result == Result.FAILED)

    def test_write_sync(self):
        """ test_write_sync """
        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientBulkWriteSync', return_value=Result.OK):
            with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_bulkGetResponseAddress', return_value='/write/value/1'.encode('utf-8')):
                with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_bulkGetResponseTimestamp', return_value=ctypes.c_uint64(116444736000000000)):
                    with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_bulkGetResponseResult', return_value=Result.OK):
                        with Variant() as data:
                            with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_bulkGetResponseData', return_value=data.get_handle()):

                                with Client(112233) as client:
                                    bulk = client.create_bulk()
                                    with bulk:
                                        data.set_bool8(True)
                                        req = [BulkWriteRequest(
                                            '/write/value/1', data)]
                                        data.set_string('write_value')
                                        req.append(BulkWriteRequest(
                                            '/write/value/2', data))
                                        result = bulk.write(req)
                                        self.assertTrue(result == Result.OK)
                                        self.assertEqual(
                                            len(bulk.get_response()), 2)

    def test_browse_error(self):
        """ test_browse_error """
        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientBulkBrowseSync', return_value=Result.FAILED):
            with Client(112233) as client:
                bulk = client.create_bulk()
                with bulk:
                    result = bulk.browse(['/framework/metrics/system/'])
                    self.assertTrue(result == Result.FAILED)

    def test_browse_error2(self):
        """ test_browse_error2 """
        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientBulkBrowseSync', return_value=Result.OK):
            with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_bulkGetResponseAddress', return_value='/framework/metrics/system/'.encode('utf-8')):
                with Variant() as v:
                    v.set_bool8(False)
                    with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_bulkGetResponseData', return_value=v.get_handle()):
                        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_bulkGetResponseTimestamp', return_value=ctypes.c_uint64(116444736000000000)):
                            with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_bulkGetResponseResult', return_value=Result.FAILED):
                                with Client(112233) as client:
                                    bulk = client.create_bulk()
                                    with bulk:
                                        result = bulk.browse(
                                            ['/framework/metrics/system/'])

                                        self.assertTrue(result == Result.OK)
                                        self.assertTrue(
                                            len(bulk.get_response()) == 1)
                                        self.assertEqual(bulk.get_response()[
                                                         0].get_result(), Result.FAILED)

    def test_browse(self):
        """ test_browse """
        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientBulkBrowseSync', return_value=Result.OK):
            with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_bulkGetResponseAddress', return_value='/framework/metrics/system/'.encode('utf-8')):
                with Variant() as v:
                    v.set_array_string(
                        ['/framework/metrics/system/A', '/framework/metrics/system/B'])
                    with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_bulkGetResponseData', return_value=v.get_handle()):
                        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_bulkGetResponseTimestamp', return_value=ctypes.c_uint64(116444736000000000)):
                            with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_bulkGetResponseResult', return_value=Result.OK):
                                with Client(112233) as client:
                                    bulk = client.create_bulk()
                                    with bulk:
                                        result = bulk.browse(
                                            ['/framework/metrics/system/'])

                                        self.assertTrue(result == Result.OK)
                                        self.assertTrue(
                                            len(bulk.get_response()) == 1)
                                        self.assertEqual(bulk.get_response()[0].get_address(
                                        ), '/framework/metrics/system/')
                                        self.assertEqual(bulk.get_response()[
                                            0].get_result(), Result.OK)
                                        self.assertEqual(bulk.get_response()[
                                            0].get_datetime(), datetime.datetime(1970, 1, 1))

    def test_metadata_error(self):
        """ test_metadata_error """
        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientBulkMetadataSync', return_value=Result.FAILED):
            with Client(112233) as client:
                bulk = client.create_bulk()
                with bulk:
                    result = bulk.metadata(['/framework/metrics/system/'])
                    self.assertTrue(result == Result.FAILED)

    def test_metadata_error2(self):
        """ test_metadata_error2 """
        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientBulkMetadataSync', return_value=Result.OK):
            with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_bulkGetResponseAddress', return_value='framework/metrics/system/cpu-utilisation-percent'.encode('utf-8')):
                with Variant() as v:
                    v.set_bool8(False)
                    with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_bulkGetResponseData', return_value=v.get_handle()):
                        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_bulkGetResponseTimestamp', return_value=ctypes.c_uint64(116444736000000000)):
                            with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_bulkGetResponseResult', return_value=Result.FAILED):
                                with Client(112233) as client:
                                    bulk = client.create_bulk()
                                    with bulk:
                                        result = bulk.metadata(
                                            ['framework/metrics/system/cpu-utilisation-percent'])

                                        self.assertTrue(result == Result.OK)
                                        self.assertTrue(
                                            len(bulk.get_response()) == 1)
                                        self.assertEqual(bulk.get_response()[
                                                         0].get_result(), Result.FAILED)

    def test_metadata(self):
        """ test_metadata """
        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientBulkMetadataSync', return_value=Result.OK):
            with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_bulkGetResponseAddress', return_value='framework/metrics/system/cpu-utilisation-percent'.encode('utf-8')):
                with Variant() as v:
                    v.set_bool8(False)
                    with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_bulkGetResponseData', return_value=v.get_handle()):
                        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_bulkGetResponseTimestamp', return_value=ctypes.c_uint64(116444736000000000)):
                            with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_bulkGetResponseResult', return_value=Result.OK):
                                with Client(112233) as client:
                                    bulk = client.create_bulk()
                                    with bulk:

                                        result = bulk.metadata(
                                            ['framework/metrics/system/cpu-utilisation-percent'])

                                        self.assertTrue(result == Result.OK)
                                        self.assertTrue(
                                            len(bulk.get_response()) == 1)
                                        self.assertEqual(bulk.get_response()[0].get_address(
                                        ), 'framework/metrics/system/cpu-utilisation-percent')
                                        self.assertEqual(bulk.get_response()[
                                            0].get_result(), Result.OK)
                                        self.assertEqual(bulk.get_response()[
                                            0].get_datetime(), datetime.datetime(1970, 1, 1))

    def test_create_error(self):
        """     def test_create_error(self): """
        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientBulkCreateSync', return_value=Result.FAILED):
            with Client(112233) as client:
                bulk = client.create_bulk()
                with bulk:
                    result = bulk.create(
                        [BulkCreateRequest('/framework/metrics/system/')])
                    self.assertTrue(result == Result.FAILED)

    def test_create_error2(self):
        """ test_create_error2 """
        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientBulkCreateSync', return_value=Result.OK):
            with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_bulkGetResponseAddress', return_value='framework/metrics/system/cpu-utilisation-percent'.encode('utf-8')):
                with Variant() as v:
                    v.set_bool8(False)
                    with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_bulkGetResponseData', return_value=v.get_handle()):
                        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_bulkGetResponseTimestamp', return_value=ctypes.c_uint64(116444736000000000)):
                            with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_bulkGetResponseResult', return_value=Result.FAILED):
                                with Client(112233) as client:
                                    bulk = client.create_bulk()
                                    with bulk:
                                        result = bulk.create(
                                            [BulkCreateRequest('framework/metrics/system/cpu-utilisation-percent')])

                                        self.assertTrue(result == Result.OK)
                                        self.assertTrue(
                                            len(bulk.get_response()) == 1)
                                        self.assertEqual(bulk.get_response()[
                                                         0].get_result(), Result.FAILED)

    def test_create(self):
        """ test_create """
        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientBulkCreateSync', return_value=Result.OK):
            with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_bulkGetResponseAddress', return_value='framework/metrics/system/cpu-utilisation-percent'.encode('utf-8')):
                with Variant() as v:
                    v.set_bool8(False)
                    with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_bulkGetResponseData', return_value=v.get_handle()):
                        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_bulkGetResponseTimestamp', return_value=ctypes.c_uint64(116444736000000000)):
                            with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_bulkGetResponseResult', return_value=Result.OK):
                                with Client(112233) as client:
                                    bulk = client.create_bulk()
                                    with bulk:
                                        result = bulk.create(
                                            [BulkCreateRequest('framework/metrics/system/cpu-utilisation-percent')])

                                        self.assertTrue(result == Result.OK)
                                        self.assertTrue(
                                            len(bulk.get_response()) == 1)
                                        self.assertEqual(bulk.get_response()[0].get_address(
                                        ), 'framework/metrics/system/cpu-utilisation-percent')
                                        self.assertEqual(bulk.get_response()[
                                            0].get_result(), Result.OK)
                                        self.assertEqual(bulk.get_response()[
                                            0].get_datetime(), datetime.datetime(1970, 1, 1))

    def test_delete_error(self):
        """     def test_delete_error(self): """
        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientBulkDeleteSync', return_value=Result.FAILED):
            with Client(112233) as client:
                bulk = client.create_bulk()
                with bulk:
                    result = bulk.delete(['/framework/metrics/system/'])
                    self.assertTrue(result == Result.FAILED)

    def test_delete_error2(self):
        """ test_delete_error2 """
        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientBulkDeleteSync', return_value=Result.OK):
            with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_bulkGetResponseAddress', return_value='framework/metrics/system/cpu-utilisation-percent'.encode('utf-8')):
                with Variant() as v:
                    v.set_bool8(False)
                    with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_bulkGetResponseData', return_value=v.get_handle()):
                        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_bulkGetResponseTimestamp', return_value=ctypes.c_uint64(116444736000000000)):
                            with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_bulkGetResponseResult', return_value=Result.FAILED):
                                with Client(112233) as client:
                                    bulk = client.create_bulk()
                                    with bulk:
                                        result = bulk.delete(
                                            ['framework/metrics/system/cpu-utilisation-percent'])

                                        self.assertTrue(result == Result.OK)
                                        self.assertTrue(
                                            len(bulk.get_response()) == 1)
                                        self.assertEqual(bulk.get_response()[
                                                         0].get_result(), Result.FAILED)

    def test_delete(self):
        """ test_delete """
        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientBulkDeleteSync', return_value=Result.OK):
            with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_bulkGetResponseAddress', return_value='framework/metrics/system/cpu-utilisation-percent'.encode('utf-8')):
                with Variant() as v:
                    v.set_bool8(False)
                    with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_bulkGetResponseData', return_value=v.get_handle()):
                        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_bulkGetResponseTimestamp', return_value=ctypes.c_uint64(116444736000000000)):
                            with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_bulkGetResponseResult', return_value=Result.OK):
                                with Client(112233) as client:
                                    bulk = client.create_bulk()
                                    with bulk:
                                        result = bulk.delete(
                                            ['framework/metrics/system/cpu-utilisation-percent'])

                                        self.assertTrue(result == Result.OK)
                                        self.assertTrue(
                                            len(bulk.get_response()) == 1)
                                        self.assertEqual(bulk.get_response()[0].get_address(
                                        ), 'framework/metrics/system/cpu-utilisation-percent')
                                        self.assertEqual(bulk.get_response()[
                                            0].get_result(), Result.OK)
                                        self.assertEqual(bulk.get_response()[
                                            0].get_datetime(), datetime.datetime(1970, 1, 1))


if __name__ == '__main__':
    unittest.main()
