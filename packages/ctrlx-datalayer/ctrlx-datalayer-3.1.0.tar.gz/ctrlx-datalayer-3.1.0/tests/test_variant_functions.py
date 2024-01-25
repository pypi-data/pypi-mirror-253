import faulthandler
import unittest

from ctrlxdatalayer.variant import Result, Variant, VariantType

faulthandler.enable()


class TestVariantFunctions(unittest.TestCase):
    """ TestVariantFunctions """

    def test_bool8(self):
        """ test_bool8 """
        with Variant() as v:
            r = v.set_bool8(True)
            self.assertTrue(r == Result.OK)
            self.assertTrue(v.get_type() == VariantType.BOOL8)
            self.assertTrue(v.get_size() == 1)
            self.assertTrue(v.get_count() == 1)
            b = v.get_data()
            self.assertTrue(len(b) == 1)
            self.assertTrue(b == b'\x01')
            r = v.check_convert(VariantType.STRING)
            self.assertTrue(r == Result.TYPE_MISMATCH)
            r, c = v.clone()
            self.assertTrue(r == Result.OK)
            self.assertIsNotNone(c)
            self.assertTrue(v.get_bool8() == c.get_bool8())
            c.close()
            r, c = Variant.copy(v.get_handle())
            self.assertTrue(r == Result.OK)
            self.assertIsNotNone(c)
            self.assertTrue(v.get_bool8() == c.get_bool8())
            c.close()

    def test_int8(self):
        """ test_int8 """
        with Variant() as v:
            r = v.set_int8(1)
            self.assertTrue(r == Result.OK)
            self.assertTrue(v.get_type() == VariantType.INT8)
            self.assertTrue(v.get_size() == 1)
            self.assertTrue(v.get_count() == 1)
            b = v.get_data()
            self.assertTrue(len(b) == 1)
            self.assertTrue(b == b'\x01')
            r = v.check_convert(VariantType.STRING)
            self.assertTrue(r == Result.TYPE_MISMATCH)
            r, c = v.clone()
            self.assertTrue(r == Result.OK)
            self.assertIsNotNone(c)
            self.assertTrue(v.get_int8() == c.get_int8())
            c.close()
            r, c = Variant.copy(v.get_handle())
            self.assertTrue(r == Result.OK)
            self.assertIsNotNone(c)
            self.assertTrue(v.get_int8() == c.get_int8())
            c.close()

    def test_uint8(self):
        """ test_uint8 """
        with Variant() as v:
            r = v.set_uint8(255)
            self.assertTrue(r == Result.OK)
            self.assertTrue(v.get_type() == VariantType.UINT8)
            self.assertTrue(v.get_size() == 1)
            self.assertTrue(v.get_count() == 1)
            b = v.get_data()
            self.assertTrue(len(b) == 1)
            self.assertTrue(b == b'\xff')
            r = v.check_convert(VariantType.STRING)
            self.assertTrue(r == Result.TYPE_MISMATCH)
            r, c = v.clone()
            self.assertTrue(r == Result.OK)
            self.assertIsNotNone(c)
            self.assertTrue(v.get_uint8() == c.get_uint8())
            c.close()

    def test_int16(self):
        """ test_int16 """
        with Variant() as v:
            r = v.set_int16(-1)
            self.assertTrue(r == Result.OK)
            self.assertTrue(v.get_type() == VariantType.INT16)
            self.assertTrue(v.get_size() == 2)
            self.assertTrue(v.get_count() == 1)
            b = v.get_data()
            self.assertTrue(len(b) == 2)
            self.assertTrue(b == b'\xff\xff')
            r = v.check_convert(VariantType.STRING)
            self.assertTrue(r == Result.TYPE_MISMATCH)
            r, c = v.clone()
            self.assertTrue(r == Result.OK)
            self.assertIsNotNone(c)
            self.assertTrue(v.get_int16() == c.get_int16())
            c.close()

    def test_uint16(self):
        """ test_uint16 """
        with Variant() as v:
            r = v.set_uint16(-1)
            self.assertTrue(r == Result.OK)
            self.assertTrue(v.get_type() == VariantType.UINT16)
            self.assertTrue(v.get_size() == 2)
            self.assertTrue(v.get_count() == 1)
            b = v.get_data()
            self.assertTrue(len(b) == 2)
            self.assertTrue(b == b'\xff\xff')
            r = v.check_convert(VariantType.STRING)
            self.assertTrue(r == Result.TYPE_MISMATCH)
            r, c = v.clone()
            self.assertTrue(r == Result.OK)
            self.assertIsNotNone(c)
            self.assertTrue(v.get_uint16() == c.get_uint16())
            c.close()

    def test_int32(self):
        """ test_int32 """
        with Variant() as v:
            r = v.set_int32(-1)
            self.assertTrue(r == Result.OK)
            self.assertTrue(v.get_type() == VariantType.INT32)
            self.assertTrue(v.get_size() == 4)
            self.assertTrue(v.get_count() == 1)
            b = v.get_data()
            self.assertTrue(len(b) == 4)
            self.assertTrue(b == b'\xff\xff\xff\xff')
            r = v.check_convert(VariantType.STRING)
            self.assertTrue(r == Result.TYPE_MISMATCH)
            r, c = v.clone()
            self.assertTrue(r == Result.OK)
            self.assertIsNotNone(c)
            self.assertTrue(v.get_int32() == c.get_int32())
            c.close()

    def test_uint32(self):
        """ test_uint32 """
        with Variant() as v:
            r = v.set_uint32(-1)
            self.assertTrue(r == Result.OK)
            self.assertTrue(v.get_type() == VariantType.UINT32)
            self.assertTrue(v.get_size() == 4)
            self.assertTrue(v.get_count() == 1)
            b = v.get_data()
            self.assertTrue(len(b) == 4)
            self.assertTrue(b == b'\xff\xff\xff\xff')
            r = v.check_convert(VariantType.STRING)
            self.assertTrue(r == Result.TYPE_MISMATCH)
            r, c = v.clone()
            self.assertTrue(r == Result.OK)
            self.assertIsNotNone(c)
            self.assertTrue(v.get_uint32() == c.get_uint32())
            c.close()

    def test_int64(self):
        """ test_int64 """
        with Variant() as v:
            r = v.set_int64(-1)
            self.assertTrue(r == Result.OK)
            self.assertTrue(v.get_type() == VariantType.INT64)
            self.assertTrue(v.get_size() == 8)
            self.assertTrue(v.get_count() == 1)
            b = v.get_data()
            self.assertTrue(len(b) == 8)
            self.assertTrue(b == b'\xff\xff\xff\xff\xff\xff\xff\xff')
            r = v.check_convert(VariantType.STRING)
            self.assertTrue(r == Result.TYPE_MISMATCH)
            r, c = v.clone()
            self.assertTrue(r == Result.OK)
            self.assertIsNotNone(c)
            self.assertTrue(v.get_int64() == c.get_int64())
            c.close()

    def test_uint64(self):
        """ test_uint64 """
        with Variant() as v:
            r = v.set_uint64(-1)
            self.assertTrue(r == Result.OK)
            self.assertTrue(v.get_type() == VariantType.UINT64)
            self.assertTrue(v.get_size() == 8)
            self.assertTrue(v.get_count() == 1)
            b = v.get_data()
            self.assertTrue(len(b) == 8)
            self.assertTrue(b == b'\xff\xff\xff\xff\xff\xff\xff\xff')
            r = v.check_convert(VariantType.STRING)
            self.assertTrue(r == Result.TYPE_MISMATCH)
            r, c = v.clone()
            self.assertTrue(r == Result.OK)
            self.assertIsNotNone(c)
            self.assertTrue(v.get_uint64() == c.get_uint64())
            c.close()

    def test_float32(self):
        """ test_float32 """
        with Variant() as v:
            r = v.set_float32(-1)
            self.assertTrue(r == Result.OK)
            self.assertTrue(v.get_type() == VariantType.FLOAT32)
            self.assertTrue(v.get_size() == 4)
            self.assertTrue(v.get_count() == 1)
            b = v.get_data()
            self.assertTrue(len(b) == 4)
            self.assertTrue(b == b'\x00\x00\x80\xbf')
            r = v.check_convert(VariantType.STRING)
            self.assertTrue(r == Result.TYPE_MISMATCH)
            r, c = v.clone()
            self.assertTrue(r == Result.OK)
            self.assertIsNotNone(c)
            self.assertTrue(v.get_float32() == c.get_float32())
            c.close()

    def test_float64(self):
        """ test_float64 """
        with Variant() as v:
            r = v.set_float64(-1)
            self.assertTrue(r == Result.OK)
            self.assertTrue(v.get_type() == VariantType.FLOAT64)
            self.assertTrue(v.get_size() == 8)
            self.assertTrue(v.get_count() == 1)
            b = v.get_data()
            self.assertTrue(len(b) == 8)
            self.assertTrue(b == b'\x00\x00\x00\x00\x00\x00\xf0\xbf')
            r = v.check_convert(VariantType.STRING)
            self.assertTrue(r == Result.TYPE_MISMATCH)
            r, c = v.clone()
            self.assertTrue(r == Result.OK)
            self.assertIsNotNone(c)
            self.assertTrue(v.get_float64() == c.get_float64())
            c.close()

    def test_string(self):
        """ test_string """
        with Variant() as v:
            r = v.set_string("hello")
            self.assertTrue(r == Result.OK)
            self.assertTrue(v.get_type() == VariantType.STRING)
            self.assertTrue(v.get_size() == 6)
            self.assertTrue(v.get_count() == 1)
            b = v.get_data()
            self.assertTrue(len(b) == 6)
            self.assertTrue(b == bytearray(b'hello\x00'))
            r = v.check_convert(VariantType.STRING)
            self.assertTrue(r == Result.OK)
            r, c = v.clone()
            self.assertTrue(r == Result.OK)
            self.assertIsNotNone(c)
            self.assertTrue(v.get_string() == c.get_string())
            c.close()

    def test_array_bool8(self):
        """ test_array_bool8 """
        with Variant() as v:
            r = v.set_array_bool8([True, False])
            self.assertTrue(r == Result.OK)
            self.assertTrue(v.get_type() == VariantType.ARRAY_BOOL8)
            self.assertTrue(v.get_size() == 2)
            self.assertTrue(v.get_count() == 2)
            b = v.get_data()
            self.assertTrue(len(b) == 2)
            self.assertTrue(b == b'\x01\x00')
            r = v.check_convert(VariantType.STRING)
            self.assertTrue(r == Result.TYPE_MISMATCH)
            r, c = v.clone()
            self.assertTrue(r == Result.OK)
            self.assertIsNotNone(c)
            self.assertTrue(v.get_array_bool8() == c.get_array_bool8())
            c.close()

    def test_array_int8(self):
        """ test_array_int8 """
        with Variant() as v:
            r = v.set_array_int8([1, 2])
            self.assertTrue(r == Result.OK)
            self.assertTrue(v.get_type() == VariantType.ARRAY_INT8)
            self.assertTrue(v.get_size() == 2)
            self.assertTrue(v.get_count() == 2)
            b = v.get_data()
            self.assertTrue(len(b) == 2)
            self.assertTrue(b == b'\x01\x02')
            r = v.check_convert(VariantType.STRING)
            self.assertTrue(r == Result.TYPE_MISMATCH)
            r, c = v.clone()
            self.assertTrue(r == Result.OK)
            self.assertIsNotNone(c)
            self.assertTrue(v.get_array_int8() == c.get_array_int8())
            c.close()

    def test_array_uint8(self):
        """ test_array_uint8 """
        with Variant() as v:
            r = v.set_array_uint8([1, 2])
            self.assertTrue(r == Result.OK)
            self.assertTrue(v.get_type() == VariantType.ARRAY_UINT8)
            self.assertTrue(v.get_size() == 2)
            self.assertTrue(v.get_count() == 2)
            b = v.get_data()
            self.assertTrue(len(b) == 2)
            self.assertTrue(b == b'\x01\x02')
            r = v.check_convert(VariantType.STRING)
            self.assertTrue(r == Result.TYPE_MISMATCH)
            r, c = v.clone()
            self.assertTrue(r == Result.OK)
            self.assertIsNotNone(c)
            self.assertTrue(v.get_array_uint8() == c.get_array_uint8())
            c.close()

    def test_array_int16(self):
        """ test_array_int16 """
        with Variant() as v:
            r = v.set_array_int16([1, 2])
            self.assertTrue(r == Result.OK)
            self.assertTrue(v.get_type() == VariantType.ARRAY_INT16)
            self.assertTrue(v.get_size() == 4)
            self.assertTrue(v.get_count() == 2)
            b = v.get_data()
            self.assertTrue(len(b) == 4)
            self.assertTrue(b == b'\x01\x00\x02\x00')
            r = v.check_convert(VariantType.STRING)
            self.assertTrue(r == Result.TYPE_MISMATCH)
            r, c = v.clone()
            self.assertTrue(r == Result.OK)
            self.assertIsNotNone(c)
            self.assertTrue(v.get_array_int16() == c.get_array_int16())
            c.close()

    def test_array_uint16(self):
        """ test_array_uint16 """
        with Variant() as v:
            r = v.set_array_uint16([1, 2])
            self.assertTrue(r == Result.OK)
            self.assertTrue(v.get_type() == VariantType.ARRAY_UINT16)
            self.assertTrue(v.get_size() == 4)
            self.assertTrue(v.get_count() == 2)
            b = v.get_data()
            self.assertTrue(len(b) == 4)
            self.assertTrue(b == b'\x01\x00\x02\x00')
            r = v.check_convert(VariantType.STRING)
            self.assertTrue(r == Result.TYPE_MISMATCH)
            r, c = v.clone()
            self.assertTrue(r == Result.OK)
            self.assertIsNotNone(c)
            self.assertTrue(v.get_array_uint16() == c.get_array_uint16())
            c.close()

    def test_array_int32(self):
        """ test_array_int32 """
        with Variant() as v:
            r = v.set_array_int32([1, 2])
            self.assertTrue(r == Result.OK)
            self.assertTrue(v.get_type() == VariantType.ARRAY_INT32)
            self.assertTrue(v.get_size() == 8)
            self.assertTrue(v.get_count() == 2)
            b = v.get_data()
            self.assertTrue(len(b) == 8)
            self.assertTrue(b == b'\x01\x00\x00\x00\x02\x00\x00\x00')
            r = v.check_convert(VariantType.STRING)
            self.assertTrue(r == Result.TYPE_MISMATCH)
            r, c = v.clone()
            self.assertTrue(r == Result.OK)
            self.assertIsNotNone(c)
            self.assertTrue(v.get_array_int32() == c.get_array_int32())
            c.close()

    def test_array_uint32(self):
        """ test_array_uint32 """
        with Variant() as v:
            r = v.set_array_uint32([1, 2])
            self.assertTrue(r == Result.OK)
            self.assertTrue(v.get_type() == VariantType.ARRAY_UINT32)
            self.assertTrue(v.get_size() == 8)
            self.assertTrue(v.get_count() == 2)
            b = v.get_data()
            self.assertTrue(len(b) == 8)
            self.assertTrue(b == b'\x01\x00\x00\x00\x02\x00\x00\x00')
            r = v.check_convert(VariantType.STRING)
            self.assertTrue(r == Result.TYPE_MISMATCH)
            r, c = v.clone()
            self.assertTrue(r == Result.OK)
            self.assertIsNotNone(c)
            self.assertTrue(v.get_array_uint32() == c.get_array_uint32())
            c.close()

    def test_array_int64(self):
        """ test_array_int64 """
        with Variant() as v:
            r = v.set_array_int64([1, 2])
            self.assertTrue(r == Result.OK)
            self.assertTrue(v.get_type() == VariantType.ARRAY_INT64)
            self.assertTrue(v.get_size() == 16)
            self.assertTrue(v.get_count() == 2)
            b = v.get_data()
            self.assertTrue(len(b) == 16)
            self.assertTrue(
                b == b'\x01\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00')
            r = v.check_convert(VariantType.STRING)
            self.assertTrue(r == Result.TYPE_MISMATCH)
            r, c = v.clone()
            self.assertTrue(r == Result.OK)
            self.assertIsNotNone(c)
            self.assertTrue(v.get_array_int64() == c.get_array_int64())
            c.close()

    def test_array_uint64(self):
        """ test_array_uint64 """
        with Variant() as v:
            r = v.set_array_uint64([1, 2])
            self.assertTrue(r == Result.OK)
            self.assertTrue(v.get_type() == VariantType.ARRAY_UINT64)
            self.assertTrue(v.get_size() == 16)
            self.assertTrue(v.get_count() == 2)
            b = v.get_data()
            self.assertTrue(len(b) == 16)
            self.assertTrue(
                b == b'\x01\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00')
            r = v.check_convert(VariantType.STRING)
            self.assertTrue(r == Result.TYPE_MISMATCH)
            r, c = v.clone()
            self.assertTrue(r == Result.OK)
            self.assertIsNotNone(c)
            self.assertTrue(v.get_array_uint64() == c.get_array_uint64())
            c.close()

    def test_array_float32(self):
        """ test_array_float32 """
        with Variant() as v:
            r = v.set_array_float32([1, 2])
            self.assertTrue(r == Result.OK)
            self.assertTrue(v.get_type() == VariantType.ARRAY_FLOAT32)
            self.assertTrue(v.get_size() == 8)
            self.assertTrue(v.get_count() == 2)
            b = v.get_data()
            self.assertTrue(len(b) == 8)
            self.assertTrue(b == bytearray(b'\x00\x00\x80?\x00\x00\x00@'))
            r = v.check_convert(VariantType.STRING)
            self.assertTrue(r == Result.TYPE_MISMATCH)
            r, c = v.clone()
            self.assertTrue(r == Result.OK)
            self.assertIsNotNone(c)
            self.assertTrue(v.get_array_float32() == c.get_array_float32())
            c.close()

    def test_array_float64(self):
        """ test_array_float64 """
        with Variant() as v:
            r = v.set_array_float64([1, 2])
            self.assertTrue(r == Result.OK)
            self.assertTrue(v.get_type() == VariantType.ARRAY_FLOAT64)
            self.assertTrue(v.get_size() == 16)
            self.assertTrue(v.get_count() == 2)
            b = v.get_data()
            self.assertTrue(len(b) == 16)
            self.assertTrue(b == bytearray(
                b'\x00\x00\x00\x00\x00\x00\xf0?\x00\x00\x00\x00\x00\x00\x00@'))
            r = v.check_convert(VariantType.STRING)
            self.assertTrue(r == Result.TYPE_MISMATCH)
            r, c = v.clone()
            self.assertTrue(r == Result.OK)
            self.assertIsNotNone(c)
            self.assertTrue(v.get_array_float64() == c.get_array_float64())
            c.close()

    def test_array_bool8_reinit(self):
        """ test_array_bool8 """
        with Variant() as v:
            r = v.set_array_bool8([True, False])
            self.assertTrue(r == Result.OK)
            self.assertTrue(v.get_type() == VariantType.ARRAY_BOOL8)
            self.assertTrue(v.get_size() == 2)
            self.assertTrue(v.get_count() == 2)

            r = v.set_array_bool8([False, True, False])
            self.assertTrue(r == Result.OK)
            self.assertTrue(v.get_type() == VariantType.ARRAY_BOOL8)
            self.assertTrue(v.get_size() == 3)
            self.assertTrue(v.get_count() == 3)


if __name__ == '__main__':
    unittest.main()
