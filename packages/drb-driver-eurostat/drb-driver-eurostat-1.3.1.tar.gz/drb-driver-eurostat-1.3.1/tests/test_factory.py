import unittest
from drb.drivers.eurostat import (
    DrbEurostatFactory,
    DrbEurostatServiceNode,
    DrbEurostatDataNode
)
from drb.exceptions.core import DrbFactoryException


class TestEurostatFactory(unittest.TestCase):

    def test_create(self):
        factory = DrbEurostatFactory()

        node = factory.create('eurostat://')
        self.assertIsInstance(node, DrbEurostatServiceNode)

        node = factory.create('eurostat://reg_area3')
        self.assertIsInstance(node, DrbEurostatDataNode)

        with self.assertRaises(DrbFactoryException):
            node = factory.create('eurostat')

        with self.assertRaises(DrbFactoryException):
            node = factory.create('eurostat://toto')
