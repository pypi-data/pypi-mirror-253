from typing import Dict
import unittest
import eurostat
import pandas.core.frame
from drb.core.path import ParsedPath
from drb.exceptions.core import DrbException
from drb.drivers.eurostat import (
    DrbEurostatFactory,
    DrbEurostatDataNode,
    DrbEurostatRowNode
)


class TestEurostatDataNode(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        code = 'reg_area3'
        factory = DrbEurostatFactory()
        cls.service_node = factory.create('eurostat://')
        cls.node = DrbEurostatDataNode(cls.service_node, 'foo', code)
        data = eurostat.get_data(code)
        cls.header = data[0]
        cls.data = data[1:]

    def test_name(self):
        self.assertEqual('foo', self.node.name)

    def test_namespace_uri(self):
        self.assertIsNone(self.node.namespace_uri)

    def test_item(self):
        with self.assertRaises(NotImplementedError):
            del self.node[0]
        with self.assertRaises(NotImplementedError):
            self.node[0] = self.node

    def test_path(self):
        path = ParsedPath('eurostat://reg_area3')
        self.assertEqual(path.scheme, self.node.path.scheme)
        self.assertEqual(path.netloc, self.node.path.netloc)
        self.assertEqual(path.name, self.node.path.name)

    def test_value(self):
        self.assertIsNone(self.node.value)

    def test_parent(self):
        self.assertEqual(self.service_node, self.node.parent)

    def test_children(self):

        children = self.node.children
        self.assertIsNotNone(children)
        self.assertIsInstance(children, list)
        self.assertEqual(len(self.data), len(children))

    def test_bracket_browse(self):

        child = DrbEurostatRowNode(self.node, self.header, self.data[0], 0)

        self.assertEqual(self.node[0], child)
        with self.assertRaises(KeyError):
            self.node['foo']

        sub_children = self.node[:3]
        self.assertIsInstance(sub_children, list)
        self.assertEqual(3, len(sub_children))
        with self.assertRaises(TypeError):
            self.node[{'toto': 2}]

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
        self.assertTrue(self.node.has_impl(pandas.core.frame.DataFrame))
        self.assertFalse(self.node.has_impl(int))

    def test_get_impl(self):
        self.assertIsInstance(
            self.node.get_impl(pandas.core.frame.DataFrame),
            pandas.core.frame.DataFrame
        )
        with self.assertRaises(DrbException):
            self.node.get_impl(int)
