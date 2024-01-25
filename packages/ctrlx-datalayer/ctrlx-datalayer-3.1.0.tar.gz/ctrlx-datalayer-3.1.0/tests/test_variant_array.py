import datetime
import faulthandler
import unittest
from unittest import mock

from ctrlxdatalayer.variant import Result, Variant

faulthandler.enable()


class TestVariantArray(unittest.TestCase):
    """ TestVariantArray """

    def test_variant_string(self):
        """ test_variant_string """
        with Variant() as v:
            r = v.set_string("Hello World")
            self.assertTrue(r == Result.OK)
            self.assertEqual(v.get_string(), "Hello World")

            v.close()
            r = v.set_string("Hello World")
            self.assertTrue(r == Result.NOT_INITIALIZED)

    def test_variant_array_bool8(self):
        """ test_variant_array_bool8 """
        with Variant() as v:
            r = v.set_array_bool8([True, False, True])
            self.assertTrue(r == Result.OK)
            self.assertEqual(v.get_array_bool8(), [True, False, True])

            v.close()
            r = v.set_bool8([True, False, True])
            self.assertTrue(r == Result.NOT_INITIALIZED)

    def test_variant_array_int8(self):
        """ test_variant_array_int8 """
        with Variant() as v:
            r = v.set_array_int8([-128, -1, 0, 1, 127])
            self.assertTrue(r == Result.OK)
            self.assertEqual(v.get_array_int8(), [-128, -1, 0, 1, 127])

            v.close()
            r = v.set_array_int8([-128, -1, 0, 1, 127])
            self.assertTrue(r == Result.NOT_INITIALIZED)

    def test_variant_array_uint8(self):
        """ test_variant_array_uint8 """
        with Variant() as v:
            r = v.set_array_uint8([0, 1, 2, 255])
            self.assertTrue(r == Result.OK)
            self.assertEqual(v.get_array_uint8(), [0, 1, 2, 255])

            v.close()
            r = v.set_array_uint8([0, 1, 2, 255])
            self.assertTrue(r == Result.NOT_INITIALIZED)

    def test_variant_array_int16(self):
        """ test_variant_array_int16 """
        with Variant() as v:
            r = v.set_array_int16([-32768, -1, 0, 1, 32767])
            self.assertTrue(r == Result.OK)
            self.assertEqual(v.get_array_int16(), [-32768, -1, 0, 1, 32767])

            v.close()
            r = v.set_array_int16([-32768, -1, 0, 1, 32767])
            self.assertTrue(r == Result.NOT_INITIALIZED)

    def test_variant_array_uint16(self):
        """ test_variant_array_uint16 """
        with Variant() as v:
            r = v.set_array_uint16([0, 1, 2, 65535])
            self.assertTrue(r == Result.OK)
            self.assertEqual(v.get_array_uint16(), [0, 1, 2, 65535])

            v.close()
            r = v.set_array_uint16([0, 1, 2, 65535])
            self.assertTrue(r == Result.NOT_INITIALIZED)

    def test_variant_array_int32(self):
        """ test_variant_array_int32 """
        with Variant() as v:
            r = v.set_array_int32([-2147483648, -1, 0, 1, 2147483647])
            self.assertTrue(r == Result.OK)
            self.assertEqual(v.get_array_int32(),
                             [-2147483648, -1, 0, 1, 2147483647])

            v.close()
            r = v.set_array_int32([-2147483648, -1, 0, 1, 2147483647])
            self.assertTrue(r == Result.NOT_INITIALIZED)

    def test_variant_array_uint32(self):
        """ test_variant_array_uint32 """
        with Variant() as v:
            r = v.set_array_uint32([0, 1, 2, 4294967295])
            self.assertTrue(r == Result.OK)
            self.assertEqual(v.get_array_uint32(), [0, 1, 2, 4294967295])

            v.close()
            r = v.set_array_uint32([0, 1, 2, 4294967295])
            self.assertTrue(r == Result.NOT_INITIALIZED)

    def test_variant_array_int64(self):
        """ test_variant_array_int64 """
        with Variant() as v:
            r = v.set_array_int64(
                [-9223372036854775808, -1, 0, 1, 9223372036854775807])
            self.assertTrue(r == Result.OK)
            self.assertEqual(v.get_array_int64(),
                             [-9223372036854775808, -1, 0, 1, 9223372036854775807])

            v.close()
            r = v.set_array_int64(
                [-9223372036854775808, -1, 0, 1, 9223372036854775807])
            self.assertTrue(r == Result.NOT_INITIALIZED)

    def test_variant_array_uint64(self):
        """ test_variant_array_uint64 """
        with Variant() as v:
            r = v.set_array_uint64([0, 1, 2, 18446744073709551615])
            self.assertTrue(r == Result.OK)
            self.assertEqual(v.get_array_uint64(), [
                             0, 1, 2, 18446744073709551615])

            v.close()
            r = v.set_array_uint64([0, 1, 2, 18446744073709551615])
            self.assertTrue(r == Result.NOT_INITIALIZED)

    def test_variant_array_float32(self):
        """ test_variant_array_float32 """
        with Variant() as v:
            r = v.set_array_float32([2, 4])
            self.assertTrue(r == Result.OK)
            self.assertEqual(v.get_array_float32(), [2, 4])

            v.close()
            r = v.set_array_float32([2, 4])
            self.assertTrue(r == Result.NOT_INITIALIZED)

    def test_variant_array_float64(self):
        """ test_variant_array_float64 """
        with Variant() as v:
            r = v.set_array_float64([2, 4])
            self.assertTrue(r == Result.OK)
            self.assertEqual(v.get_array_float64(), [2, 4])

            v.close()
            r = v.set_array_float64([2, 4])
            self.assertTrue(r == Result.NOT_INITIALIZED)

    def test_variant_array_string(self):
        """ test_variant_array_string """
        with Variant() as v:
            r = v.set_array_string(["Hallo", "Welt"])
            self.assertTrue(r == Result.OK)
            self.assertEqual(v.get_array_string(), ["Hallo", "Welt"])

            v.close()
            r = v.set_array_string(["Hallo", "Welt"])
            self.assertTrue(r == Result.NOT_INITIALIZED)

    def test_variant_array_bool_none(self):
        """ test_variant_array_bool_none """
        with Variant() as v:
            r = v.set_array_uint8([0, 1])
            self.assertTrue(r == Result.OK)
            val = v.get_array_bool8()
            self.assertIsNone(val)

    def test_variant_array_int8_none(self):
        """ test_variant_array_int8_none """
        with Variant() as v:
            r = v.set_array_uint8([0, 1])
            self.assertTrue(r == Result.OK)
            val = v.get_array_int8()
            self.assertIsNone(val)

    def test_variant_array_uint8_none(self):
        """ test_variant_array_uint8_none """
        with Variant() as v:
            r = v.set_array_int8([0, 1])
            self.assertTrue(r == Result.OK)
            val = v.get_array_uint8()
            self.assertIsNone(val)

    def test_variant_array_int16_none(self):
        """ test_variant_array_int16_none """
        with Variant() as v:
            r = v.set_array_uint16([0, 1])
            self.assertTrue(r == Result.OK)
            val = v.get_array_int16()
            self.assertIsNone(val)

    def test_variant_array_uint16_none(self):
        """ test_variant_array_uint16_none """
        with Variant() as v:
            r = v.set_array_int16([0, 1])
            self.assertTrue(r == Result.OK)
            val = v.get_array_uint16()
            self.assertIsNone(val)

    def test_variant_array_int32_none(self):
        """ test_variant_array_int32_none """
        with Variant() as v:
            r = v.set_array_uint32([0, 1])
            self.assertTrue(r == Result.OK)
            val = v.get_array_int32()
            self.assertIsNone(val)

    def test_variant_array_uint32_none(self):
        """ test_variant_array_uint32_none """
        with Variant() as v:
            r = v.set_array_int32([0, 1])
            self.assertTrue(r == Result.OK)
            val = v.get_array_uint32()
            self.assertIsNone(val)

    def test_variant_array_int64_none(self):
        """ test_variant_array_int64_none """
        with Variant() as v:
            r = v.set_array_uint64([0, 1])
            self.assertTrue(r == Result.OK)
            val = v.get_array_int64()
            self.assertIsNone(val)

    def test_variant_array_uint64_none(self):
        """ test_variant_array_uint64_none """
        with Variant() as v:
            r = v.set_array_int64([0, 1])
            self.assertTrue(r == Result.OK)
            val = v.get_array_uint64()
            self.assertIsNone(val)

    def test_variant_array_float64_none(self):
        """ test_variant_array_float64_none """
        with Variant() as v:
            r = v.set_array_float32([0, 1])
            self.assertTrue(r == Result.OK)
            val = v.get_array_float64()
            self.assertIsNone(val)

    def test_variant_array_float32_none(self):
        """ test_variant_array_float32_none """
        with Variant() as v:
            r = v.set_array_float64([0, 1])
            self.assertTrue(r == Result.OK)
            val = v.get_array_float32()
            self.assertIsNone(val)

    def test_variant_array_string_none(self):
        """ test_variant_array_string_none """
        with Variant() as v:
            r = v.set_string("hallo")
            self.assertTrue(r == Result.OK)
            val = v.get_array_string()
            self.assertIsNone(val)

    def test_variant_flatbuffers_none(self):
        """ test_variant_flatbuffers_none """
        with Variant() as v:
            r = v.set_array_uint8([0, 1])
            self.assertTrue(r == Result.OK)
            val = v.get_flatbuffers()
            self.assertIsNone(val)

    def test_variant_string_none(self):
        """ test_variant_string_none """
        with Variant() as v:
            r = v.set_array_uint8([0, 1])
            self.assertTrue(r == Result.OK)
            val = v.get_string()
            self.assertIsNone(val)

    def test_variant_string_fail(self):
        """ test_variant_string_fail """
        with mock.patch('ctrlxdatalayer.clib.libcomm_datalayer.DLR_variantGetSTRING', return_value=None):
            with Variant() as v:
                v.set_string("failed")
                val = v.get_string()
                self.assertIsNone(val)

    def test_variant_float64_0(self):
        """ test_variant_float64_0 """
        with Variant() as v:
            r = v.set_float32(1)
            self.assertTrue(r == Result.OK)
            val = v.get_float32()
            self.assertTrue(val != 0)
            val = v.get_float64()
            self.assertTrue(val != 0)
            val = v.get_uint64()
            self.assertTrue(val != 0)
            val = v.get_int64()
            self.assertTrue(val != 0)
            val = v.get_uint32()
            self.assertTrue(val != 0)
            val = v.get_int32()
            self.assertTrue(val != 0)
            val = v.get_uint16()
            self.assertTrue(val != 0)
            val = v.get_int16()
            self.assertTrue(val != 0)
            val = v.get_uint8()
            self.assertTrue(val != 0)
            val = v.get_int8()
            self.assertTrue(val != 0)
            val = v.get_bool8()
            self.assertTrue(val != 0)

            r = v.set_int32(1)
            self.assertTrue(r == Result.OK)
            val = v.get_float32()
            self.assertTrue(val != 0)
            val = v.get_float64()
            self.assertTrue(val != 0)
            val = v.get_uint64()
            self.assertTrue(val != 0)
            val = v.get_int64()
            self.assertTrue(val != 0)
            val = v.get_uint32()
            self.assertTrue(val != 0)
            val = v.get_int32()
            self.assertTrue(val != 0)
            val = v.get_uint16()
            self.assertTrue(val != 0)
            val = v.get_int16()
            self.assertTrue(val != 0)
            val = v.get_uint8()
            self.assertTrue(val != 0)
            val = v.get_int8()
            self.assertTrue(val != 0)
            val = v.get_bool8()
            self.assertTrue(val != 0)

            r = v.set_string("1.0")
            self.assertTrue(r == Result.OK)
            val = v.get_float64()
            self.assertTrue(val == 0)
            val = v.get_float32()
            self.assertTrue(val == 0)
            val = v.get_float64()
            self.assertTrue(val == 0)
            val = v.get_uint64()
            self.assertTrue(val == 0)
            val = v.get_int64()
            self.assertTrue(val == 0)
            val = v.get_uint32()
            self.assertTrue(val == 0)
            val = v.get_int32()
            self.assertTrue(val == 0)
            val = v.get_uint16()
            self.assertTrue(val == 0)
            val = v.get_int16()
            self.assertTrue(val == 0)
            val = v.get_uint8()
            self.assertTrue(val == 0)
            val = v.get_int8()
            self.assertTrue(val == 0)
            val = v.get_bool8()
            self.assertTrue(val == 0)

    def test_variant_timestamp(self):
        """ test_variant_timestamp """
        data = [(116444736000000000, datetime.datetime(1970, 1, 1)),
                (87790176000000000, datetime.datetime(1879, 3, 14)),
                (13256352000000000, datetime.datetime(1643, 1, 4)),
                (130496832000000000, datetime.datetime(2014, 7, 13))]
        with Variant() as v:
            r = v.set_array_timestamp([data[0][0], data[1][0], data[2][0], data[3][0]])
            self.assertTrue(r == Result.OK)
            vals = v.get_array_uint64()
            self.assertIsNotNone(vals)
            self.assertTrue(len(vals)==4)
            #compare filetime
            self.assertTrue([i for i, x in enumerate(vals) if x == data[i][0]])

    def test_variant_get_datetime(self):
        """ test_variant_get_datetime """
        data = [(116444736000000000, datetime.datetime(1970, 1, 1)),
                (87790176000000000, datetime.datetime(1879, 3, 14)),
                (13256352000000000, datetime.datetime(1643, 1, 4)),
                (130496832000000000, datetime.datetime(2014, 7, 13))]
        with Variant() as v:
            r = v.set_array_timestamp([x[0] for x in data])
            self.assertTrue(r == Result.OK)

            vals = v.get_array_datetime()
            self.assertIsNotNone(vals)
            self.assertTrue(len(vals) == 4)
            #compare datatime
            self.assertTrue([i for i, x in enumerate(vals) if x == data[i][1]])

    def test_variant_set_datetime(self):
        """ test_variant_get_datetime """
        data = [(116444736000000000, datetime.datetime(1970, 1, 1)),
                (87790176000000000, datetime.datetime(1879, 3, 14)),
                (13256352000000000, datetime.datetime(1643, 1, 4)),
                (130496832000000000, datetime.datetime(2014, 7, 13))]
        with Variant() as v:
            r = v.set_array_datetime([x[1] for x in data])
            self.assertTrue(r == Result.OK)

            vals = v.get_array_datetime()
            self.assertIsNotNone(vals)
            self.assertTrue(len(vals) == 4)
            #compare datatime
            self.assertTrue([i for i, x in enumerate(vals) if x == data[i][1]])
            
if __name__ == '__main__':
    unittest.main()
