# test_player.py

import unittest
from Game.bagtiles import BagTiles
from Game.player import Player
from Game.tile import Tile

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player()
        self.bag = BagTiles()

    def test_get_tiles(self):
        self.player.get_tiles(7, self.bag)
        self.assertEqual(len(self.player.rack), 7)  # Verificar que se agregaron las fichas al rack del jugador

    def test_exchange_tiles(self):
        self.player.get_tiles(7, self.bag)
        initial_rack = self.player.rack[:]
        self.player.exchange_tiles(1, self.bag)
        self.assertNotEqual(self.player.rack, initial_rack)  # Verificar que se intercambió una ficha
        self.assertEqual(len(self.player.rack), 7)  # Verificar que el tamaño del rack se mantiene constante

    def test_has_letters(self):
        tiles = [Tile('A'), Tile('B'), Tile('C')]
        self.player.rack = [Tile('A'), Tile('B'), Tile('D')]
        self.assertTrue(self.player.has_letters(tiles))  # Verificar que el jugador tiene las fichas necesarias

        tiles = [Tile('A'), Tile('B'), Tile('C')]
        self.player.rack = [Tile('A'), Tile('D'), Tile('E')]
        self.assertFalse(self.player.has_letters(tiles))  # Verificar que el jugador no tiene las fichas necesarias

    def test_has_wildcard(self):
        self.player.rack = [Tile('A'), Tile('B'), Tile('C')]
        self.assertFalse(self.player.has_wildcard())  # Verificar que el jugador no tiene fichas comodín

        self.player.rack = [Tile('A'), Tile('B'), Tile('W')]
        self.assertTrue(self.player.has_wildcard())  # Verificar que el jugador tiene una ficha comodín

    def test_find_wildcard(self):
        self.player.rack = [Tile('A'), Tile('B'), Tile('C')]
        self.assertIsNone(self.player.find_wildcard())  # Verificar que no se encuentra una ficha comodín

        self.player.rack = [Tile('A'), Tile('W'), Tile('C')]
        self.assertEqual(self.player.find_wildcard(), 1)  # Verificar que se encuentra la ficha comodín en la posición 1

if __name__ == '__main__':
    unittest.main()

'''import unittest
from Game.player import Player
from Game.tile import Tile
from Game.board import Board
from Game.cell import Cell
from Game.models import Miscellaneos
from Game.bagtiles import BagTiles

class TestPlayer(unittest.TestCase):
    def test_player(self):
        player1 = Player()
        self.assertEqual(player1.rack,[])
    
    def test_player_get_tile(self):
        bag1 = BagTiles()
        player = Player()
        player.get_tiles(3,bag1)
        self.assertEqual(len(player.rack),3)

    def test_player_exchange(self):
        bag1 = BagTiles()
        player = Player()
        player.rack = [Tile('A', 1), Tile('B',3), Tile('C',2)]
        player.exchange_tiles(2,bag1)
        self.assertEqual(len(player.rack),3)
        self.assertEqual(len(bag1.tiles),29)
    
    def test_validate_rack_true(self):
        player_1 = Player()
        tiles = [Tile("H",1),Tile("O",1),Tile("L",1),Tile("A",1)]
        player_1.rack = [Tile("H",1),Tile("O",1),Tile("L",1),Tile("A",1), Tile("Z",1), Tile("Z",1), Tile("Z",1)]
        is_valid = player_1.has_letters(tiles)
        assert is_valid == True
    
    def test_validate_rack_false(self):
        player_1 = Player()
        tiles = [Tile("H",1),Tile("O",1),Tile("L",1),Tile("A",1)]
        player_1.rack = [Tile("H",1),Tile("O",1),Tile("E",1),Tile("A",1), Tile("Z",1), Tile("Z",1), Tile("Z",1)]
        is_valid = player_1.has_letters(tiles)
        assert is_valid == False
    
    def test_has_required_tiles(self):
        misc = Miscellaneos()
        player = Player()
        player.rack = [Tile('F',1), Tile('C',1)]
        board = Board()
        word = "Facu"
        location = (4, 7)
        orientation = "H"
        board.grid[4][8] = Cell(letter=Tile('A',1))
        board.grid[4][10] = Cell(letter=Tile('U',1))
        required_tiles = misc.tiles_needed_to_form_word(word, location, orientation, board)
        self.assertEqual(player.has_letters(required_tiles), True)
    
    def test_has_wildcard_true(self):
        player = Player()
        player.rack = [Tile('A', 1), Tile('?', 0)]
        self.assertEqual(player.has_wildcard(), True)

    def test_has_wildcard_false(self):
        player = Player()
        player.rack = [Tile('A', 1), Tile('B', 2)]
        self.assertEqual(player.has_wildcard(), False)
    
    def test_find_wildcard(self):
        player = Player()
        player.rack = [Tile('A', 1), Tile('B', 2), Tile('?', 0)]
        self.assertEqual(player.find_wildcard(), 2)
    
    def test_no_find_wildcard(self):
        player = Player()
        player.rack = [Tile('A', 1), Tile('B', 2)]
        self.assertEqual(player.find_wildcard(), False)'''