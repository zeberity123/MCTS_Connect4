import math
import numpy as np

import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

class Node:
    """A class to represent nodes for the game tree in MCTS.
    """     
    def __init__(self, board, won, col, parent):
        """Init by setting the attributes for selected node.

        Args:
            board (numpy.ndarray): board size of 6*7
            won (int): integer value for estimated winning player.
            col (int): positional column index of the node.
            parent (Node): parent node of the current node.
            children (Node): children nodes.
            wins (int): number of wins.
            visits (int) number of visits.
        """        
        self.board =board
        self.won_player = won
        self.col = col
        self.parent = parent

        self.children = None
        self.wins = 0
        self.visits = 0
    
    def calc_ucb(self, c=None):
        """Calculates UCB value for the node.
        Uses UCB formula to calculate the values. If there is no c value given,
        original c value from ucb1 (sqrt(2)) will be used.

        Returns:
            float: ucb value for the given node.
        """        
        if self.visits == 0:
            return None
        
        if c == None:
            c = np.sqrt(2)

        ucb = (self.wins/self.visits) + c * np.sqrt(np.log(self.parent.visits)/self.visits)
        return ucb

    def add_child(self, child):
        """Add child node.

        Args:
            child (Node): Node that will be a child node for selected node.
        """        
        self.children = child

    def choose_node(self):
        """Return a Node with the highest win rates.

        If there is no child Node exist for the selected Node,
        return None for both Node and column index.
        If there is a winning Node, return the winning Node immediately.


        Returns:
            best_node (Node): Node with the highest win rate
            best_node.col (int): column index of the best_node
        """        
        if self.children is None:
            return None, None
        
        win_nodes = []
        for child in self.children:
            if child.won_player:
                win_nodes.append(child)
        if win_nodes:
            return win_nodes[0], win_nodes[0].col

        visits = []
        for child in self.children:
            if child.visits > 0:
                visits.append(child.wins/child.visits)
            else: visits.append(0)
        best_node = self.children[np.argmax(visits)]
        print(f'WinRates:{[round(rnd, 5) for rnd in visits]}')
        return best_node, best_node.col
    
    def get_node(self, col):
        """Return a child Node in the selected column index.

        Returns None if there is no children for selected Node.
        
        Args:
            col (int): column index

        Returns:
            node (Node): child Node in the column index
        """        
        if self.children is None:
            return None
        for node in self.children:
            if node.col == col:
                return node