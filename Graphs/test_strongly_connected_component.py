import sys
import os
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from strongly_connected_component import tr, scc


class TestTranspose(unittest.TestCase):

    def test_empty_graph(self):
        self.assertEqual(tr({}), {})

    def test_single_node_no_edges(self):
        self.assertEqual(tr({0: set()}), {0: set()})

    def test_single_edge_reversed(self):
        GT = tr({0: {1}, 1: set()})
        self.assertEqual(GT[0], set())
        self.assertEqual(GT[1], {0})

    def test_simple_cycle_stays_cycle(self):
        GT = tr({0: {1}, 1: {2}, 2: {0}})
        self.assertEqual(GT[0], {2})
        self.assertEqual(GT[1], {0})
        self.assertEqual(GT[2], {1})

    def test_fan_out_becomes_fan_in(self):
        GT = tr({0: {1, 2}, 1: set(), 2: set()})
        self.assertEqual(GT[0], set())
        self.assertEqual(GT[1], {0})
        self.assertEqual(GT[2], {0})

    def test_transpose_of_transpose_is_original(self):
        G = {0: {1}, 1: {2}, 2: {0, 3}, 3: set()}
        self.assertEqual(tr(tr(G)), G)


class TestSCC(unittest.TestCase):

    def _as_frozensets(self, sccs):
        return set(frozenset(s) for s in sccs)

    def test_single_node(self):
        result = self._as_frozensets(scc({0: set()}))
        self.assertEqual(result, {frozenset({0})})

    def test_single_cycle_one_scc(self):
        G = {0: {1}, 1: {2}, 2: {0}}
        result = self._as_frozensets(scc(G))
        self.assertEqual(result, {frozenset({0, 1, 2})})

    def test_no_edges_each_node_is_own_scc(self):
        G = {0: set(), 1: set(), 2: set()}
        result = self._as_frozensets(scc(G))
        self.assertEqual(result, {frozenset({0}), frozenset({1}), frozenset({2})})

    def test_linear_graph_each_node_is_own_scc(self):
        G = {0: {1}, 1: {2}, 2: set()}
        result = self._as_frozensets(scc(G))
        self.assertEqual(result, {frozenset({0}), frozenset({1}), frozenset({2})})

    def test_two_separate_cycles(self):
        G = {0: {1}, 1: {0}, 2: {3}, 3: {2}}
        result = self._as_frozensets(scc(G))
        self.assertEqual(result, {frozenset({0, 1}), frozenset({2, 3})})

    def test_complex_graph(self):
        # SCCs: {0,1,2}, {3,4}, {5}
        G = {
            0: {1},
            1: {2},
            2: {0},
            3: {1, 4},
            4: {3, 5},
            5: set()
        }
        result = self._as_frozensets(scc(G))
        self.assertEqual(result, {frozenset({0, 1, 2}), frozenset({3, 4}), frozenset({5})})

    def test_count_of_sccs(self):
        # A graph with 4 SCCs
        G = {0: {1}, 1: {0}, 2: {3}, 3: {2}, 4: {5}, 5: set()}
        result = scc(G)
        self.assertEqual(len(result), 4)

    def test_complete_graph_one_scc(self):
        G = {0: {1, 2}, 1: {0, 2}, 2: {0, 1}}
        result = self._as_frozensets(scc(G))
        self.assertEqual(result, {frozenset({0, 1, 2})})


if __name__ == '__main__':
    unittest.main()
