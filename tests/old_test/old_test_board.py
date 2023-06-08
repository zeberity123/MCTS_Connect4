from cgi import test
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from unittest import TestCase, main
from connect_four import board

game_board = board.Board()

class BoardTests(TestCase):

    def test0_board_row(self):
        self.assertEqual(game_board.row, 6)

    def test1_board_column(self):
        self.assertEqual(game_board.col, 7)

    # def test_board_print(self):
    #     game_board.print_board()

    def test2_add_stone(self):
        print('\n')
        game_board.add_stone(0,0,'O')
        self.assertEqual(game_board.board[0][0], 'O')
        # game_board.print_board()

    def test3_get_free_row_index(self):
        print('\n')
        print(game_board.get_free_row_index(0))
        game_board.print_board()
        game_board.add_stone(1,0, 'X')
        print(game_board.get_free_row_index(0))
        game_board.print_board()

    def test4_put_stone(self):
        print('\n')
        game_board.print_board()
        column_idx = 0
        print('put stone at col_1')
        game_board.put_stone(column_idx, 'X')
        game_board.print_board()

    def test5_check_status1(self):
        print('\n')
        game_board = board.Board()
        for i in range(4):
            game_board.board[0][i] = 'O'
        game_board.print_board()
        isWin = game_board.check_status('O')
        self.assertEqual(isWin, True)

    def test6_check_status(self):
        print('\n')
        game_board = board.Board()
        for i in range(4):
            game_board.board[i][0] = 'O'
        game_board.print_board()
        isWin = game_board.check_status('O')
        self.assertEqual(isWin, True)
    
    def test7_check_status(self):
        print('\n')
        game_board = board.Board()
        for i in range(4):
            game_board.board[i][i] = 'X'
        game_board.print_board()
        isWin = game_board.check_status('X')
        self.assertEqual(isWin, True)

    def test8_check_status(self):
        print('\n')
        game_board = board.Board()
        for i in range(4):
            game_board.board[i][3 - i] = 'X'
        game_board.print_board()
        isWin = game_board.check_status('X')
        self.assertEqual(isWin, True)
    
    def test8_check_status(self):
        print('\n')
        game_board = board.Board()
        for i in range(4):
            game_board.board[i][3 - i] = 'X'
        game_board.print_board()
        isWin = game_board.check_status('X')
        self.assertEqual(isWin, True)
    
    def test9_check_full(self):
        print('\n')
        game_board = board.Board()
        for i in range(game_board.col):
            for j in range(game_board.row):
                game_board.put_stone(i, 'O')
        game_board.print_board()
        print(f'count: {game_board.count}')
        isFull = game_board.is_board_full()
        self.assertEqual(isFull, True)
    
    def test10_check_max_row_index(self):
        print('\n')
        game_board = board.Board()
        for i in range(6):
            game_board.board[i][0] = 'O'
        game_board.print_board()
        self.assertEqual(game_board.get_free_row_index(0), -1)

    def test11_check_free_columns(self):
        print('\n')
        game_board = board.Board()
        for i in range(6):
            game_board.board[i][0] = 'O'
        game_board.print_board()
        self.assertEqual(game_board.get_free_columns(), [1,2,3,4,5,6])



if __name__ == '__main__':
    main()