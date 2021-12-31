class Board:

  def __init__(self, columns, rows):
    self.rows = rows
    self.cols = columns
    self.board = [ [" "] * self.cols for _ in range(self.rows) ]
    self.isfull = [False] * columns
    self.isover = False

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

    if self.isfull[column]:
      print("Column full, try again.")
      return

    for row in range(self.rows - 1, -1, -1):
      if self.board[row][column] == " ":
        self.board[row][column] = piece

        if row == 0:
          self.isfull[column] = True

        break

    print(self)
    self.is_over()

  def is_over(self):

    # Check horizontal
    current = 'x'
    count = 0
    for row in range(self.rows):
      for col in range(self.cols):
        if self.board[row][col] == " ":
          continue
        elif self.board[row][col] == current:
          count += 1
          if count == 4:
            self.isover = True
            return
        else:
          current = self.board[row][col]
          count = 1

    # Check vertical
    current = 'x'
    count = 0
    for col in range(self.cols):
      for row in range(self.rows):
        if self.board[row][col] == " ":
          continue
        elif self.board[row][col] == current:
          count += 1
          if count == 4:
            self.isover = True
            return
        else:
          current = self.board[row][col]
          count = 1

    self.isover = False
    return

board = Board(7, 6)
print(board)
