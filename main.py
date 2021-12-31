class Board:

  def __init__(self):
    self.board = [ [" "] * 7 for _ in range(6) ]

board = Board()
print(board.board)
print(board)
