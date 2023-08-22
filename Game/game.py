import random

class Tile:
    def __init__(self, letter, value):
        self.letter = letter
        self.value = value


class BagTiles:
    def __init__(self):
        self.tiles = [
            Tile('A', 1),
            Tile('A', 1),
            Tile('A', 1),
            Tile('A', 1),
            Tile('A', 1),
        ]
        random.shuffle(self.tiles)

    def take(self, count):
        tiles = []
        for _ in range(count):
            tiles.append(self.tiles.pop())
        return tiles

    def put(self, tiles):
        self.tiles.extend(tiles)


class ScrabbleTiles:
    def __init__(self):
        self.tiles = []
        self.init_tiles()

    def init_tiles(self):
        # Inicializar las fichas de letras con valores
        letters = [
            ('A', 9, 1), ('B', 2, 3), ('C', 2, 3), ('D', 4, 2), ('E', 12, 1),
            ('F', 2, 4), ('G', 3, 2), ('H', 2, 4), ('I', 9, 1), ('J', 1, 8),
            ('K', 1, 5), ('L', 4, 1), ('M', 2, 3), ('N', 6, 1), ('O', 8, 1),
            ('P', 2, 3), ('Q', 1, 10), ('R', 6, 1), ('S', 4, 1), ('T', 6, 1),
            ('U', 4, 1), ('V', 2, 4), ('W', 2, 4), ('X', 1, 8), ('Y', 2, 4), ('Z', 1, 10)
        ]
        
        for letter, count, value in letters:
            for _ in range(count):
                self.tiles.append((letter, value))

        # Agregar los comodines
        self.tiles.extend([('*', 0), ('*', 0)])

    def draw_tile(self):
        if self.tiles:
            index = random.randint(0, len(self.tiles) - 1)
            return self.tiles.pop(index)
        else:
            return None

    def tiles_left(self):
        return len(self.tiles)

# Crear el conjunto de fichas
tiles = ScrabbleTiles()

# Sacar fichas al azar
for _ in range(10):  # Sacar 10 fichas como ejemplo
    tile, value = tiles.draw_tile()
    if tile is not None:
        print(f"Se sacó la ficha: {tile[0]} (Valor: {value})")
    else:
        print("No quedan fichas en el conjunto.")

