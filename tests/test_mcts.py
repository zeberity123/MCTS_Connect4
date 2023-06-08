from cgi import test
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from unittest import TestCase, main
from connect_four.mcts import *
from connect_four.mcts import *
import numpy as np
import random

class MctsTests(TestCase):

    def test0_random_move_empty_board(self):
        game_board = create_board()
        # print_board(game_board)
        winner = random_move(game_board)
        
        if winner == 1:
            print(f'winner: O')
        elif winner == -1:
            print(f'winner: X')
        else:
            print(f'Tie')
        

    def test1_random_move_full_board(self):
        game_board = create_board()
        game_board = [
            [1, 1, -1, -1, 1, -1, -1],
            [-1, -1, 1, 1, -1, 1, 1],
            [1, 1, -1, -1, 1, -1, -1],
            [-1, -1, 1, 1, -1, 1, 1],
            [1, 1, -1, -1, 1, -1, -1],
            [-1, -1, 1, 1, 0, 1, 1]
        ]
        winner = random_move(game_board)
        self.assertEqual(winner, 0)

    def test2_mcts_root_none(self):
        init = None
        root = mcts(init)
        print_board(root.board)
        print(root)

    def test3_selection(self):
        # Test case when there is no winning child
        node_1 = Node(board=None, won=None, col=None, parent=None)
        child_1 = Node(board=None, won=0, col=2, parent=node_1)
        child_2 = Node(board=None, won=0, col=3, parent=node_1)
        node_1.visits = 10
        child_1.wins = 5
        child_1.visits = 10
        child_2.wins = 8
        child_2.visits = 10
        node_1.add_child([child_1, child_2])
        print(f'child_1 ucb: {child_1.calc_ucb(1)}')
        print(f'child_2 ucb: {child_2.calc_ucb(1)}')
        print(f'child1: {child_1}')
        print(f'child2: {child_2}')
        better_winrate = selection(node_1, 1)
        print(f'better: {better_winrate}')
        self.assertEqual(better_winrate, child_2)

    def test4_expansion(self):
        board = create_board()
        root = Node(board, 0, None, None)
        node = root
        free_columns = get_free_columns(node.board)
        expansion(node, free_columns)
        print(root.children)
        self.assertEqual(len(root.children), 7)

    def test5_backpropagation(self):
        board = create_board()
        root = Node(board, 0, None, None)
        node_1 = Node(board, won=0, col=1, parent=root)
        child_1 = Node(board, won=0, col=2, parent=node_1)
        root.visits = 0
        root.wins = 0
        node_1.visits = 1
        node_1.wins = 1
        child_1.visits = 2
        child_1.wins = 2
        
        backpropagation(child_1, -1)

        self.assertEqual(root.visits, 1)
        self.assertEqual(root.wins, 1)
        self.assertEqual(node_1.visits, 2)
        self.assertEqual(node_1.wins, 2)



if __name__ == '__main__':
    main()