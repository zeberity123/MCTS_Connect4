class Player:
    """Defines the player for Connect 4.
    """    
    def __init__(self):
        """Inits with 2 attributes; turn and stone.
        Player 1 has turn value(1) and stone marker('O').
        Player 2 has turn value(-1) and stone marker('X').

        Initially, it starts from player 1.
        """        
        self.turn = 1
        self.stone = 'O'

    def change_turn(self):
        """Switches the turn to another player.
        Changes the turn value and stone marker.
         
        """        
        self.turn *= -1
        if self.turn == 1:
            self.stone = 'O'
        else:
            self.stone = 'X'

                