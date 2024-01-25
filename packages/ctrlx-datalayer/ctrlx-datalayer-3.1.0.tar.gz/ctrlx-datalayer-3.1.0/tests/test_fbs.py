import unittest

import flatbuffers

from ctrlxdatalayer.variant import Variant, Result
from sample import SampleType


class TestFbs(unittest.TestCase):
    """ class TestFbs(unittest.TestCase):
 """

    def test_fbs(self):
        """ test_fbs """
        builder = flatbuffers.Builder(1024)
        sample_string = builder.CreateString("Test123!")
        SampleType.SampleTypeStart(builder)
        SampleType.SampleTypeAddId(builder, 111)
        SampleType.SampleTypeAddText(builder, sample_string)
        sample_type = SampleType.SampleTypeEnd(builder)
        builder.Finish(sample_type)
        with Variant() as v:
            self.assertEqual(v.set_flatbuffers(builder.Output()), Result.OK)

            sample_bytes = v.get_flatbuffers()
            new_sample_type = SampleType.SampleType.GetRootAsSampleType(
                sample_bytes, 0)
            self.assertEqual(new_sample_type.Id(), 111)
            self.assertEqual(
                new_sample_type.Text().decode("utf-8"), "Test123!")

            v.close()
            r = v.set_flatbuffers(builder.Output())
            self.assertTrue(r == Result.NOT_INITIALIZED)


if __name__ == '__main__':
    unittest.main()
