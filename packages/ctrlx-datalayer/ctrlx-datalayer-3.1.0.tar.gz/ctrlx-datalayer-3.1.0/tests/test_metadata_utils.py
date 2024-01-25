""" Tests for metadata_utils.py """

import unittest

from comm.datalayer import DisplayFormat, Metadata, NodeClass

from ctrlxdatalayer.metadata_utils import (AllowedOperation, MetadataBuilder,
                                           ReferenceType)


class TestReferenceType(unittest.TestCase):
    """ TestAllowedOperationFlags """

    def test_typess(self):
        """ Test all types """

        str_len = len(ReferenceType.create())
        self.assertTrue(str_len > 0)

        str_len = len(ReferenceType.has_save())
        self.assertTrue(str_len > 0)

        str_len = len(ReferenceType.read())
        self.assertTrue(str_len > 0)

        str_len = len(ReferenceType.read_in())
        self.assertTrue(str_len > 0)

        str_len = len(ReferenceType.read_out())
        self.assertTrue(str_len > 0)

        str_len = len(ReferenceType.uses())
        self.assertTrue(str_len > 0)

        str_len = len(ReferenceType.write())
        self.assertTrue(str_len > 0)

        str_len = len(ReferenceType.write_in())
        self.assertTrue(str_len > 0)

        str_len = len(ReferenceType.write_out())
        self.assertTrue(str_len > 0)


class TestMetadataBuilder(unittest.TestCase):
    """ TestMetadataBuilder """

    def test_create_metadata(self):
        """ Test all types """
        metadata = MetadataBuilder.create_metadata(
            name="name",
            description="description", unit="unit", description_url="description-url",
            node_class=NodeClass.NodeClass.Variable,
            read_allowed=True, write_allowed=True, create_allowed=True,
            delete_allowed=False, browse_allowed=False,
            type_path="/this/is/a/type/path")
        self.assertIsNotNone(metadata)
        m = Metadata.Metadata.GetRootAsMetadata(
            metadata.get_flatbuffers(), 0)
        self.assertIsNotNone(m)
        o = m.Operations()
        self.assertIsNotNone(o)
        self.assertTrue(o.Read())
        self.assertTrue(o.Write())
        self.assertTrue(o.Create())
        self.assertFalse(o.Delete())
        self.assertFalse(o.Browse())
        self.assertEqual(m.NodeClass(), NodeClass.NodeClass.Variable)
        self.assertEqual(str(m.Description(), 'utf-8'), "description")
        self.assertEqual(str(m.DescriptionUrl(), 'utf-8'), "description-url")
        self.assertEqual(str(m.DisplayName(), 'utf-8'), "name")
        self.assertEqual(str(m.Unit(), 'utf-8'), "unit")
        l = m.ReferencesLength()
        self.assertEqual(l, 3)
        t = m.References(0)
        self.assertIsNotNone(t)
        self.assertEqual(str(t.Type(), 'utf-8'), ReferenceType.create())
        self.assertEqual(str(t.TargetAddress(), 'utf-8'),
                         "/this/is/a/type/path")
        t = m.References(1)
        self.assertIsNotNone(t)
        self.assertEqual(str(t.Type(), 'utf-8'), ReferenceType.read())
        self.assertEqual(str(t.TargetAddress(), 'utf-8'),
                         "/this/is/a/type/path")
        t = m.References(2)
        self.assertIsNotNone(t)
        self.assertEqual(str(t.Type(), 'utf-8'), ReferenceType.write())
        self.assertEqual(str(t.TargetAddress(), 'utf-8'),
                         "/this/is/a/type/path")
        metadata.close()

    def test_metadata_builder(self):
        """ Test MetadataBuilder """
        builder = MetadataBuilder(AllowedOperation.READ)
        self.assertIsNotNone(builder)
        metadata = builder.build()
        with metadata:
            self.assertIsNotNone(metadata)
            m = Metadata.Metadata.GetRootAsMetadata(
                metadata.get_flatbuffers(), 0)
            self.assertIsNotNone(m)
            o = m.Operations()
            self.assertIsNotNone(o)
            self.assertTrue(o.Read())
            self.assertFalse(o.Write())

    def test_metadata_builder_simple(self):
        """ Test MetadataBuilder """
        builder = MetadataBuilder(description="test")
        self.assertIsNotNone(builder)
        metadata = builder.set_unit(
            "m/s").set_node_class(NodeClass.NodeClass.Variable).set_operations(AllowedOperation.READ | AllowedOperation.WRITE).build()
        with metadata:
            self.assertIsNotNone(metadata)
            m = Metadata.Metadata.GetRootAsMetadata(
                metadata.get_flatbuffers(), 0)
            self.assertIsNotNone(m)
            o = m.Operations()
            self.assertIsNotNone(o)
            self.assertTrue(o.Read())
            self.assertTrue(o.Write())
            self.assertEqual(str(m.Unit(), 'utf-8'), "m/s")
            self.assertEqual(m.NodeClass(), NodeClass.NodeClass.Variable)

    def test_metadata_builder_all(self):
        """ Test MetadataBuilder all"""

        builder = MetadataBuilder(
            description="description", description_url="description_url")
        self.assertIsNotNone(builder)
        metadata = builder.set_unit(
            "m/s").set_node_class(NodeClass.NodeClass.Variable).set_operations(AllowedOperation.ALL).set_display_format(DisplayFormat.DisplayFormat.Bin).build()
        with metadata:
            self.assertIsNotNone(metadata)
            m = Metadata.Metadata.GetRootAsMetadata(
                metadata.get_flatbuffers(), 0)
            self.assertIsNotNone(m)
            o = m.Operations()
            self.assertIsNotNone(o)
            self.assertTrue(o.Read())
            self.assertTrue(o.Write())
            self.assertTrue(o.Delete())
            self.assertTrue(o.Browse())
            self.assertTrue(o.Create())
            self.assertEqual(m.DisplayFormat(),
                             DisplayFormat.DisplayFormat.Bin)

    def test_metadata_builder_reference(self):
        """ Test MetadataBuilder test_metadata_builder_reference"""

        builder = MetadataBuilder(
            description="description", description_url="description_url")
        self.assertIsNotNone(builder)
        builder.add_reference(ReferenceType.write(), "/this/is/a/type/path")
        builder.add_reference(ReferenceType.read(), "/this/is/a/type/path")
        builder.add_reference(ReferenceType.write_out(),
                              "/this/is/a/type/path")
        builder.add_reference(ReferenceType.read_in(), "/this/is/a/type/path")
        builder.add_reference(ReferenceType.create(), "/this/is/a/type/path")
        builder.add_reference(ReferenceType.write_in(), "/this/is/a/type/path")
        builder.add_reference(ReferenceType.read_out(), "/this/is/a/type/path")

        builder.set_unit(
            "m/s").set_node_class(NodeClass.NodeClass.Variable).set_operations(AllowedOperation.READ | AllowedOperation.WRITE | AllowedOperation.BROWSE | AllowedOperation.CREATE | AllowedOperation.DELETE)
        metadata = builder.build()
        with metadata:
            self.assertIsNotNone(metadata)
            m = Metadata.Metadata.GetRootAsMetadata(
                metadata.get_flatbuffers(), 0)
            self.assertIsNotNone(m)
            l = m.ReferencesLength()
            self.assertEqual(l, 7)
            lst = [ReferenceType.create(),
                   ReferenceType.read_in(),
                   ReferenceType.read_out(),
                   ReferenceType.read(),
                   ReferenceType.write_in(),
                   ReferenceType.write_out(),
                   ReferenceType.write()]
            for i in range(len(lst)):
                t = m.References(i)
                self.assertIsNotNone(t)
                print("meta:", str(t.Type(), 'utf-8'),
                      str(t.TargetAddress(), 'utf-8'))
                self.assertEqual(str(t.Type(), 'utf-8'), lst[i])
                self.assertEqual(str(t.TargetAddress(), 'utf-8'),
                                 "/this/is/a/type/path")

    def test_metadata_builder_extensions(self):
        """ Test MetadataBuilder test_metadata_builder_extensions"""

        builder = MetadataBuilder(
            description="description", description_url="description_url")
        self.assertIsNotNone(builder)
        lst = ["1key", "2key", "3key", "4key"]

        builder.add_extensions(lst[2], "value_" + lst[2])
        builder.add_extensions(lst[1], "value_" + lst[1])
        builder.add_extensions(lst[3], "value_" + lst[3])
        builder.add_extensions(lst[0], "value_" + lst[0])

        builder.set_unit(
            "m/s").set_node_class(NodeClass.NodeClass.Variable).set_operations(AllowedOperation.READ | AllowedOperation.WRITE | AllowedOperation.BROWSE | AllowedOperation.CREATE | AllowedOperation.DELETE)
        metadata = builder.build()
        with metadata:
            self.assertIsNotNone(metadata)
            m = Metadata.Metadata.GetRootAsMetadata(
                metadata.get_flatbuffers(), 0)
            self.assertIsNotNone(m)
            l = m.ExtensionsLength()
            self.assertEqual(l, 4)
            for i in range(len(lst)):
                e = m.Extensions(i)
                self.assertIsNotNone(e)
                self.assertEqual(str(e.Key(), 'utf-8'), lst[i])
                self.assertEqual(str(e.Value(), 'utf-8'),
                                 "value_" + lst[i])

    def test_metadata_builder_provider(self):
        """ Test MetadataBuilder test_metadata_builder_provider"""

        builder = MetadataBuilder(AllowedOperation.READ)
        builder.add_reference(ReferenceType.read(), "self.registertype")
        metadata = builder.build()
        with metadata:
            self.assertIsNotNone(metadata)
            m = Metadata.Metadata.GetRootAsMetadata(
                metadata.get_flatbuffers(), 0)
            self.assertIsNotNone(m)

    def test_metadata_builder_descriptions(self):
        """ Test MetadataBuilder test_metadata_builder_descriptions"""

        builder = MetadataBuilder(
            description="description", description_url="description_url")
        self.assertIsNotNone(builder)
        lst = ["1key", "2key", "3key", "4key"]

        builder.add_localization_description(lst[2], "value_" + lst[2])
        builder.add_localization_description(lst[1], "value_" + lst[1])
        builder.add_localization_description(lst[3], "value_" + lst[3])
        builder.add_localization_description(lst[0], "value_" + lst[0])

        builder.set_unit(
            "m/s").set_node_class(NodeClass.NodeClass.Variable).set_operations(AllowedOperation.READ | AllowedOperation.WRITE | AllowedOperation.BROWSE | AllowedOperation.CREATE | AllowedOperation.DELETE)
        metadata = builder.build()
        with metadata:
            self.assertIsNotNone(metadata)
            m = Metadata.Metadata.GetRootAsMetadata(
                metadata.get_flatbuffers(), 0)
            self.assertIsNotNone(m)
            l = m.DescriptionsLength()
            self.assertEqual(l, 4)
            for i in range(len(lst)):
                e = m.Descriptions(i)
                self.assertIsNotNone(e)
                self.assertEqual(str(e.Id(), 'utf-8'), lst[i])
                self.assertEqual(str(e.Text(), 'utf-8'),
                                 "value_" + lst[i])

    def test_metadata_builder_display_names(self):
        """ Test MetadataBuilder test_metadata_builder_display_names"""

        builder = MetadataBuilder(
            description="description", description_url="description_url")
        self.assertIsNotNone(builder)
        lst = ["1key", "2key", "3key", "4key"]

        builder.add_localization_display_name(lst[2], "value_" + lst[2])
        builder.add_localization_display_name(lst[1], "value_" + lst[1])
        builder.add_localization_display_name(lst[3], "value_" + lst[3])
        builder.add_localization_display_name(lst[0], "value_" + lst[0])

        builder.set_unit(
            "m/s").set_node_class(NodeClass.NodeClass.Variable).set_operations(AllowedOperation.READ | AllowedOperation.WRITE | AllowedOperation.BROWSE | AllowedOperation.CREATE | AllowedOperation.DELETE)
        metadata = builder.build()
        with metadata:
            self.assertIsNotNone(metadata)
            m = Metadata.Metadata.GetRootAsMetadata(
                metadata.get_flatbuffers(), 0)
            self.assertIsNotNone(m)
            l = m.DisplayNamesLength()
            self.assertEqual(l, 4)
            for i in range(len(lst)):
                e = m.DisplayNames(i)
                self.assertIsNotNone(e)
                self.assertEqual(str(e.Id(), 'utf-8'), lst[i])
                self.assertEqual(str(e.Text(), 'utf-8'),
                                 "value_" + lst[i])

if __name__ == '__main__':
    unittest.main()
