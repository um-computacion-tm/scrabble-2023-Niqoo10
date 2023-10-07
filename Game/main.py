from Game.tile import Tile
from Game.bagtile import BagTiles
from Game.board import Board
from Game.player import Player
from Game.scrabble import ScrabbleGame

class Main:
    def __init__(self):
        self.game = ScrabbleGame()

    def valid_player_count(self, number):
        try:
            number = int(number)
            if number >= 2:
                return True
            else:
                return False
        except ValueError:
            return False

    def show_current_player(self):
        print("Bienvenido")
        print(f"Turno del jugador {self.game.current_player.id}")

    def next_turn(self):
        self.game.next_turn()

    def exchange_tiles(self):
        self.game.exchange_tiles()

    def reorganize(self):
        self.game.reorganize()

    def add_score(self, word, location, orientation):
        self.game.add_score(word, location, orientation)

    def initial_tiles(self):
        self.game.initial_tiles()

    def show_board(self, board):
        print("\n  |  0   1 ")
        for i in range(len(board.grid)):
            print(f"{i}|", end=" ")
            for j in range(len(board.grid[i])):
                cell = board.grid[i][j]
                if cell.is_empty():
                    print(" - ", end=" ")
                else:
                    print(f" {cell.tile.letter} ", end=" ")
            print()

    def show_scores(self):
        print("Bienvenido")
        print("Puntajes de los jugadores:")
        for player in self.game.players:
            print(f"Jugador {player.id}: Puntaje = {player.score}")

if __name__ == "__main__":
    main = Main()
    main.show_current_player()
