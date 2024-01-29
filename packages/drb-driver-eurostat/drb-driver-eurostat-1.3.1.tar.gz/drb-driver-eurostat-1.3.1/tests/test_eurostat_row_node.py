from typing import Dict
import unittest
import eurostat
from drb.core.path import ParsedPath
from drb.exceptions.core import DrbException
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
        cls.node = DrbEurostatRowNode(cls.data_node, cls.header, cls.data, 0)

    def test_item(self):
        with self.assertRaises(NotImplementedError):
            del self.node[0]
        with self.assertRaises(NotImplementedError):
            self.node[0] = self.node

    def test_name(self):
        self.assertEqual('foo0', self.node.name)

    def test_namespace_uri(self):
        self.assertIsNone(self.node.namespace_uri)

    def test_path(self):
        path = ParsedPath('eurostat://reg_area3/0')
        self.assertEqual(path.scheme, self.node.path.scheme)
        self.assertEqual(path.netloc, self.node.path.netloc)
        self.assertEqual(path.name, self.node.path.name)

    def test_value(self):
        self.assertIsNone(self.node.value)

    def test_parent(self):
        self.assertEqual(self.data_node, self.node.parent)

    def test_children(self):

        children = self.node.children
        self.assertIsNotNone(children)
        self.assertIsInstance(children, list)
        self.assertEqual(len(self.data), len(children))

    def test_bracket_browse(self):

        child = DrbEurostatValueNode(self.node, self.header[1], self.data[1])

        self.assertEqual(self.node[1], child)
        self.assertEqual(self.node[self.header[1]], child)

        sub_children = self.node[:2]
        self.assertIsInstance(sub_children, list)
        self.assertEqual(2, len(sub_children))

    def test_attributes(self):
        mock_attributes = {('columns', None): self.header}

        attributes = self.node.attributes
        self.assertIsNotNone(attributes)
        self.assertIsInstance(attributes, Dict)
        self.assertEqual(1, len(attributes.keys()))
        self.assertEqual(mock_attributes, attributes)

        with self.assertRaises(DrbException):
            self.node.get_attribute('columns', 'foo')
            self.node.get_attribute('foo')

        self.assertEqual(self.header, self.node.get_attribute('columns'))

    def test_has_impl(self):
        self.assertFalse(self.node.has_impl(int))

    def test_get_impl(self):
        with self.assertRaises(DrbException):
            self.node.get_impl(int)
