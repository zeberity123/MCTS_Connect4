

# 30 MAR 2023
    - fixed errors when reaching max column happens in gui.py

    - added restarting fuction in gui.py

    - worked on documentation for all files

    - updated diary.md

# 29 MAR 2023
    - fixed errors when a tie game happens in mcts.

    - fixed wrong implementation of number of iterations in MCTS

    - enabled printing boards during auto_mcts

# 28 MAR 2023
    - added option in mcts() for number of simulation(rollouts) for better performance of AI

# 27 MAR 2023
    - added option in auto_mcts() for AI players with different exploration constant

    - fixed gui.py for new board.py

    - enabled playing against AI with Graphic interface

# 26 MAR 2023
    - made mcts() work in mcts.py by unit test

    - fixed errors in play_text() in game.py with new board.py

    - added auto_mcts() fuction to test AI playing against each other for experiment

# 25 MAR 2023
    - modified random move() in mcts.py for new board

    - created new unit test for mcts.py

# 24 MAR 2023
    - added new version of unit test for board.py

    - refactored board.py during unit test

    - refactored node.py during unit test

# 22 MAR 2023
    - removed 'class' for board so that the board is no longer an object itself, for easier access of methods in board.py from external code

# 21 MAR 2023
    - merged from branch 'mcts' to 'main'

    - created branch 'refactoring'

    - started to work on refactoring board.py

# 04 MAR 2023
    - added getter for stone marker in board.py

    - initial work on expansion and simulation process in MCTS

# 03 MAR 2023
    - modified attributes for object Node

    - added method for choosing best winrate Node in node.py

    - initial work for MCTS process (selection)

# 22 FEB 2023
    - better move() for AI is now working
     
    - improved better move() during unit test

# 21 FEB 2023
    - refactored random move from AI by unit test

    - added method for better move(winning moves) for AI

# 16 FEB 2023
    - AI making random move is now available

    - added random move in game.py and game.py for driver

# 15 FEB 2023
    - added method for random move in mcts.py

# 03 FEB 2023
    - added method to add child node in node.py

    - added method to change the stone marker in node.py

# 09 DEC 2022
    - updated diary.md

    - tag version 1.05 published

# 08 DEC 2022
    - added documentation docstrings in the python files

    - managed exception of input from main.py

    - added a function calculates UCB1 in node.py

# 07 DEC 2022
    - now the GUI is fully implemented for connect 4!

    - GUI version Connect Instructions:
        1. Player RED starts first to play
        2. Uses mouse pointer to select column position
        3. Click to drop a stone
        4. Type ctrl+C in terminal to close the game

# 06 DEC 2022
    - created gui.py to draw graphics for connect 4
    
    - setup instruction to turn gui on in main.py:
        1. Player inputs '1' to select 'play by 2 human players'
        2. Player inputs '2' to select GUI game play

    - minor updates for fixing line numbers
    

# 17 NOV 2022
    - tested initialising node from node.py
    - added a function that returns free columns as a list in board.py

# 16 NOV 2022
    - now it displays option to choose when starts:
        1. Play by 2 human players (select 1)
        2. Play against AI (select 2)

    - created node.py and mcts.py:
        1. mcts.py working as a game tree for connect 4
        2. node.py working as a nodes in the game tree

# 14 NOV 2022
    - created game.py to split the game runner from main.

# 11 NOV 2022
    - added error case for wrong input:
        1. when player inputs a number in correct range(0~6)
        2. but the corresponding column is full of stones
            - will display column '{input}' is full

# 06 NOV 2022
    - added case for draw:
        1. It will display 'Draw!' on command-line

    - handled error case for wrong input:
        1. when the player inputs a number out of range(0~6)
        2. when the player inputs which is not a number

# 04 NOV 2022
    - enabled 2 human players playing:
        If anyone wins:
            1. The game stops
            2. It will display who won the game by stone

    - column number is now visible while playing
        

# 03 NOV 2022
    - putting stones is available on Terminal:
        1. Input integer from 0 to 6 (column_index)
        2. It will put corresponding stone on board
        3. Player turn will be changed

    - added stone marker:
        player  '1' has stone 'O'
        player '-1' has stone 'X'
    
    - defined game state:
        1. Win state is defined by
            A: horizontal (-)
            B: vertical   (|)
            C: diagonal   (/)
            D: diagonal   (\)
        
        2. Draw state is defined by
            A: When there is no win state
            B: The full of stones(42 stones on board)

# 28 OCT 2022
    - added put_stone function:
        if a column index selected, put stone to the column

# 24 OCT 2022
    - added turn variable for player:
        player variable will vary from 1 to -1 or -1 to 1

# 23 OCT 2022
    - Added diary.md
    - renamed file and class name

# 17 OCT 2022
    - setup the size of the board for connect4
    - now the tile of the board is visible as '_' on command-line

# 10 OCT 2022
    - added .gitignore