from Game.cell import Cell
from Game.miscellaneos import Miscellaneos
from Game.dictionary import Dictionary
from Game.converter import Converter
from Game.tools import Tools

class Board:
    def __init__(self):
        board_multipliers = [
            ["3W", None, None, "2L", None, None, None, "3W", None, None, None, "2L", None, None, "3W"],
            [None, "2W", None, None, None, "3L", None, None, None, "3L", None, None, None, "2W", None],  
            [None, None, "2W", None, None, None, "2L", None, "2L", None, None, None, "2W", None, None], 
            ["2L", None, None, "2W", None, None, None, "2L", None, None, None, "2W", None, None, "2L"],  
            [None, None, None, None, "2W", None, None, None, None, None, "2W", None, None, None, None],  
            [None, "3L", None, None, None, "3L", None, None, None, "3L", None, None, None, "3L", None],  
            [None, None, "2L", None, None, None, "2L", None, "2L", None, None, None, "2L", None, None],  
            ["3W", None, None, "2L", None, None, None, "2W", None, None, None, "2L", None, None, "3W"],  
            [None, None, "2L", None, None, None, "2L", None, "2L", None, None, None, "2L", None, None],  
            [None, "3L", None, None, None, "3L", None, None, None, "3L", None, None, None, "3L", None],  
            [None, None, None, None, "2W", None, None, None, None, None, "2W", None, None, None, None],  
            ["2L", None, None, "2W", None, None, None, "2L", None, None, None, "2W", None, None, "2L"],  
            [None, None, "2W", None, None, None, "2L", None, "2L", None, None, None, "2W", None, None],  
            [None, "2W", None, None, None, "3L", None, None, None, "3L", None, None, None, "2W", None],  
            ["3W", None, None, "2L", None, None, None, "3W", None, None, None, "2L", None, None, "3W"] 
        ]
        self.grid = [
            [self.put_multipliers(multiplier) for multiplier in row]
            for row in board_multipliers
        ]

    def put_multipliers(self, multiplier):
        if multiplier is None:
            return Cell()
        multiplier_type = multiplier[-1]
        multiplier_value = int(multiplier[0])
        if multiplier_type == "W":
            return Cell(multiplier=multiplier_value, multiplier_type="word")
        elif multiplier_type == "L":
            return Cell(multiplier=multiplier_value, multiplier_type="letter")
    
    def put_words_board(self, word, location, orientation):
        converter = Converter()
        tool = Tools()
        list_word = converter.word_to_tiles(word)
        row = location[0]
        column = location[1]
        i = 0
        for _ in list_word:
            self.grid[row][column].letter = list_word[i]
            self.grid[row][column].deactive_cell()
            row, column = tool.move_pointer(orientation, row, column)
            i += 1
        
    def validate_word_inside_board(self,word, location, orientation):
        row = location[0]
        column = location[1]
        word_length = len(word)
        if orientation == "H":
            return column + word_length <= 15
        elif orientation == "V":
            return row + word_length <= 15
    
    def is_empty(self):
        if self.grid[7][7].letter is None:
            return True
        else:
            return False
        
    def word_in_the_center(self, word, location, orientation):
        coordinate = {"H":location[0], "V" : location[1]}
        central_coordinate = coordinate.get(orientation)
        if central_coordinate == 7:
            return self.validate_word_inside_board(word, location, orientation)
        else:
            return False

    def check_right_letters(self, tile, letter, list):
        misc = Miscellaneos()
        if misc.compare_tiles_and_letters(tile, letter) == 0:
            list[0].append(letter)
        elif misc.compare_tiles_and_letters(tile, letter) == 1:
            list[1].append(letter)

    def check_conditions(self, list):
        if len(list[0]) > 0:
            return False
        elif len(list[0]) == 0 and len(list[1]) > 0:
            return True
        elif len(list[0]) == 0 and len(list[1]) == 0:
            return True

    def validate_word_horizontal(self, word, location):
        converter = Converter()
        word = converter.word_to_tiles(word)
        row = location[0]
        column = location[1]
        found_coincidences = []
        found_problem = []
        found_something = [found_problem, found_coincidences]
        for i in range(len(word)):
            actual_tile = self.grid[row][column + i].letter
            self.check_right_letters(actual_tile, word[i].letter, found_something)
        return self.check_conditions(found_something)
    
    def validate_word_vertical(self, word, location):
        converter = Converter()
        word = converter.word_to_tiles(word)
        row = location[0]
        column = location[1]
        found_coincidences = []
        found_problem = []
        found_something = [found_problem, found_coincidences]
        for i in range(len(word)):
            actual_tile = self.grid[row + i][column].letter
            self.check_right_letters(actual_tile, word[i].letter, found_something)
        return self.check_conditions(found_something)
    
    def validate_word_place_board(self, word, location, orientation):
        if self.is_empty() is True:
           return self.word_in_the_center(word, location, orientation)
        else:
            if orientation == "H":
                return self.validate_word_horizontal(word, location)
            else:
                return self.validate_word_vertical(word, location)    
       
    def get_cell_around_word(self, word, location, orientation, adjacent_cells):
        misc = Miscellaneos()
        if orientation == "H":
            misc.get_cell_around_word_horizontal(word, location, adjacent_cells)
        elif orientation == "V":
            misc.get_cell_around_word_vertical(word, location, adjacent_cells)
    
    def get_tiles_around_word(self, orientation, adjacent_tiles, board):
        tool = Tools()
        misc = Miscellaneos()
        if orientation == "H":
            adjacent_tiles = tool.filter_reapeted_column(adjacent_tiles)
            return misc.check_tiles_around_word(adjacent_tiles, 'H', board)
        elif orientation == "V":
            adjacent_tiles = tool.filter_reapeted_row(adjacent_tiles)
            return misc.check_tiles_around_word(adjacent_tiles, 'V', board)
    
    def get_validation_of_another_board(self, word_in_validation, other_words):
        board2 = Board()
        original_word = word_in_validation[0]
        original_location = word_in_validation[1]
        original_orientation = word_in_validation[2]
        adjacent_cells = []
        adjacent_tiles = []
        for list in other_words:
            another_word = list[0]
            another_location = list[1]
            another_orientation = list[2]
            board2.put_words_board(another_word, another_location, another_orientation)
        board2.put_words_board(original_word, original_location, original_orientation)
        self.get_cell_around_word(original_word, original_location, original_orientation, adjacent_cells)
        if Miscellaneos().verify_cell_around_word(adjacent_cells, adjacent_tiles, board2):
            word = self.get_tiles_around_word(original_orientation, adjacent_tiles, board2)
            return word

    def validate_words_around(self, word, location, orientation, residual_words=[]):
        board = self
        adjacent_cells = []
        adjacent_tiles = []
        misc = Miscellaneos()
        converter = Converter()
        dict = Dictionary()
        word_in_validation = [word, location, orientation]
        self.get_cell_around_word(word, location, orientation, adjacent_cells)
        if misc.verify_cell_around_word(adjacent_cells, adjacent_tiles, board) is True:
            words_to_validate_without_word = self.get_tiles_around_word(orientation, adjacent_tiles, board)
            words_to_validate_with_word = self.get_validation_of_another_board(word_in_validation, words_to_validate_without_word)
            real_words_to_validate_without_word = converter.result_to_list_of_words(words_to_validate_without_word)
            real_words_to_validate_with_word = converter.result_to_list_of_words(words_to_validate_with_word)
            new_words = set(real_words_to_validate_with_word) - set(real_words_to_validate_without_word)
            residual_words.extend(list(new_words))
            return dict.verify_word_list(real_words_to_validate_with_word)
        else:
            if self.is_empty() is True:
                return self.word_in_the_center(word, location, orientation)
