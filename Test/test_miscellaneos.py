import unittest
from Game.converter import Converter
from Game.tools import Tools
from Game.board import Board
from Game.tile import Tile
from Game.miscellaneos import Miscellaneos

class TestMiscellaneos(unittest.TestCase):

    def setUp(self):
        self.miscellaneos = Miscellaneos()

    def test_calculate_word_value(self):
        self.assertEqual(self.miscellaneos.calculate_word_value("hello"), 8)
        self.assertEqual(self.miscellaneos.calculate_word_value("world"), 9)

    def test_compare_tiles_and_letters(self):
        self.assertEqual(self.miscellaneos.compare_tiles_and_letters(Tile("A"), "A"), 1)
        self.assertEqual(self.miscellaneos.compare_tiles_and_letters(Tile("B"), "C"), 0)

    def test_get_tiles_for_word_placement(self):
        board = Board()
        board.grid[7][7].letter = Tile("H")
        board.grid[7][8].letter = Tile("E")
        board.grid[7][9].letter = Tile("L")
        board.grid[7][10].letter = Tile("L")
        board.grid[7][11].letter = Tile("O")
        self.assertEqual(self.miscellaneos.get_tiles_for_word_placement("HELLO", (7, 7), "H", board), ["H", "E", "L", "L", "O"])

    def test_tiles_needed_to_form_word(self):
        board = Board()
        board.grid[7][7].letter = Tile("H")
        board.grid[7][8].letter = Tile("E")
        board.grid[7][9].letter = Tile("L")
        board.grid[7][10].letter = Tile("L")
        self.assertEqual(self.miscellaneos.tiles_needed_to_form_word("HELLO", (7, 7), "H", board), [Tile("O")])

    def test_get_cell_in_the_extreme_horizontal(self):
        result = []
        self.miscellaneos.get_cell_in_the_extreme_horizontal(5, (7, 7), result)
        self.assertEqual(result, [(7, 6), (7, 12)])

    def test_get_cell_in_the_extreme_vertical(self):
        result = []
        self.miscellaneos.get_cell_in_the_extreme_vertical(5, (7, 7), result)
        self.assertEqual(result, [(6, 7), (12, 7)])

    def test_get_cell_around_word_horizontal(self):
        result = []
        self.miscellaneos.get_cell_around_word_horizontal("HELLO", (7, 7), result)
        self.assertEqual(result, [(6, 7), (8, 7), (8, 8), (8, 9), (8, 10), (8, 11), (8, 12), (6, 12)])

    def test_get_cell_around_word_vertical(self):
        result = []
        self.miscellaneos.get_cell_around_word_vertical("HELLO", (7, 7), result)
        self.assertEqual(result, [(6, 6), (6, 8), (7, 6), (7, 12), (8, 6), (8, 12), (8, 8), (8, 9), (8, 10), (8, 11)])

    def test_verify_cell_around_word(self):
        board = Board()
        board.grid[6][6].letter = Tile("T")
        board.grid[6][8].letter = Tile("E")
        self.assertTrue(self.miscellaneos.verify_cell_around_word([(6, 6), (6, 8)], [], board))
        self.assertFalse(self.miscellaneos.verify_cell_around_word([(6, 6), (6, 8)], [], board))

    def test_check_cells_before_horizontal(self):
        board = Board()
        board.grid[6][6].letter = Tile("T")
        board.grid[5][6].letter = Tile("E")
        location = []
        result = self.miscellaneos.check_cells_before_horizontal(6, 6, location, board)
        self.assertEqual(result, ["E"])
        self.assertEqual(location, [(5, 6)])

    def test_check_cells_before_vertical(self):
        board = Board()
        board.grid[6][6].letter = Tile("T")
        board.grid[6][5].letter = Tile("E")
        location = []
        result = self.miscellaneos.check_cells_before_vertical(6, 6, location, board)
        self.assertEqual(result, ["E"])
        self.assertEqual(location, [(6, 5)])

    def test_check_cells_after_horizontal(self):
        board = Board()
        board.grid[6][6].letter = Tile("T")
        board.grid[7][6].letter = Tile("E")
        result = self.miscellaneos.check_cells_after_horizontal(6, 6, board)
        self.assertEqual(result, ["E"])

    def test_check_cells_after_vertical(self):
        board = Board()
        board.grid[6][6].letter = Tile("T")
        board.grid[6][7].letter = Tile("E")
        result = self.miscellaneos.check_cells_after_vertical(6, 6, board)
        self.assertEqual(result, ["E"])

    def test_check_cells_before(self):
        board = Board()
        board.grid[6][6].letter = Tile("T")
        board.grid[5][6].letter = Tile("E")
        result, location, orientation = self.miscellaneos.check_cells_before(6, 6, "H", board)
        self.assertEqual(result, ["E"])
        self.assertEqual(location, [(5, 6)])
        self.assertEqual(orientation, ["V"])

    def test_check_cells_after(self):
        board = Board()
        board.grid[6][6].letter = Tile("T")
        board.grid[7][6].letter = Tile("E")
        result = self.miscellaneos.check_cells_after(6, 6, "H", board)
        self.assertEqual(result, ["E"])

if __name__ == "__main__":
    unittest.main()