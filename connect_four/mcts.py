import numpy as np
import sys, os
import random
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from connect_four.board import *
from connect_four.node import Node

def random_move(input_board):
    """Place a stone in input board until the winner is found(final state).

    Place a stone in a random column index of the input board an return player.
    If player'O' wins, return 1
    If player'X' wins, return -1
    If the game ties, return 2.
    If there is no winner, return 0.

    Args:
        input_board (numpy.ndarray): a board size of 6*7

    Returns:
        player (int): 1 if player 'O' wins, -1 if player 'X' wins, else 0
    """    
    cnt = 0
    while True:
        cols = get_free_columns(input_board)
        if len(cols) == 0:
            return 0
        new_col = random.choice(cols)
        player = next_player(input_board)
        input_board, winner = add_stone(input_board, new_col)
        if winner != 0:
            return player
        cnt += 1

def selection(node, c):
    """Selection process in MCTS
    
    Select a child node with the highest UCB value.
    If there is no UCB value in the child, return a random Node from children.

    Args:
        node (Node): root node in selection process
        c (float): exploration constant for mcts (c_value)

    Returns:
        node (Node): child node with the highest UCB value.
    """    
    while node.children:
        # Select highest uct
        ucbs = []
        for child in node.children:
            ucb = child.calc_ucb(c)
            if ucb == None:
                node = random.choice(node.children)
                break
            ucbs.append(ucb)
        else: 
            node = node.children[np.argmax(ucbs)]

    return node

def expansion(node, free_columns):
    """Expansion process in MCTS

    Expands every expandable columns from the selected node.
    Then add all the expanded node as a child node for the selected Node.

    Args:
        node (Node): root node before expansion
        free_columns (list): list of expandable column indices
    """    
    expansions = []
    for column in free_columns:
        expanded_board, winner = add_stone(node.board, column)
        expansions.append([[expanded_board, winner], column])
    
    new_children = []
    for expanded_node, column in expansions:
        expanded_board = expanded_node[0]
        winner_mark = expanded_node[1]
        new_child = Node(expanded_board, winner_mark, column, node)
        new_children.append(new_child)

    node.add_child(new_children)

def simulation(node, n_of_simulations=1):
    """Simluation(rollout) process in MCTS

    From the selected Node, simulate by randomly add stones
    until a winner is found(game over).

    If there is any child node which already has winner, 
    it returns winning child node immediately.

    Returns original node before simulation and winner from the simulation.

    Args:
        node (Node): root node before simulation
        n_of_simulations (int, optional): number of simulations/rollouts. Defaults to 1.

    Returns:
        node (Node): root node before simulation
        simulation_winner (int): winner player(1 or -1 or 0(no winner)) from the simulation 
    """    
    winning_nodes = []
    for child in node.children:
        if child.won_player != 0:
            winning_nodes.append(child)

    if winning_nodes:
        node = winning_nodes[0]
        simulation_winner = node.won_player
    else:
        node = random.choice(node.children)
        simulation_winners = []
        for i in range(n_of_simulations):
            simulation_winner = random_move(node.board)
            simulation_winners.append(simulation_winner)
            
        simulation_sum = sum(simulation_winners)

        if simulation_sum == 0:
            simulation_winner = 0
        else:
            simulation_winner = 1 if simulation_sum > 0 else -1
    return node, simulation_winner

def backpropagation(node, simulation_winner):
    """Backpropagation process in MCTS

    Backpropagate the results from the previous process by recording
    the nubmer of wins and visits.

    Args:
        node (Node): child node that has win/visits data
        simulation_winner (int): winner player(1 or -1 or 0(no winner)) from the simulation 
    """    
    parent_node = node
    while parent_node:
        parent_node.visits += 1
        parent_next_player = next_player(parent_node.board)
        if simulation_winner != parent_next_player:
            if simulation_winner:
                parent_node.wins += 1
        parent_node = parent_node.parent

def mcts(root=None, c=None, n_of_simulations=1):
    """MCTS process for Connect 4.
    
    Start by setting the root node with empty board.
    The process of MCTS consists of 4 phases:
        1. Selection
        2. Expansion
        3. Simulations/rollouts
        4. Backpropagation

    Args:
        root (Node, optional): root Node. Defaults to None.
        c (float, optional): exploration constant(c_value). Defaults to None.
        n_of_simulations (int, optional): number of simulations. Defaults to 1.

    Returns:
        root (Node): root Node
    """    
    if root == None:
        board = create_board()
        root = Node(board, 0, None,  None)

    if root.children:
        node = selection(root,c)
    else:
        node = root

    free_columns = get_free_columns(node.board)

    if not free_columns:
        return root

    else:
    # expansion process
        if node.won_player == 0:
            expansion(node, free_columns)

    # Simulation process
            node, simulation_winner = simulation(node, n_of_simulations)
        else:
            simulation_winner = node.won_player

    # backpropagation process
        backpropagation(node, simulation_winner)
    
    return root