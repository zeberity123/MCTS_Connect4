from cgi import test
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from unittest import TestCase, main
from connect_four import board
from connect_four.mcts import random_move, better_move

game_board = board.Board()

class MctsTests(TestCase):

    def test0_random_move_empty_board(self):
        self.assertNotEqual(random_move(game_board.board), -1)

    def test1_random_move_full_board(self):
        game_board.board = [['O' for i in range(game_board.col)] \
            for j in range(game_board.row)]
        self.assertEqual(random_move(game_board.board), -1)
    
    def test2_random_move_1_empty_board(self):
        game_board.board = [['O' for i in range(game_board.col)] \
            for j in range(game_board.row)]
        game_board.board[5][6] = '_'
        self.assertEqual(random_move(game_board.board), 6)

    def test3_better_move_empty_board(self):
        game_board.board = [['_' for i in range(game_board.col)] \
            for j in range(game_board.row)]
        # game_board.print_board()
        self.assertNotEqual(better_move(game_board.board), -1)

    def test4_better_move_winning_board(self):
        for i in range(3):
            game_board.board[0][i] = 'X'
        # game_board.print_board()
        self.assertEqual(better_move(game_board.board), 3)
    
    def test5_better_move_losing_board(self):
        for i in range(3):
            game_board.board[0][i] = 'O'
        game_board.print_board()
        self.assertEqual(better_move(game_board.board), 3)



if __name__ == '__main__':
    main()