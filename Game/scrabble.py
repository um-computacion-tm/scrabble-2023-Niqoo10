from Game.board import Board
from Game.player import Player
from Game.bagtile import BagTiles
from Game.tile import Tile
import time
import threading

class ScrabbleGame:
    def __init__(self, players_count,):
        self.board = Board()
        self.bag_tiles = BagTiles()
        self.player = Player()
        self.players = []
        self.current_player = 0
        self.turn_limit = 60
        for _ in range(players_count):
            self.players.append(Player())

    def get_current_player(self):
            return self.players[self.current_player]

    def start_game(self):
        for player in self.players:
            tilesToDraw = 7 - len(player.tiles)
            newTiles = self.bag_tiles.take(tilesToDraw)
            player.tiles.extend(newTiles)

    def next_turn(self):
        self.current_player += 1
        if self.current_player >= len(self.players):
            self.current_player = 0

    def pass_turn_scrabble(self, player_index):
        current_player = self.players[self.current_player]
        current_player.pass_turn_player()
        self.current_player += 1
        if self.current_player >= len(self.players):
            self.current_player = 0

    def is_game_over(self):
        if len(self.bag_tiles.tiles) == 0 and not self.can_exchange_tiles():
            return True
        
    def can_exchange_tiles(self):
        current_player = self.players[self.current_player]
        exchangeable_tiles = [tile for tile in current_player.tiles if tile.letter != '' and tile.value != 0]
        return len(exchangeable_tiles) > 0

    def set_time_limit(self, time_limit):
        self.turn_limit = time_limit
    
    def start_timer(self):
        threading.Thread(target = self._timer_thread).start()

    def _timer_thread(self):
        current_player = self.players[self.current_player]
        start_time = time.time()
        while time.time() - start_time < self.turn_limit:
            time.sleep(1)
        print(f"Tiempo agotado para {current_player} - Turno perdido.")
        self.next_turn()
        
if __name__ == '__main__':
    pass