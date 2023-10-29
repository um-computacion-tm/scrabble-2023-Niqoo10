import unittest
from colorama import Fore, Style
from Game.tools import Tools
from Game.cell import Cell

class TestTools(unittest.TestCase):
    def setUp(self):
        self.tools = Tools()

    def test_move_pointer_horizontal(self):
        # Caso de prueba positivo
        row, column = self.tools.move_pointer("H", 0, 0)
        self.assertEqual((row, column), (0, 1))

        # Caso de prueba negativo
        row, column = self.tools.move_pointer("H", 0, 0)
        self.assertNotEqual((row, column), (1, 0))

    def test_move_pointer_vertical(self):
        # Caso de prueba positivo
        row, column = self.tools.move_pointer("V", 0, 0)
        self.assertEqual((row, column), (1, 0))

        # Caso de prueba negativo
        row, column = self.tools.move_pointer("V", 0, 0)
        self.assertNotEqual((row, column), (0, 1))

    def test_is_active_and_letter_multiplier(self):
        # Caso de prueba positivo
        cell = Cell(status='active', multiplier_type='letter')
        result = self.tools.is_active_and_letter_multiplier(cell)
        self.assertTrue(result)

        # Caso de prueba negativo
        cell = Cell(status='inactive', multiplier_type='letter')
        result = self.tools.is_active_and_letter_multiplier(cell)
        self.assertFalse(result)

    def test_is_active_and_word_multiplier(self):
        # Caso de prueba positivo
        cell = Cell(status='active', multiplier_type='word')
        result = self.tools.is_active_and_word_multiplier(cell)
        self.assertTrue(result)

        # Caso de prueba negativo
        cell = Cell(status='inactive', multiplier_type='word')
        result = self.tools.is_active_and_word_multiplier(cell)
        self.assertFalse(result)

    def test_format_placed_word_cell(self):
        # Caso de prueba positivo
        cell = Cell(letter=Letter('A'))
        result = self.tools.format_placed_word_cell(cell)
        self.assertEqual(result, ' A ')

        # Caso de prueba negativo
        cell = Cell(letter=Letter('B'))
        result = self.tools.format_placed_word_cell(cell)
        self.assertNotEqual(result, ' C ')

    def test_format_active_cell(self):
        # Caso de prueba positivo
        cell = Cell(status='active')
        result = self.tools.format_active_cell(cell)
        self.assertIsNotNone(result)

        # Caso de prueba negativo
        cell = Cell(status='inactive')
        result = self.tools.format_active_cell(cell)
        self.assertIsNone(result)

    def test_format_cell_contents(self):
        # Caso de prueba positivo
        cell = Cell(letter=None, multiplier=2, multiplier_type='word')
        result = self.tools.format_cell_contents(cell)
        self.assertEqual(result, f"{Fore.LIGHTMAGENTA_EX}2W{Style.RESET_ALL} ")

        # Caso de prueba negativo
        cell = Cell(letter=None, multiplier=3, multiplier_type='letter')
        result = self.tools.format_cell_contents(cell)
        self.assertNotEqual(result, " - ")

    def test_format_multiplier(self):
        # Caso de prueba positivo
        result = self.tools.format_multiplier(2, 'word')
        self.assertEqual(result, f"{Fore.LIGHTMAGENTA_EX}2W{Style.RESET_ALL} ")

        # Caso de prueba negativo
        result = self.tools.format_multiplier(3, 'letter')
        self.assertNotEqual(result, "3L")

    def test_filter_repeated_column(self):
        # Caso de prueba positivo
        list_tuples = [(0, 0), (1, 0), (2, 1), (3, 1)]
        result = self.tools.filter_repeated_column(list_tuples)
        self.assertEqual(result, [(0, 0), (2, 1)])

        # Caso de prueba negativo
        list_tuples = [(0, 0), (1, 0), (2, 1), (3, 1)]
        result = self.tools.filter_repeated_column(list_tuples)
        self.assertNotEqual(result, [(0, 0), (1, 0), (2, 1), (3, 1)])

    def test_filter_repeated_row(self):
        # Caso de prueba positivo
        list_tuples = [(0, 0), (0, 1), (1, 2), (1, 3)]
        result = self.tools.filter_repeated_row(list_tuples)
        self.assertEqual(result, [(0, 0), (1, 2)])

        # Caso de prueba negativo
        list_tuples = [(0, 0), (0, 1), (1, 2), (1, 3)]
        result = self.tools.filter_repeated_row(list_tuples)
        self.assertNotEqual(result, [(0, 0), (0, 1), (1, 2), (1, 3)])

if __name__ == '__main__':
    unittest.main()


'''import unittest
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
        expected_result = "\x1b[95m2W\x1b[0m "  # Es lightmagenta
        #El \x1b[0m es para que las demas string sigan con el mismo color
        result = tool.format_multiplier(multiplier, multiplier_type)
        self.assertEqual(result, expected_result)

    def test_format_multiplier_letter_3(self):
        tool = Tools()
        multiplier = 3
        multiplier_type = 'letter'
        expected_result = "\x1b[34m3L\x1b[0m "  # Es azul
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
        self.assertEqual(list, [(7,7)])'''
