import unittest
from Game.bagtiles import BagTiles
from Game.tools import Tools
from Game.cell import Cell
from Game.converter import Converter

class ConverterTestCase(unittest.TestCase):
    def setUp(self):
        self.converter = Converter()
        self.bag = BagTiles()
        self.tools = Tools()

    def test_string_to_tiles_positive(self):
        tile_list = []
        input_string = "HELLO"
        expected_tiles = [self.bag.tiles[7], self.bag.tiles[4], self.bag.tiles[11], self.bag.tiles[11], self.bag.tiles[14]]
        self.converter.string_to_tiles(input_string, tile_list)
        self.assertEqual(tile_list, expected_tiles)

    def test_string_to_tiles_negative(self):
        tile_list = []
        input_string = "WORLD"
        unexpected_tiles = [self.bag.tiles[7], self.bag.tiles[4], self.bag.tiles[11], self.bag.tiles[11], self.bag.tiles[14]]
        self.converter.string_to_tiles(input_string, tile_list)
        self.assertNotEqual(tile_list, unexpected_tiles)

    def test_especial_to_tiles_positive(self):
        tile_list = []
        input_string = "CH"
        expected_tiles = [self.bag.tiles[26]]
        self.converter.especial_to_tiles(input_string, tile_list)
        self.assertEqual(tile_list, expected_tiles)

    def test_especial_to_tiles_negative(self):
        tile_list = []
        input_string = "RR"
        unexpected_tiles = [self.bag.tiles[26]]
        self.converter.especial_to_tiles(input_string, tile_list)
        self.assertNotEqual(tile_list, unexpected_tiles)

    def test_word_to_tiles(self):
        word = "HELLO"
        expected_tiles = [self.bag.tiles[7], self.bag.tiles[4], self.bag.tiles[11], self.bag.tiles[11], self.bag.tiles[14]]
        tiles_list = self.converter.word_to_tiles(word)
        self.assertEqual(tiles_list, expected_tiles)

    def test_locations_to_positions(self):
        word = "HELLO"
        location = (2, 3)
        orientation = "horizontal"
        expected_positions = [(2, 3), (2, 4), (2, 5), (2, 6), (2, 7)]
        positions = self.converter.locations_to_positions(word, location, orientation)
        self.assertEqual(positions, expected_positions)

    def test_word_to_cells(self):
        word = "HELLO"
        location = (2, 3)
        orientation = "horizontal"
        board = self.tools.create_empty_board()
        expected_cells = [
            Cell(1, 'H', self.bag.tiles[7]),
            Cell(1, 'E', self.bag.tiles[4]),
            Cell(1, 'L', self.bag.tiles[11]),
            Cell(1, 'L', self.bag.tiles[11]),
            Cell(1, 'O', self.bag.tiles[14])
        ]
        cells = self.converter.word_to_cells(word, location, orientation, board)
        self.assertEqual(cells, expected_cells)

    def test_word_to_false_cells(self):
        word = "HELLO"
        expected_false_cells = [
            Cell(1, '', self.bag.tiles[7]),
            Cell(1, '', self.bag.tiles[4]),
            Cell(1, '', self.bag.tiles[11]),
            Cell(1, '', self.bag.tiles[11]),
            Cell(1, '', self.bag.tiles[14])
        ]
        false_cells = self.converter.word_to_false_cells(word)
        self.assertEqual(false_cells, expected_false_cells)

    def test_result_to_list_of_words(self):
        result = [('HELLO', 10), ('WORLD', 15)]
        expected_words = ['HELLO', 'WORLD']
        words = self.converter.result_to_list_of_words(result)
        self.assertEqual(words, expected_words)

if __name__ == '__main__':
    unittest.main()