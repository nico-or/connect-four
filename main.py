class Board:

  def __init__(self, columns, rows):
    self.rows = rows
    self.cols = columns
    self.board = [ [" "] * self.cols for _ in range(self.rows) ]

  def __repr__(self):

    header = "  " + "   ".join(list(map(str, range(1, self.cols + 1)))) + "  \n"

    separator = "---".join(["+"] * (self.cols + 1)) + "\n"

    out = header + separator
    for row in self.board:
      for cell in row:
        out += f"| {cell} "
      out += "|\n" + separator
    return out

  def new_piece(self, column, piece):
    column -= 1

    if piece not in 'xo':
      print("Invalid piece marker, please use x or o")
      return

    if column not in range(self.cols):
      print("Column out of bounds, please try again")
      return

    for row in range(self.rows - 1, 0, -1):
      if self.board[row][column] == " ":
        self.board[row][column] = piece
        break
    print(self)

board = Board(7, 6)
print(board)
