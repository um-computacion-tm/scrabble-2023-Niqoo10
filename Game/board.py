from Game.cell import Cell

class Board:
    def __init__(self):
        self.grid = [[' ' for _ in range(15)] for _ in range(15)]

    @property
    def is_empty(self):
        return all(all(cell == ' ' for cell in row) for row in self.grid)

    def validate_word_place_board(self, word, location, orientation):
        x, y = location
        if orientation == 'H':
            for letter in word:
                if self.grid[x][y] != ' ':
                    return False
                x += 1
        elif orientation == 'V':
            for letter in word:
                if self.grid[x][y] != ' ':
                    return False
                y += 1
        else:
            return False
        return True


    def calculate_word_value(self,word):
         value = 0
         word_multiplier = 1
         for cell in word:
             if not(cell.multiplier_type) and cell.active:
                 word_multiplier *= cell.multiplier
             value += cell.calculate_value()
             cell.active = False
         value = value * word_multiplier
         return value
    
    def validate_word_inside_board(self, word, location, orientation):
        x , y = location
        if orientation == 'H' and y + len(word) > 15:
                raise ValueError("La palabra no cabe en el tablero en la posicion especificada.")
        elif orientation == 'V' and x + len(word) > 15:
                raise ValueError("La palabra no cabe en el tablero en la posicion especificada.")
        return orientation in ('H', 'V')
    

    
if __name__ == '__main__':
    pass