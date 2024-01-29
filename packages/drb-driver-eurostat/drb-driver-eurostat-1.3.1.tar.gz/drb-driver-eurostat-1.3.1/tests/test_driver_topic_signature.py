from drb.core.factory import FactoryLoader
from drb.topics.dao import ManagerDao

from drb.drivers.eurostat import DrbEurostatFactory
from drb.nodes.logical_node import DrbLogicalNode
import unittest
import uuid


class TestDriverTopicSignature(unittest.TestCase):
    def test_load_driver(self):
        factory = FactoryLoader().get_factory('eurostat')
        self.assertIsInstance(factory, DrbEurostatFactory)

    def test_load_topic(self):
        tid = uuid.UUID('f2d39b1e-253a-4c2c-901c-c8685f2de55c')
        t = ManagerDao().get_drb_topic(tid)
        self.assertEqual('eurostat', t.label)
        self.assertEqual('eurostat', t.factory)

    def test_topic_signature(self):
        tid = uuid.UUID('f2d39b1e-253a-4c2c-901c-c8685f2de55c')
        t = ManagerDao().get_drb_topic(tid)
        self.assertIsNotNone(t)

        node = DrbLogicalNode('eurostat://REG_AREA3')
        self.assertTrue(t.matches(node))

        node = DrbLogicalNode('eurostar://train1901')
        self.assertFalse(t.matches(node))
