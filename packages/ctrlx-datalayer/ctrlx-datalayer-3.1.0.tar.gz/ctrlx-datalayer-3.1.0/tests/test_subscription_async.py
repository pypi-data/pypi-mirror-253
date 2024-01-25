import ctypes
import faulthandler
import typing
import unittest
from unittest import mock

import ctrlxdatalayer
import ctrlxdatalayer.clib
import ctrlxdatalayer.clib_client
import ctrlxdatalayer.client
import ctrlxdatalayer.subscription
from ctrlxdatalayer.client import Client
from ctrlxdatalayer.variant import Result, Variant

faulthandler.enable()


class TestSubBaseAsync(unittest.TestCase):
    """
    TestSubBaseAsync
    """

    def setUp(self):
        """ setUp """
        self.patcher_client_delete = mock.patch(
            'ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientDelete', return_value=None)
        self.patcher_client_delete.start()

    def tearDown(self):
        """  """
        self.patcher_client_delete.stop()


class TestSubAsync(TestSubBaseAsync):
    """
    TestSubSync
    """

    def test_close(self):
        """ test_close """
        with Client(112233) as client:
            client.close()

    def test_create(self):
        """ test_create """

        def cb(result: Result, data: typing.Optional[Variant], userdata: ctrlxdatalayer.clib.userData_c_void_p):
            pass

        def cnb(result: Result, items: typing.List[ctrlxdatalayer.subscription.NotifyItem], userdata: ctrlxdatalayer.clib.userData_c_void_p):
            pass

        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientCreateSubscriptionAsync', return_value=Result.OK), \
                mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientUnsubscribeAllAsync', return_value=Result.OK):
            with Client(112233) as client:
                with Variant() as v:
                    r, sub = client.create_subscription_async(v, cnb, cb)
                    self.assertTrue(r == Result.OK)
                    sub.close()

    def test_create_fail(self):
        """ test_create """

        def cb(result: Result, data: typing.Optional[Variant], userdata: ctrlxdatalayer.clib.userData_c_void_p):
            pass

        def cnb(result: Result, items: typing.List[ctrlxdatalayer.subscription.NotifyItem], userdata: ctrlxdatalayer.clib.userData_c_void_p):
            pass

        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientCreateSubscriptionAsync', return_value=Result.FAILED), \
                mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientUnsubscribeAllAsync', return_value=Result.OK):
            with Client(112233) as client:
                with Variant() as v:
                    r, sub = client.create_subscription_async(v, cnb, cb)
                    self.assertTrue(r == Result.FAILED)
                    sub.close()

    def test_close_all(self):
        """ test_close_all """

        def cb(result: Result, data: typing.Optional[Variant], userdata: ctrlxdatalayer.clib.userData_c_void_p):
            pass

        def cnb(result: Result, items: typing.List[ctrlxdatalayer.subscription.NotifyItem], userdata: ctrlxdatalayer.clib.userData_c_void_p):
            pass

        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientCreateSubscriptionAsync', return_value=Result.OK), \
                mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientUnsubscribeAllAsync', return_value=Result.OK):
            client = Client(112233)
            with Variant() as v:
                r, sub = client.create_subscription_async(v, cnb, cb)
                self.assertTrue(r == Result.OK)
                self.assertIsNotNone(sub)
            client.close()  # here close all subscriptions

    def test_unsubscribe_all(self):
        """ test_unsubscribe_all """

        def cb(result: Result, data: typing.Optional[Variant], userdata: ctrlxdatalayer.clib.userData_c_void_p):
            pass

        def cnb(result: Result, items: typing.List[ctrlxdatalayer.subscription.NotifyItem], userdata: ctrlxdatalayer.clib.userData_c_void_p):
            pass

        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientCreateSubscriptionAsync', return_value=Result.OK), \
                mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientUnsubscribeAllAsync', return_value=Result.OK):
            with Client(112233) as client:
                with Variant() as v:
                    r, sub = client.create_subscription_async(v, cnb, cb)
                    self.assertTrue(r == Result.OK)
                    r = sub.unsubscribe_all(cb)
                    self.assertTrue(r == Result.OK)
                    sub.close()

    def test_unsubscribe_all_fail(self):
        """ test_unsubscribe_all_fail """

        def cb(result: Result, data: typing.Optional[Variant], userdata: ctrlxdatalayer.clib.userData_c_void_p):
            pass

        def cnb(result: Result, items: typing.List[ctrlxdatalayer.subscription.NotifyItem], userdata: ctrlxdatalayer.clib.userData_c_void_p):
            pass

        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientCreateSubscriptionAsync', return_value=Result.OK), \
                mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientUnsubscribeAllAsync', return_value=Result.FAILED):
            with Client(112233) as client:
                with Variant() as v:
                    r, sub = client.create_subscription_async(v, cnb, cb)
                    self.assertTrue(r == Result.OK)
                    r = sub.unsubscribe_all(cb)
                    self.assertTrue(r == Result.FAILED)
                    sub.close()

    def test_subscribe(self):
        """ test_subscribe """
        def cb(result: Result, data: typing.Optional[Variant], userdata: ctrlxdatalayer.clib.userData_c_void_p):
            pass

        def cnb(result: Result, items: typing.List[ctrlxdatalayer.subscription.NotifyItem], userdata: ctrlxdatalayer.clib.userData_c_void_p):
            pass

        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientCreateSubscriptionAsync', return_value=Result.OK), \
                mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientUnsubscribeAllAsync', return_value=Result.OK), \
                mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientSubscribeAsync', return_value=Result.OK):
            with Client(112233) as client:
                with Variant() as v:
                    r, sub = client.create_subscription_async(v, cnb, cb)
                    self.assertTrue(r == Result.OK)
                    with sub:
                        r = sub.subscribe("test/value", cb)
                        self.assertTrue(r == Result.OK)

    def test_subscribe_fail(self):
        """ test_subscribe_fail """
        def cb(result: Result, data: typing.Optional[Variant], userdata: ctrlxdatalayer.clib.userData_c_void_p):
            pass

        def cnb(result: Result, items: typing.List[ctrlxdatalayer.subscription.NotifyItem], userdata: ctrlxdatalayer.clib.userData_c_void_p):
            pass

        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientCreateSubscriptionAsync', return_value=Result.OK), \
                mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientUnsubscribeAllAsync', return_value=Result.OK), \
                mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientSubscribeAsync', return_value=Result.FAILED):
            with Client(112233) as client:
                with Variant() as v:
                    r, sub = client.create_subscription_async(v, cnb, cb)
                    self.assertTrue(r == Result.OK)
                    with sub:
                        r = sub.subscribe("test/value", cb)
                        self.assertTrue(r == Result.FAILED)

    def test_unsubscribe(self):
        """ test_unsubscribe """

        def cb(result: Result, items: typing.List[ctrlxdatalayer.subscription.NotifyItem], userdata: ctrlxdatalayer.clib.userData_c_void_p):
            pass

        def cnb(result: Result, items: typing.List[ctrlxdatalayer.subscription.NotifyItem], userdata: ctrlxdatalayer.clib.userData_c_void_p):
            pass

        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientCreateSubscriptionAsync', return_value=Result.OK), \
                mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientUnsubscribeAllAsync', return_value=Result.OK), \
                mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientUnsubscribeAsync', return_value=Result.OK):
            with Client(112233) as client:
                with Variant() as v:
                    r, sub = client.create_subscription_async(v, cnb, cb)
                    self.assertTrue(r == Result.OK)
                    with sub:
                        r = sub.unsubscribe("test/value", cb)
                        self.assertTrue(r == Result.OK)

    def test_unsubscribe_fail(self):
        """ test_unsubscribe_fail """

        def cb(result: Result, items: typing.List[ctrlxdatalayer.subscription.NotifyItem], userdata: ctrlxdatalayer.clib.userData_c_void_p):
            pass

        def cnb(result: Result, items: typing.List[ctrlxdatalayer.subscription.NotifyItem], userdata: ctrlxdatalayer.clib.userData_c_void_p):
            pass

        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientCreateSubscriptionAsync', return_value=Result.OK), \
                mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientUnsubscribeAllAsync', return_value=Result.OK), \
                mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientUnsubscribeAsync', return_value=Result.FAILED):
            with Client(112233) as client:
                with Variant() as v:
                    r, sub = client.create_subscription_async(v, cnb, cb)
                    self.assertTrue(r == Result.OK)
                    with sub:
                        r = sub.unsubscribe("test/value", cb)
                        self.assertTrue(r == Result.FAILED)

    def test_subscribe_multi(self):
        """ test_subscribe_multi """

        def cb(result: Result, items: typing.List[ctrlxdatalayer.subscription.NotifyItem], userdata: ctrlxdatalayer.clib.userData_c_void_p):
            pass

        def cnb(result: Result, items: typing.List[ctrlxdatalayer.subscription.NotifyItem], userdata: ctrlxdatalayer.clib.userData_c_void_p):
            pass

        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientCreateSubscriptionAsync', return_value=Result.OK), \
                mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientUnsubscribeAllAsync', return_value=Result.OK), \
                mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientSubscribeMultiAsync', return_value=Result.OK):
            with Client(112233) as client:
                with Variant() as v:
                    r, sub = client.create_subscription_async(v, cnb, cb)
                    self.assertTrue(r == Result.OK)
                    with sub:
                        l = ["test/value", "test/value1"]
                        r = sub.subscribe_multi(l, cb)
                        self.assertTrue(r == Result.OK)

    def test_subscribe_multi_fail(self):
        """ test_subscribe_multi_fail """

        def cb(result: Result, items: typing.List[ctrlxdatalayer.subscription.NotifyItem], userdata: ctrlxdatalayer.clib.userData_c_void_p):
            pass

        def cnb(result: Result, items: typing.List[ctrlxdatalayer.subscription.NotifyItem], userdata: ctrlxdatalayer.clib.userData_c_void_p):
            pass

        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientCreateSubscriptionAsync', return_value=Result.OK), \
                mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientUnsubscribeAllAsync', return_value=Result.OK), \
                mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientSubscribeMultiAsync', return_value=Result.FAILED):
            with Client(112233) as client:
                with Variant() as v:
                    r, sub = client.create_subscription_async(v, cnb, cb)
                    self.assertTrue(r == Result.OK)
                    with sub:
                        l = ["test/value", "test/value1"]
                        r = sub.subscribe_multi(l, cb)
                        self.assertTrue(r == Result.FAILED)

    def test_unsubscribe_multi(self):
        """ test_unsubscribe_multi """

        def cb(result: Result, items: typing.List[ctrlxdatalayer.subscription.NotifyItem], userdata: ctrlxdatalayer.clib.userData_c_void_p):
            pass

        def cnb(result: Result, items: typing.List[ctrlxdatalayer.subscription.NotifyItem], userdata: ctrlxdatalayer.clib.userData_c_void_p):
            pass

        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientCreateSubscriptionAsync', return_value=Result.OK), \
                mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientUnsubscribeAllAsync', return_value=Result.OK), \
                mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientUnsubscribeMultiAsync', return_value=Result.OK):
            with Client(112233) as client:
                with Variant() as v:
                    r, sub = client.create_subscription_async(v, cnb, cb)
                    self.assertTrue(r == Result.OK)
                    with sub:
                        l = ["test/value", "test/value1"]
                        r = sub.unsubscribe_multi(l, cb)
                        self.assertTrue(r == Result.OK)

    def test_unsubscribe_multi_fail(self):
        """ test_unsubscribe_multi_fail """

        def cb(result: Result, items: typing.List[ctrlxdatalayer.subscription.NotifyItem], userdata: ctrlxdatalayer.clib.userData_c_void_p):
            pass

        def cnb(result: Result, items: typing.List[ctrlxdatalayer.subscription.NotifyItem], userdata: ctrlxdatalayer.clib.userData_c_void_p):
            pass

        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientCreateSubscriptionAsync', return_value=Result.OK), \
                mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientUnsubscribeAllAsync', return_value=Result.OK), \
                mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientUnsubscribeMultiAsync', return_value=Result.FAILED):
            with Client(112233) as client:
                with Variant() as v:
                    r, sub = client.create_subscription_async(v, cnb, cb)
                    self.assertTrue(r == Result.OK)
                    with sub:
                        l = ["test/value", "test/value1"]
                        r = sub.unsubscribe_multi(l, cb)
                        self.assertTrue(r == Result.FAILED)


class _CallbackSubscription(ctrlxdatalayer.subscription_async.SubscriptionAsync):

    def create_cnb(self, cnb: ctrlxdatalayer.subscription.ResponseNotifyCallback):
        """ create_cnb """
        return self._test_notify_callback(cnb)

    def create_cb(self, cb: ctrlxdatalayer.client.ResponseCallback):
        """ create_cb """
        return self._test_response_callback(cb)


class TestSubCallbackAsync(TestSubBaseAsync):
    """ TestSubCallbackSync """

    def setUp(self):
        """ setUp """
        self.patcher_unsubscribeallsync = mock.patch(
            'ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientUnsubscribeAllAsync', return_value=Result.OK)
        self.patcher_unsubscribeallsync.start()
        super().setUp()

    def tearDown(self):
        """  """
        self.patcher_unsubscribeallsync.stop()
        super().tearDown()

    def test_notify_callback_failed(self):
        """ test_notify_callback_failed """

        def cb_fail(result: Result, items: typing.List[ctrlxdatalayer.subscription.NotifyItem], userdata: ctrlxdatalayer.clib.userData_c_void_p):
            if result == Result.FAILED:
                self.counter = self.counter + 1

        with Client(112233) as client:
            with _CallbackSubscription(client) as sub:
                call_back = sub.create_cnb(cb_fail)
                self.assertIsNotNone(call_back)

                self.counter = 0
                call_back(Result.FAILED.value, None, 0, None)
                self.assertTrue(self.counter == 1)

    def test_response_callback_failed(self):
        """ test_response_callback_failed """

        def cb_fail(result: Result, data: typing.Optional[Variant], userdata: ctrlxdatalayer.clib.userData_c_void_p):
            if result == Result.FAILED:
                self.counter = self.counter + 1

        with Client(112233) as client:
            with _CallbackSubscription(client) as sub:
                call_back = sub.create_cb(cb_fail)
                self.assertIsNotNone(call_back)

                self.counter = 0
                call_back(Result.FAILED.value, None, None)
                self.assertTrue(self.counter == 1)

    def test_notify_callback_userdata_failed(self):
        """ test_notify_callback_userdata_failed """

        def cb_fail(result: Result, items: typing.List[ctrlxdatalayer.subscription.NotifyItem], userdata: ctrlxdatalayer.clib.userData_c_void_p):
            if result == Result.FAILED and userdata == 1234:
                self.counter = self.counter + 1

        with Client(112233) as client:
            with _CallbackSubscription(client) as sub:
                call_back = sub.create_cnb(cb_fail)
                self.assertIsNotNone(call_back)

                self.counter = 0
                call_back(Result.FAILED.value, None, 0, 1234)
                self.assertTrue(self.counter == 1)

    def test_response_callback_userdata_failed(self):
        """ test_response_callback_userdata_failed """

        def cb_fail(result: Result, data: typing.Optional[Variant], userdata: ctrlxdatalayer.clib.userData_c_void_p):
            if result == Result.FAILED and userdata == 1234:
                self.counter = self.counter + 1

        with Client(112233) as client:
            with _CallbackSubscription(client) as sub:
                call_back = sub.create_cb(cb_fail)
                self.assertIsNotNone(call_back)

                self.counter = 0
                call_back(Result.FAILED.value, None, 1234)
                self.assertTrue(self.counter == 1)

    def test_notify_callback_data(self):
        """ test_notify_callback_data """

        def cb_fail(result: Result, items: typing.List[ctrlxdatalayer.subscription.NotifyItem], userdata: ctrlxdatalayer.clib.userData_c_void_p):
            if result == Result.OK and userdata == 1234:
                if len(items) == 3:
                    self.counter = self.counter + 1
                    for i in range(0, len(items)):
                        print("callback item[{}]: data={}".format(
                            i, items[i].get_data().get_int16()))

        with Client(112233) as client:
            with _CallbackSubscription(client) as sub:
                call_back = sub.create_cnb(cb_fail)
                self.assertIsNotNone(call_back)

                self.counter = 0
                # create an array of C_NotifyItem with len=3
                elems = (ctrlxdatalayer.clib_client.C_NotifyItem * 3)()
                notify_items = ctypes.cast(elems, ctypes.POINTER(
                    ctrlxdatalayer.clib_client.C_NotifyItem))
                # create simple callback-datas
                datas = []  # required for the object's (variant) lifetime
                infos = []
                for i in range(0, 3):
                    data = Variant()
                    datas.append(data)
                    info = Variant()
                    infos.append(info)
                    data.set_int16(i)
                    notify_items[i].data = data.get_handle()
                    notify_items[i].info = info.get_handle()  # dummy

                call_back(Result.OK.value, notify_items, 3, 1234)
                self.assertTrue(self.counter == 1)
                # clean up
                for i in range(0, len(datas)):
                    datas[i].close()
                    infos[i].close()

    def test_response_callback_data(self):
        """ test_response_callback_data """

        def cb_fail(result: Result, data: typing.Optional[Variant], userdata: ctrlxdatalayer.clib.userData_c_void_p):
            if result == Result.OK and \
                    userdata == 1234 and \
                    data.get_int16() == 1701:
                self.counter = self.counter + 1
            print("resp-callback: result={}, data={}, userdata={}".format(result,
                  data.get_int16(), userdata))

        with Client(112233) as client:
            with _CallbackSubscription(client) as sub:
                call_back = sub.create_cb(cb_fail)
                self.assertIsNotNone(call_back)

                self.counter = 0
                with Variant() as v:
                    v.set_int16(1701)
                    call_back(Result.OK.value, v.get_handle(), 1234)
                    self.assertTrue(self.counter == 1)


if __name__ == '__main__':
    unittest.main()
