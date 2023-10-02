import unittest
from Game.cell import Cell
from Game.tile import Tile


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