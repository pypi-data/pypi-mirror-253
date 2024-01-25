import unittest

import ctrlxdatalayer
import ctrlxdatalayer.system
from ctrlxdatalayer.client import Result
from ctrlxdatalayer.variant import VariantType, Variant
from tests.test_utils import (client_connection, client_timeout,
                              is_integration_test)
from comm.datalayer import Metadata

# port 443 is needed
_connectionClient = client_connection()
_timeout = client_timeout()

# export INTEGRATION=1
# unset INTEGRATION

b = is_integration_test()


@unittest.skipIf(is_integration_test() == False, "no integration test")
class TestConverterBase(unittest.TestCase):
    """ TestConverterBase """

    @classmethod
    def setUpClass(cls):
        """ setUpClass """
        print("Using ctrlX CORE as client: ", _connectionClient)
        cls.system = ctrlxdatalayer.system.System("")
        cls.system.start(False)
        cls.client = cls.system.factory().create_client(_connectionClient)
        bc = cls.client.is_connected()
        print("cls connect={}".format(bc))

    @classmethod
    def tearDownClass(cls):
        """ tearDownClass """
        print("tearDownClass")
        cls.client.close()
        cls.system.stop(True)
        cls.system.close()


@unittest.skipIf(is_integration_test() == False, "no integration test")
class TestConverter(TestConverterBase):
    """ TestConverter """

    def test_is_connected(self):
        """ test_is_connected """
        print("test_is_connected")
        self.client.set_timeout(
            ctrlxdatalayer.client.TimeoutSetting.PING, _timeout)
        b = self.client.is_connected()
        self.assertTrue(b)

    def test_converter_generate(self):
        """ test_converter_generate """
        print("test_converter_generate")
        r, v = self.client.read_sync("datalayer/subscriptions/settings")
        with v:
            self.assertTrue(r == Result.OK)
            self.assertIsNotNone(v)
            self.assertTrue(v.get_type() == VariantType.FLATBUFFERS)
            type_addr = self.get_type_address(
                "datalayer/subscriptions/settings")
            self.assertIsNotNone(type_addr)

            r, bfbs = self.client.read_sync(type_addr)
            self.assertTrue(r == Result.OK)
            self.assertIsNotNone(bfbs)
            self.converter_complex(v, bfbs)

    def converter_complex(self, data, bfbs):
        converter = self.system.json_converter()
        self.assertIsNotNone(converter)
        r, json = converter.converter_generate_json_complex(data, bfbs, -1)
        self.assertTrue(r == Result.OK)
        with json:
            self.assertIsNotNone(json)
            self.assertTrue(len(json.get_string()) != 0)
            print(json.get_string())

    def test_converter_parse(self):
        """ test_converter_parseself """
        print("test_converter_parseself")
        r, v = self.client.read_sync("datalayer/subscriptions/settings")
        with v:
            self.assertTrue(r == Result.OK)
            self.assertIsNotNone(v)
            self.assertTrue(v.get_type() == VariantType.FLATBUFFERS)
            type_addr = self.get_type_address(
                "datalayer/subscriptions/settings")
            self.assertIsNotNone(type_addr)

            r, bfbs = self.client.read_sync(type_addr)
            self.assertTrue(r == Result.OK)
            self.assertIsNotNone(bfbs)
            self.converter_complex_parse(bfbs)

    def converter_complex_parse(self, bfbs):
        converter = self.system.json_converter()
        self.assertIsNotNone(converter)
        r, data, err = converter.parse_json_complex(
            '{"minimumPublishInterval": 50, "minimumSampleInterval": 100000, "maximumBufferSize": 50, "minimumErrorInterval": 10000}', bfbs)
        self.assertTrue(r == Result.OK)
        with data, err:
            self.assertIsNotNone(data)
            self.assertTrue(data.get_type() == VariantType.FLATBUFFERS)
            self.assertIsNotNone(err)

    def test_converter_generate_simple(self):
        """ test_converter_generate_simple """
        print("test_converter_generate_simple")
        v = Variant()
        v.set_string("Das ist ein Test")
        with v:
            converter = self.system.json_converter()
            self.assertIsNotNone(converter)
            r, json = converter.converter_generate_json_simple(v, -1)
            self.assertTrue(r == Result.OK)
            with json:
                self.assertIsNotNone(json)
                self.assertEqual(json.get_type(), VariantType.STRING)

    def get_type_address(self, address: str) -> str:

        result, metadata = self.client.metadata_sync(address)
        if result != Result.OK:
            return None

        with metadata:
            metadata_root = Metadata.Metadata.GetRootAsMetadata(
                metadata.get_flatbuffers())

            if metadata_root.ReferencesLength() == 0:
                return None

            for i in range(0, metadata_root.ReferencesLength()):
                reference = metadata_root.References(i)

                if reference is None:
                    continue

                if reference.Type().decode('utf-8').lower() == "readtype":
                    type_address = reference.TargetAddress().decode('utf-8')
                    return type_address

            return None


if __name__ == '__main__':
    unittest.main()
