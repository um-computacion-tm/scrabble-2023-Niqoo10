# test_models.py

import unittest
from Game.models import Miscellaneos
from Game.cell import Cell
from Game.tile import Tile
from Game.board import Board

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