from connect_four.mcts import *
from connect_four.board import *
from connect_four import gui
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import time

class Game:
    """Run the connect 4 game in 3 ways.

    There are 3 versions of connect 4:
    1. Play by 2 human players, 2. Play against AI, 3. AI against AI
    """    
    def __init__(self):
        """Init by creating a board and a turn variable.
        """        
        self.game_board = create_board()
        self.turn = 0

    def play_text(self):
        """Run the text-based Connect 4 on command line.

        Play by 2 human players
        """        
        print_board(self.game_board)
        while self.turn < 42:
            print(f"Player: '{get_player_marker(self.game_board)}'")
            print(f'Please Enter Input Column: ', end='')

            while True:
                try:
                    input_col = int(input())
                    if input_col >= 0 and input_col <= 6:
                        if get_free_row(self.game_board, input_col) == -1:
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
                    
            self.game_board, winner = add_stone(self.game_board, input_col)
            print_board(self.game_board)
            self.turn += 1

            if winner != 0:
                if winner == 2:
                    print('\nTie!')
                elif winner == 1:
                    print(f"Player 'O' Won!")
                else: 
                    print(f"Player 'X' Won!")
                break
            
    
    def play_gui(self):
        """Run the GUI version of Connect 4 powered by Pygame.
        Play by 2 human players.
        """        
        self.gui = gui.Gui()
        self.gui.runGame()

    def play_gui_mcts(self, first_player):
        """Run the GUI version of Connect 4 powered by Pygame.
        Play against AI.

        Args:
            first_player (int): 1 if the human player play first, -1 if AI play first 
        """        
        self.gui = gui.Gui()
        self.gui.run_mcts(first_player)

    def play_mcts(self, first_player, n_of_iterations, c, n_of_simulations=4):
        """Run the Text version of Connect 4 for playing against AI

        Args:
            first_player (int): 1 if the human player play first, -1 if AI play first
            n_of_iterations (int): number of iterations
            c (float): exploration constant(c_value)
            n_of_simulations (int, optional): number of simulations. Defaults to 3.
        """        
        root = None
        for _ in range(n_of_iterations):
            root = mcts(root, c)

        # play_count without termination of code
        play_count = 0

        while play_count<1:
            board = create_board()
            self.turn = 0
            if first_player: self.turn += 1
            node = root
            print_board(board)
            while True:
                # Human's turn
                if (self.turn % 2) == 0:
                    print('Please Enter Integer 0~6: ', end='')
                    while True:
                        try:
                            input_col = int(input())
                            if input_col >= 0 and input_col <= 6:
                                if get_free_row(board, input_col) == -1:
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

                    column = input_col

                    new_node = node
                    for _ in range(1):
                        new_node = mcts(node, c).get_node(input_col)
                    node = new_node

                # AI's turn
                else:
                    start = time.time()
                    for _ in range(n_of_iterations):
                        node = mcts(node, c, n_of_simulations)
                    node, column = node.choose_node()
                    end = time.time()
                    print(f'Time used: {end - start:.3f} seconds')
                board, winner = add_stone(board, column)

                print_board(board)

                if winner != 0:
                    if winner == 2:
                        print('Tie')
                    elif winner == 1:
                        print(f"Player 'O' Won!")
                    else: 
                        print(f"Player 'X' Won!")
                    break

                self.turn += 1
            play_count += 1
        print(f'C Value used: {c}')
        if first_player: self.turn += 1
        print(f'Turn used for games: {self.turn + 1}')

    def auto_mcts(self, n_of_games, n_of_iterations, c1, c2, n_of_simulations1=1, n_of_simulations2=1):
        """Run the Text version of Connect 4 for AI against AI
        Play by 2 AI against each other automatically.

        Args:
            n_of_games (int): number of games to be played
            n_of_iterations (int): number of iterations
            c1 (int): exploration constant(c_value) for player 1
            c2 (int): exploration constant(c_value) for player 2
            n_of_simulations1 (int, optional): number of simulations for player 1. Defaults to 1.
            n_of_simulations2 (int, optional): number of simulations for player 2. Defaults to 1.

        Returns:
            winner_cnt (list): list of number of wins for each player
            p1_time_taken (list): list of time taken for each move by player 1
            p2_time_taken (list): list of time taken for each move by player 2
        """        
        play_count = 0
        winner_cnt = [0,0,0] # player1, player2, Tie
        turn_used = []
        p1_time_taken = []
        p2_time_taken = []
        while play_count<n_of_games:
            root = None

            for _ in range(n_of_iterations):
                root = mcts(root, c1)
            # test AI with real play
            board = create_board()
            self.turn = 0
            node = root
            print_board(board)
            while True:
                # AI 'O' Turn
                if (self.turn % 2) == 0:
                    p1_start = time.time()
                    for _ in range(n_of_iterations):
                        node = mcts(node, c1, n_of_simulations1)

                    if node.children != None:
                        print([(child.wins, child.visits) for child in node.children])

                    node, column = node.choose_node()
                    p1_end = time.time()
                    p1_time_taken.append((p1_end - p1_start))

                # AI 'X' Turn  
                else:
                    p2_start = time.time()
                    for _ in range(n_of_iterations):
                        node = mcts(node, c2, n_of_simulations2)

                    if node.children != None:
                        print([(child.wins, child.visits) for child in node.children])

                    node, column = node.choose_node()
                    p2_end = time.time()
                    p2_time_taken.append((p2_end - p2_start))

                board, winner = add_stone(board, column)

                print_board(board)

                if winner != 0:
                    if winner == 2:
                        winner_cnt[2] += 1
                    elif winner == 1:
                        winner_cnt[0] += 1
                    else: 
                        winner_cnt[1] += 1
                    break
                self.turn += 1
            play_count += 1

        return winner_cnt, p1_time_taken, p2_time_taken