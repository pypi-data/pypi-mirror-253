import faulthandler
import unittest
from unittest import mock

import ctrlxdatalayer.converter
from ctrlxdatalayer.variant import Result, Variant

faulthandler.enable()


class TestConverter(unittest.TestCase):
    """ TestConverter """

    def test_converter_generate_json_simple_system(self):
        """ test_converter_generate_json_simple_system """
        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_systemCreate', return_value=123), \
                mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_systemDelete', return_value=None), \
                mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_systemStop', return_value=None), \
                mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_systemJsonConverter', return_value=3333444), \
                mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_converterGenerateJsonSimple', return_value=Result.OK):
            with ctrlxdatalayer.system.System("") as system:
                self.assertIsNotNone(system)
                self.assertTrue(system.get_handle() != 0)
                json_conv = system.json_converter()
                self.assertIsNotNone(json_conv)
                self.assertTrue(json_conv.get_handle() == 3333444)
                with Variant() as v:
                    result, v = json_conv.converter_generate_json_simple(
                        v, 1)
                    self.assertTrue(result == Result.OK)

    def test_converter_generate_json_simple(self):
        """ test_converter_generate_json_simple """
        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_converterGenerateJsonSimple', return_value=Result.OK):
            c = ctrlxdatalayer.converter.Converter(1234)
            with Variant() as v:
                result, v = c.converter_generate_json_simple(
                    v, 1)
                self.assertTrue(result == Result.OK)
                v.close()

    def test_converter_generate_json_simple_fail(self):
        """ test_converter_generate_json_simple_fail """
        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_converterGenerateJsonSimple', return_value=Result.FAILED):
            c = ctrlxdatalayer.converter.Converter(1234)
            with Variant() as v:
                result, v = c.converter_generate_json_simple(
                    v, 1)
                self.assertTrue(result == Result.FAILED)
                v.close()

    def testconverter_generate_json_complex(self):
        """ testconverter_generate_json_complex """
        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_converterGenerateJsonComplex', return_value=Result.OK):
            c = ctrlxdatalayer.converter.Converter(1234)
            with Variant() as v:
                result, v = c.converter_generate_json_complex(
                    v, v, 1)
                self.assertTrue(result == Result.OK)
                v.close()

    def test_converter_generate_json_complex_fail(self):
        """ test_converter_generate_json_complex_fail """
        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_converterGenerateJsonComplex', return_value=Result.FAILED):
            c = ctrlxdatalayer.converter.Converter(1234)
            with Variant() as v:
                result, v = c.converter_generate_json_complex(
                    v, v, 1)
                self.assertTrue(result == Result.FAILED)
                v.close()

    def test_converter_parse_json_simple(self):
        """ test_converter_parse_json_simple """
        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_converterParseJsonSimple', return_value=Result.OK):
            c = ctrlxdatalayer.converter.Converter(1234)
            with Variant() as v:
                result, v, e = c.parse_json_simple(
                    "test")
                self.assertTrue(result == Result.OK)
                self.assertIsNotNone(v)
                self.assertIsNotNone(e)
                v.close()
                e.close()

    def test_converter_parse_json_simple_fail(self):
        """ test_converter_parse_json_simple_fail """
        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_converterParseJsonSimple', return_value=Result.FAILED):
            c = ctrlxdatalayer.converter.Converter(1234)
            with Variant() as v:
                result, v, e = c.parse_json_simple(
                    "test")
                self.assertTrue(result == Result.FAILED)
                self.assertIsNotNone(v)
                self.assertIsNotNone(e)
                v.close()
                e.close()

    def testconverter_parse_json_complex(self):
        """ testconverter_parse_json_complex """
        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_converterParseJsonComplex', return_value=Result.OK):
            c = ctrlxdatalayer.converter.Converter(1234)
            with Variant() as v:
                result, v, e = c.parse_json_complex(
                    "test", v)
                self.assertTrue(result == Result.OK)
                self.assertIsNotNone(v)
                self.assertIsNotNone(e)
                v.close()
                e.close()

    def test_converter_parse_json_complex_fail(self):
        """ test_converter_parse_json_complex_fail """
        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_converterParseJsonComplex', return_value=Result.FAILED):
            c = ctrlxdatalayer.converter.Converter(1234)
            with Variant() as v:
                result, v, e = c.parse_json_complex(
                    "test", v)
                self.assertTrue(result == Result.FAILED)
                self.assertIsNotNone(v)
                self.assertIsNotNone(e)
                v.close()
                e.close()

    def testconverter_get_schema(self):
        """ testconverter_get_schema """
        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_converterGetSchema', return_value=Result.OK):
            c = ctrlxdatalayer.converter.Converter(1234)
            result, v = c.get_schema(
                ctrlxdatalayer.converter.C_DLR_SCHEMA.DIAGNOSIS)
            self.assertTrue(result == Result.OK)
            self.assertIsNotNone(v)
            v.close()

    def test_converter_get_schema_fail(self):
        """ test_converter_get_schema_fail """
        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_converterGetSchema', return_value=Result.FAILED):
            c = ctrlxdatalayer.converter.Converter(1234)
            result, v = c.get_schema(
                ctrlxdatalayer.converter.C_DLR_SCHEMA.DIAGNOSIS)
            self.assertTrue(result == Result.FAILED)
            self.assertIsNotNone(v)
            v.close()


if __name__ == '__main__':
    unittest.main()
