import unittest
from Game.board import Board


class TestBoard(unittest.TestCase):
    def test_init(self):
        board = Board()
        self.assertEqual(
            len(board.grid),
            15,
        )
        self.assertEqual(
            len(board.grid[0]),
            15,
        )

class TesteBoardAndValues(unittest.TestCase):
     def test_init_different_multipliers_and_letters(self):
        board = Board()
        assert len(board.grid) == 15
        assert len(board.grid[0]) == 15
        for row in board.grid:
            for cell in row:
                assert cell.multiplier != 0
                assert cell.multiplier_type in ['', 'letter']
                assert cell.letter is None

if __name__ == '__main__':
    unittest.main()