# test_models.py

import unittest
from Game.models import Converter, Miscellaneos
from Game.board import Board
from Game.cell import Cell
from Game.tile import Tile

class TestMiscellaneos(unittest.TestCase):    
    def test_calculate_word_value_simple(self):
        misc = Miscellaneos()
        word = [
            Cell(letter=Tile('C',1)),
            Cell(letter=Tile('A',1)),
            Cell(letter=Tile('S',2)),
            Cell(letter=Tile('A',1))
        ]
        value = misc.calculate_word_value(word)
        self.assertEqual(value,5)

    def test_calculate_word_value_with_letter_multiplier(self):
        misc = Miscellaneos()
        word = [
            Cell(letter=Tile('C',1)),
            Cell(letter=Tile('A',1)),
            Cell(letter=Tile('S',2), multiplier=2, multiplier_type='letter'),
            Cell(letter=Tile('A',1))
        ]
        value = misc.calculate_word_value(word)
        self.assertEqual(value,7)
    def test_calculate_word_value_with_word_multiplier(self):
        misc = Miscellaneos()
        word = [
            Cell(letter=Tile('C',1)),
            Cell(letter=Tile('A',1)),
            Cell(letter=Tile('S',2), multiplier=2, multiplier_type='word'),
            Cell(letter=Tile('A',1))
        ]
        value = misc.calculate_word_value(word)
        self.assertEqual(value,10)
    def test_calculate_word_value_with_word_and_letter_multiplier(self):
        misc = Miscellaneos()
        word = [
            Cell(letter=Tile('C',1), multiplier=3, multiplier_type='letter'),
            Cell(letter=Tile('A',1)),
            Cell(letter=Tile('S',2), multiplier=2, multiplier_type='word'),
            Cell(letter=Tile('A',1))
        ]
        value = misc.calculate_word_value(word)
        self.assertEqual(value,14)
        
    def test_calculate_word_value_with_word_and_letter_multiplier_no_active(self):
        misc = Miscellaneos()
        word = [
            Cell(letter=Tile('C',1), multiplier=3, multiplier_type='letter', status='desactive'),
            Cell(letter=Tile('A',1)),
            Cell(letter=Tile('S',2), multiplier=2, multiplier_type='word', status='desactive'),
            Cell(letter=Tile('A',1))
        ]
        value = misc.calculate_word_value(word)
        self.assertEqual(value,5)
      
    def test_get_tiles_for_word_placement(self):
        board = Board()
        misc = Miscellaneos()
        word = "Facu"
        location = (4, 7)
        orientation = "H"
        board.grid[4][8] = Cell(letter=Tile('A',1))
        board.grid[4][10] = Cell(letter=Tile('U',1))
        list_tiles = misc.get_tiles_for_word_placement(word,location, orientation, board)
        self.assertEqual(len(list_tiles), 2)
        self.assertEqual(list_tiles[0].letter, 'A')
        self.assertEqual(list_tiles[1].letter, 'U')

    def test_get_tiles_for_word_placement_another_word_in_board(self):
        board = Board()
        misc = Miscellaneos()
        word = "hola"
        location = (6, 8)
        orientation = "V"
        board.put_words_board('hola', (7,7), 'H')
        list_tiles = misc.get_tiles_for_word_placement(word,location, orientation, board)
        self.assertEqual(len(list_tiles), 1)
        self.assertEqual(list_tiles[0].letter, 'O')

    def test_tiles_needed_to_form_word(self):
        board = Board()
        misc = Miscellaneos()
        word = "Facu"
        location = (4, 7)
        orientation = "H"
        board.grid[4][8] = Cell(letter=Tile('A',1))
        board.grid[4][10] = Cell(letter=Tile('U',1))
        list_tiles = misc.tiles_needed_to_form_word(word,location, orientation, board)
        self.assertEqual(len(list_tiles), 2)
        self.assertEqual(list_tiles[0].letter, 'F')
        self.assertEqual(list_tiles[1].letter, 'C')
    
    def test_get_cell_around_word_horizontal(self):
        misc = Miscellaneos()
        word = "AB"
        location = (7,7)
        list = []
        misc.get_cell_around_word_horizontal(word,location,list)
        self.assertEqual(len(list), 6)
        self.assertEqual(list[0], (7,6))
        self.assertEqual(list[1], (7,9))
        self.assertEqual(list[2], (6,7))
        self.assertEqual(list[3], (8,7))
        self.assertEqual(list[4], (6,8))
        self.assertEqual(list[5], (8,8))

    
    def test_get_cell_around_word_vertical(self):
        misc = Miscellaneos()
        word = "AB"
        location = (7,7)
        list = []
        misc.get_cell_around_word_vertical(word,location,list)
        self.assertEqual(len(list), 6)
        self.assertEqual(list[0], (6,7))
        self.assertEqual(list[1], (9,7))
        self.assertEqual(list[2], (7,6))
        self.assertEqual(list[3], (7,8))
        self.assertEqual(list[4], (8,6))
        self.assertEqual(list[5], (8,8))
    
    def test_verify_cell_around_word_false(self):
        misc = Miscellaneos()
        board = Board()
        list_cell = [(6,7), (9,7), (7,6), (7,8), (8,6), (8,8)]
        list_tiles = []
        self.assertEqual(misc.verify_cell_around_word(list_cell, list_tiles, board), False)
        self.assertEqual(len(list_tiles), 0)
    
    def test_verify_cell_around_word_true(self):
        misc = Miscellaneos()
        board = Board()
        board.grid[9][7] = Cell(letter=Tile('A',1))
        board.grid[7][8] = Cell(letter=Tile('B',1))
        list_cell = [(6,7), (9,7), (7,6), (7,8), (8,6), (8,8)]
        list_tiles = []
        self.assertEqual(misc.verify_cell_around_word(list_cell, list_tiles, board), True)
        self.assertEqual(len(list_tiles), 2)
        self.assertEqual(list_tiles[0], (9,7))
        self.assertEqual(list_tiles[1], (7,8))

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