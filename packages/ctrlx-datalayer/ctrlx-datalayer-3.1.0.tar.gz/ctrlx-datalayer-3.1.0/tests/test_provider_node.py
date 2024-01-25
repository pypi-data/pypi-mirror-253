import faulthandler
import unittest
from unittest import mock

import ctrlxdatalayer.clib
from ctrlxdatalayer.clib_provider_node import (C_DLR_PROVIDER_NODE_CALLBACK,
                                               C_DLR_PROVIDER_NODE_CALLBACKDATA)
from ctrlxdatalayer.provider_node import (NodeCallback, NodeFunction,
                                          NodeFunctionData, ProviderNode,
                                          ProviderNodeCallbacks)
from ctrlxdatalayer.variant import Result, Variant
from tests.test_node import TestNode

faulthandler.enable()


class _CallbackProviderNode(ProviderNode):
    """
    _CallbackProviderNode
    """

    def create_func_data(self, cb: NodeFunctionData):
        """ create_cb """
        return self._test_function_data(cb)

    def create_func(self, cb: NodeFunction):
        """ create_cb """
        return self._test_function(cb)


class TestProviderNode(unittest.TestCase):
    """ TestProviderNode """

    def test_provider_node_none(self):
        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_providerNodeCreate', return_value=None), \
                mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_providerNodeDelete', return_value=None):
            cb = ProviderNodeCallbacks(None, None, None, None, None, None)
            with ProviderNode(cb) as node:
                self.assertIsNotNone(node)

    def test_provider_node(self):
        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_providerNodeCreate', return_value=None), \
                mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_providerNodeDelete', return_value=None):
            n = TestNode()
            with ProviderNode(n.cbs) as node:
                self.assertIsNotNone(node)

    def test_provider_node_close(self):
        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_providerNodeCreate', return_value=None), \
                mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_providerNodeDelete', return_value=None):
            n = TestNode()
            with ProviderNode(n.cbs) as node:
                self.assertIsNotNone(node)
                node.close()

    def test_provider_node_func(self):
        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_providerNodeCreate', return_value=None), \
                mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_providerNodeDelete', return_value=None):
            n = TestNode()
            with _CallbackProviderNode(n.cbs) as node:
                self.assertIsNotNone(node)

                # callback from datalayer
                def func(userdata: ctrlxdatalayer.clib.userData_c_void_p, address: str, cb: NodeCallback):
                    print("callback in Python: ", address)
                    self.check_counter = self.check_counter + 1
                    cb(Result.OK, None)

                # confirment to datalayer
                def resp_call(callbackdata: C_DLR_PROVIDER_NODE_CALLBACKDATA, result: ctrlxdatalayer.clib.C_DLR_RESULT, data: ctrlxdatalayer.clib_variant.C_DLR_VARIANT):
                    print("resp callback", result)
                    self.check_counter = self.check_counter + 1

                call_back = node.create_func(func)
                self.check_counter = 0
                call_back(None,
                          "address/test".encode('utf-8'),
                          C_DLR_PROVIDER_NODE_CALLBACK(resp_call),
                          None)
                self.assertTrue(self.check_counter == 2)

    def test_provider_node_func_fix(self):
        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_providerNodeCreate', return_value=None), \
                mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_providerNodeDelete', return_value=None):
            n = TestNode()
            with _CallbackProviderNode(n.cbs) as node:
                self.assertIsNotNone(node)

                # callback from datalayer
                def func(userdata: ctrlxdatalayer.clib.userData_c_void_p, address: str, cb: NodeCallback):
                    print("callback in Python: ", address)
                    self.check_counter = self.check_counter + 1
                    with Variant() as data:
                        cb(Result.OK, data)

                # confirment to datalayer
                def resp_call(callbackdata: C_DLR_PROVIDER_NODE_CALLBACKDATA, result: ctrlxdatalayer.clib.C_DLR_RESULT, data: ctrlxdatalayer.clib_variant.C_DLR_VARIANT):
                    print("resp callback", result)
                    self.check_counter = self.check_counter + 1

                call_back = node.create_func(func)
                self.check_counter = 0
                call_back(None,
                          "address/test".encode('utf-8'),
                          C_DLR_PROVIDER_NODE_CALLBACK(resp_call),
                          None)
                self.assertTrue(self.check_counter == 2)

    def test_provider_node_func_data(self):
        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_providerNodeCreate', return_value=None), \
                mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_providerNodeDelete', return_value=None):
            n = TestNode()
            with _CallbackProviderNode(n.cbs) as node:
                self.assertIsNotNone(node)

                # callback from datalayer
                def func(userdata: ctrlxdatalayer.clib.userData_c_void_p, address: str, data: Variant, cb: NodeCallback):
                    print("callback in Python: ", address, data.get_int16())
                    self.check_counter = self.check_counter + 1
                    cb(Result.OK, None)

                # confirment to datalayer
                def resp_call(callbackdata: C_DLR_PROVIDER_NODE_CALLBACKDATA, result: ctrlxdatalayer.clib.C_DLR_RESULT, data: ctrlxdatalayer.clib_variant.C_DLR_VARIANT):
                    print("resp callback", result)
                    self.check_counter = self.check_counter + 1

                call_back = node.create_func_data(func)
                self.check_counter = 0
                with Variant() as v:
                    v.set_int16(123)
                    call_back(None,
                              "address/test".encode('utf-8'),
                              v.get_handle(),
                              C_DLR_PROVIDER_NODE_CALLBACK(resp_call),
                              None)
                self.assertTrue(self.check_counter == 2)

    def test_provider_node_func_userdata(self):
        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_providerNodeCreate', return_value=None), \
                mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_providerNodeDelete', return_value=None):
            n = TestNode()
            with _CallbackProviderNode(n.cbs, 1234) as node:
                self.assertIsNotNone(node)

                # callback from datalayer
                def func(userdata: ctrlxdatalayer.clib.userData_c_void_p, address: str, cb: NodeCallback):
                    print("callback in Python: ", address, userdata)
                    if userdata == 1234:
                        self.check_counter = self.check_counter + 1
                    cb(Result.OK, None)

                # confirment to datalayer
                def resp_call(callbackdata: C_DLR_PROVIDER_NODE_CALLBACKDATA, result: ctrlxdatalayer.clib.C_DLR_RESULT, data: ctrlxdatalayer.clib_variant.C_DLR_VARIANT):
                    print("resp callback", result)
                    self.check_counter = self.check_counter + 1

                call_back = node.create_func(func)
                self.check_counter = 0
                call_back(1234,
                          "address/test".encode('utf-8'),
                          C_DLR_PROVIDER_NODE_CALLBACK(resp_call),
                          None)
                self.assertTrue(self.check_counter == 2)

    def test_provider_node_func_data_userdata(self):
        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_providerNodeCreate', return_value=None), \
                mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_providerNodeDelete', return_value=None):
            n = TestNode()
            with _CallbackProviderNode(n.cbs, 4567) as node:
                self.assertIsNotNone(node)

                # callback from datalayer
                def func(userdata: ctrlxdatalayer.clib.userData_c_void_p, address: str, data: Variant, cb: NodeCallback):
                    print("callback in Python: ", address,
                          userdata, data.get_int16())
                    if userdata == 4567:
                        self.check_counter = self.check_counter + 1
                    cb(Result.OK, None)

                # confirment to datalayer
                def resp_call(callbackdata: C_DLR_PROVIDER_NODE_CALLBACKDATA, result: ctrlxdatalayer.clib.C_DLR_RESULT, data: ctrlxdatalayer.clib_variant.C_DLR_VARIANT):
                    print("resp callback", result)
                    self.check_counter = self.check_counter + 1

                call_back = node.create_func_data(func)
                self.check_counter = 0
                with Variant() as v:
                    v.set_int16(123)
                    call_back(4567,
                              "address/test".encode('utf-8'),
                              v.get_handle(),
                              C_DLR_PROVIDER_NODE_CALLBACK(resp_call),
                              None)
                self.assertTrue(self.check_counter == 2)


if __name__ == '__main__':
    unittest.main()
