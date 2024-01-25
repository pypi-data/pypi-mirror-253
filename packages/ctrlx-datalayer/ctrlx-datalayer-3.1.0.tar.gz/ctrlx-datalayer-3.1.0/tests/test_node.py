import typing
import unittest

import ctrlxdatalayer.clib
from ctrlxdatalayer.provider_node import NodeCallback, ProviderNodeCallbacks
from ctrlxdatalayer.variant import Result, Variant


class TestNode:
    """ TestNode """
    pyFloat: float = 0.123456789

    def __init__(self):
        """ __init__ """
        self.cbs = ProviderNodeCallbacks(
            self.__on_create,
            self.__on_remove,
            self.__on_browse,
            self.__on_read,
            self.__on_write,
            self.__on_metadata
        )

    def __on_create(self, userdata: ctrlxdatalayer.clib.userData_c_void_p, address: str, data: Variant, cb: NodeCallback):
        """ __on_create """
        # print("OnCreate: ", address)
        self.pyFloat = 0.369
        cb(Result.OK, None)

    def __on_remove(self, userdata: ctrlxdatalayer.clib.userData_c_void_p, address: str, cb: NodeCallback):
        """ __on_remove """
        # print("OnRemove: ", address)
        self.pyFloat = 0
        cb(Result.OK, None)

    def __on_browse(self, userdata: ctrlxdatalayer.clib.userData_c_void_p, address: str, cb: NodeCallback):
        """ __on_browse """
        print("OnBrowse: ", address)
        with Variant() as new_data:
            new_data.set_array_string([])
            cb(Result.OK, new_data)

    def __on_read(self, userdata: ctrlxdatalayer.clib.userData_c_void_p, address: str, data: Variant, cb: NodeCallback):
        """ __on_read """
        print("OnRead: ", address)
        with Variant() as new_data:
            new_data.set_float32(self.pyFloat)
            cb(Result.OK, new_data)

    def __on_write(self, userdata: ctrlxdatalayer.clib.userData_c_void_p, address: str, data: Variant, cb: NodeCallback):
        """ __on_write """
        # print("OnWrite: ", address)
        self.pyFloat = data.get_float32()
        cb(Result.OK, data)

    def __on_metadata(self, userdata: ctrlxdatalayer.clib.userData_c_void_p, address: str, cb: NodeCallback):
        """ __on_metadata """
        # print("OnMetadata: ", address)
        cb(Result.OK, None)


class TestProvider(unittest.TestCase):
    """ TestProvider """

    def test_node(self):
        """ test_node """
        def cb(r: Result, v: typing.Optional[Variant]):
            print("cb result=", r)

        n = TestNode()
        with Variant() as v:
            self.assertIsNotNone(n)
            n.cbs.on_browse(123, "Hallo", cb)
            n.cbs.on_create(456, "Hallo", v, cb)
            n.cbs.on_metadata(123, "Hallo", cb)
            n.cbs.on_read(456, "Hallo", v, cb)
            n.cbs.on_write(456, "Hallo", v, cb)
            n.cbs.on_remove(123, "Hallo", cb)


if __name__ == '__main__':
    unittest.main()
