from connect_four import board, old_gui, old_player,mcts,node
from connect_four.mcts import random_move, better_move
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

class Game:
    """Runs the connect 4 game in 3 ways.
    There are 3 ways to run the connect 4; 
    1. Play text-based version, 2. Play GUI version, 3. Play against AI

    Currently, it is only available for 2 human players to play.
    Playing against AI is not fully implemented yet.
    """    
    def __init__(self):
        """Inits by creating a board and a player.
        """        
        self.game_board = board.Board()
        self.game_player = old_player.Player()

    def play_text(self):
        """Runs the text-based Connect 4 on command line.
        """        
        while self.game_board.count < 42:
            self.game_board.print_board()
            print(f"Player: '{self.game_player.stone}'")
            print(f'Please Enter Input Column: ', end='')

            while True:
                try:
                    input_col = int(input())
                    if input_col >= 0 and input_col <= 6:
                        if self.game_board.get_free_row_index(input_col) == -1:
                            print(f"Column '{input_col}' is full.Please select another column")
                            print('Please Enter Integer 0~6: ', end='')
                        else:
                            break
                    else:
                        print('Please Enter Integer 0~6: ', end='')
                
                except KeyboardInterrupt:
                    sys.exit()

                except:
                    print('Please Enter Integer 0~6: ', end='')
                    
            input_row = self.game_board.get_free_row_index(input_col)
            self.game_board.add_stone(input_row, input_col, self.game_player.stone)
            if self.game_board.check_status(self.game_player.stone):
                self.game_board.print_board()
                print(f"Player '{self.game_player.stone}' Won!")
                break
            elif self.game_board.count == 42:
                print(f"Draw!")
                break
            
            self.game_player.change_turn()
    
    def play_gui(self):
        """Runs the GUI version Connect 4 powered by Pygame.
        """        
        self.gui = old_gui.Gui()
        self.gui.runGame()

    def play_mcts(self):
        """Play against AI using MCTS.
        *This is not fully implemented yet.
        """        
        while self.game_board.count < 42:
            self.game_board.print_board()
            # player's turn
            if self.game_player.stone == 'O':
                print(f"Player: '{self.game_player.stone}'")
                print(f'Please Enter Input Column: ', end='')
                while True:
                    try:
                        input_col = int(input())
                        if input_col >= 0 and input_col <= 6:
                            if self.game_board.get_free_row_index(input_col) == -1:
                                print(f"Column '{input_col}' is full.Please select another column")
                                print('Please Enter Integer 0~6: ', end='')
                            else:
                                break
                        else:
                            print('Please Enter Integer 0~6: ', end='')
                    
                    except KeyboardInterrupt:
                        sys.exit()

                    except:
                        print('Please Enter Integer 0~6: ', end='')
                        
                input_row = self.game_board.get_free_row_index(input_col)
                self.game_board.add_stone(input_row, input_col, self.game_player.stone)

            # ai's turn
            elif self.game_player.stone == 'X':
                input_board = self.game_board.board.copy()

                # random_node_col = random_move(input_board)
                better_node_col = better_move(input_board)
                
                # input_row = self.game_board.get_free_row_index(random_node_col)
                input_row = self.game_board.get_free_row_index(better_node_col)

                if input_row != -1: 
                    # self.game_board.add_stone(input_row, random_node_col, self.game_player.stone)
                    self.game_board.add_stone(input_row, better_node_col, self.game_player.stone)

            if self.game_board.check_status(self.game_player.stone):
                self.game_board.print_board()
                print(f"Player '{self.game_player.stone}' Won!")
                break
            elif self.game_board.count == 42:
                print(f"Draw!")
                break
             
            self.game_player.change_turn()