# test_tools.py

import unittest
from Game.tools import Tools
from Game.cell import Cell
from Game.tile import Tile

class TestTools(unittest.TestCase):
    def test_format_cell_content(self):
        tool = Tools()
        cell = Cell(letter=Tile("A",1))
        self.assertEqual(tool.format_cell_contents(cell).strip(), "A")
    
    def test_format_multiplier_word_2(self):
        tool = Tools()
        multiplier = 2
        multiplier_type = 'word'
        expected_result = "\x1b[95m2W\x1b[0m "
        result = tool.format_multiplier(multiplier, multiplier_type)
        self.assertEqual(result, expected_result)

    def test_format_multiplier_letter_3(self):
        tool = Tools()
        multiplier = 3
        multiplier_type = 'letter'
        expected_result = "\x1b[34m3L\x1b[0m "
        result = tool.format_multiplier(multiplier, multiplier_type)
        self.assertEqual(result, expected_result)

    def test_filter_reapeated_colums(self):
        tool = Tools()
        list = [(7,7), (9,7)]
        list = tool.filter_reapeted_column(list)
        self.assertEqual(list, [(7,7)])

    def test_filter_reapeated_rows(self):
        tool = Tools()
        list = [(7,7), (7,9)]
        list = tool.filter_reapeted_row(list)
        self.assertEqual(list, [(7,7)])
