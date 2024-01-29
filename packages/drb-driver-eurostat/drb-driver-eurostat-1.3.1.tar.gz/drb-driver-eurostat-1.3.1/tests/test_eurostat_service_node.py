from typing import Dict
import unittest
import eurostat
from drb.exceptions.core import DrbException
from drb.core.path import ParsedPath
from drb.drivers.eurostat import DrbEurostatFactory, DrbEurostatDataNode


class TestEurostatServiceNode(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        factory = DrbEurostatFactory()
        cls.node = factory.create('eurostat://')
        cls.eurostat_list = [r for r in eurostat.get_toc() if r[2] in [
            'dataset', 'table']]

    def test_item(self):
        with self.assertRaises(NotImplementedError):
            del self.node[0]
        with self.assertRaises(NotImplementedError):
            self.node[0] = self.node

    def test_name(self):
        self.assertEqual('Eurostat service', self.node.name)

    def test_namespace_uri(self):
        self.assertIsNone(self.node.namespace_uri)

    def test_path(self):
        path = ParsedPath('eurostat://')
        self.assertEqual(path.scheme, self.node.path.scheme)
        self.assertEqual(path.netloc, self.node.path.netloc)
        self.assertEqual(path.name, self.node.path.name)

    def test_value(self):
        self.assertIsNone(self.node.value)

    def test_parent(self):
        self.assertIsNone(self.node.parent)

    def test_children(self):

        children = self.node.children
        self.assertIsNotNone(children)
        self.assertIsInstance(children, list)
        self.assertEqual(len(self.eurostat_list), len(children))

    def test_bracket_browse(self):

        title = self.eurostat_list[0][0]
        code = self.eurostat_list[0][1]
        child = DrbEurostatDataNode(self.node, title, code)

        self.assertEqual(self.node[0], child)
        self.assertEqual(self.node[code], child)

        sub_children = self.node[:3]
        self.assertIsInstance(sub_children, list)
        self.assertEqual(3, len(sub_children))

    def test_attributes(self):
        table_list = [(row[0], row[1]) for row in self.eurostat_list]
        mock_attributes = {('tables', None): table_list}

        attributes = self.node.attributes
        self.assertIsNotNone(attributes)
        self.assertIsInstance(attributes, Dict)
        self.assertEqual(1, len(attributes.keys()))
        self.assertEqual(mock_attributes, attributes)

        with self.assertRaises(DrbException):
            self.node.get_attribute('tables', 'foo')
            self.node.get_attribute('foo')

        self.assertEqual(table_list, self.node.get_attribute('tables'))

    def test_has_impl(self):
        self.assertFalse(self.node.has_impl(int))

    def test_get_impl(self):
        with self.assertRaises(DrbException):
            self.node.get_impl(int)
