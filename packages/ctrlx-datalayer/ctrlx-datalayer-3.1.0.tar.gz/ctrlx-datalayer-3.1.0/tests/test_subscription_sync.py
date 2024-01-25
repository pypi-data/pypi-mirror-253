import ctypes
import faulthandler
import typing
import unittest
from unittest import mock

import flatbuffers

import comm.datalayer.NotifyInfo
import comm.datalayer.SubscriptionProperties
import ctrlxdatalayer
import ctrlxdatalayer.clib_client
import ctrlxdatalayer.subscription
from ctrlxdatalayer.client import Client
from ctrlxdatalayer.variant import Result, Variant

faulthandler.enable()


class TestSubBaseSync(unittest.TestCase):
    """
    TestSubBaseSync
    """

    def setUp(self):
        """ setUp """
        self.patcher_client_delete = mock.patch(
            'ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientDelete', return_value=None)
        self.patcher_client_delete.start()

    def tearDown(self):
        """  """
        self.patcher_client_delete.stop()


class TestSubSync(TestSubBaseSync):
    """
    TestSubSync
    """

    def test_close(self):
        """ test_close """
        with Client(112233) as client:
            client.close()

    def test_create(self):
        """ test_create """

        def cb(result: Result, items: typing.List[ctrlxdatalayer.subscription.NotifyItem], userdata: ctrlxdatalayer.clib.userData_c_void_p):
            pass

        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientCreateSubscriptionSync', return_value=Result.OK), \
                mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientUnsubscribeAllSync', return_value=Result.OK):
            with Client(112233) as client:
                with Variant() as v:
                    r, sub = client.create_subscription_sync(v, cb)
                    self.assertTrue(r == Result.OK)
                    sub.close()

    def test_sub_notify_info(self):
        """ test_sub_notify_info """
        builder = flatbuffers.Builder(1024)
        # Hint: CreateString must be done beforehand
        node = builder.CreateString("node")
        self.assertIsNotNone(node)
        comm.datalayer.NotifyInfo.NotifyInfoStart(
            builder)
        comm.datalayer.NotifyInfo.NotifyInfoAddNode(builder, node)
        comm.datalayer.NotifyInfo.NotifyInfoAddTimestamp(
            builder, 132608769637407570)
        comm.datalayer.NotifyInfo.NotifyInfoAddNotifyType(builder, 0)
        prop = comm.datalayer.NotifyInfo.NotifyInfoEnd(
            builder)
        builder.Finish(prop)
        with Variant() as v:
            r = v.set_flatbuffers(builder.Output())
            self.assertTrue(r == Result.OK)
            b = v.get_flatbuffers()
            p = comm.datalayer.NotifyInfo.NotifyInfo.GetRootAsNotifyInfo(
                b, 0)
            self.assertIsNotNone(p)
            self.assertTrue(p.Node().decode("utf-8") == "node")
            self.assertTrue(p.Timestamp() == 132608769637407570)
            self.assertTrue(p.NotifyType() == 0)
            n = ctrlxdatalayer.subscription.NotifyItem(
                v.get_handle(), v.get_handle())
            self.assertIsNotNone(n)
            self.assertTrue(n.get_address() == "node")
            self.assertTrue(n.get_timestamp() == 132608769637407570)
            self.assertTrue(
                n.get_type() == ctrlxdatalayer.subscription.NotifyType.DATA)

    def test_sub_properties(self):
        """ test_sub_properties """
        builder = flatbuffers.Builder(1024)
        # Hint: CreateString must be done beforehand
        id = builder.CreateString("Hallo")
        self.assertIsNotNone(id)
        comm.datalayer.SubscriptionProperties.SubscriptionPropertiesStart(
            builder)
        comm.datalayer.SubscriptionProperties.SubscriptionPropertiesAddId(
            builder, id)
        comm.datalayer.SubscriptionProperties.SubscriptionPropertiesAddPublishInterval(
            builder, 1234)
        comm.datalayer.SubscriptionProperties.SubscriptionPropertiesAddKeepaliveInterval(
            builder, 5678)
        comm.datalayer.SubscriptionProperties.SubscriptionPropertiesAddErrorInterval(
            builder, 1314)
        prop = comm.datalayer.SubscriptionProperties.SubscriptionPropertiesEnd(
            builder)
        builder.Finish(prop)
        with Variant() as v:
            r = v.set_flatbuffers(builder.Output())
            self.assertTrue(r == Result.OK)
            b = v.get_flatbuffers()
            p = comm.datalayer.SubscriptionProperties.SubscriptionProperties.GetRootAsSubscriptionProperties(
                b, 0)
            self.assertIsNotNone(p)
            self.assertTrue(p.Id().decode("utf-8") == "Hallo")
            self.assertTrue(p.PublishInterval() == 1234)
            self.assertTrue(p.KeepaliveInterval() == 5678)
            self.assertTrue(p.ErrorInterval() == 1314)

    def test_sub_properties_2(self):
        v = ctrlxdatalayer.subscription.create_properties("Hallo")
        with v:
            b = v.get_flatbuffers()
            p = comm.datalayer.SubscriptionProperties.SubscriptionProperties.GetRootAsSubscriptionProperties(
                b, 0)
            self.assertIsNotNone(p)
            self.assertTrue(p.Id().decode("utf-8") == "Hallo")
            self.assertTrue(p.PublishInterval() == 1000)
            self.assertTrue(p.KeepaliveInterval() == 60000)
            self.assertTrue(p.ErrorInterval() == 10000)

    def test_create_ruleset(self):
        """ test_create_ruleset """

        def cb(result: Result, items: typing.List[ctrlxdatalayer.subscription.NotifyItem], userdata: ctrlxdatalayer.clib.userData_c_void_p):
            pass

        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientCreateSubscriptionSync', return_value=Result.OK), \
                mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientUnsubscribeAllSync', return_value=Result.OK):
            with Client(112233) as client:
                with Variant() as v:
                    builder = flatbuffers.Builder(1024)
                    # Hint: CreateString must be done beforehand
                    id = builder.CreateString("Hallo")
                    self.assertIsNotNone(id)
                    comm.datalayer.SubscriptionProperties.SubscriptionPropertiesStart(
                        builder)
                    comm.datalayer.SubscriptionProperties.SubscriptionPropertiesAddId(
                        builder, id)
                    comm.datalayer.SubscriptionProperties.SubscriptionPropertiesAddPublishInterval(
                        builder, 1234)
                    comm.datalayer.SubscriptionProperties.SubscriptionPropertiesAddKeepaliveInterval(
                        builder, 5678)
                    comm.datalayer.SubscriptionProperties.SubscriptionPropertiesAddErrorInterval(
                        builder, 1314)
                    prop = comm.datalayer.SubscriptionProperties.SubscriptionPropertiesEnd(
                        builder)
                    builder.Finish(prop)
                    v.set_flatbuffers(builder.Output())
                    r, sub = client.create_subscription_sync(v, cb)
                    self.assertTrue(r == Result.OK)
                    self.assertTrue(sub.id() == "Hallo")
                    sub.close()

    def test_create_helper_ruleset(self):
        """ test_create_helper_ruleset """

        def cb(result: Result, items: typing.List[ctrlxdatalayer.subscription.NotifyItem], userdata: ctrlxdatalayer.clib.userData_c_void_p):
            pass

        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientCreateSubscriptionSync', return_value=Result.OK), \
                mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientUnsubscribeAllSync', return_value=Result.OK):
            with Client(112233) as client:
                v = ctrlxdatalayer.subscription.create_properties("Hallo")
                with v:
                    r, sub = client.create_subscription_sync(v, cb)
                    self.assertTrue(r == Result.OK)
                    self.assertTrue(sub.id() == "Hallo")
                    sub.close()

    def test_close_all(self):
        """ test_close_all """

        def cb(result: Result, items: typing.List[ctrlxdatalayer.subscription.NotifyItem], userdata: ctrlxdatalayer.clib.userData_c_void_p):
            pass

        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientCreateSubscriptionSync', return_value=Result.OK), \
                mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientUnsubscribeAllSync', return_value=Result.OK):
            client = Client(112233)
            with Variant() as v:
                r, sub = client.create_subscription_sync(v, cb)
                self.assertTrue(r == Result.OK)
                self.assertIsNotNone(sub)
            client.close()  # here close all subscriptions

    def test_unsubscribe_all(self):
        """ test_unsubscribe_all """

        def cb(result: Result, items: typing.List[ctrlxdatalayer.subscription.NotifyItem], userdata: ctrlxdatalayer.clib.userData_c_void_p):
            pass

        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientCreateSubscriptionSync', return_value=Result.OK), \
                mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientUnsubscribeAllSync', return_value=Result.OK):
            with Client(112233) as client:
                with Variant() as v:
                    r, sub = client.create_subscription_sync(v, cb)
                    self.assertTrue(r == Result.OK)
                    r = sub.unsubscribe_all()
                    self.assertTrue(r == Result.OK)
                    sub.close()

    def test_unsubscribe_all_fail(self):
        """ test_unsubscribe_all """

        def cb(result: Result, items: typing.List[ctrlxdatalayer.subscription.NotifyItem], userdata: ctrlxdatalayer.clib.userData_c_void_p):
            pass

        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientCreateSubscriptionSync', return_value=Result.OK), \
                mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientUnsubscribeAllSync', return_value=Result.FAILED):
            with Client(112233) as client:
                with Variant() as v:
                    r, sub = client.create_subscription_sync(v, cb)
                    self.assertTrue(r == Result.OK)
                    r = sub.unsubscribe_all()
                    self.assertTrue(r == Result.FAILED)
                    sub.close()

    def test_subscribe(self):
        """ test_subscribe """

        def cb(result: Result, items: typing.List[ctrlxdatalayer.subscription.NotifyItem], userdata: ctrlxdatalayer.clib.userData_c_void_p):
            pass

        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientCreateSubscriptionSync', return_value=Result.OK), \
                mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientUnsubscribeAllSync', return_value=Result.OK), \
                mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientSubscribeSync', return_value=Result.OK):
            with Client(112233) as client:
                with Variant() as v:
                    r, sub = client.create_subscription_sync(v, cb)
                    self.assertTrue(r == Result.OK)
                    with sub:
                        r = sub.subscribe("test/value")
                        self.assertTrue(r == Result.OK)

    def test_subscribe_fail(self):
        """ test_subscribe_fail """

        def cb(result: Result, items: typing.List[ctrlxdatalayer.subscription.NotifyItem], userdata: ctrlxdatalayer.clib.userData_c_void_p):
            pass

        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientCreateSubscriptionSync', return_value=Result.OK), \
                mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientUnsubscribeAllSync', return_value=Result.OK), \
                mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientSubscribeSync', return_value=Result.FAILED):
            with Client(112233) as client:
                with Variant() as v:
                    r, sub = client.create_subscription_sync(v, cb)
                    self.assertTrue(r == Result.OK)
                    with sub:
                        r = sub.subscribe("test/value")
                        self.assertTrue(r == Result.FAILED)

    def test_unsubscribe(self):
        """ test_unsubscribe """

        def cb(result: Result, items: typing.List[ctrlxdatalayer.subscription.NotifyItem], userdata: ctrlxdatalayer.clib.userData_c_void_p):
            pass

        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientCreateSubscriptionSync', return_value=Result.OK), \
                mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientUnsubscribeAllSync', return_value=Result.OK), \
                mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientUnsubscribeSync', return_value=Result.OK):
            with Client(112233) as client:
                with Variant() as v:
                    r, sub = client.create_subscription_sync(v, cb)
                    self.assertTrue(r == Result.OK)
                    with sub:
                        r = sub.unsubscribe("test/value")
                        self.assertTrue(r == Result.OK)

    def test_unsubscribe_fail(self):
        """ test_unsubscribe_fail """

        def cb(result: Result, items: typing.List[ctrlxdatalayer.subscription.NotifyItem], userdata: ctrlxdatalayer.clib.userData_c_void_p):
            pass

        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientCreateSubscriptionSync', return_value=Result.OK), \
                mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientUnsubscribeAllSync', return_value=Result.OK), \
                mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientUnsubscribeSync', return_value=Result.FAILED):
            with Client(112233) as client:
                with Variant() as v:
                    r, sub = client.create_subscription_sync(v, cb)
                    self.assertTrue(r == Result.OK)
                    with sub:
                        r = sub.unsubscribe("test/value")
                        self.assertTrue(r == Result.FAILED)

    def test_subscribe_multi(self):
        """ test_subscribe_multi """

        def cb(result: Result, items: typing.List[ctrlxdatalayer.subscription.NotifyItem], userdata: ctrlxdatalayer.clib.userData_c_void_p):
            pass

        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientCreateSubscriptionSync', return_value=Result.OK), \
                mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientUnsubscribeAllSync', return_value=Result.OK), \
                mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientSubscribeMultiSync', return_value=Result.OK):
            with Client(112233) as client:
                with Variant() as v:
                    r, sub = client.create_subscription_sync(v, cb)
                    self.assertTrue(r == Result.OK)
                    with sub:
                        l = ["test/value", "test/value1"]
                        r = sub.subscribe_multi(l)
                        self.assertTrue(r == Result.OK)

    def test_subscribe_multi_fail(self):
        """ test_subscribe_multi_fail """

        def cb(result: Result, items: typing.List[ctrlxdatalayer.subscription.NotifyItem], userdata: ctrlxdatalayer.clib.userData_c_void_p):
            pass

        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientCreateSubscriptionSync', return_value=Result.OK), \
                mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientUnsubscribeAllSync', return_value=Result.OK), \
                mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientSubscribeMultiSync', return_value=Result.FAILED):
            with Client(112233) as client:
                with Variant() as v:
                    r, sub = client.create_subscription_sync(v, cb)
                    self.assertTrue(r == Result.OK)
                    with sub:
                        l = ["test/value", "test/value1"]
                        r = sub.subscribe_multi(l)
                        self.assertTrue(r == Result.FAILED)

    def test_unsubscribe_multi(self):
        """ test_unsubscribe_multi """

        def cb(result: Result, items: typing.List[ctrlxdatalayer.subscription.NotifyItem], userdata: ctrlxdatalayer.clib.userData_c_void_p):
            pass

        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientCreateSubscriptionSync', return_value=Result.OK), \
                mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientUnsubscribeAllSync', return_value=Result.OK), \
                mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientUnsubscribeMultiSync', return_value=Result.OK):
            with Client(112233) as client:
                with Variant() as v:
                    r, sub = client.create_subscription_sync(v, cb)
                    self.assertTrue(r == Result.OK)
                    with sub:
                        l = ["test/value", "test/value1"]
                        r = sub.unsubscribe_multi(l)
                        self.assertTrue(r == Result.OK)

    def test_unsubscribe_multi_fail(self):
        """ test_unsubscribe_multi_fail """

        def cb(result: Result, items: typing.List[ctrlxdatalayer.subscription.NotifyItem], userdata: ctrlxdatalayer.clib.userData_c_void_p):
            pass

        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientCreateSubscriptionSync', return_value=Result.OK), \
                mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientUnsubscribeAllSync', return_value=Result.OK), \
                mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientUnsubscribeMultiSync', return_value=Result.FAILED):
            with Client(112233) as client:
                with Variant() as v:
                    r, sub = client.create_subscription_sync(v, cb)
                    self.assertTrue(r == Result.OK)
                    with sub:
                        l = ["test/value", "test/value1"]
                        r = sub.unsubscribe_multi(l)
                        self.assertTrue(r == Result.FAILED)


class _CallbackSubscription(ctrlxdatalayer.subscription_sync.SubscriptionSync):

    def create_cb(self, cb: ctrlxdatalayer.subscription.ResponseNotifyCallback):
        """ create_cb """
        return self._test_notify_callback(cb)


class TestSubCallbackSync(TestSubBaseSync):
    """ TestSubCallbackSync """

    def setUp(self):
        """ setUp """
        self.patcher_unsubscribeallsync = mock.patch(
            'ctrlxdatalayer.clib.libcomm_datalayer.DLR_clientUnsubscribeAllSync', return_value=Result.OK)
        self.patcher_unsubscribeallsync.start()
        super().setUp()

    def tearDown(self):
        """  """
        self.patcher_unsubscribeallsync.stop()
        super().tearDown()

    def test_callback_failed(self):
        """ test_create_sync """

        def cb_fail(result: Result, items: typing.List[ctrlxdatalayer.subscription.NotifyItem], userdata: ctrlxdatalayer.clib.userData_c_void_p):
            if result == Result.FAILED:
                self.counter = self.counter + 1

        with Client(112233) as client:
            with _CallbackSubscription(client) as sub:
                call_back = sub.create_cb(cb_fail)
                self.assertIsNotNone(call_back)

                self.counter = 0
                call_back(Result.FAILED.value, None, 0, None)
                self.assertTrue(self.counter == 1)

    def test_callback_ok(self):
        """ test_create_sync """

        def cb(result: Result, items: typing.List[ctrlxdatalayer.subscription.NotifyItem], userdata: ctrlxdatalayer.clib.userData_c_void_p):
            if result == Result.OK:
                if len(items) == 3:
                    self.counter = self.counter + 1
                    for i in range(0, len(items)):
                        print("callback item[{}]: data={}".format(
                            i, items[i].get_data().get_int16()))

        with Client(112233) as client:
            with _CallbackSubscription(client) as sub:
                call_back = sub.create_cb(cb)
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

                call_back(Result.OK.value, notify_items, 3, None)
                self.assertTrue(self.counter == 1)
                # clean up
                for i in range(0, len(datas)):
                    datas[i].close()
                    infos[i].close()

    def test_callback_failed_userdata(self):
        """ test_create_sync """

        def cb_fail(result: Result, items: typing.List[ctrlxdatalayer.subscription.NotifyItem], userdata: ctrlxdatalayer.clib.userData_c_void_p):
            if result == Result.FAILED:
                if userdata == 1234:
                    self.counter = self.counter + 1

        with Client(112233) as client:
            with _CallbackSubscription(client) as sub:
                call_back = sub.create_cb(cb_fail)
                self.assertIsNotNone(call_back)

                self.counter = 0
                call_back(Result.FAILED.value, None, 0, 1234)
                self.assertTrue(self.counter == 1)

    def test_timestamp(self):
        d = ctrlxdatalayer.subscription.to_datetime(132608769637407570)
        self.assertIsNotNone(d)
        print("timestamp: ", d)


if __name__ == '__main__':
    unittest.main()
