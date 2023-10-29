# test_cell.py

import unittest
from Game.tile import Tile
from Game.cell import Cell

class CellTestCase(unittest.TestCase):
    def setUp(self):
        self.cell = Cell()
    
    def test_add_letter_positive(self):
        # Prueba positiva: agregar una letra a la celda
        letter = Tile('A', 1)
        self.cell.add_letter(letter)
        self.assertEqual(self.cell.letter, letter)
    
    def test_add_letter_negative(self):
        # Prueba negativa: agregar una letra inválida a la celda
        letter = 'A'
        self.assertRaises(TypeError, self.cell.add_letter, letter)
    
    def test_calculate_value_no_letter(self):
        # Prueba: calcular el valor de la celda sin una letra
        self.assertEqual(self.cell.calculate_value(), 0)
    
    def test_calculate_value_letter_multiplier(self):
        # Prueba: calcular el valor de la celda con un multiplicador de letra
        letter = Tile('A', 1)
        self.cell.add_letter(letter)
        self.cell.multiplier_type = 'letter'
        self.cell.multiplier = 2
        self.assertEqual(self.cell.calculate_value(), 2)
    
    def test_calculate_value_word_multiplier(self):
        # Prueba: calcular el valor de la celda con un multiplicador de palabra
        letter = Tile('A', 1)
        self.cell.add_letter(letter)
        self.cell.multiplier_type = 'word'
        self.cell.multiplier = 3
        self.assertEqual(self.cell.calculate_value(), 1)
    
    def test_deactivate_cell(self):
        # Prueba: desactivar la celda
        self.cell.deactivate_cell()
        self.assertEqual(self.cell.status, 'inactive')
    
    def test_reset_cell(self):
        # Prueba: restablecer la celda a su estado original
        letter = Tile('A', 1)
        self.cell.add_letter(letter)
        self.cell.deactivate_cell()
        self.cell.multiplier_type = 'word'
        self.cell.multiplier = 2
        self.cell.reset_cell()
        self.assertEqual(self.cell.letter, None)
        self.assertEqual(self.cell.status, 'active')
        self.assertEqual(self.cell.multiplier_type, '')
        self.assertEqual(self.cell.multiplier, 1)
    
    def test_repr_active_cell(self):
        # Prueba: representación de la celda cuando está activa
        letter = Tile('A', 1)
        self.cell.add_letter(letter)
        self.assertEqual(repr(self.cell), '[A]')
    
    def test_repr_inactive_cell(self):
        # Prueba: representación de la celda cuando está inactiva
        self.cell.deactivate_cell()
        self.assertEqual(repr(self.cell), '[ ]')

if __name__ == '__main__':
    unittest.main()

'''import unittest
from Game.cell import Cell
from Game.tile import Tile
from Game.models import Tools

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
    unittest.main()'''