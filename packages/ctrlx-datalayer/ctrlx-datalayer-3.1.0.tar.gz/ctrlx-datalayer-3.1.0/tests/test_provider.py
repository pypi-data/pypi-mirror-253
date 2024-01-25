import faulthandler
import unittest
from unittest import mock

import ctrlxdatalayer
import ctrlxdatalayer.clib_provider
from ctrlxdatalayer.provider import Provider
from ctrlxdatalayer.provider_node import ProviderNode
from ctrlxdatalayer.variant import Result, Variant
from tests.test_node import TestNode

faulthandler.enable()


class TestProvider(unittest.TestCase):
    """ TestProvider """

    def setUp(self):
        """ setUp """
        self.patcher_provider_stop = mock.patch(
            'ctrlxdatalayer.clib.libcomm_datalayer.DLR_providerStop', return_value=None)
        self.patcher_provider_stop.start()
        self.patcher_provider_delete = mock.patch(
            'ctrlxdatalayer.clib.libcomm_datalayer.DLR_providerDelete', return_value=None)
        self.patcher_provider_delete.start()

    def tearDown(self):
        """ tearDown """
        self.patcher_provider_stop.stop()
        self.patcher_provider_delete.start()

    def test_factory_create_provider(self):
        """ test_factory_create_provider """
        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_systemDelete', return_value=None), \
                mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_systemCreate', return_value=123), \
                mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_systemStop', return_value=None), \
                mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_systemFactory', return_value=111222):
            with ctrlxdatalayer.system.System("") as system:
                self.assertIsNotNone(system)
                self.assertTrue(system.get_handle() != 0)
                factory = system.factory()
                self.assertIsNotNone(factory)
                with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_factoryCreateProvider', return_value=33334444):
                    provider = factory.create_provider("")
                    self.assertIsNotNone(provider)

    def test_register_type(self):
        """ test_register_type """
        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_providerRegisterType', return_value=Result.OK):
            with Provider("") as provider:
                self.assertIsNotNone(provider)
                result = provider.register_type("", "")
                self.assertTrue(result == Result.OK)

            with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_providerRegisterType', return_value=Result.FAILED):
                with Provider("") as provider:
                    self.assertIsNotNone(provider)
                    result = provider.register_type("", "")
                    self.assertTrue(result == Result.FAILED)

    def test_unregister_type(self):
        """ test_unregister_type """
        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_providerUnregisterType', return_value=Result.OK):
            with Provider("") as provider:
                self.assertIsNotNone(provider)
                result = provider.unregister_type("")
                self.assertTrue(result == Result.OK)

        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_providerUnregisterType', return_value=Result.FAILED):
            with Provider("") as provider:
                self.assertIsNotNone(provider)
                result = provider.unregister_type("")
                self.assertTrue(result == Result.FAILED)

    def test_register_node_ok(self):
        """ test_register_node_ok """
        cbs = TestNode().cbs

        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_providerRegisterNode', return_value=Result.OK):
            with ProviderNode(cbs) as providernode, \
                    Provider("") as provider:
                self.assertIsNotNone(provider)
                result = provider.register_node("", providernode)
                self.assertTrue(result == Result.OK)

    def test_register_node_failed(self):
        """ test_register_node_failed """
        cbs = TestNode().cbs
        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_providerRegisterNode', return_value=Result.FAILED):
            with ProviderNode(cbs) as providernode, \
                    Provider("") as provider:
                self.assertIsNotNone(provider)
                result = provider.register_node("", providernode)
                self.assertTrue(result == Result.FAILED)

    def test_unregister_node(self):
        """ test_unregister_node """
        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_providerUnregisterNode', return_value=Result.OK):
            with Provider("") as provider:
                self.assertIsNotNone(provider)
                result = provider.unregister_node("")
                self.assertTrue(result == Result.OK)

        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_providerUnregisterNode', return_value=Result.FAILED):
            with Provider("") as provider:
                self.assertIsNotNone(provider)
                result = provider.unregister_node("")
                self.assertTrue(result == Result.FAILED)

    def test_set_timeout_node_ok(self):
        """ test_set_timeout_node_ok """
        cbs = TestNode().cbs
        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_providerSetTimeoutNode', return_value=Result.OK):
            with ProviderNode(cbs) as providernode, \
                    Provider("") as provider:
                self.assertIsNotNone(provider)
                result = provider.set_timeout_node(
                    providernode, 1000)
                self.assertTrue(result == Result.OK)

    def test_set_timeout_node_failed(self):
        """ test_set_timeout_node_failed """
        cbs = TestNode().cbs
        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_providerSetTimeoutNode', return_value=Result.FAILED):
            with ProviderNode(cbs) as providernode, \
                    Provider("") as provider:
                self.assertIsNotNone(provider)
                result = provider.set_timeout_node(
                    providernode, 1000)
                self.assertTrue(result == Result.FAILED)

    def test_start(self):
        """ test_start """
        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_providerStart', return_value=Result.OK):
            with Provider("") as provider:
                self.assertIsNotNone(provider)
                result = provider.start()
                self.assertTrue(result == Result.OK)

        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_providerStart', return_value=Result.FAILED):
            with Provider("") as provider:
                self.assertIsNotNone(provider)
                result = provider.start()
                self.assertTrue(result == Result.FAILED)

    def test_stop(self):
        """ test_stop """
        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_providerStop', return_value=Result.OK):
            with Provider("") as provider:
                self.assertIsNotNone(provider)
                result = provider.stop()
                self.assertTrue(result == Result.OK)

        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_providerStop', return_value=Result.FAILED):
            with Provider("") as provider:
                self.assertIsNotNone(provider)
                result = provider.stop()
                self.assertTrue(result == Result.FAILED)

    def test_is_connected(self):
        """ test_is_connected """
        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_providerIsConnected', return_value=True):
            with Provider("") as provider:
                self.assertIsNotNone(provider)
                result = provider.is_connected()
                self.assertTrue(result)

        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_providerIsConnected', return_value=False):
            with Provider("") as provider:
                self.assertIsNotNone(provider)
                result = provider.is_connected()
                self.assertFalse(result)

    def test_get_token(self):
        """ test_get_token """
        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_providerGetToken', return_value=0xcafe):
            with Provider("") as provider:
                self.assertIsNotNone(provider)
                with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_variantDelete', return_value=None):
                    with provider.get_token() as result:
                        self.assertTrue(result.get_handle() == 0xcafe)

    def test_register_type_variant(self):
        """ register_type_variant """
        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_providerRegisterTypeVariant', return_value=Result.OK):
            with Variant() as data:
                with Provider("") as provider:
                    self.assertIsNotNone(provider)
                    result = provider.register_type_variant("", data)
                    self.assertTrue(result == Result.OK)

                with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_providerRegisterTypeVariant', return_value=Result.FAILED):
                    with Provider("") as provider:
                        self.assertIsNotNone(provider)
                        result = provider.register_type_variant("", data)
                        self.assertTrue(result == Result.FAILED)


if __name__ == '__main__':
    unittest.main()
