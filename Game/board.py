from Game.cell import Cell
from Game.dictionary import Dictionary

class Board:
    def __init__(self):
        self.grid = [[Cell('', 1) for _ in range(15) ]for _ in range(15)]
    
    def calculate_word_value(self, word):
        value = 0
        word_multiplier = 1
        for cell in word:
            if not cell.multiplier_type and cell.active:
                word_multiplier *= cell.multiplier
            value += cell.calculate_value()
            cell.active = False
        value *= word_multiplier
        return value
    
    def validate_word_inside_board(self, word, location, orientation, board_size=15):
        x, y = location
        if orientation == 'H':
            if y + len(word) > board_size:
                raise ValueError("La palabra no cabe en el tablero en la posicion especificada.")
        elif orientation == 'V':
            if x + len(word) > board_size:
                raise ValueError("La palabra no cabe en el tablero en la posicion especificada.")
        return orientation in ('H', 'V')
    
    def check_word(self, word, words_set):
        return word.lower() in words_set
    
    def put_word(self, word, location, orientation):
        x, y = location
        dx, dy = (0, 1) if orientation == 'H' else (1, 0)
        for letter in word:
            self.grid[x][y].add_letter(letter)
            x += dx
            y += dy
    
    @property
    def is_empty(self):
        return not any(cell.letter for row in self.grid for cell in row)

if __name__ == '__main__':
    pass