import unittest

from task2.app.game_board import GameBoard
from task2.app.player import HumanPlayer, AIPlayer


class TestMaxSequence(unittest.TestCase):
    DEBUG_BOARD = [['X', 'O', 'O', 'X', 'O'],
                   [' ', 'X', 'O', 'X', ' '],
                   ['X', 'O', 'O', 'X', ' '],
                   ['O', 'O', 'X', 'O', 'X'],
                   ['X', 'X', 'O', 'X', 'O']]

    def test_max_sequence_in_cell_secondary_diagonal(self):
        new_board = GameBoard(5, 3)
        new_board.board_list = self.DEBUG_BOARD
        max_sequence = new_board.max_sequence_cell(2, 1, 'O')
        self.assertEqual(max_sequence, 3)

    def test_max_sequence_in_cell_main_diagonal(self):
        new_board = GameBoard(5, 3)
        new_board.board_list = self.DEBUG_BOARD
        max_sequence = new_board.max_sequence_cell(3, 3, 'O')
        self.assertEqual(max_sequence, 3)

    def test_max_sequence_in_cell_vertical(self):
        new_board = GameBoard(5, 3)
        new_board.board_list = self.DEBUG_BOARD
        max_sequence = new_board.max_sequence_cell(1, 3, 'X')
        self.assertEqual(max_sequence, 3)

    def test_max_sequence_in_cell_horizontal(self):
        new_board = GameBoard(5, 3)
        new_board.board_list = self.DEBUG_BOARD
        max_sequence = new_board.max_sequence_cell(0, 1, 'O')
        self.assertEqual(max_sequence, 2)


class TestAIPlayer(unittest.TestCase):
    DEBUG_BOARD_1 = [['X', 'O', 'O', 'X', 'O'],
                     [' ', 'X', 'O', 'X', ' '],
                     ['X', 'O', 'O', 'X', ' '],
                     ['O', 'O', 'X', 'O', 'X'],
                     ['X', 'X', 'O', 'X', 'O']]

    DEBUG_BOARD_2 = [['X', 'O', ' ', 'X', 'O'],
                     [' ', ' ', ' ', ' ', ' '],
                     ['X', 'O', ' ', 'X', 'O'],
                     [' ', ' ', ' ', ' ', ' '],
                     ['X', ' ', ' ', ' ', ' ']]

    def test_cells_scores_calculation_1_0(self):
        new_board = GameBoard(5, 3)
        new_board.board_list = self.DEBUG_BOARD_1
        ai_player = AIPlayer('X')
        new_board.players = [ai_player, HumanPlayer('O')]

        scores = ai_player.calculate_cells_scores(new_board, ai_player.marker)
        self.assertIn(((1, 0), 3, 2), scores)

    def test_cells_scores_calculation_1_4(self):
        new_board = GameBoard(5, 3)
        new_board.board_list = self.DEBUG_BOARD_1
        ai_player = AIPlayer('X')
        new_board.players = [ai_player, HumanPlayer('O')]

        scores = ai_player.calculate_cells_scores(new_board, ai_player.marker)
        self.assertIn(((1, 4), 4, 2), scores)

    def test_cells_scores_calculation_2_4(self):
        new_board = GameBoard(5, 3)
        new_board.board_list = self.DEBUG_BOARD_1
        ai_player = AIPlayer('X')
        new_board.players = [ai_player, HumanPlayer('O')]

        scores = ai_player.calculate_cells_scores(new_board, ai_player.marker)
        self.assertIn(((2, 4), 2, 3), scores)

    def test_cells_scores_calculation_board_2_3_3(self):
        new_board = GameBoard(5, 3)
        new_board.board_list = self.DEBUG_BOARD_2
        ai_player = AIPlayer('O')
        new_board.players = [ai_player, HumanPlayer('X')]

        scores = ai_player.calculate_cells_scores(new_board, ai_player.marker)
        self.assertIn(((3, 3), 2, 2), scores)


if __name__ == '__main__':
    unittest.main()
