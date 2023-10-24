# models.py

from game.bagtiles import BagTiles
from game.cell import Cell
import colorama
from colorama import Fore, Style
import copy

class Tools:
    def move_pointer(self, orientation, row, column):
        if orientation == "H":
            column += 1
        elif orientation == "V":
            row += 1
        return row, column
    
    def is_active_and_letter_multiplier(self,cell):
        return cell.status == 'active' and cell.multiplier_type == 'letter'

    def is_active_and_word_multiplier(self,cell):
        return cell.status == 'active' and cell.multiplier_type == 'word'

    def format_placed_word_cell(self, cell):
        return f" {cell.letter.letter} "

    def format_active_cell(self, cell):
        if cell.status == 'active':
            return self.format_cell_contents(cell)

    def format_cell_contents(self, cell):
        if cell.letter is None:
            return self.format_multiplier(cell.multiplier, cell.multiplier_type)
        else:
            return self.format_placed_word_cell(cell)

    def format_multiplier(self, multiplier, multiplier_type):
        if multiplier_type == 'word':
            colors = {2: Fore.LIGHTMAGENTA_EX, 3: Fore.RED}
        elif multiplier_type == 'letter':
            colors = {2: Fore.CYAN, 3: Fore.BLUE}
        else:
            return " - "

        return f"{colors.get(multiplier, '')}{multiplier}{multiplier_type[0].upper()}{Style.RESET_ALL} "
    
    def filter_reapeted_column(self, list_tuples):
        columns = {}
        for row, column in list_tuples:
            if column not in columns:
                columns[column] = (row, column)
        list_tuples = list(columns.values())
        return list_tuples
    
    def filter_reapeted_row(self, list_tuples):
        rows = {}
        for row, column in list_tuples:
            if row not in rows:
                rows[row] = (row, column)
        list_tuples = list(rows.values())
        return list_tuples

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
    

class Converter:
    def string_to_tiles(self, input_string, list):
        bag = BagTiles()
        letter_set = set(tile.letter for tile in bag.tiles)
        for letter in input_string.upper():
            if letter in letter_set:
                matching_tile = next(tile for tile in bag.tiles if tile.letter == letter)
                #Next es una función para buscar elementos de un iterador (en esta caso: el conjunto)
                list.append(matching_tile)


    def especial_to_tiles(self, input_string, list):
        bag = BagTiles()
        for tile in bag.tiles:
            if tile.letter == input_string.upper():
                list.append(tile)
                break

    def word_to_tiles(self, word):
        tiles_list = []
        i = 0
        while i < len(word):
            two_letter_combo = word[i:i+2]
            if two_letter_combo.upper() in ('CH', 'LL', 'RR'):
                self.especial_to_tiles(two_letter_combo, tiles_list)
                i += 2
            else:
                self.string_to_tiles(word[i], tiles_list)
                i += 1
        return tiles_list

    def locations_to_positions(self, word, location, orientation):
        tool = Tools()
        positions = []
        row = location[0]
        column = location[1]
        for _ in word:
            positions.append((row, column))
            row, column = tool.move_pointer(orientation, row, column)
        return positions

    def word_to_cells(self, word, location, orientation, board):
        list_tiles = self.word_to_tiles(word)
        two_letter_tile = 0
        for tile in list_tiles:
            if tile.letter in ['CH', 'RR', 'LL']:
                two_letter_tile += 1
        positions = self.locations_to_positions(word, location, orientation)
        list_cell = []
        for i in range(len(word) - two_letter_tile):
            tile = list_tiles[i]
            position = positions[i]
            column, row = position
            cell = copy.copy(board.grid[column][row])
            cell.add_letter(tile)
            list_cell.append(cell)
        return list_cell
    
    def word_to_false_cells(self, word):
        word_cells = []
        word_tiles = self.word_to_tiles(word)
        for tile in word_tiles:
            word_cells.append(Cell(1, '', tile))
        return word_cells
    
    def result_to_list_of_words(self, result):
        words = []
        for list in result:
            words.append(list[0])
        return words
