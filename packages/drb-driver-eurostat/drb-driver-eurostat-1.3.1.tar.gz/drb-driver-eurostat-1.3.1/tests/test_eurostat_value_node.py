from typing import Dict
import unittest
import eurostat
from drb.exceptions.core import DrbException
from drb.core.path import ParsedPath
from drb.drivers.eurostat import (
    DrbEurostatFactory,
    DrbEurostatDataNode,
    DrbEurostatRowNode,
    DrbEurostatValueNode
)


class TestEurostatRowNode(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        factory = DrbEurostatFactory()
        cls.service_node = factory.create('eurostat://')
        code = 'reg_area3'
        data = eurostat.get_data(code)
        cls.header = data[0]
        cls.data = data[1]
        cls.data_node = DrbEurostatDataNode(cls.service_node, 'foo', code)
        cls.row_node = DrbEurostatRowNode(
            cls.data_node, cls.header, cls.data, 0)
        cls.node = DrbEurostatValueNode(cls.row_node, 'landuse', 'L0008')

    def test_item(self):
        with self.assertRaises(NotImplementedError):
            del self.node[0]
        with self.assertRaises(NotImplementedError):
            self.node[0] = self.node

    def test_name(self):
        self.assertEqual('landuse', self.node.name)

    def test_namespace_uri(self):
        self.assertIsNone(self.node.namespace_uri)

    def test_path(self):
        path = ParsedPath('eurostat://reg_area3/0/landuse')
        self.assertEqual(path.scheme, self.node.path.scheme)
        self.assertEqual(path.netloc, self.node.path.netloc)
        self.assertEqual(path.name, self.node.path.name)

    def test_value(self):
        self.assertEqual('L0008', self.node.value)

    def test_parent(self):
        self.assertEqual(self.row_node, self.node.parent)

    def test_children(self):

        children = self.node.children
        self.assertIsNotNone(children)
        self.assertIsInstance(children, list)
        self.assertEqual(0, len(children))

    def test_attributes(self):

        attributes = self.node.attributes
        self.assertIsNotNone(attributes)
        self.assertIsInstance(attributes, Dict)
        self.assertEqual(0, len(attributes.keys()))

        with self.assertRaises(DrbException):
            self.node.get_attribute('columns', 'foo')
            self.node.get_attribute('foo')

    def test_has_impl(self):
        self.assertFalse(self.node.has_impl(int))

    def test_get_impl(self):
        with self.assertRaises(DrbException):
            self.node.get_impl(int)
