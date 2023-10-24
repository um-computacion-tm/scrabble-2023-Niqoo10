#test_tile.py

import unittest
from Game.tile import Tile

class TestTiles(unittest.TestCase):
    def test_tile(self):
        tile = Tile('A', 1)
        self.assertEqual(tile.letter, 'A')
        self.assertEqual(tile.value, 1)
    def test_is_wildcard(self):
        tile = Tile('?', 0)
        self.assertEqual(tile.is_wildcard(), True)
    def test_convert_tile(self):
        tile = Tile('A',1)
        tile.convert_tile('B', 2)
        self.assertEqual(tile.letter, 'B')
        self.assertEqual(tile.value, 2)