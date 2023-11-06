import unittest
from Game.cell import Cell
from Game.tile import Tile
from Game.tools import Tools

class TestCell(unittest.TestCase):
    def test_cell(self):
        cell = Cell(multiplier=2, multiplier_type='letter')
        self.assertEqual(cell.multiplier,2)
        self.assertEqual(cell.multiplier_type,'letter')
        self.assertEqual(cell.letter, None)
    
    def test_add_letter(self):
        cell = Cell(multiplier=1, multiplier_type='letter')
        letter = Tile(letter='p', value=3)
        cell.add_letter(letter=letter)
        self.assertEqual(cell.letter, letter)
    
    def test_cell_value(self):
        cell = Cell(multiplier=1, multiplier_type='letter')
        letter = Tile(letter='p', value=3)
        cell.add_letter(letter=letter)
        self.assertEqual(cell.calculate_value(), 3)
    
    def test_cell_multiplayer_letter(self):
        cell = Cell(multiplier=2, multiplier_type='word')
        letter = Tile(letter='p', value=3)
        cell.add_letter(letter=letter)

    def test_cell_multiplayer_word(self):
        cell = Cell(multiplier=2, multiplier_type='word')
        letter = Tile(letter='p', value=3)
        cell.add_letter(letter=letter)
        self.assertEqual(cell.calculate_value(),3,)

    def test_cell_letter(self):
        cell = Cell(1, None)
        self.assertEqual(cell.calculate_value(),0)
    
    def test_deactive(self):
        cell = Cell()
        self.assertEqual(cell.status, "active")
        cell.deactive_cell()
        self.assertEqual(cell.status, "desactive")
    
    def test_reset_cell(self):
        cell = Cell(3, 'word')
        cell.multiplier = 1
        cell.multiplier_type = ''
        cell.status = 'desactive'
        cell.letter = Tile('H',1)
        cell.reset_cell()
        self.assertEqual(cell.multiplier, 3)
        self.assertEqual(cell.multiplier_type, 'word')
        self.assertEqual(cell.status, 'active')
        self.assertEqual(cell.letter, None)
    
    def test_repr_active(self):
        cell = Cell(2, "word")
        tool = Tools()
        self.assertEqual(repr(cell), tool.format_active_cell(cell))
    
    def test_repr_deactive(self):
        cell = Cell(2, "word", status="desactive")
        tool = Tools()
        self.assertEqual(repr(cell), tool.format_cell_contents(cell))
if __name__ == '__main__':
    unittest.main()