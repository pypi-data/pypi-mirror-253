import faulthandler
import unittest
from unittest import mock

import ctrlxdatalayer.clib_system

faulthandler.enable()


class TestSystem(unittest.TestCase):
    """ TestSystem """

    def setUp(self):
        """ setUp """
        self.patcher_system_delete = mock.patch(
            'ctrlxdatalayer.clib.libcomm_datalayer.DLR_systemDelete', return_value=None)
        self.patcher_system_delete.start()

    def tearDown(self):
        """ tearDown """
        self.patcher_system_delete.stop()

    def test_create(self):
        """ test_create """
        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_systemCreate', return_value=123), \
                mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_systemStop', return_value=None):
            with ctrlxdatalayer.system.System("") as system:
                self.assertIsNotNone(system)
                self.assertTrue(system.get_handle() == 123)

    def test_create_bad(self):
        """ test_create_bad """
        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_systemCreate', return_value=456), \
                mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_systemStop', return_value=None):
            with ctrlxdatalayer.system.System("") as system:
                self.assertIsNotNone(system)
                self.assertFalse(system.get_handle() == 123)

    def test_start_false(self):
        """ test_start_false """
        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_systemCreate', return_value=123), \
                mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_systemStop', return_value=None):
            with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_systemStart', return_value=None):
                with ctrlxdatalayer.system.System("") as system:
                    self.assertIsNotNone(system)
                    self.assertTrue(system.get_handle() != 0)
                    system.start(False)

    def test_start_true(self):
        """ test_start_true """
        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_systemCreate', return_value=123), \
                mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_systemStop', return_value=None):
            with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_systemStart', return_value=None):
                with ctrlxdatalayer.system.System("") as system:
                    self.assertIsNotNone(system)
                    self.assertTrue(system.get_handle() != 0)
                    system.start(True)

    def test_stop_false(self):
        """ test_stop_false """
        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_systemCreate', return_value=123):
            with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_systemStop', return_value=None):
                with ctrlxdatalayer.system.System("") as system:
                    self.assertIsNotNone(system)
                    self.assertTrue(system.get_handle() != 0)
                    system.stop(False)

    def test_stop_true(self):
        """ test_stop_true """
        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_systemCreate', return_value=123):
            with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_systemStop', return_value=None):
                with ctrlxdatalayer.system.System("") as system:
                    self.assertIsNotNone(system)
                    self.assertTrue(system.get_handle() != 0)
                    system.stop(True)

    def test_factory(self):
        """ test_factory """
        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_systemCreate', return_value=123), \
                mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_systemStop', return_value=None):
            with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_systemFactory', return_value=111222):
                with ctrlxdatalayer.system.System("") as system:
                    self.assertIsNotNone(system)
                    self.assertTrue(system.get_handle() != 0)
                    factory = system.factory()
                    self.assertIsNotNone(factory)
                    self.assertTrue(factory.get_handle() == 111222)

    def test_factory_bad(self):
        """ test_factory_bad """
        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_systemCreate', return_value=123), \
                mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_systemStop', return_value=None):
            with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_systemFactory', return_value=22221111):
                with ctrlxdatalayer.system.System("") as system:
                    self.assertIsNotNone(system)
                    self.assertTrue(system.get_handle() != 0)
                    factory = system.factory()
                    self.assertIsNotNone(factory)
                    self.assertFalse(factory.get_handle() == 111222)

    def test_json_converter(self):
        """ test_json_converter """
        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_systemCreate', return_value=123), \
                mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_systemStop', return_value=None):
            with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_systemJsonConverter', return_value=3333444):
                with ctrlxdatalayer.system.System("") as system:
                    self.assertIsNotNone(system)
                    self.assertTrue(system.get_handle() != 0)
                    json_conv = system.json_converter()
                    self.assertIsNotNone(json_conv)
                    self.assertTrue(json_conv.get_handle() == 3333444)

    def test_json_converter_bad(self):
        """ test_json_converter_bad """
        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_systemCreate', return_value=123), \
                mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_systemStop', return_value=None):
            with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_systemJsonConverter', return_value=44443333):
                with ctrlxdatalayer.system.System("") as system:
                    self.assertIsNotNone(system)
                    self.assertTrue(system.get_handle() != 0)
                    json_conv = system.json_converter()
                    self.assertIsNotNone(json_conv)
                    self.assertFalse(json_conv.get_handle() == 3333444)

    def test_set_bfbs_path(self):
        """ test_set_bfbs_path """
        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_systemCreate', return_value=123), \
                mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_systemStop', return_value=None):
            with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_systemSetBfbsPath', return_value=None):
                with ctrlxdatalayer.system.System("") as system:
                    self.assertIsNotNone(system)
                    self.assertTrue(system.get_handle() != 0)
                    system.set_bfbs_path("path_test")


if __name__ == '__main__':
    unittest.main()
