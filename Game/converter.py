# converter.py

from Game.bagtiles import BagTiles
from Game.tools import Tools
from Game.cell import Cell
import copy

class Converter:
    def string_to_tiles(self, input_string, tile_list):
        # Convierte una cadena en una lista de objetos Tile.
        bag = BagTiles()
        letter_set = set(tile.letter for tile in bag.tiles)
        for letter in input_string.upper():
            if letter in letter_set:
                matching_tile = next(tile for tile in bag.tiles if tile.letter == letter)
                tile_list.append(matching_tile)

    def especial_to_tiles(self, input_string, tile_list):
        # Convierte un carácter especial en un objeto Tile.
        bag = BagTiles()
        for tile in bag.tiles:
            if tile.letter == input_string.upper():
                tile_list.append(tile)
                break

    def word_to_tiles(self, word):
        # Convierte una palabra en una lista de objetos Tile.
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
        # Convierte las ubicaciones de una palabra en posiciones en el tablero.
        tool = Tools()
        positions = []
        row = location[0]
        column = location[1]
        for _ in word:
            positions.append((row, column))
            row, column = tool.move_pointer(orientation, row, column)
        return positions

    def word_to_cells(self, word, location, orientation, board):
        # Convierte una palabra en una lista de celdas en el tablero.
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
        # Convierte una palabra en una lista de celdas ficticias.
        word_cells = []
        word_tiles = self.word_to_tiles(word)
        for tile in word_tiles:
            word_cells.append(Cell(1, '', tile))
        return word_cells
    
    def result_to_list_of_words(self, result):
        # Convierte una lista de resultados en una lista de palabras.
        words = []
        for item in result:
            words.append(item[0])
        return words
