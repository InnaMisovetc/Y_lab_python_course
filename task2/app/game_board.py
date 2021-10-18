import copy
import random

import numpy as np
from termcolor import colored

from task2.app.player import HumanPlayer, AIPlayer


class GameBoard:
    MARKERS = ['X', 'O']

    def __init__(self, board_size=10, defeat_length=5):
        self.board_size = board_size
        self.defeat_length = defeat_length
        self.board_list = [[' ' for _i in range(self.board_size)] for _k in range(self.board_size)]
        self.players = []
        self.current_player = None
        self.occupied_count = 0

    @staticmethod
    def create_players(marker):
        """ Creates Players according to the marker, that was chosen by the first Player
        The second Player gets the remaining marker. Returns both players. """

        first_player = HumanPlayer(marker)
        if marker == 'X':
            second_player = AIPlayer('O')
        else:
            second_player = AIPlayer('X')
        return [first_player, second_player]

    @staticmethod
    def split_line(line, index):
        after_line = line[index:]
        before_line = line[:index]
        before_line.reverse()
        return after_line, before_line

    @staticmethod
    def count_consecutive_markers(line, marker):
        count = 0
        for element in line:
            if element == marker:
                count += 1
            else:
                return count
        return count

    @staticmethod
    def get_diagonal_offset(row, column, size, main_diagonal):
        if main_diagonal:
            return column - row
        else:
            return size - 1 - row - column

    def draw_board(self, row=0, column=0):
        """ Draws game board"""

        field = f'    {"   ".join(list(map(str, (range(self.board_size)))))}'
        for index, line in enumerate(self.board_list):
            if index == row:
                field += f'\n{index} | '
                for col_i in range(len(line)):
                    if col_i == column:
                        field += colored(f'{line[col_i]}', 'red')
                    else:
                        field += f'{line[col_i]}'
                    field += ' | '
            else:
                field += f'\n{index} | {" | ".join(line)} |'
        return field

    def start_game(self):
        self.players = self.create_players(self.choose_marker())
        self.current_player = self.choose_first_player()

    def choose_marker(self):
        """ Allows player to choose marker: X or O. Returns this marker. """

        marker = input('Do you want to play for X or for O? ').strip().upper()
        if marker == '0':
            marker = 'O'
        elif marker not in self.MARKERS:
            print('Enter X or O')
            return self.choose_marker()
        return marker

    def choose_first_player(self):
        """ Randomly chooses who is playing first: X or O. Returns this player. """

        player = random.choice(self.players)
        print(f'{player} player goes first')
        return player

    def play_round(self, row, column):
        """ Allows player to place its marker, increases the number of taken cells, print play board on the screen,
        checks whether the game is finished and change the current player to the next one.
         Return True if the game should continue. Otherwise, returns False. """

        self.current_player.place_marker(self, row, column)
        self.occupied_count += 1

        print(self.draw_board(row, column))

        if self.is_game_finished(row, column):
            return False

        self.current_player = self.get_other_player(self.current_player)
        return True

    def get_cell_axes(self, row, column, marker):
        board_list_copy = copy.deepcopy(self.board_list)
        board_list_copy[row][column] = marker

        horizontal = board_list_copy[row][0:self.board_size]
        vertical = [board_list_copy[x][column] for x in range(0, self.board_size)]

        offset = self.get_diagonal_offset(row, column, self.board_size, main_diagonal=True)
        main_diagonal = list(np.diag(board_list_copy, offset))

        offset = self.get_diagonal_offset(row, column, self.board_size, main_diagonal=False)
        flip_board_list = np.fliplr(board_list_copy)
        side_diagonal = list(np.diag(flip_board_list, offset))

        return horizontal, vertical, main_diagonal, side_diagonal

    def max_sequence_cell(self, row, column, marker):
        h, v, main_diag, side_diag = self.get_cell_axes(row, column, marker)
        max_h = self.max_sequence_line(h, row, column, marker, 'h')
        max_v = self.max_sequence_line(v, row, column, marker, 'v')
        max_main_diag = self.max_sequence_line(main_diag, row, column, marker, 'md')
        max_side_diag = self.max_sequence_line(side_diag, row, column, marker, 'sd')
        return max(max_h, max_v, max_main_diag, max_side_diag)

    def max_sequence_line(self, line, row, column, marker, line_type):
        if line_type == 'h':
            after_line, before_line = self.split_line(line, column)
        elif line_type == 'v':
            after_line, before_line = self.split_line(line, row)
        elif line_type == 'sd':
            offset = self.get_diagonal_offset(row, column, self.board_size, main_diagonal=False)
            after_line, before_line = self.split_line(line, row if offset >= 0 else row + offset)
        elif line_type == 'md':
            offset = self.get_diagonal_offset(row, column, self.board_size, main_diagonal=True)
            after_line, before_line = self.split_line(line, row if offset >= 0 else column)
        return self.count_consecutive_markers(after_line, marker) + self.count_consecutive_markers(before_line, marker)

    def is_current_player_won(self, row, column):
        """Returns True if the board game has DEFEAT LENGTH in a row.
        Otherwise, returns False. """

        if self.max_sequence_cell(row, column, self.current_player.marker) >= self.defeat_length:
            return True
        return False

    def is_game_finished(self, row, column):
        """ Returns True if one of the players won or the board is full.
         Otherwise, returns False. """

        if self.is_current_player_won(row, column):
            print(f'{self.get_other_player(self.current_player)} won!')
            return True
        elif self.is_board_full():
            print('Draw')
            return True
        return False

    def is_board_full(self):
        """ Returns True if there is no available cells on the board.
         Otherwise, returns False. """

        return self.occupied_count == self.board_size ** 2

    def is_cell_available(self, row, column):
        """ Returns True if the cell with row, column coordinates is available.
         Otherwise, returns False. """

        return self.board_list[row][column] not in self.MARKERS

    def is_cell_in_bounds(self, coord):
        return 0 <= coord < self.board_size

    def get_other_player(self, current_player):
        """ Returns a next player who should make move """

        players_copy = self.players.copy()
        players_copy.remove(current_player)
        return players_copy[0]
