from cgi import test
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from unittest import TestCase, main
from connect_four.board import *
from connect_four.node import *

class NodeTests(TestCase):
    def test_calc_ucb(self):
        node = Node(board=None, won=None, col=None, parent=None)
        node.wins = 5
        node.visits = 10
        node.parent = Node(board=None, won=None, col=None, parent=None)
        node.parent.visits = 20
        
        # Test calculation of UCB when c is None
        ucb = node.calc_ucb()
        self.assertAlmostEqual(1.274, ucb, places=3)
    
    def test_add_child(self):
        node = Node(board=None, won=None, col=None, parent=None)
        child = Node(board=None, won=None, col=None, parent=None)
        node.add_child(child)
        self.assertEqual(node.children, child)
        
    def test_choose_node(self):
        node_1 = Node(board=None, won=None, col=None, parent=None)
        
        # Test case when children is None
        best_node, node_col = node_1.choose_node()
        self.assertEqual(best_node, None)
        self.assertEqual(node_col, None)
        
        # Test case when there is a winning child
        node_2 = Node(board=None, won=1, col=1, parent=node_1)
        node_1.add_child([node_2])
        # print(f'children: {node_1.children}')
        # win_nodes = [child for child in node_1.children]
        # print(win_nodes)
        best_node, node_col = node_1.choose_node()
        self.assertEqual(best_node, node_2)
        self.assertEqual(node_col, 1)
        
        # Test case when there is no winning child
        child_1 = Node(board=None, won=0, col=2, parent=node_1)
        child_2 = Node(board=None, won=0, col=3, parent=node_1)
        child_1.wins = 5
        child_1.visits = 10
        child_2.wins = 8
        child_2.visits = 10

        node_1.add_child([child_1, child_2])
        print(f'children: {node_1.children}')
        best_node, node_col = node_1.choose_node()
        self.assertEqual(best_node, child_2)
        self.assertEqual(node_col, 3)
    
    def test_get_node(self):
        node = Node(board=None, won=None, col=0, parent=None)
        child_1 = Node(board=None, won=None, col=1, parent=node)
        child_2 = Node(board=None, won=None, col=2, parent=node)

        # Test case when child does not exist
        none_node = node.get_node(1)
        self.assertEqual(none_node, None)
        
        # Test case when child exists
        node.add_child([child_1, child_2])
        node_col_1 = node.get_node(1)
        self.assertEqual(node_col_1, child_1)
        node_col_2 = node.get_node(2)
        self.assertEqual(node_col_2, child_2)
        

if __name__ == '__main__':
    main()