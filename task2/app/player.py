from abc import ABC, abstractmethod


class AbstractPlayer(ABC):
    def __init__(self, marker):
        self.marker = marker

    def __str__(self):
        return self.marker

    @abstractmethod
    def select_cell(self, board):
        pass

    def place_marker(self, board, row, column):
        board.board_list[row][column] = self.marker


class HumanPlayer(AbstractPlayer):
    def select_cell(self, board):
        """ Asks user to enter coordinates for a move. If the input is valid (coordinates are in board size range
        and the cell is empty) returns obtained coordinates. Otherwise, asks user to enter coordinates again. """

        position = (input(f'Player {self.marker}, choose cell coordinates in a format x y: ')).split(' ')
        try:
            row, column = map(int, position)
        except ValueError:
            print(f'Invalid Input. Enter coordinates from 0 to {board.board_size - 1}')
            return self.select_cell(board)
        if not (board.is_cell_in_bounds(row) and board.is_cell_in_bounds(column)):
            print(f'Enter coordinates from 0 to {board.board_size - 1}')
            return self.select_cell(board)
        elif not board.is_cell_available(row, column):
            print('This cell is not empty. Choose coordinates of another cell.')
            return self.select_cell(board)
        return row, column


class AIPlayer(AbstractPlayer):
    def select_cell(self, board):
        available_cells = self.calculate_cells_scores(board, self.marker)
        available_cells.sort(key=lambda cell: (cell[1], cell[2]))
        row, column = available_cells[0][0]
        return row, column

    def calculate_cells_scores(self, board, marker):
        cell_scores = []
        for row in range(board.board_size):
            for column in range(board.board_size):
                if board.board_list[row][column] == ' ':
                    max_seq_ai = board.max_sequence_cell(row, column, marker)
                    max_seq_player = board.max_sequence_cell(row, column, board.get_other_player(self).marker)
                    cell_scores.append(((row, column), max_seq_ai, max_seq_player))
        return cell_scores
