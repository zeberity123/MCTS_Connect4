from cgi import test
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from unittest import TestCase, main
from connect_four.board import *

class BoardTests(TestCase):

    def test_board_print_player(self):
        game_board = create_board()
        self.assertEqual(next_player(game_board), 1)
        game_board[0][0] = 1
        self.assertEqual(next_player(game_board), -1)
        game_board[0][1] = -1
        # print_board(game_board)
        self.assertEqual(next_player(game_board), 1)

    def test0_board_row(self):
        game_board = create_board()
        self.assertEqual(game_board.shape[0], 6)

    def test1_board_column(self):
        game_board = create_board()
        self.assertEqual(game_board.shape[1], 7)

    def test2_get_free_row(self):
        game_board = create_board()
        self.assertEqual(get_free_row(game_board, 0), 0)
        game_board[0][0] = 1
        game_board[1][0] = -1
        self.assertEqual(get_free_row(game_board, 0), 2)

    def test3_get_free_columns(self):
        game_board = create_board()
        for i in range (5):
            for j in range(7):
                game_board[i][j] = 1
        # print_board(game_board)
        # w = get_free_columns(game_board)
        # print(w)
        self.assertEqual(get_free_columns(game_board), [0,1,2,3,4,5,6])
        game_board[5][0] = -1
        game_board[5][1] = -1
        self.assertEqual(get_free_columns(game_board), [2,3,4,5,6])

    def test4_add_stone(self):
        game_board = create_board()
        column_idx = 0
        print_board(game_board)
        print('add stone at col_1')
        game_board, winner = add_stone(game_board,column_idx)
        self.assertEqual(game_board[0][0], 1)

    def test5_check_status1(self):
        print('\n')
        game_board = create_board()
        for i in range(4):
            game_board[0][i] = 1
        print_board(game_board)
        isWin = check_status(game_board,1)
        self.assertEqual(isWin, True)

    def test6_check_status(self):
        print('\n')
        game_board = create_board()
        for i in range(4):
            game_board[i][0] = 1
        print_board(game_board)
        isWin = check_status(game_board, 1)
        self.assertEqual(isWin, True)
    
    def test7_check_status(self):
        print('\n')
        game_board = create_board()
        for i in range(4):
            game_board[i][i] = -1
        print_board(game_board)
        isWin = check_status(game_board, -1)
        self.assertEqual(isWin, True)

    def test8_check_status(self):
        print('\n')
        game_board = create_board()
        for i in range(4):
            game_board[i][3 - i] = -1
        print_board(game_board)
        isWin = check_status(game_board, -1)
        self.assertEqual(isWin, True)
    
    def test8_check_status(self):
        print('\n')
        game_board = create_board()
        for i in range(4):
            game_board[i][3 - i] = -1
        print_board(game_board)
        isWin = check_status(game_board, -1)
        self.assertEqual(isWin, True)
    
    def test9_check_full(self):
        print('\n')
        game_board = create_board()
        for i in range(7):
            for j in range(6):
                game_board[j][i] = 1
        print_board(game_board)
        isFull = is_board_full(game_board)
        self.assertEqual(isFull, True)



if __name__ == '__main__':
    main()