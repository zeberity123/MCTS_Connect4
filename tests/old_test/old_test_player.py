from cgi import test
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from unittest import TestCase, main
from connect_four import board
from connect_four import old_player

game_board = board.Board()

game_player = old_player.Player()

class PlayerTests(TestCase):

    def test_player_turn(self):
        self.assertEqual(game_player.turn, 1)

    def test_change_player(self):
        game_player = old_player.Player()
        game_player.change_turn()
        self.assertEqual(game_player.turn, -1)

if __name__ == '__main__':
    main()