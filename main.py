class Board:

  def __init__(self, columns, rows):
    self.rows = rows
    self.cols = columns
    self.board = [ [" "] * self.cols for _ in range(self.rows) ]

board = Board(7, 6)
print(board.board)
print(board)
