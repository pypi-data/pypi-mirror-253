import unittest

import pandas as pd
import numpy as np

from bartpy2.data import Data

from bartpy2.mutation import GrowMutation, PruneMutation
from bartpy2.node import DecisionNode, LeafNode
from bartpy2.split import Split

class TestNode(unittest.TestCase):

    def setUp(self):
        self.data = Data(pd.DataFrame({"a": [1]}).values, np.array([1]))

    def test_pruning_leaf(self):
        with self.assertRaises(TypeError):
            PruneMutation(LeafNode(Split(self.data)), LeafNode(Split(self.data)))

    def test_growing_decision_node(self):
        a = LeafNode(Split(self.data))
        b = LeafNode(Split(self.data))
        c = LeafNode(Split(self.data))
        d = DecisionNode(Split(self.data), a, b)
        e = DecisionNode(Split(self.data), c, d)

        with self.assertRaises(TypeError):
            GrowMutation(d, a)

    def test_pruning_non_leaf_parent(self):
        a = LeafNode(Split(self.data))
        b = LeafNode(Split(self.data))
        c = LeafNode(Split(self.data))
        d = DecisionNode(Split(self.data), a, b)
        e = DecisionNode(Split(self.data), c, d)

        with self.assertRaises(TypeError):
            PruneMutation(e, a)
