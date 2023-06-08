import numpy as np

ROW = 6
COLUMN = 7

def create_board():
    """Create a numpy array size of (6,7)

    Returns:
        numpy.ndarray: board size of 6*7
    """    
    return np.zeros((ROW,COLUMN), dtype=int)

def print_board(board):
    """Print the game board on command line with column numbers.

    Args:
        board (numpy.ndarray): board size of 6*7
    """        
    for i in board[::-1]:
        temp = []
        for j in i:
            if j == 1:
                temp.append('O')
            elif j == -1:
                temp.append('X')
            else:
                temp.append(' ')
        print(temp)
    print('-----------------------------------')
    print("  0    1    2    3    4    5    6")

def next_player(board):
    """Return the next player as an integer

    Args:
        board (numpy.ndarry): board size of 6*7

    Returns:
        int: 1 if the next player is 'O' else, -1
    """    
    board_sum = np.sum(board)
    if board_sum == 0:
        return 1
    else:
        return -1

def get_free_row(board, column_index):
    """Return the position of free(empty) row in the given column index

    Args:
        board (numpy.ndarray): board size of 6*7
        column_index (int): selected column index (from 0 to 6)

    Returns:
        int: position of empty row index
    """    
    for row_index in range(ROW):
        if board[row_index][column_index] == 0:
            return row_index
    return -1

def get_free_columns(board):
    """Return a list of column indices

    The column indices inside the list should have at least 1 empty space

    Args:
        board (numpy.ndarray): board size of 6*7

    Returns:
        free_columns (list): list of column indices
    """    
    free_columns = []
    for column_index in range(COLUMN):
        if get_free_row(board, column_index) != -1:
            free_columns.append(column_index)
    return free_columns

def check_status(board, player):
    """Checks whether there is any win state on the board.
    There are 4 types of winning states; Horizontal(-), Vertical (|), Diagonal(/) and another Diagonal(\).
    If the board has any types of winning state described above, returns True.

    Args:
        board (numpy.ndarray): a board size of 6*7
        player (int): integer 1 as a player 'O' and -1 as a player 'X'

    Returns:
        boolean: True if there is a winning state, if not, False.
    """        
    # 1 Horizontal (-)
    for col in range(COLUMN - 3):
        for row in range(ROW):
            if board[row][col] == player and board[row][col + 1] == player and \
                board[row][col + 2] == player and board[row][col + 3] == player:
                return True

    # 2 Vertical (|)
    for col in range(COLUMN):
        for row in range(ROW - 3):
            if board[row][col] == player and board[row + 1][col] == player and \
                board[row + 2][col] == player and board[row + 3][col] == player:
                return True
    
    # 3 Diagonal (/)
    for col in range(COLUMN - 3):
        for row in range(ROW - 3):
            if board[row][col] == player and board[row + 1][col + 1] == player and \
                board[row + 2][col + 2] == player and board[row + 3][col + 3] == player:
                return True
    # 4 Diagonal (\)
    for col in range(COLUMN - 3):
        for row in range(3, ROW):
            if board[row][col] == player and board[row - 1][col + 1] == player and \
                board[row - 2][col + 2] == player and board[row - 3][col + 3] == player:
                return True

def add_stone(game_board, column_index):
    """Place a stone in the selected column.

    It checks if there is an empty space in the given column index.
    If there is, it places a stone and checks if there is any win pattern.
    It returns a board after placing a stone and player if the player wins.
    It returns 0 for player if there is no winner
    It returns 2 for player if the board is full.

    Args:
        game_board (numpy.ndarray): a board size of 6*7
        column_index (int): selected column index (from 0 to 6)

    Returns:
        board (numpy.ndarray): a board size of 6*7
        player (int): 
            0 if there is no winner,
            1 if player 'O' wins,
            -1 if player 'X' wins,
            2 if the board is full.
    """    
    board = game_board.copy()
    player = next_player(board)
    row_index = get_free_row(board, column_index)
    if row_index != -1:
        board[row_index][column_index] = player
    else:
        print(f'column{column_index} is full')
    
    if check_status(board, player):
        return board, player
    else:
        if is_board_full(board):
            return board, 2
        return board, 0
    
def is_board_full(board):
    """Check if the board is full or not.

    Returns:
        Boolean: True if the board is full, if not, False.
    """        
    board_sum = np.sum(abs(board))
    if board_sum == 42:
        return True
    return  False

def get_player_marker(board):
    """Return next player as a marker 'O' or 'X'

    Args:
        board (numpy.ndarray): a board size of 6*7

    Returns:
        String: 'O' if the next player is 1 else 'X'
    """    
    player = next_player(board)
    return 'O' if player == 1 else 'X'