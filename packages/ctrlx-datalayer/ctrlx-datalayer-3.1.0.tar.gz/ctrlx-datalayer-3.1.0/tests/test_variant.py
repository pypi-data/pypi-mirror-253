import datetime
import faulthandler
import unittest

from ctrlxdatalayer.variant import Result, Variant, VariantRef, copy

faulthandler.enable()


class TestVariantBase(unittest.TestCase):
    """ TestVariantBase """

    def test_result(self):
        """ test_result """
        r = Result(Result.OK)
        self.assertTrue(r == Result.OK)
        r = Result(0)
        self.assertTrue(r == Result.OK)

        r = Result(Result.FAILED)
        self.assertTrue(r == Result.FAILED)
        r = Result(0x80000001)
        self.assertTrue(r == Result.FAILED)

        r = Result(Result.CLIENT_NOT_CONNECTED)
        self.assertTrue(r == Result.CLIENT_NOT_CONNECTED)
        r = Result(0x80030001)
        self.assertTrue(r == Result.CLIENT_NOT_CONNECTED)

        r = Result(0x80010001)
        self.assertTrue(r == Result.INVALID_ADDRESS)
        r = -2147418111
        r = r & 0xFFFFFFFF
        self.assertTrue(Result(r) == Result.INVALID_ADDRESS)

        r = -2147418111
        self.assertTrue(Result(r) == Result.INVALID_ADDRESS)

        r = -2147418099
        self.assertTrue(Result(r) == Result.INVALID_VALUE)

        r = 0x80070005
        self.assertTrue(Result(r) == Result.SEC_PAYMENT_REQUIRED)

        r = 0x8001001B
        self.assertTrue(Result(r) == Result.WOULD_BLOCK)

        r = 0x80060009
        self.assertTrue(Result(r) == Result.RT_MALLOC_FAILED)

        # different handling between python 3.6 and 3.8
        #r = -1701
        #v = Result(r)
        #self.assertTrue(v == r)

        #r = 0x80070004+1
        #v = Result(r)
        #self.assertTrue(v == r)

    def test_close(self):
        """ test_close """
        # test auf segfault
        with Variant() as v:
            v.close()

    def test_variantref(self):
        """ test_variantref """
        with Variant() as v:
            r = v.set_int16(123)
            self.assertTrue(r == Result.OK)
            with VariantRef(v.get_handle()) as ref:
                self.assertIsNotNone(ref)
                self.assertTrue(v.get_int16() == ref.get_int16())
                ref.close()


class TestVariantScalar(unittest.TestCase):
    """ TestVariantScalar """

    def test_bool8(self):
        """ test_bool8 """
        with Variant() as v:
            r = v.set_bool8(True)
            self.assertTrue(r == Result.OK)
            b = v.get_bool8()
            self.assertTrue(b == True)

            r = v.set_bool8(False)
            self.assertTrue(r == Result.OK)
            b = v.get_bool8()
            self.assertTrue(b == False)

    def test_int8(self):
        """ test_int8 """
        with Variant() as v:
            r = v.set_int8(-128)
            self.assertTrue(r == Result.OK)
            b = v.get_int8()
            self.assertTrue(b == -128)

            r = v.set_int8(127)
            self.assertTrue(r == Result.OK)
            b = v.get_int8()
            self.assertTrue(b == 127)

    def test_uint8(self):
        """ test_uint8 """
        with Variant() as v:
            r = v.set_uint8(0)
            self.assertTrue(r == Result.OK)
            b = v.get_uint8()
            self.assertTrue(b == 0)

            r = v.set_uint8(255)
            self.assertTrue(r == Result.OK)
            b = v.get_uint8()
            self.assertTrue(b == 255)

    def test_int16(self):
        """ test_int16 """
        with Variant() as v:
            r = v.set_int16(-32768)
            self.assertTrue(r == Result.OK)
            b = v.get_int16()
            self.assertTrue(b == -32768)

            r = v.set_int16(32767)
            self.assertTrue(r == Result.OK)
            b = v.get_int16()
            self.assertTrue(b == 32767)

    def test_uint16(self):
        """ test_uint16 """
        with Variant() as v:
            r = v.set_uint16(0)
            self.assertTrue(r == Result.OK)
            b = v.get_uint16()
            self.assertTrue(b == 0)

            r = v.set_uint16(65535)
            self.assertTrue(r == Result.OK)
            b = v.get_uint16()
            self.assertTrue(b == 65535)

    def test_int32(self):
        """ test_int32 """
        with Variant() as v:
            r = v.set_int32(-2147483648)
            self.assertTrue(r == Result.OK)
            b = v.get_int32()
            self.assertTrue(b == -2147483648)

            r = v.set_int32(2147483647)
            self.assertTrue(r == Result.OK)
            b = v.get_int32()
            self.assertTrue(b == 2147483647)

    def test_uint32(self):
        """ test_uint32 """
        with Variant() as v:
            r = v.set_uint32(0)
            self.assertTrue(r == Result.OK)
            b = v.get_uint32()
            self.assertTrue(b == 0)

            r = v.set_uint32(4294967295)
            self.assertTrue(r == Result.OK)
            b = v.get_uint32()
            self.assertTrue(b == 4294967295)

    def test_int64(self):
        """ test_int64 """
        with Variant() as v:
            r = v.set_int64(-9223372036854775808)
            self.assertTrue(r == Result.OK)
            b = v.get_int64()
            self.assertTrue(b == -9223372036854775808)

            r = v.set_int64(9223372036854775807)
            self.assertTrue(r == Result.OK)
            b = v.get_int64()
            self.assertTrue(b == 9223372036854775807)

    def test_uint64(self):
        """ test_uint64 """
        with Variant() as v:
            r = v.set_uint64(0)
            self.assertTrue(r == Result.OK)
            b = v.get_uint64()
            self.assertTrue(b == 0)

            r = v.set_uint64(18446744073709551615)
            self.assertTrue(r == Result.OK)
            b = v.get_uint64()
            self.assertTrue(b == 18446744073709551615)

    def test_float32(self):
        """ test_float32 """
        with Variant() as v:
            r = v.set_float32(-3.14)
            self.assertTrue(r == Result.OK)
            b = v.get_float32()
            self.assertTrue(b <= -3.14)

            r = v.set_float32(3.14)
            self.assertTrue(r == Result.OK)
            b = v.get_float32()
            self.assertTrue(b >= 3.14)

    def test_float64(self):
        """ test_float64 """
        with Variant() as v:
            r = v.set_float64(-3.14)
            self.assertTrue(r == Result.OK)
            b = v.get_float64()
            self.assertTrue(b <= -3.14)

            r = v.set_float64(3.14)
            self.assertTrue(r == Result.OK)
            b = v.get_float64()
            self.assertTrue(b >= 3.14)

    def test_timestamp(self):
        """ test_timestamp """
        with Variant() as v:
            r = v.set_timestamp(0)
            self.assertTrue(r == Result.OK)
            b = v.get_uint64()
            self.assertTrue(b == 0)

            r = v.set_timestamp(116444736000000000)
            self.assertTrue(r == Result.OK)
            b = v.get_uint64()
            self.assertTrue(b == 116444736000000000)

    def test_datetime(self):
        """ test_datetime """
        data = [(116444736000000000, datetime.datetime(1970, 1, 1)),
                (87790176000000000, datetime.datetime(1879, 3, 14)),
                (13256352000000000, datetime.datetime(1643, 1, 4)),
                (130496832000000000, datetime.datetime(2014, 7, 13))]
        for x in data:
            ft = x[0]
            dt = x[1]

            date_time = Variant.from_filetime(ft)
            # print(date_time)
            self.assertEqual(date_time, dt)
            file_time = Variant.to_filetime(dt)
            # print(file_time)
            self.assertEqual(file_time, ft)

    def test_setdatetime(self):
        """ test_setdatetime """
        data = [(116444736000000000, datetime.datetime(1970, 1, 1)),
                (87790176000000000, datetime.datetime(1879, 3, 14)),
                (13256352000000000, datetime.datetime(1643, 1, 4)),
                (130496832000000000, datetime.datetime(2014, 7, 13))]
        for x in data:
            ft = x[0]
            dt = x[1]
            with Variant() as v:
                r = v.set_datetime(dt)
                self.assertTrue(r == Result.OK)
                b = v.get_uint64()
                self.assertTrue(b == ft)

    def test_getdatetime(self):
        """ test_getdatetime """
        data = [(116444736000000000, datetime.datetime(1970, 1, 1)),
                (87790176000000000, datetime.datetime(1879, 3, 14)),
                (13256352000000000, datetime.datetime(1643, 1, 4)),
                (130496832000000000, datetime.datetime(2014, 7, 13))]
        for x in data:
            ft = x[0]
            dt = x[1]
            with Variant() as v:
                r = v.set_datetime(dt)
                self.assertTrue(r == Result.OK)
                d = v.get_datetime()
                self.assertEqual(d, dt)
                r = v.set_timestamp(ft)
                self.assertTrue(r == Result.OK)
                d = v.get_datetime()
                self.assertEqual(d, dt)


class TestVariantError(unittest.TestCase):
    """ TestVariantError """

    def test_bool8(self):
        """ test_bool8 """
        with Variant() as v:
            r = v.set_bool8(True)
            self.assertTrue(r == Result.OK)
            b = v.get_bool8()
            self.assertTrue(b == True)

            v.close()

            r = v.set_bool8(False)
            self.assertTrue(r == Result.NOT_INITIALIZED)

    def test_int8(self):
        """ test_int8 """
        with Variant() as v:
            r = v.set_int8(-128)
            self.assertTrue(r == Result.OK)
            b = v.get_int8()
            self.assertTrue(b == -128)

            v.close()

            r = v.set_int8(127)
            self.assertTrue(r == Result.NOT_INITIALIZED)

    def test_uint8(self):
        """ test_uint8 """
        with Variant() as v:
            r = v.set_uint8(0)
            self.assertTrue(r == Result.OK)
            b = v.get_uint8()
            self.assertTrue(b == 0)

            v.close()

            r = v.set_uint8(255)
            self.assertTrue(r == Result.NOT_INITIALIZED)

    def test_int16(self):
        """ test_int16 """
        with Variant() as v:
            r = v.set_int16(-32768)
            self.assertTrue(r == Result.OK)
            b = v.get_int16()
            self.assertTrue(b == -32768)

            v.close()

            r = v.set_int16(32767)
            self.assertTrue(r == Result.NOT_INITIALIZED)

    def test_uint16(self):
        """ test_uint16 """
        with Variant() as v:
            r = v.set_uint16(0)
            self.assertTrue(r == Result.OK)
            b = v.get_uint16()
            self.assertTrue(b == 0)

            v.close()

            r = v.set_uint16(65535)
            self.assertTrue(r == Result.NOT_INITIALIZED)

    def test_int32(self):
        """ test_int32 """
        with Variant() as v:
            r = v.set_int32(-2147483648)
            self.assertTrue(r == Result.OK)
            b = v.get_int32()
            self.assertTrue(b == -2147483648)

            v.close()

            r = v.set_int32(2147483647)
            self.assertTrue(r == Result.NOT_INITIALIZED)

    def test_uint32(self):
        """ test_uint32 """
        with Variant() as v:
            r = v.set_uint32(0)
            self.assertTrue(r == Result.OK)
            b = v.get_uint32()
            self.assertTrue(b == 0)

            v.close()

            r = v.set_uint32(4294967295)
            self.assertTrue(r == Result.NOT_INITIALIZED)

    def test_int64(self):
        """ test_int64 """
        with Variant() as v:
            r = v.set_int64(-9223372036854775808)
            self.assertTrue(r == Result.OK)
            b = v.get_int64()
            self.assertTrue(b == -9223372036854775808)

            v.close()

            r = v.set_int64(9223372036854775807)
            self.assertTrue(r == Result.NOT_INITIALIZED)

    def test_uint64(self):
        """ test_uint64 """
        with Variant() as v:
            r = v.set_uint64(0)
            self.assertTrue(r == Result.OK)
            b = v.get_uint64()
            self.assertTrue(b == 0)

            v.close()

            r = v.set_uint64(18446744073709551615)
            self.assertTrue(r == Result.NOT_INITIALIZED)

    def test_float32(self):
        """ test_float32 """
        with Variant() as v:
            r = v.set_float32(-3.14)
            self.assertTrue(r == Result.OK)
            b = v.get_float32()
            self.assertTrue(b <= -3.14)

            v.close()

            r = v.set_float32(3.14)
            self.assertTrue(r == Result.NOT_INITIALIZED)

    def test_float64(self):
        """ test_float64 """
        with Variant() as v:
            r = v.set_float64(-3.14)
            self.assertTrue(r == Result.OK)
            b = v.get_float64()
            self.assertTrue(b <= -3.14)

            v.close()

            r = v.set_float64(3.14)
            self.assertTrue(r == Result.NOT_INITIALIZED)

    def test_copy(self):
        """ test_float64 """
        with Variant() as s, Variant() as d:
            d.set_bool8(False)
            s.set_bool8(True)
            r = copy(d, s)
            self.assertTrue(r == Result.OK)
            self.assertTrue(d.get_bool8() == True)


if __name__ == '__main__':
    unittest.main()
