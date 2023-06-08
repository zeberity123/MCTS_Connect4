import pygame
from connect_four.mcts import *
from connect_four.board import *
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import numpy as np
import random

class Gui:
    """Run GUI version of Connect 4.
    Uses Pygame to draw Graphics on pop up screen.
    """    
    pygame.init()

    def __init__(self):
        """Init by creating a board set up attributes.
        """        
        self.game_board = create_board()
        self.player = 1
        self.turn = 0
        self.ROW = 6
        self.COLUMN = 7
        print("gui created")

    def drawScreen(self, x_pos, winner, player, using_AI=False, wrong_input=False):
        """Draw connect 4 game play by graphics on the screen.

        Args:
            x_pos (int): current horizontal position of mouse
            winner (int): an integer indicates who's winner
            player (int): current player
            using_AI (bool, optional): True if it is played by an AI. Defaults to False.
            wrong_input (bool, optional): True if the column at x_pos is full. Defaults to False.
        """        
        BLUE = (0, 0, 255)
        BLACK = (0, 0, 0)
        RED = (255, 0, 0)
        YELLOW = (255, 255, 0)
        ORANGE = (255, 204, 0)
        WHITE = (255, 255, 255)

        end_font = pygame.font.SysFont('calibri', 80)
        play_gain = pygame.font.SysFont('calibri', 50)
        input_error_font = pygame.font.SysFont('calibri', 50)
        thinking_font = pygame.font.SysFont('calibri', 50)
        start_font = pygame.font.SysFont('calibri', 50)

        SCREEN_WIDTH = 700
        SCREEN_HEIGHT = 700
        CELL_SIZE = 100

        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        screen.fill(BLACK)

        pygame.draw.rect(screen, BLACK, pygame.Rect(0, 0, SCREEN_WIDTH, CELL_SIZE))

        if player == 1:
            pygame.draw.circle(screen, RED, (x_pos, CELL_SIZE // 2), CELL_SIZE // 2 - 5)
        else: 
            pygame.draw.circle(screen, YELLOW, (x_pos, CELL_SIZE // 2), CELL_SIZE // 2 - 5)

        for col in range(self.COLUMN):
            for row in range(self.ROW):
                pygame.draw.rect(screen, BLUE, pygame.Rect(col * CELL_SIZE, row * CELL_SIZE + CELL_SIZE, CELL_SIZE, CELL_SIZE))
                pygame.draw.circle(screen, BLACK, (col * CELL_SIZE + CELL_SIZE // 2, row * CELL_SIZE + CELL_SIZE + CELL_SIZE // 2), CELL_SIZE // 2 - 5)

        for col in range(self.COLUMN):
            for row in range(self.ROW):
                upperScreenPos = CELL_SIZE * (self.ROW + 1) 
                if self.game_board[row][col] == 1:
                    pygame.draw.circle(screen, RED, (col * CELL_SIZE + CELL_SIZE // 2, upperScreenPos - (row * CELL_SIZE + CELL_SIZE // 2)), CELL_SIZE // 2 - 5)
                elif self.game_board[row][col] == -1:
                    pygame.draw.circle(screen, YELLOW, (col * CELL_SIZE + CELL_SIZE // 2, upperScreenPos - (row * CELL_SIZE + CELL_SIZE // 2)), CELL_SIZE // 2 - 5)  

        if winner != 0:
            if winner == 1:
                img = end_font.render('Player Red Won!', True, BLACK)
            elif winner == -1:
                img = end_font.render('Player Yellow Won', True, BLACK)
            else:
                img = end_font.render('DRAW', True, BLACK)

            play_again_1 = play_gain.render('Click mouse button', True, BLACK)
            play_again_2 = play_gain.render('to play again', True, BLACK)
            
            size = (600, 300)
            green_image = pygame.Surface(size)
            green_image.set_alpha(180)
            pygame.draw.rect(green_image, WHITE, green_image.get_rect())
            
            screen.blit(green_image, (50, 250))
            screen.blit(img, img.get_rect(centerx=SCREEN_WIDTH // 2, centery=SCREEN_HEIGHT // 2))
            screen.blit(play_again_1, play_again_1.get_rect(centerx=SCREEN_WIDTH // 2, centery=(SCREEN_HEIGHT // 2)+100))
            screen.blit(play_again_2, play_again_2.get_rect(centerx=SCREEN_WIDTH // 2, centery=(SCREEN_HEIGHT // 2)+150))
            
        else:
            if self.turn == 0:
                click_to_start = start_font.render('Click to start', True, ORANGE)
                screen.blit(click_to_start, click_to_start.get_rect(centerx=SCREEN_WIDTH // 2, centery=(SCREEN_HEIGHT // 2)-100))
            else:
                if wrong_input == True:
                    input_error = input_error_font.render('Column is full', True, ORANGE)
                    screen.blit(input_error, input_error.get_rect(centerx=SCREEN_WIDTH // 2, centery=(SCREEN_HEIGHT // 2)-100))

                if using_AI:
                    thinking = thinking_font.render('Thinking', True, ORANGE)
                    if self.player == -1:
                        screen.blit(thinking, thinking.get_rect(centerx=SCREEN_WIDTH // 2, centery=(SCREEN_HEIGHT // 2)-100))
        
        pygame.display.update()

    def is_over(self, winner):
        """Check if there is winner in game.

        Args:
            winner (int): winner player(1 or -1 or 0(no winner))

        Returns:
            Boolean: True if there is any winner or draw, else False
        """        
        self.turn += 1
        self.player *= -1

        if winner != 0:
            print_board(self.game_board)
            winner_marker = ('O' if winner == 1 else 'X')
            print(f"Player '{winner_marker}' Won!")
            
            return True
        elif self.turn == 42:
            print(f"Draw!")
            return True
        
        else: return False

    def run_mcts(self, first_player):
        """Play Connect 4 GUI version against AI

        Get input from mouse pointer position which the player controls.

        Args:
            first_player (int): 1 if human player play first, -1 if AI play first
        """        
        mouse_x, mouse_y = pygame.mouse.get_pos()

        clock = pygame.time.Clock()
        winner = 0

        c = 1.41
        n_of_iterations = 1000
        root = None
        self.player = first_player

        for _ in range(100):
            root = mcts(root, c, 10)

        node = root

        while True:
            clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.QUIT()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if winner != 0:
                        new_game = Gui()
                        new_game.run_mcts(first_player)

                    # human's turn
                    if self.player == 1:
                        self.drawScreen(mouse_x, winner, self.player, False, True)
                        input_col = event.pos[0] // 100
                        column = input_col
                        if get_free_row(self.game_board, column) == -1:
                            self.drawScreen(mouse_x, winner, self.player, False, True)
                            break

                        new_node = node
                        for _ in range(1):
                            new_node = mcts(node, c).get_node(input_col)
                        node = new_node

                        self.game_board, winner = add_stone(self.game_board, column)
                    
                        result = self.is_over(winner)
                        if result == True:
                            break
                    
                    if self.player == -1:
                        self.drawScreen(mouse_x, winner, self.player, True)

                        # AI's turn
                        for _ in range(n_of_iterations):
                            node = mcts(node, c, 3)

                        print_board(self.game_board)
                        print([(child.wins, child.visits) for child in node.children])
                        node, column = node.choose_node()

                        self.game_board, winner = add_stone(self.game_board, column)

                        result = self.is_over(winner)
                        if result == True:
                            break

            if winner == 0:
                mouse_x, mouse_y = pygame.mouse.get_pos()   
            
            self.drawScreen(mouse_x, winner, self.player, True)

        pygame.QUIT()


    def runGame(self):
        """Run Connect4 by using Pygame.

        Get input from mouse pointer position which the player controls.
        """        
        mouse_x, mouse_y = pygame.mouse.get_pos()

        clock = pygame.time.Clock()
        winner = 0

        while True:
            clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.QUIT()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if winner != 0:
                        new_game = Gui()
                        new_game.runGame()

                    input_col = event.pos[0] // 100
                    if get_free_row(self.game_board, input_col) == -1:
                        self.drawScreen(mouse_x, winner, self.player, False, True)
                        break
                    else:
                        self.game_board, winner = add_stone(self.game_board, input_col)

                        result = self.is_over(winner)
                        if result == True:
                            break

            if winner == 0:
                mouse_x, mouse_y = pygame.mouse.get_pos()   
            
            self.drawScreen(mouse_x, winner, self.player)

        pygame.QUIT()
        