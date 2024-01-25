import threading
import typing
import unittest

import ctrlxdatalayer
import ctrlxdatalayer.subscription
import ctrlxdatalayer.system
import tests.test_integration_client
from ctrlxdatalayer.client import Result
from tests.test_utils import client_timeout, is_integration_test

# port 443 is needed
_timeout = client_timeout()

# export INTEGRATION=1
# unset INTEGRATION


@unittest.skipIf(is_integration_test() == False, "no integration test")
class TestClient(tests.test_integration_client.TestClientBase):
    """ TestClient """

    def __init__(self, *args, **kwargs):  # Accept all unrecognized args for delegation
        """ __init__ """
        # Delegate to parent initializer
        super().__init__(*args, **kwargs)
        self.ev = threading.Event()
        self.__cpu = False
        self.__mem = False

    def wait(self):
        """ wait """
        self.ev.wait(10)

    def setUp(self):
        """ setUp """
        self.ev.clear()

    def test_is_connected(self):
        """ test_is_connected """
        print("test_is_connected")
        self.client.set_timeout(ctrlxdatalayer.client.TimeoutSetting.PING, _timeout)
        b = self.client.is_connected()
        self.assertTrue(b)

    def test_create_sub(self):
        """ test_create_sub """

        def cb(result: Result, items: typing.List[ctrlxdatalayer.subscription.NotifyItem], userdata: ctrlxdatalayer.clib.userData_c_void_p):
            pass

        v = ctrlxdatalayer.subscription.create_properties("Hallo")
        with v:
            r, sub = self.client.create_subscription_sync(v, cb)
            self.assertTrue(r == Result.OK)
            sub.close()

    def test_unsubscribe_all(self):
        """ test_unsubscribe_all """

        def cb(result: Result, items: typing.List[ctrlxdatalayer.subscription.NotifyItem], userdata: ctrlxdatalayer.clib.userData_c_void_p):
            pass

        v = ctrlxdatalayer.subscription.create_properties("Hallo")
        with v:
            r, sub = self.client.create_subscription_sync(v, cb)
            self.assertTrue(r == Result.OK)
            sub.unsubscribe_all()
            sub.close()

    def test_subscribe(self):
        """ test_subscribe """

        def cb(result: Result, items: typing.List[ctrlxdatalayer.subscription.NotifyItem], userdata: ctrlxdatalayer.clib.userData_c_void_p):
            print("Sub: result={}, len={}".format(result,
                                                  [0, len(items)][items is not None]))
            if items is not None:
                for i in items:
                    print("  item: data={}, address={}, type={}, time={}, datetime={}".format(
                        i.get_data().get_float32(), i.get_address(), i.get_type(), i.get_timestamp(), ctrlxdatalayer.subscription.to_datetime(i.get_timestamp())))
            self.ev.set()

        v = ctrlxdatalayer.subscription.create_properties("id: Hallo")
        with v:
            r, sub = self.client.create_subscription_sync(v, cb)
            self.assertTrue(r == Result.OK)
            with sub:
                r = sub.subscribe(
                    "framework/metrics/system/cpu-utilisation-percent")
                self.assertTrue(r == Result.OK)
                self.wait()
                self.assertTrue(self.ev.is_set())

    def test_unsubscribe_without(self):
        """ test_unsubscribe_without """

        def cb(result: Result, items: typing.List[ctrlxdatalayer.subscription.NotifyItem], userdata: ctrlxdatalayer.clib.userData_c_void_p):
            pass

        v = ctrlxdatalayer.subscription.create_properties("id: Hallo")
        with v:
            r, sub = self.client.create_subscription_sync(v, cb)
            self.assertTrue(r == Result.OK)
            with sub:
                r = sub.unsubscribe(
                    "framework/metrics/system/cpu-utilisation-percent")
                self.assertTrue(r == Result.OK)

    def test_unsubscribe(self):
        """ test_subscribe """

        def cb(result: Result, items: typing.List[ctrlxdatalayer.subscription.NotifyItem], userdata: ctrlxdatalayer.clib.userData_c_void_p):
            print("Sub: result={}, len={}".format(result,
                                                  [0, len(items)][items is not None]))
            if items is not None:
                for i in items:
                    print("  item: data={}, address={}, type={}, time={}, datetime={}".format(
                        i.get_data().get_float32(), i.get_address(), i.get_type(), i.get_timestamp(), ctrlxdatalayer.subscription.to_datetime(i.get_timestamp())))
            self.ev.set()

        v = ctrlxdatalayer.subscription.create_properties("id: Hallo")
        with v:
            r, sub = self.client.create_subscription_sync(v, cb)
            self.assertTrue(r == Result.OK)
            with sub:
                r = sub.subscribe(
                    "framework/metrics/system/cpu-utilisation-percent")
                self.assertTrue(r == Result.OK)
                self.wait()
                self.assertTrue(self.ev.is_set())
                r = sub.unsubscribe(
                    "framework/metrics/system/cpu-utilisation-percent")
                self.assertTrue(r == Result.OK)

    def test_subscribe_multi(self):
        """ test_subscribe_multi """

        def cb(result: Result, items: typing.List[ctrlxdatalayer.subscription.NotifyItem], userdata: ctrlxdatalayer.clib.userData_c_void_p):
            print("Sub: result={}, len={}".format(result,
                                                  [0, len(items)][items is not None]))
            if items is not None:
                for i in items:
                    print("  item: data={}, address={}, type={}, time={}, datetime={}".format(
                        i.get_data().get_float32(), i.get_address(), i.get_type(), i.get_timestamp(), ctrlxdatalayer.subscription.to_datetime(i.get_timestamp())))
                    if i.get_address().find("cpu-utilisation-percent") != -1:
                        self.__cpu = True
                    if i.get_address().find("memused-percent") != -1:
                        self.__mem = True
            if self.__cpu and self.__mem:
                self.ev.set()

        v = ctrlxdatalayer.subscription.create_properties("id: Hallo")
        with v:
            r, sub = self.client.create_subscription_sync(v, cb)
            self.assertTrue(r == Result.OK)
            with sub:
                self.__cpu = False
                self.__mem = False
                l = ["framework/metrics/system/cpu-utilisation-percent",
                     "framework/metrics/system/memused-percent"]
                r = sub.subscribe_multi(l)
                self.assertTrue(r == Result.OK)
                self.wait()
                self.assertTrue(self.ev.is_set())

    def test_unsubscribe_multi_without(self):
        """ test_subscribe_multi """

        def cb(result: Result, items: typing.List[ctrlxdatalayer.subscription.NotifyItem], userdata: ctrlxdatalayer.clib.userData_c_void_p):
            pass
        v = ctrlxdatalayer.subscription.create_properties("id: Hallo")
        with v:
            r, sub = self.client.create_subscription_sync(v, cb)
            self.assertTrue(r == Result.OK)
            with sub:
                self.__cpu = False
                self.__mem = False
                l = ["framework/metrics/system/cpu-utilisation-percent",
                     "framework/metrics/system/memused-percent"]
                r = sub.unsubscribe_multi(l)
                self.assertTrue(r == Result.OK)

    def test_unsubscribe_multi(self):
        """ test_unsubscribe_multi """

        def cb(result: Result, items: typing.List[ctrlxdatalayer.subscription.NotifyItem], userdata: ctrlxdatalayer.clib.userData_c_void_p):
            print("Sub: result={}, len={}".format(result,
                                                  [0, len(items)][items is not None]))
            if items is not None:
                for i in items:
                    print("  item: data={}, address={}, type={}, time={}, datetime={}".format(
                        i.get_data().get_float32(), i.get_address(), i.get_type(), i.get_timestamp(), ctrlxdatalayer.subscription.to_datetime(i.get_timestamp())))
                    if i.get_address().find("cpu-utilisation-percent") != -1:
                        self.__cpu = True
                    if i.get_address().find("memused-percent") != -1:
                        self.__mem = True
            if self.__cpu and self.__mem:
                self.ev.set()

        v = ctrlxdatalayer.subscription.create_properties("id: Hallo")
        with v:
            r, sub = self.client.create_subscription_sync(v, cb)
            self.assertTrue(r == Result.OK)
            with sub:
                self.__cpu = False
                self.__mem = False
                l = ["framework/metrics/system/cpu-utilisation-percent",
                     "framework/metrics/system/memused-percent"]
                r = sub.subscribe_multi(l)
                self.assertTrue(r == Result.OK)
                self.wait()
                self.assertTrue(self.ev.is_set())
                r = sub.unsubscribe_multi(l)
                self.assertTrue(r == Result.OK)

    def test_unsubscribe_multi_cpu(self):
        """ test_unsubscribe_multi_cpu """

        def cb(result: Result, items: typing.List[ctrlxdatalayer.subscription.NotifyItem], userdata: ctrlxdatalayer.clib.userData_c_void_p):
            print("Sub: result={}, len={}".format(result,
                                                  [0, len(items)][items is not None]))
            if items is not None:
                for i in items:
                    print("  item: data={}, address={}, type={}, time={}, datetime={}".format(
                        i.get_data().get_float32(), i.get_address(), i.get_type(), i.get_timestamp(), ctrlxdatalayer.subscription.to_datetime(i.get_timestamp())))
                    if i.get_address().find("cpu-utilisation-percent") != -1:
                        self.__cpu = True
                    if i.get_address().find("memused-percent") != -1:
                        self.__mem = True
            if self.__cpu and self.__mem:
                self.ev.set()

        v = ctrlxdatalayer.subscription.create_properties("id: Hallo")
        with v:
            r, sub = self.client.create_subscription_sync(v, cb)
            self.assertTrue(r == Result.OK)
            with sub:
                self.__cpu = False
                self.__mem = False
                l = ["framework/metrics/system/cpu-utilisation-percent",
                     "framework/metrics/system/memused-percent"]
                r = sub.subscribe_multi(l)
                self.assertTrue(r == Result.OK)
                self.wait()
                self.assertTrue(self.ev.is_set())
                l = ["framework/metrics/system/cpu-utilisation-percent"]
                r = sub.unsubscribe_multi(l)
                self.assertTrue(r == Result.OK)

    def test_unsubscribe_multi_mem(self):
        """ test_unsubscribe_multi_mem """

        def cb(result: Result, items: typing.List[ctrlxdatalayer.subscription.NotifyItem], userdata: ctrlxdatalayer.clib.userData_c_void_p):
            print("Sub: result={}, len={}".format(result,
                                                  [0, len(items)][items is not None]))
            if items is not None:
                for i in items:
                    print("  item: data={}, address={}, type={}, time={}, datetime={}".format(
                        i.get_data().get_float32(), i.get_address(), i.get_type(), i.get_timestamp(), ctrlxdatalayer.subscription.to_datetime(i.get_timestamp())))
                    if i.get_address().find("cpu-utilisation-percent") != -1:
                        self.__cpu = True
                    if i.get_address().find("memused-percent") != -1:
                        self.__mem = True
            if self.__cpu and self.__mem:
                self.ev.set()

        v = ctrlxdatalayer.subscription.create_properties("id: Hallo")
        with v:
            r, sub = self.client.create_subscription_sync(v, cb)
            self.assertTrue(r == Result.OK)
            with sub:
                self.__cpu = False
                self.__mem = False
                l = ["framework/metrics/system/cpu-utilisation-percent",
                     "framework/metrics/system/memused-percent"]
                r = sub.subscribe_multi(l)
                self.assertTrue(r == Result.OK)
                self.wait()
                self.assertTrue(self.ev.is_set())
                l = ["framework/metrics/system/memused-percent"]
                r = sub.unsubscribe_multi(l)
                self.assertTrue(r == Result.OK)


if __name__ == '__main__':
    unittest.main()
