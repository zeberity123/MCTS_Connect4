import pygame
from connect_four import board,old_player
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

class Gui:
    """Runs GUI version of Connect 4.
    Uses Pygame to draw Graphics on pop up screen.
    """    
    pygame.init()

    def __init__(self):
        """Inits by creating a board and a player.
        """        
        self.game_board = board.Board()
        self.game_player = old_player.Player()
        print("gui created")

    def drawScreen(self, x_pos, game_winner, turn):
        """Draws graphics on the screen
        The screen size is given as 700 * 700 and uses 5 colours.

        Args:
            x_pos (int): current horizontal position of mouse
            game_winner (int): an integer indicates who's winner
            turn (int): an integer indicates which player's turn at the moment
        """        
        BLUE = (0, 0, 255)
        BLACK = (0, 0, 0)
        RED = (255, 0, 0)
        YELLOW = (255, 255, 0)
        ORANGE = (255, 165, 0)
        end_font = pygame.font.SysFont('calibri', 80)

        SCREEN_WIDTH = 700
        SCREEN_HEIGHT = 700
        CELL_SIZE = 100
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        
        screen.fill(BLACK)

        pygame.draw.rect(screen, BLACK, pygame.Rect(0, 0, SCREEN_WIDTH, CELL_SIZE))

        if turn == 1:
            pygame.draw.circle(screen, RED, (x_pos, CELL_SIZE // 2), CELL_SIZE // 2 - 5)
        else: 
            pygame.draw.circle(screen, YELLOW, (x_pos, CELL_SIZE // 2), CELL_SIZE // 2 - 5)

        for col in range(self.game_board.col):
            for row in range(self.game_board.row):
                pygame.draw.rect(screen, BLUE, pygame.Rect(col * CELL_SIZE, row * CELL_SIZE + CELL_SIZE, CELL_SIZE, CELL_SIZE))
                pygame.draw.circle(screen, BLACK, (col * CELL_SIZE + CELL_SIZE // 2, row * CELL_SIZE + CELL_SIZE + CELL_SIZE // 2), CELL_SIZE // 2 - 5)

        for col in range(self.game_board.col):
            for row in range(self.game_board.row):
                upperScreenPos = CELL_SIZE * (self.game_board.row + 1) 
                if self.game_board.board[row][col] == 'O':
                    pygame.draw.circle(screen, RED, (col * CELL_SIZE + CELL_SIZE // 2, upperScreenPos - (row * CELL_SIZE + CELL_SIZE // 2)), CELL_SIZE // 2 - 5)
                elif self.game_board.board[row][col] == 'X':
                    pygame.draw.circle(screen, YELLOW, (col * CELL_SIZE + CELL_SIZE // 2, upperScreenPos - (row * CELL_SIZE + CELL_SIZE // 2)), CELL_SIZE // 2 - 5)  

        if game_winner != 0:
            if game_winner == 1:
                img = end_font.render('Player Red Won!', True, ORANGE)
            elif game_winner == -1:
                img = end_font.render('Player Yellow Won', True, ORANGE)
            else:
                img = end_font.render('DRAW', True, ORANGE)

            screen.blit(img, img.get_rect(centerx=SCREEN_WIDTH // 2, centery=SCREEN_HEIGHT // 2))

        pygame.display.update()

    def runGame(self):
        """Runs Connect4 by using Pygame.
        Gets input from mouse pointer position which the player controls.

        To terminate the program, it needs (ctrl + c) on the command line.
        """        
        mouse_x, mouse_y = pygame.mouse.get_pos()

        clock = pygame.time.Clock()
        game_winner = 0

        while True :
            clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    break
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    input_col = event.pos[0] // 100
                    input_row = self.game_board.get_free_row_index(input_col)
                    if input_row != -1:
                        self.game_board.add_stone(input_row, input_col, self.game_player.stone)
                        if self.game_board.check_status(self.game_player.stone):
                            game_winner = self.game_player.turn
                        elif self.game_board.count == 42:
                            game_winner = 2

                        self.game_player.change_turn()
            
            if game_winner == 0:
                mouse_x, mouse_y = pygame.mouse.get_pos()   
            
            self.drawScreen(mouse_x, game_winner, self.game_player.turn)
        pygame.QUIT()
        