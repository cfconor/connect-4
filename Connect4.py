class Connect4:
    """
    The Connect4 class will contain the initial attributes of the board, and the methods to add a coin to a column,
    and check for a 4 line match. Sounds simple!
    """
    
    # imports
    import numpy as np

    def __init__(self, height, width):
        self.height = height
        self.width = width

    def create_board(height, width):
        board = np.zeros((width,height))
        return board