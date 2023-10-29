# test_board.py

import unittest
from Game.cell import Cell
from Game.board import Board

class TestBoard(unittest.TestCase):

    def test_put_multipliers(self):
        board = Board()
        cell1 = board.put_multipliers("3W")
        cell2 = board.put_multipliers("2L")
        cell3 = board.put_multipliers(None)

        self.assertEqual(cell1.multiplier, 3)
        self.assertEqual(cell1.multiplier_type, "word")
        self.assertEqual(cell2.multiplier, 2)
        self.assertEqual(cell2.multiplier_type, "letter")
        self.assertIsInstance(cell3, Cell)

    def test_put_words_board(self):
        board = Board()
        board.put_words_board("WORD", (7, 7), "H")

        self.assertEqual(board.grid[7][7].letter, "W")
        self.assertEqual(board.grid[7][8].letter, "O")
        self.assertEqual(board.grid[7][9].letter, "R")
        self.assertEqual(board.grid[7][10].letter, "D")

    def test_validate_word_inside_board(self):
        board = Board()
        result1 = board.validate_word_inside_board("WORD", (0, 0), "H")
        result2 = board.validate_word_inside_board("LONGWORD", (0, 10), "H")
        result3 = board.validate_word_inside_board("WORD", (0, 0), "V")
        result4 = board.validate_word_inside_board("LONGWORD", (10, 0), "V")

        self.assertTrue(result1)
        self.assertFalse(result2)
        self.assertTrue(result3)
        self.assertFalse(result4)

    def test_is_empty(self):
        board = Board()
        empty_result = board.is_empty()
        board.grid[7][7].letter = "A"
        non_empty_result = board.is_empty()

        self.assertTrue(empty_result)
        self.assertFalse(non_empty_result)

    def test_word_in_the_center(self):
        board = Board()
        result1 = board.word_in_the_center("WORD", (7, 7), "H")
        result2 = board.word_in_the_center("WORD", (7, 7), "V")
        result3 = board.word_in_the_center("WORD", (0, 0), "H")
        result4 = board.word_in_the_center("WORD", (0, 0), "V")

        self.assertTrue(result1)
        self.assertTrue(result2)
        self.assertFalse(result3)
        self.assertFalse(result4)

    def test_check_right_letters(self):
        board = Board()
        tile1 = Cell(letter="W")
        tile2 = Cell(letter="O")
        tile3 = Cell(letter="R")
        letter1 = "W"
        letter2 = "O"
        letter3 = "R"
        found_problem = []
        found_coincidences = []

        board.check_right_letters(tile1, letter1, [found_problem, found_coincidences])
        board.check_right_letters(tile2, letter2, [found_problem, found_coincidences])
        board.check_right_letters(tile3, letter3, [found_problem, found_coincidences])

        self.assertEqual(found_coincidences, ["W", "O", "R"])
        self.assertEqual(found_problem, [])

    def test_check_conditions(self):
        board = Board()
        result1 = board.check_conditions([[], []])
        result2 = board.check_conditions([[], ["A"]])
        result3 = board.check_conditions([[], []])

        self.assertTrue(result1)
        self.assertFalse(result2)
        self.assertTrue(result3)

    def test_validate_word_horizontal(self):
        board = Board()
        board.grid[7][7].letter = "W"
        board.grid[7][8].letter = "O"
        board.grid[7][9].letter = "R"
        board.grid[7][10].letter = "D"
        result1 = board.validate_word_horizontal("WORD", (7, 7))
        result2 = board.validate_word_horizontal("LONGWORD", (7, 7))
        result3 = board.validate_word_horizontal("WORD", (0, 0))

        self.assertTrue(result1)
        self.assertFalse(result2)
        self.assertTrue(result3)

    def test_validate_word_vertical(self):
        board = Board()
        board.grid[7][7].letter = "W"
        board.grid[8][7].letter = "O"
        board.grid[9][7].letter = "R"
        board.grid[10][7].letter = "D"
        result1 = board.validate_word_vertical("WORD", (7, 7))
        result2 = board.validate_word_vertical("LONGWORD", (7, 7))
        result3 = board.validate_word_vertical("WORD", (0, 0))

        self.assertTrue(result1)
        self.assertFalse(result2)
        self.assertTrue(result3)

    def test_validate_word_place_board(self):
        board = Board()
        result1 = board.validate_word_place_board("WORD", (7, 7), "H")
        result2 = board.validate_word_place_board("LONGWORD", (7, 7), "H")
        result3 = board.validate_word_place_board("WORD", (0, 0), "H")
        result4 = board.validate_word_place_board("WORD", (7, 7), "V")
        result5 = board.validate_word_place_board("LONGWORD", (7, 7), "V")
        result6 = board.validate_word_place_board("WORD", (0, 0), "V")

        self.assertTrue(result1)
        self.assertFalse(result2)
        self.assertTrue(result3)
        self.assertTrue(result4)
        self.assertFalse(result5)
        self.assertTrue(result6)

    def test_get_cell_around_word(self):
        board = Board()
        word = "WORD"
        location = (7, 7)
        orientation = "H"
        adjacent_cells = []
        expected_result = [
            board.grid[6][7],  # Cell above the word
            board.grid[8][7]   # Cell below the word
        ]

        board.get_cell_around_word(word, location, orientation, adjacent_cells)

        self.assertEqual(adjacent_cells, expected_result)

    def test_get_tiles_around_word(self):
        board = Board()
        orientation = "H"
        adjacent_tiles = [
            Cell(letter="A"),
            Cell(letter="B"),
            Cell(letter="C")
        ]
        expected_result = [
            Cell(letter="A"),
            Cell(letter="B"),
            Cell(letter="C")
        ]

        result = board.get_tiles_around_word(orientation, adjacent_tiles, board)

        self.assertEqual(result, expected_result)

    def test_get_validation_of_another_board(self):
        board = Board()
        word_in_validation = ("WORD", (7, 7), "H")
        other_words = [
            ("HELLO", (7, 6), "H"),
            ("WORLD", (7, 8), "H")
        ]
        expected_result = "HELLO"

        result = board.get_validation_of_another_board(word_in_validation, other_words)

        self.assertEqual(result, expected_result)

    def test_validate_words_around(self):
        board = Board()
        word = "WORD"
        location = (7, 7)
        orientation = "H"
        residual_words = []
        expected_result = True

        result = board.validate_words_around(word, location, orientation, residual_words)

        self.assertEqual(result, expected_result)
        self.assertIn("HELLO", residual_words)
        self.assertNotIn("WORLD", residual_words)

if __name__ == '__main__':
    unittest.main()

'''import unittest
from Game.board import Board
from Game.cell import Cell
from Game.tile import Tile

class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    def test_board(self):
        self.assertEqual(len(self.board.grid), 15)
        self.assertEqual(len(self.board.grid[0]), 15)

    def test_board_multiplier_word_in_board(self):
        # Triple Word
        multipliers = [(0, 0), (7, 0), (14, 0), (0, 7), (0, 14), (14, 0), (14, 7), (14, 14)]
        for multiplier in multipliers:
            self.assertEqual(self.board.grid[multiplier[0]][multiplier[1]].multiplier, 3)
        
        # Double Word
        multipliers = [(1, 1), (2, 2), (3, 3), (4, 4), (13, 1), (12, 2), (11, 3), (10, 4), (1, 13), (2, 12), (3, 11), (4, 10), (13, 13), (12, 12), (11, 11), (10, 10), (7, 7)]
        for multiplier in multipliers:
            self.assertEqual(self.board.grid[multiplier[0]][multiplier[1]].multiplier, 2)
    
    def test_board_multiplier_letter_in_board(self):
        # Triple letter
        multipliers = [(1, 5), (1, 9), (5, 1), (5, 5), (5, 13), (9, 1), (9, 5), (9, 9), (9, 13), (13, 5), (13, 9)]
        for multiplier in multipliers:
            self.assertEqual(self.board.grid[multiplier[0]][multiplier[1]].multiplier, 3)
        
        # Double letter
        multipliers = [(0, 3), (0, 11), (2, 6), (2, 8), (3, 0), (3, 7), (3, 14), (6, 2), (6, 6), (6, 8), (6, 12), (7, 3), (7, 11), (8, 2), (8, 6), (8, 8), (8, 12), (11, 0), (11, 7), (11, 14), (12, 6), (12, 8), (14, 3), (14, 11)]
        for multiplier in multipliers:
            self.assertEqual(self.board.grid[multiplier[0]][multiplier[1]].multiplier, 2)
    
    def test_word_inside_board_horizontal(self):
        word = "Facultad"
        location = (5, 4)
        orientation = "H"
        word_is_valid = self.board.validate_word_inside_board(word, location, orientation)
        self.assertEqual(word_is_valid, True)
    
    def test_word_inside_board_vertical(self):
        word = "Facultad"
        location = (5, 4)
        orientation = "V"
        word_is_valid = self.board.validate_word_inside_board(word, location, orientation)
        self.assertEqual(word_is_valid, True)
    
    def test_word_out_of_board_horizontal(self):
        word = "Facultad"
        location = (4, 14)
        orientation = "H"
        word_is_valid = self.board.validate_word_inside_board(word, location, orientation)
        self.assertEqual(word_is_valid, False)
    
    def test_word_out_of_board_vertical(self):
        word = "Facultad"
        location = (14, 4)
        orientation = "V"
        word_is_valid = self.board.validate_word_inside_board(word, location, orientation)
        self.assertEqual(word_is_valid, False)
    
    def test_board_is_empty(self):
        self.assertEqual(self.board.is_empty(), True)
    
    def test_board_is_not_empty(self):
        self.board.grid[7][7] = Tile('C', 1)
        self.assertEqual(self.board.is_empty(), False)
    
    def test_place_word_empty_board_horizontal_fine(self):
        word = "Facultad"
        location = (7, 4)
        orientation = "H"
        word_is_valid = self.board.validate_word_place_board(word, location, orientation)
        self.assertEqual(word_is_valid, True)
    
    def test_place_word_empty_board_horizontal_wrong(self):
        word = "Facultad"
        location = (2, 4)
        orientation = "H"
        word_is_valid = self.board.validate_word_place_board(word, location, orientation)
        self.assertEqual(word_is_valid, False)
    
    def test_place_word_empty_board_vertical_fine(self):
        word = "Facultad"
        location = (4, 7)
        orientation = "V"
        word_is_valid = self.board.validate_word_place_board(word, location, orientation)
        self.assertEqual(word_is_valid, True)
    
    def test_place_word_empty_board_vertical_wrong(self):
        word = "Facultad"
        location = (4, 2)
        orientation = "V"
        word_is_valid = self.board.validate_word_place_board(word, location, orientation)
        self.assertEqual(word_is_valid, False)
    
    def test_place_word_no_empty_board_horizontal_fine(self):
        self.board.grid[7][7].add_letter(Tile('C',1))
        self.board.grid[8][7].add_letter(Tile('A',1))
        self.board.grid[9][7].add_letter(Tile('S',1))
        self.board.grid[10][7].add_letter(Tile('A',1))
        word = "Hola"
        location = (8, 4)
        orientation = "H"
        word_is_valid = self.board.validate_word_place_board(word, location, orientation)
        self.assertEqual(word_is_valid, True)
    
    def test_place_word_no_empty_board_horizontal_wrong(self):
        self.board.grid[7][7].add_letter(Tile('C',1))
        self.board.grid[8][7].add_letter(Tile('A',1))
        self.board.grid[9][7].add_letter(Tile('S',1))
        self.board.grid[10][7].add_letter(Tile('A',1))
        word = "Hola"
        location = (8, 5)
        orientation = "H"
        word_is_valid = self.board.validate_word_place_board(word, location, orientation)
        self.assertEqual(word_is_valid, False)
    
    def test_place_word_no_empty_board_vertical_fine(self):
        self.board.grid[7][7].add_letter(Tile('C',1))
        self.board.grid[7][8].add_letter(Tile('A',1))
        self.board.grid[7][9].add_letter(Tile('S',1))
        self.board.grid[7][10].add_letter(Tile('A',1))
        word = "Hola"
        location = (4, 8)
        orientation = "V"
        word_is_valid = self.board.validate_word_place_board(word, location, orientation)
        self.assertEqual(word_is_valid, True)
    
    def test_place_word_no_empty_board_vertical_wrong(self):
        self.board.grid[7][7].add_letter(Tile('C',1))
        self.board.grid[7][8].add_letter(Tile('A',1))
        self.board.grid[7][9].add_letter(Tile('S',1))
        self.board.grid[7][10].add_letter(Tile('A',1))
        word = "Hola"
        location = (5, 8)
        orientation = "V"
        word_is_valid = self.board.validate_word_place_board(word, location, orientation)
        self.assertEqual(word_is_valid, False)
    
    def test_place_word_no_empthy_2_coincidence_horizontal_fine(self):
        self.board.grid[7][7].add_letter(Tile('C',1))
        self.board.grid[8][7].add_letter(Tile('A',1))
        self.board.grid[9][7].add_letter(Tile('S',1))
        self.board.grid[10][7].add_letter(Tile('A',1))
        self.board.grid[7][8].add_letter(Tile('A',1))
        self.board.grid[8][8].add_letter(Tile('L',1))
        self.board.grid[9][8].add_letter(Tile('A',1))
        word = "Foca"
        location = (7,5)
        orientation = "H"
        word_is_valid = self.board.validate_word_place_board(word, location, orientation)
        self.assertEqual(word_is_valid, True)
    
    def test_place_word_no_empthy_2_coincidence_horizontal_wrong(self):
        self.board.grid[7][7].add_letter(Tile('C',1))
        self.board.grid[8][7].add_letter(Tile('A',1))
        self.board.grid[9][7].add_letter(Tile('S',1))
        self.board.grid[10][7].add_letter(Tile('A',1))
        self.board.grid[7][8].add_letter(Tile('M',1))
        self.board.grid[8][8].add_letter(Tile('A',1))
        self.board.grid[9][8].add_letter(Tile('L',1))
        word = "Foca"
        location = (7,5)
        orientation = "H"
        word_is_valid = self.board.validate_word_place_board(word, location, orientation)
        self.assertEqual(word_is_valid, False)
    
    def test_place_word_no_empthy_2_coincidence_vertical_fine(self):
        self.board.grid[7][7].add_letter(Tile('C',1))
        self.board.grid[7][8].add_letter(Tile('A',1))
        self.board.grid[7][9].add_letter(Tile('S',1))
        self.board.grid[7][10].add_letter(Tile('A',1))
        self.board.grid[8][6].add_letter(Tile('A',1))
        self.board.grid[8][7].add_letter(Tile('L',1))
        self.board.grid[8][8].add_letter(Tile('A',1))
        word = "Foca"
        location = (5,7)
        orientation = "V"
        word_is_valid = self.board.validate_word_place_board(word, location, orientation)
        self.assertEqual(word_is_valid, True)
    
    def test_place_word_no_empthy_2_coincidence_vertical_wrong(self):
        self.board.grid[7][7].add_letter(Tile('C',1))
        self.board.grid[7][8].add_letter(Tile('A',1))
        self.board.grid[7][9].add_letter(Tile('S',1))
        self.board.grid[7][10].add_letter(Tile('A',1))
        self.board.grid[8][7].add_letter(Tile('M',1))
        self.board.grid[8][8].add_letter(Tile('A',1))
        self.board.grid[8][9].add_letter(Tile('L',1))
        word = "Foca"
        location = (5,7)
        orientation = "V"
        word_is_valid = self.board.validate_word_place_board(word, location, orientation)
        self.assertEqual(word_is_valid, False)
    
    def test_place_word_complex(self):
        self.board.put_words_board("Facu", (5,7), "H")
        self.board.put_words_board("Hola", (2,8), "V")
        self.assertEqual(self.board.validate_word_place_board("Lacra", (3,9), "V"), False)
    
    def test_put_words_horizontal(self):
        word = "Facultad"
        location = (5, 4)
        orientation = "H"
        self.board.put_words_board(word, location, orientation)
        for i, letter in enumerate(word):
            self.assertEqual(self.board.grid[location[0]][location[1] + i].letter.letter, letter)
    
    def test_put_words_vertical(self):
        word = "Facultad"
        location = (5, 4)
        orientation = "V"
        self.board.put_words_board(word, location, orientation)
        for i, letter in enumerate(word):
            self.assertEqual(self.board.grid[location[0] + i][location[1]].letter.letter, letter)
    
    def test_cross_word_right_way(self):
        self.board.grid[7][7] = Cell(1, '', Tile('H', 1))
        self.board.grid[7][8] = Cell(1, '', Tile('O', 1))   
        self.board.grid[7][9] = Cell(1, '', Tile('L', 1))   
        self.board.grid[7][10] = Cell(1, '', Tile('A', 1))       
        self.assertTrue(self.board.validate_word_place_board('CAMA', (6,10), 'V'))
    
    def test_cross_word_wrong_way(self):
        self.board.grid[7][7] = Cell(1, '', Tile('H', 1))
        self.board.grid[7][8] = Cell(1, '', Tile('O', 1))   
        self.board.grid[7][9] = Cell(1, '', Tile('L', 1))   
        self.board.grid[7][10] = Cell(1, '', Tile('A', 1))       
        self.assertFalse(self.board.validate_word_place_board('CAMA', (6,8), 'V'))
    
    def test_validate_words_around_horizontal_true(self):
        self.board.put_words_board('Hola', (7,7), 'V')
        word = 'coso'
        location = (8,6)
        orientation = 'H'
        self.assertEqual(self.board.validate_words_around(word, location, orientation), True)
    
    def test_validate_words_around_vertical_true(self):
        self.board.put_words_board('Hola', (7,7), 'H')
        word = 'coso'
        location = (6,8)
        orientation = 'V'
        self.assertEqual(self.board.validate_words_around(word, location, orientation), True)
    
    def test_validate_words_around_horizontal_false(self):
        self.board.put_words_board('Pola', (7,7), 'V')
        word = 'coso'
        location = (8,6)
        orientation = 'H'
        self.assertEqual(self.board.validate_words_around(word, location, orientation), False)
    
    def test_validate_words_around_vertical_false(self):
        self.board.put_words_board('Pola', (7,7), 'H')
        word = 'coso'
        location = (6,8)
        orientation = 'V'
        self.assertEqual(self.board.validate_words_around(word, location, orientation), False)
    
    def test_validate_words_around_false(self):
        self.board.put_words_board('P', (7,7), 'H')
        word = 'coso'
        location = (6,8)
        orientation = 'V'
        self.assertEqual(self.board.validate_words_around(word, location, orientation), False)
    
    def test_validate_words_around_in_the_extreme(self):
        self.board.put_words_board('Ave', (7,7), 'H')
        self.assertTrue(self.board.validate_words_around('Narco', (7,6), 'V'))
    
    def test_validate_words_around_create_another_words_complex(self):
        self.board.put_words_board('abal', (7,11), 'H')
        self.board.put_words_board('imaginacio', (12,0), 'H')
        self.assertTrue(self.board.validate_words_around('nacion', (7,10), 'V'))
    
    def test_validate_words_around_false_in_empty(self):
        self.assertEqual(self.board.validate_words_around('nacion', (0,0), 'H'), False)'''