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

board = Board(7, 6)
print(board)
