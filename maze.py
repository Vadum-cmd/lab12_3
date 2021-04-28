"""Implemention of the Maze ADT using a 2-D array."""
from arrays import Array2D
from lliststack import Stack


class Maze:
    """Define constants to represent contents of the maze cells."""
    MAZE_WALL = "*"
    PATH_TOKEN = "x"
    TRIED_TOKEN = "o"

    def __init__(self, num_rows, num_cols):
        """Initialize new Maze."""
        self._maze_cells = Array2D(num_rows, num_cols)
        self._start_cell = None
        self._exit_cell = None

    def num_rows(self):
        """Returns the number of rows in the maze."""
        return self._maze_cells.num_rows()

    def num_cols(self):
        """Returns the number of columns in the maze."""
        return self._maze_cells.num_cols()

    def set_wall(self, row, col):
        """Fills the indicated cell with a "wall" marker."""
        assert row >= 0 and row < self.num_rows() and \
               col >= 0 and col < self.num_cols(), "Cell index out of range."
        self._maze_cells[row, col] = self.MAZE_WALL

    def set_start(self, row, col):
        """Sets the starting cell position."""
        assert row >= 0 and row < self.num_rows() and \
               col >= 0 and col < self.num_cols(), "Cell index out of range."
        self._start_cell = _CellPosition(row, col)

    def set_exit(self, row, col):
        """Sets the exit cell position."""
        assert row >= 0 and row < self.num_rows() and \
               col >= 0 and col < self.num_cols(), "Cell index out of range."
        self._exit_cell = _CellPosition(row, col)


    def find_path(self):
        """
        Attempts to solve the maze by finding a path from the starting cell
        to the exit. Returns True if a path is found and False otherwise.
        """
        curr_position = _CellPosition(self._start_cell.row, self._start_cell.col)
        self._mark_path(curr_position.row, curr_position.col)

        while (curr_position.row, curr_position.col) != (self._exit_cell.row, self._exit_cell.col):
            for cords in [(curr_position.row - 1, curr_position.col), (curr_position.row, curr_position.col + 1),
                          (curr_position.row + 1, curr_position.col), (curr_position.row, curr_position.col - 1)]:
                (next_row, next_col) = cords
                if self._valid_move(next_row, next_col):
                    self._mark_path(next_row, next_col)
                    curr_position = _CellPosition(next_row, next_col)
                    break

            for cords in [(curr_position.row, curr_position.col - 1), (curr_position.row, curr_position.col + 1),
                          (curr_position.row + 1, curr_position.col), (curr_position.row, curr_position.col - 1)]:
                (next_row, next_col) = cords
                if self._maze_cells[next_row, next_col] == "x":
                    self._mark_tried(curr_position.row, curr_position.col)
                    curr_position.row, curr_position.col = next_row, next_col
                    break
            else:
                return False

        if (curr_position.row, curr_position.col) != (self._exit_cell.row, self._exit_cell.col):
            return True

    def reset(self):
        """Resets the maze by removing all "path" and "tried" tokens."""
        for i in range(self.num_rows()):
            for j in range(self.num_cols()):
                if self._maze_cells[i, j] in ['x', 'o']:
                    self._maze_cells[i, j] = None

    def __str__(self):
        """Returns a text-based representation of the maze."""
        for row in range(self.num_rows() - 1):
            line = ''
            for col in range(self.num_cols()):
                if self._maze_cells[row, col] is None:
                    line += "  "
                else:
                    line += self._maze_cells[row, col] + " "
            print(line)

        line = ''
        for col in range(self.num_cols()):
          if self._maze_cells[self.num_rows(), col] is None:
            line += "  "
        else:
            line += self._maze_cells[self.num_rows(), col] + " "
        return line

    def _valid_move(self, row, col):
        """Returns True if the given cell position is a valid move."""
        return row >= 0 and row < self.num_rows() \
               and col >= 0 and col < self.num_cols() \
               and self._maze_cells[row, col] is None

    def _exit_found(self, row, col):
        """Helper method to determine if the exit was found."""
        return row == self._exit_cell.row and col == self._exit_cell.col

    def _mark_tried(self, row, col):
        """Drops a "tried" token at the given cell."""
        self._maze_cells[row, col] = self.TRIED_TOKEN

    def _mark_path(self, row, col):
        """Drops a "path" token at the given cell."""
        self._maze_cells[row, col] = self.PATH_TOKEN


class _CellPosition(object):
    """Private storage class for holding a cell position."""
    def __init__(self, row, col):
        self.row = row
        self.col = col
