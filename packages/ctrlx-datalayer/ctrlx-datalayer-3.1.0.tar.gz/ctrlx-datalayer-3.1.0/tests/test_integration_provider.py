import threading
import unittest

import ctrlxdatalayer
import ctrlxdatalayer.system
from ctrlxdatalayer.client import Result
from tests.test_node import TestNode
from tests.test_utils import (client_connection, client_timeout,
                              is_integration_test, provider_connection)

# port 443 is needed
_connectionClient = client_connection()
_connectionProvider = provider_connection()
_timeout = client_timeout()

# export INTEGRATION=1
# unset INTEGRATION


@unittest.skipIf(is_integration_test() == False, "no integration test")
class TestProviderBase(unittest.TestCase):
    """ TestProviderBase """

    @classmethod
    def setUpClass(cls):
        """ setUpClass """
        print("Using ctrlX CORE as provider: ", _connectionClient)
        cls.system = ctrlxdatalayer.system.System("")
        cls.system.start(False)
        cls.provider = cls.system.factory().create_provider(_connectionProvider)

    @classmethod
    def tearDownClass(cls):
        """ tearDownClass """
        print("tearDownClass")
        cls.provider.close()
        cls.system.close()


@unittest.skipIf(is_integration_test() == False, "no integration test")
class TestProvider(TestProviderBase):
    """ TestProvider """

    def test_is_connected(self):
        """ test_is_connected """
        print("test_is_connected")
        self.assertFalse(self.provider.is_connected())
        r = self.provider.start()
        self.assertTrue(r == Result.OK)
        self.assertTrue(self.provider.is_connected())

        threading.Event().wait(2)
        print(">stop test_is_connected")
        r = self.provider.stop()
        print("<stop test_is_connected")
        self.assertTrue(r == Result.OK)
        self.assertFalse(self.provider.is_connected())

    def test_register_node(self):
        """ test_register_node """
        print("test_register_node")
        with ctrlxdatalayer.provider_node.ProviderNode(TestNode().cbs) as node:
            r = self.provider.register_node("pydata/test", node)
            self.assertTrue(r == Result.OK)

    def test_unregister_node(self):
        """ test_unregister_node """
        print("test_unregister_node")
        with ctrlxdatalayer.provider_node.ProviderNode(TestNode().cbs) as node:
            r = self.provider.register_node("pydata/test", node)
            self.assertTrue(r == Result.OK)

            r = self.provider.unregister_node("pydata/test")
            self.assertTrue(r == Result.OK)

    def test_register_type(self):
        """ test_register_type """
        print("test_register_type")
        self.provider.start()
        r = self.provider.register_type(
            "types/pydata/test", "tests/fbs/sampleSchema.bfbs")
        self.assertTrue(r == Result.OK)
        self.provider.stop()

    def test_unregister_type(self):
        """ test_unregister_type """
        print("test_unregister_type")
        self.provider.start()
        r = self.provider.unregister_type(
            "types/pydata/test")
        self.assertTrue(r == Result.OK)
        self.provider.stop()

    def test_set_timeout_node(self):
        """ test_set_timeout_node """
        print("test_set_timeout_node")
        with ctrlxdatalayer.provider_node.ProviderNode(TestNode().cbs) as node:
            r = self.provider.register_node("pydata/test", node)
            self.assertTrue(r == Result.OK)
            r = self.provider.set_timeout_node(node, _timeout)
            self.assertTrue(r == Result.OK)

    def test_set_timeout_node_none(self):
        """ test_set_timeout_node_none """
        print("test_set_timeout_node_none")
        r = self.provider.set_timeout_node(None, _timeout)
        self.assertTrue(r == Result.FAILED)

    def test_get_token(self):
        """ test_get_token """
        print("test_get_token")
        with self.provider.get_token() as v:
            self.assertIsNotNone(v)


if __name__ == '__main__':
    unittest.main()
