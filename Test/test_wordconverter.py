# test_converter.py

import unittest
from Game.wordconverter import Converter
from Game.board import Board

class TestConverter(unittest.TestCase):
    def test_word_to_tiles_simple_hola(self):
        conv = Converter()
        list_tiles = conv.word_to_tiles("hola")
        self.assertEqual(list_tiles[0].letter, "H")
        self.assertEqual(list_tiles[0].value, 4)
        self.assertEqual(list_tiles[1].letter, "O")
        self.assertEqual(list_tiles[1].value, 1)
        self.assertEqual(list_tiles[2].letter, "L")
        self.assertEqual(list_tiles[2].value, 1)
        self.assertEqual(list_tiles[3].letter, "A")
        self.assertEqual(list_tiles[3].value, 1)

    def test_word_to_tiles_simple_facultad(self):
        conv = Converter()
        list_tiles = conv.word_to_tiles("facultad")
        self.assertEqual(list_tiles[0].letter, "F")
        self.assertEqual(list_tiles[0].value, 4)
        self.assertEqual(list_tiles[1].letter, "A")
        self.assertEqual(list_tiles[1].value, 1)
        self.assertEqual(list_tiles[2].letter, "C")
        self.assertEqual(list_tiles[2].value, 2)
        self.assertEqual(list_tiles[3].letter, "U")
        self.assertEqual(list_tiles[3].value, 1)
        self.assertEqual(list_tiles[4].letter, "L")
        self.assertEqual(list_tiles[4].value, 1)
        self.assertEqual(list_tiles[5].letter, "T")
        self.assertEqual(list_tiles[5].value, 1)
        self.assertEqual(list_tiles[6].letter, "A")
        self.assertEqual(list_tiles[6].value, 1)
        self.assertEqual(list_tiles[7].letter, "D")
        self.assertEqual(list_tiles[7].value, 2)

    def test_word_to_tiles_simple_casa(self):
        conv = Converter()
        list_tiles = conv.word_to_tiles("casa")
        self.assertEqual(list_tiles[0].letter, "C")
        self.assertEqual(list_tiles[0].value, 2)
        self.assertEqual(list_tiles[1].letter, "A")
        self.assertEqual(list_tiles[1].value, 1)
        self.assertEqual(list_tiles[2].letter, "S")
        self.assertEqual(list_tiles[2].value, 1)
        self.assertEqual(list_tiles[3].letter, "A")
        self.assertEqual(list_tiles[3].value, 1)

    def test_word_to_tiles_complex_CH(self):
        conv = Converter()
        list_tiles = conv.word_to_tiles("chita")
        self.assertEqual(list_tiles[0].letter, "CH")
        self.assertEqual(list_tiles[0].value, 5)
        self.assertEqual(list_tiles[1].letter, "I")
        self.assertEqual(list_tiles[1].value, 1)
        self.assertEqual(list_tiles[2].letter, "T")
        self.assertEqual(list_tiles[2].value, 1)
        self.assertEqual(list_tiles[3].letter, "A")
        self.assertEqual(list_tiles[3].value, 1)

    def test_word_to_tiles_complex_RR(self):
        conv = Converter()
        list_tiles = conv.word_to_tiles("perro")
        self.assertEqual(list_tiles[0].letter, "P")
        self.assertEqual(list_tiles[0].value, 2)
        self.assertEqual(list_tiles[1].letter, "E")
        self.assertEqual(list_tiles[1].value, 1)
        self.assertEqual(list_tiles[2].letter, "RR")
        self.assertEqual(list_tiles[2].value, 8)
        self.assertEqual(list_tiles[3].letter, "O")
        self.assertEqual(list_tiles[3].value, 1)

    def test_word_to_tilescomplex_LL(self):
        conv = Converter()
        list_tiles = conv.word_to_tiles("llanto")
        self.assertEqual(list_tiles[0].letter, "LL")
        self.assertEqual(list_tiles[0].value, 8)
        self.assertEqual(list_tiles[1].letter, "A")
        self.assertEqual(list_tiles[1].value, 1)
        self.assertEqual(list_tiles[2].letter, "N")
        self.assertEqual(list_tiles[2].value, 1)
        self.assertEqual(list_tiles[3].letter, "T")
        self.assertEqual(list_tiles[3].value, 1)
        self.assertEqual(list_tiles[4].letter, "O")
        self.assertEqual(list_tiles[4].value, 1)
    
    def test_word_to_cells(self):
        conv = Converter()
        board = Board()
        word = 'llanto'
        location = (7,7)
        orientation = 'H'
        list_cell = conv.word_to_cells(word, location, orientation, board)
        self.assertEqual(list_cell[0].letter.letter, 'LL')
        self.assertEqual(list_cell[0].multiplier_type, 'word')
        self.assertEqual(list_cell[1].letter.letter, 'A')
        self.assertEqual(list_cell[2].letter.letter, 'N')
        self.assertEqual(list_cell[3].letter.letter, 'T')
        self.assertEqual(list_cell[4].letter.letter, 'O')

    def test_locations_to_positions_vertical(self):
        conv = Converter()
        word = "Facu"
        location = (4, 7)
        orientation = "V"
        result = conv.locations_to_positions(word,location, orientation)
        self.assertEqual(result, [(4,7), (5,7),(6,7),(7,7)])

    def test_locations_to_positions_horizontal(self):
        conv = Converter()
        word = "Facu"
        location = (4, 7)
        orientation = "H"
        result = conv.locations_to_positions(word,location, orientation)
        self.assertEqual(result, [(4,7), (4,8),(4,9),(4,10)])