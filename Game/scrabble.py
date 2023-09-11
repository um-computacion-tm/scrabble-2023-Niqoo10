from Game.board import Board
from Game.player import Player
from Game.game import BagTiles

class ScrabbleGame:
    def __init__(self, players_count: int):
        self.board = Board()
        self.bag_tiles = BagTiles()
        self.players:list[Player] = []
        for _ in range(players_count):
            self.players.append(Player(bag_tiles=self.bag_tiles))
        
        self.current_player = None

    def next_turn(self):
        if self.current_player is None:
            self.current_player = self.players[0]
        else:
            #index = index del current player + 1
            #len(self.players)
            index = self.players.index(self.current_player) + 1
            self.current_player = self.players[index]