# models.py

from Game.wordconverter import Converter
from Game.tools import Tools

class Miscellaneos():    
    def calculate_word_value(self,word):
        tool = Tools()
        total_value = 0
        word_multiplier = 1

        for cell in word:
            if tool.is_active_and_letter_multiplier(cell):
                total_value += cell.calculate_value()
            elif tool.is_active_and_word_multiplier(cell):
                total_value += cell.calculate_value()
                word_multiplier *= cell.multiplier
            else:
                total_value += cell.letter.value
        total_value *= word_multiplier

        return total_value
    
    def compare_tiles_and_letters(self, tile, letter):
        if tile is not None:
            if tile.letter == letter.upper():
                return 1
            else:
                return 0
        else:
            return
       
    def get_tiles_for_word_placement(self, word, location, orientation, board):
        converter = Converter()
        positions = converter.locations_to_positions(word, location, orientation)
        list_tiles = []
        for position in positions:
            row, column = position
            tiles = board.grid[row][column].letter
            if tiles != None:
                list_tiles.append(tiles)
        return list_tiles
    
    def tiles_needed_to_form_word(self, word, location, orientation, board):
        converter = Converter()
        tiles_required = []
        word_tiles = converter.word_to_tiles(word)
        position_tiles = self.get_tiles_for_word_placement(word, location, orientation, board)
        position_set = set(tile.letter for tile in position_tiles)
        for tile in word_tiles:
            if tile.letter not in position_set:
                tiles_required.append(tile)
        return tiles_required
    
    def get_cell_in_the_extreme_horizontal(self, length, location, list):
        row, column = location
        if column - 1 >= 0:
                list.append((row, column - 1))
        if column + length < 15:
                list.append((row, column + length))
    
    def get_cell_in_the_extreme_vertical(self, length, location, list):
        row, column = location
        if row - 1 >= 0:
            list.append((row - 1, column))
        if row + length < 15:
            list.append((row + length, column))
    
    def get_cell_around_word_horizontal(self, word, location, list):
        row, column = location
        word_length = len(word)
        self.get_cell_in_the_extreme_horizontal(word_length, location, list)
        for i in range(word_length):
            if row - 1 >= 0:
                list.append((row - 1, column + i))
            if row + 1 < 15:
                list.append((row + 1, column + i))

    def get_cell_around_word_vertical(self, word, location, list):
        row, column = location
        word_length = len(word)
        self.get_cell_in_the_extreme_vertical(word_length, location, list)
        for i in range(word_length):
            if column - 1 >= 0:
                list.append((row + i, column - 1))
            if column + 1 < 15:
                list.append((row + i, column + 1))
        
    def verify_cell_around_word(self, list_cell, list_tiles, board):
        total_of_coincidences = []
        for coord in list_cell:
            row, column = coord
            if board.grid[row][column].letter is not None:
                list_tiles.append((row, column))
                total_of_coincidences.append(1)
        if len(total_of_coincidences) > 0:
            return True
        else:
            return False
    def check_cells_before_horizontal(self, row, column, location, board):
        new_word = []
        for i in range(row + 1):
            if board.grid[row - i][column].letter is not None:
                location.append((row - i, column))
                new_word.insert(0, board.grid[row - i][column].letter.letter)
        return new_word
    
    def check_cells_before_vertical(self, row, column, location, board):
        new_word = []
        for i in range(column + 1):
            if board.grid[row ][column - i].letter is not None:
                location.append((row, column - i))
                new_word.insert(0, board.grid[row][column - i].letter.letter)
        return new_word

    def check_cells_after_horizontal(self, row, column, board):
        new_word = []
        for i in range(1, 14-(row - 1)):
            if board.grid[row + i][column].letter is not None:
                new_word.append(board.grid[row + i][column].letter.letter)
        return new_word

    def check_cells_after_vertical(self, row, column, board):
        new_word = []
        for i in range(1, 14-(column - 1)):
            if board.grid[row][column + i].letter is not None:
                new_word.append(board.grid[row][column + i].letter.letter)
        return new_word

    def check_cells_before(self, coord1, coord2, orientation, board):
        location = []
        orientation_of_word = []
        if orientation == "H":
            orientation_of_word.append('V')
            new_word = self.check_cells_before_horizontal(coord1, coord2, location, board)
        elif orientation == "V":
            orientation_of_word.append('H')
            new_word = self.check_cells_before_vertical(coord2, coord1, location, board)
        location = location[-1:]
        return new_word, location, orientation_of_word

    def check_cells_after(self, coord1, coord2, orientation, board):
        if orientation == "H":
            row = coord1
            column = coord2
            new_word = self.check_cells_after_horizontal(row, column, board)
        elif orientation == "V":
            row = coord2
            column = coord1
            new_word = self.check_cells_after_vertical(row, column, board)
        return new_word
    
    def find_words_in_directions(self, location_of_word, orientation, string, board):
        coord1, coord2 = location_of_word
        if coord1 - 1 >= 0:
            before_word, location, orientation_of_word = self.check_cells_before(coord1, coord2, orientation, board)
            string += "".join(before_word)
        if coord1 + 1 < 15:
            after_word = self.check_cells_after(coord1, coord2, orientation, board)
            string += "".join(after_word)
        return string, location, orientation_of_word
    
    def check_tiles_around_word(self, list_tiles, orientation, board):
        list_of_words = []
        for coord in list_tiles:
            row, column = coord
            another_word = ''
            if orientation == 'H':
                location_of_word = (row, column)
                another_word, location, orientation_of_word = self.find_words_in_directions(location_of_word, 'H', another_word, board)
            elif orientation == 'V':
                location_of_word = (column, row)
                another_word, location, orientation_of_word = self.find_words_in_directions(location_of_word, 'V', another_word, board)
            new_word = [another_word, location[0], orientation_of_word[0]]
            list_of_words.append(new_word)
        return list_of_words
    
