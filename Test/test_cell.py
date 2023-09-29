import unittest
from Game.cell import Cell, Calculate_value
from Game.tile import Tile
from Game.player import Player


'''class CellTestCase(unittest.TestCase):
    def setUp(self):
        self.cell = Cell()
    
    def test_add_letter(self):
        tile = Tile('A', 1)
        self.assertTrue(self.cell.add_letter(tile))
        self.assertEqual(self.cell.letter, tile)
        
    def test_remove_letter(self):
        tile = Tile('A', 1)
        self.cell.add_letter(tile)
        removed_letter = self.cell.remove_letter()
        self.assertEqual(removed_letter, tile)
        self.assertIsNone(self.cell.letter)
        
    def test_add_player_starting_position(self):
        player = Player('John')
        self.cell.add_player_starting_position(player)
        self.assertTrue(self.cell.is_starting_position)
        self.assertEqual(self.cell.player_starting_position, player)
        
    def test_is_empty(self):
        self.assertTrue(self.cell.is_empty())
        tile = Tile('A', 1)
        self.cell.add_letter(tile)
        self.assertFalse(self.cell.is_empty())
        
    def test_has_letter(self):
        tile = Tile('A', 1)
        self.assertFalse(self.cell.has_letter('A'))
        self.cell.add_letter(tile)
        self.assertTrue(self.cell.has_letter('A'))
        
    def test_apply_word_multiplier(self):
        self.cell.multiplier_type = 'word'
        self.cell.apply_word_multiplier(2)
        self.assertEqual(self.cell.multiplier, 2)
        
    def test_apply_letter_multiplier(self):
        self.cell.multiplier_type = 'letter'
        self.cell.apply_letter_multiplier(3)
        self.assertEqual(self.cell.multiplier, 3)
        
    def test_calculate_value(self):
        self.assertEqual(self.cell.calculate_value(), 0)
        tile = Tile('A', 1)
        self.cell.add_letter(tile)
        self.assertEqual(self.cell.calculate_value(), 1)
        self.cell.multiplier_type = 'letter'
        self.cell.multiplier = 2
        self.assertEqual(self.cell.calculate_value(), 2)
        
class CalculateValueTestCase(unittest.TestCase):
    def test_calculate_word_value(self):
        cell1 = Cell(1, 'word', None, True, 2)
        cell2 = Cell(1, 'letter', Tile('A', 1), True, 0)
        cell3 = Cell(2, 'letter', Tile('B', 2), True, 0)
        cells = [cell1, cell2, cell3]
        self.assertEqual(Calculate_value.calculate_word_value(cells), 5)
        
    def test_calculate_cell_value(self):
        cell1 = Cell(1, 'word', None, True, 2)
        cell2 = Cell(1, 'letter', Tile('A', 1), True, 0)
        cell3 = Cell(2, 'letter', Tile('B', 2), True, 0)
        self.assertEqual(Calculate_value.calculate_cell_value(cell1), 0)
        self.assertEqual(Calculate_value.calculate_cell_value(cell2), 1)
        self.assertEqual(Calculate_value.calculate_cell_value(cell3), 4)
        
    def test_calculate_word_multiplier(self):
        cell1 = Cell(1, 'word', None, True, 2)
        cell2 = Cell(1, 'letter', Tile('A', 1), True, 0)
        cell3 = Cell(2, 'letter', Tile('B', 2), True, 0)
        self.assertEqual(Calculate_value.calculate_word_multiplier(cell1), 1)
        self.assertEqual(Calculate_value.calculate_word_multiplier(cell2), 1)
        self.assertEqual(Calculate_value.calculate_word_multiplier(cell3), 1)
        
if __name__ == '__main__':
    unittest.main()'''

class TestCell(unittest.TestCase):
    def test_init(self):
        cell = Cell(multiplier=2, multiplier_type=True)
        self.assertEqual(cell.multiplier,2)
        self.assertEqual(cell.multiplier_type,True)
        self.assertEqual(cell.active, True)
        self.assertIsNone(cell.letter)
        self.assertEqual(cell.calculate_value(),0)

    def test_add_letter(self):
        cell = Cell(multiplier=1, multiplier_type=False)
        letter = Tile(letter='P', value=3)
        cell.add_letter(letter=letter)
        self.assertEqual(cell.letter, letter)

if __name__ == '__main__':
    unittest.main()