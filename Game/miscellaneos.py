# miscellaneos.py

from Game.converter import Converter
from Game.tools import Tools

class Miscellaneos:
    def calculate_word_value(self, word):
        # Calcula el valor total de una palabra considerando los multiplicadores.
        tool = Tools()
        total_value = 0
        word_multiplier = 1

        for cell in word:
            if tool.is_active_and_letter_multiplier(cell) or tool.is_active_and_word_multiplier(cell):
                total_value += cell.calculate_value()
                if tool.is_active_and_word_multiplier(cell):
                    word_multiplier *= cell.multiplier
            else:
                total_value += cell.letter.value
        total_value *= word_multiplier
        return total_value
    
    def compare_tiles_and_letters(self, tile, letter):
        # Compara un objeto Tile con una letra y devuelve 1 si son iguales, 0 en caso contrario.
        if tile is not None:
            return 1 if tile.letter == letter.upper() else 0
        return 0
       
    def get_tiles_for_word_placement(self, word, location, orientation, board):
        # Obtiene las fichas ya colocadas en el tablero para una palabra.
        converter = Converter()
        positions = converter.locations_to_positions(word, location, orientation)
        list_tiles = [board.grid[row][column].letter for row, column in positions if board.grid[row][column].letter is not None]
        return list_tiles
    
    def tiles_needed_to_form_word(self, word, location, orientation, board):
        # Obtiene las fichas requeridas para formar una palabra en el tablero.
        converter = Converter()
        word_tiles = converter.word_to_tiles(word)
        position_tiles = self.get_tiles_for_word_placement(word, location, orientation, board)
        position_set = set(tile.letter for tile in position_tiles)
        tiles_required = [tile for tile in word_tiles if tile.letter not in position_set]
        return tiles_required
    
    def get_cell_in_the_extreme_horizontal(self, length, location, list):
        # Obtiene las celdas en los extremos horizontales de una palabra.
        row, column = location
        if column - 1 >= 0:
            list.append((row, column - 1))
        if column + length < 15:
            list.append((row, column + length))
    
    def get_cell_in_the_extreme_vertical(self, length, location, list):
        # Obtiene las celdas en los extremos verticales de una palabra.
        row, column = location
        if row - 1 >= 0:
            list.append((row - 1, column))
        if row + length < 15:
            list.append((row + length, column))
    
    def get_cell_around_word_horizontal(self, word, location, list):
        # Obtiene las celdas alrededor de una palabra en sentido horizontal.
        row, column = location
        word_length = len(word)
        self.get_cell_in_the_extreme_horizontal(word_length, location, list)
        for i in range(word_length):
            if row - 1 >= 0:
                list.append((row - 1, column + i))
            if row + 1 < 15:
                list.append((row + 1, column + i))

    def get_cell_around_word_vertical(self, word, location, list):
        # Obtiene las celdas alrededor de una palabra en sentido vertical.
        row, column = location
        word_length = len(word)
        self.get_cell_in_the_extreme_vertical(word_length, location, list)
        for i in range(word_length):
            if column - 1 >= 0:
                list.append((row + i, column - 1))
            if column + 1 < 15:
                list.append((row + i, column + 1))
        
    def verify_cell_around_word(self, list_cell, list_tiles, board):
        # Verifica si hay celdas activas alrededor de una palabra.
        for coord in list_cell:
            row, column = coord
            if board.grid[row][column].letter is not None:
                list_tiles.append((row, column))
        return len(list_tiles) > 0

    def check_cells_before_horizontal(self, row, column, location, board):
        # Obtiene las letras en las celdas antes de una palabra en sentido horizontal.
        new_word = []
        for i in range(row + 1):
            if board.grid[row - i][column].letter is not None:
                location.append((row - i, column))
                new_word.insert(0, board.grid[row - i][column].letter.letter)
        return new_word
    
    def check_cells_before_vertical(self, row, column, location, board):
        # Obtiene las letras en las celdas antes de una palabra en sentido vertical.
        new_word = []
        for i in range(column + 1):
            if board.grid[row][column - i].letter is not None:
                location.append((row, column - i))
                new_word.insert(0, board.grid[row][column - i].letter.letter)
        return new_word

    def check_cells_after_horizontal(self, row, column, board):
        # Obtiene las letras en las celdas después de una palabra en sentido horizontal.
        new_word = []
        for i in range(1, 14-(row - 1)):
            if board.grid[row + i][column].letter is not None:
                new_word.append(board.grid[row + i][column].letter.letter)
        return new_word

    def check_cells_after_vertical(self, row, column, board):
        # Obtiene las letras en las celdas después de una palabra en sentido vertical.
        new_word = []
        for i in range(1, 14-(column - 1)):
            if board.grid[row][column + i].letter is not None:
                new_word.append(board.grid[row][column + i].letter.letter)
        return new_word

    def check_cells_before(self, coord1, coord2, orientation, board):
        # Obtiene las letras en las celdas antes de una palabra en una dirección específica.
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
        # Obtiene las letras en las celdas después de una palabra en una dirección específica.
        if orientation == "H":
            row = coord1
            column = coord2
            new_word = self.check_cells_after_horizontal(row, column, board)
        elif orientation == "V":
            row = coord2
            column = coord1
            new_word = self.check_cells_after_vertical(row, column, board)

