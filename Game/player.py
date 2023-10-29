# player.py

from Game.bagtiles import BagTiles

class Player:
    def __init__(self, id=0):
        # Constructor de la clase Player.
        self.rack = []  # Lista de fichas en la mano del jugador.
        self.score = 0  # Puntuación del jugador.
        self.id = id  # Identificación del jugador.

    def get_tiles(self, amount, bag=BagTiles):
        # Obtiene fichas del conjunto de fichas del juego y las agrega al rack del jugador.
        for _ in range(amount):
            self.rack.append(bag.take(1))

    def exchange_tiles(self, index, bag=BagTiles):
        # Intercambia una ficha del rack del jugador por una nueva ficha del conjunto de fichas del juego.
        index = index - 1
        if 0 <= index < len(self.rack):
            tile_to_exchange = self.rack.pop(index)
            new_tile = bag.take(1)
            bag.put([tile_to_exchange])
            self.rack.insert(index, new_tile)

    def has_letters(self, tiles):
        # Verifica si el jugador tiene las fichas necesarias en su rack para formar una palabra con las fichas dadas.
        rack = set(tile.letter for tile in self.rack)
        return set(tile.letter for tile in tiles).issubset(rack)

    def has_wildcard(self):
        # Verifica si el jugador tiene una ficha comodín (wildcard) en su rack.
        return any(tile.is_wildcard() for tile in self.rack)

    def find_wildcard(self):
        # Encuentra el índice de la primera ficha comodín en el rack del jugador.
        for i, tile in enumerate(self.rack):
            if tile.is_wildcard():
                return i
        return None


'''from Game.bagtiles import BagTiles

class Player:
    def __init__(self, id=0):
        self.rack = []
        self.score = 0
        self.id = id

    def get_tiles(self,amount,bag=BagTiles):
        for _ in range(amount):
            self.rack.append(bag.take(1))

    def exchange_tiles(self,index,bag=BagTiles):
        index = index - 1
        tile_to_exchange = self.rack.pop(index)
        new_tile = bag.take(1)
        bag.put([tile_to_exchange])
        self.rack.insert(index, new_tile)
    
    def has_letters(self, tiles):
        rack = set(tile.letter for tile in self.rack) #Creación de un cojunto de python
        return set(tile.letter for tile in tiles).issubset(rack) #Se crea otro conjunto de python 
        #issubset comprueba si el nuevo conjunto es un subconjunto de rack, si es así devuelve True
    
    def has_wildcard(self):
        for tile in self.rack:
            if tile.is_wildcard() is True:
                return True
        return False
    
    def find_wildcard(self):
        for i, tile in enumerate(self.rack):
            if tile.is_wildcard() is True:
                return i
        return False'''