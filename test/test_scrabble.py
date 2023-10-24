# test_scrabble.py

'''import unittest
from game.scrabble import Scrabble, InvalidWordException, InvalidRackException, InvalidWildCardConversion
from game.player import Player
from game.board import Board
from game.cell import Cell
from game.tile import Tile
from game.models import Miscellaneos

class TestScrabble(unittest.TestCase):
    def test_scrabble(self):
        scrabble_1 = Scrabble(3)
        self.assertIsNotNone(scrabble_1.board, None)
        self.assertEqual(len(scrabble_1.players),3)
        self.assertEqual(scrabble_1.turn, 0)
    def test_unique_id(self):
        game_1 = Scrabble(1)
        game_2 = Scrabble(1)
        self.assertNotEqual(game_1.gameid, game_2.gameid)
    def test_next_turn_when_game_is_starting(self):
        game = Scrabble(2)
        game.next_turn()
        self.assertEqual(game.current_player, game.players[0])
    def test_next_turn_when_game_is_not_the_first(self):
        game = Scrabble(2)
        game.current_player = game.players[0]
        game.next_turn()
        self.assertEqual(game.current_player, game.players[1])
    def test_next_turn_when_game_is_last(self):
        game = Scrabble(2)
        game.current_player = game.players[1]
        game.next_turn()
        self.assertEqual(game.current_player, game.players[0])
    def test_next_turn(self):
        game = Scrabble(2)
        self.assertEqual(game.turn, 0)
        game.next_turn()
        self.assertEqual(game.turn, 1)
    def test_playing(self):
        game = Scrabble(1)
        self.assertEqual(game.playing(), True)
    
    def test_validate_word(self):
        game = Scrabble(2)
        word = "Facultad"
        location = (7, 7)
        orientation = "H"
        self.assertEqual(game.validate_word(word,location,orientation), True)
        
    def test_calculate_score_simple(self):
        game = Scrabble(2)
        word = "Facu"
        location = (4,0)
        orientation = "H"
        game.next_turn()
        self.assertEqual(game.current_player.score, 0)
        game.calculate_score(word, location, orientation)
        self.assertEqual(game.current_player.score, 8)
        
    def test_calculate_score_complex(self):
        game = Scrabble(2)
        word = "Facu"
        location = (0,0)
        orientation = "H"
        game.next_turn()
        self.assertEqual(game.current_player.score, 0)
        game.calculate_score(word, location, orientation)
        self.assertEqual(game.current_player.score, 27)
    
    def test_calculate_score_multiple_words(self):
        game = Scrabble(2)
        game.board.put_words_board('abal', (11,7), 'V')
        game.board.put_words_board('imaginacio', (0,12), 'V')
        word = "Nacion"
        location = (10,7)
        orientation = "H"
        game.next_turn()
        self.assertEqual(game.current_player.score, 0)
        game.calculate_score(word, location, orientation)
        #Score to the word nacion is 7 pass to 14 with the multiplier of word
        #Is created 2 new words: 'Nabal' and 'imaginacion' and your respective score are: 7 and 15
        #So the total score will be 36
        self.assertEqual(game.current_player.score, 36)
    
    def test_validate_word_not_in_dictionary(self):
        game = Scrabble(2)
        word = "Kadabra"
        location = (0,0)
        orientation = "H"
        with self.assertRaises(InvalidWordException):
            game.validate_word(word, location, orientation)

    def test_validate_word_exceeds_board(self):
        game = Scrabble(2)
        word = "Facultad"
        location = (14,14)
        orientation = "H"
        with self.assertRaises(InvalidWordException):
            game.validate_word(word, location, orientation)
    
    def test_validate_word_wrong_placement(self):
        game = Scrabble(2)
        word = "Facultad"
        location = (7,7)
        orientation = "H"
        game.board.put_words_board('ana', (7,7), 'H')
        with self.assertRaises(InvalidWordException):
            game.validate_word(word, location, orientation)
    
    def test_validate_word_form_invalid_words(self):
        game = Scrabble(2)
        word = "Facultad"
        location = (6,6)
        orientation = "V"
        game.board.put_words_board('ana', (7,7), 'H')
        with self.assertRaises(InvalidWordException):
            game.validate_word(word, location, orientation)
    
    def test_validate_word_right_placement(self):
        game = Scrabble(2)
        word = "Facultad"
        location = (6,7)
        orientation = "V"
        game.board.put_words_board('ana', (7,7), 'H')
        self.assertEqual(game.validate_word(word, location, orientation), True)
    
    def test_validate_word_in_the_extreme_of_another_word(self):
        game = Scrabble(2)
        game.board.put_words_board('Ave', (7,7), 'H')
        self.assertTrue(game.validate_word('Narco', (7,6), 'V'))
    
    def test_put_word(self):
        game = Scrabble(2)
        word = "Hola"
        location = (5, 4)
        orientation = "H"
        game.put_word(word, location, orientation)
        self.assertEqual(game.board.grid[5][4].letter.letter, "H")
        self.assertEqual(game.board.grid[5][5].letter.letter, "O")
        self.assertEqual(game.board.grid[5][6].letter.letter, "L")
        self.assertEqual(game.board.grid[5][7].letter.letter, "A")

    def test_show_amount_tiles_bag(self):
        game = Scrabble(2)
        self.assertEqual(game.show_amount_tiles_bag(), 29)
    
    def test_shuffle_rack(self):
        game = Scrabble(2)
        game.next_turn()
        game.current_player.rack = [Tile('A', 1), Tile('B',3), Tile('C',2)]
        game.shuffle_rack()
        self.assertEqual(len(game.current_player.rack), 3)
    
    def test_game_over_true(self):
        game = Scrabble(2)
        game.bagtiles.tiles = []
        self.assertEqual(game.game_over(), True)
    
    def test_game_over_false(self):
        game = Scrabble(2)
        self.assertEqual(game.game_over(), False)
    
    def test_put_tiles_in_rack_all_players(self):
        game = Scrabble(2)
        self.assertEqual(len(game.players[0].rack), 0)
        self.assertEqual(len(game.players[1].rack), 0)
        game.put_tiles_in_rack()
        self.assertEqual(len(game.players[0].rack), 7)
        self.assertEqual(len(game.players[1].rack), 7)
    
    def test_put_tiles_in_rack_one_player(self):
        game = Scrabble(2)
        self.assertEqual(len(game.players[0].rack), 0)
        self.assertEqual(len(game.players[1].rack), 0)
        game.next_turn()
        game.next_turn()
        game.put_tiles_in_rack(1)
        self.assertEqual(len(game.players[0].rack), 0)
        self.assertEqual(len(game.players[1].rack), 1)
    
    def test_put_tiles_in_rack_few_tiles_in_bag(self):
        game = Scrabble(2)
        self.assertEqual(len(game.players[0].rack), 0)
        self.assertEqual(len(game.players[1].rack), 0)
        game.next_turn()
        game.bagtiles.tiles = [Tile('H', 4), Tile('O', 1), Tile('L',1), Tile('A',1), Tile('H', 4), Tile('O', 1), Tile('L',1), Tile('A',1)]
        game.put_tiles_in_rack(7)
        self.assertEqual(len(game.players[0].rack), 7)
        self.assertEqual(len(game.players[1].rack), 0)
        game.next_turn()
        game.put_tiles_in_rack(7)
        self.assertEqual(len(game.players[0].rack), 7)
        self.assertEqual(len(game.players[1].rack), 1)

    
    def test_put_initial_tiles_bag(self):
        game = Scrabble(2)
        self.assertEqual(len(game.bagtiles.tiles), 29)
        game.put_initial_tiles_bag()
        self.assertEqual(len(game.bagtiles.tiles), 100)

    def test_descount_tiles_to_player(self):
        game = Scrabble(2)
        game.next_turn()
        game.current_player.rack = [Tile('F',1), Tile('C',1)]
        board = game.board
        word = "Facu"
        location = (4, 7)
        orientation = "H"
        board.grid[4][8] = Cell(letter=Tile('A',1))
        board.grid[4][10] = Cell(letter=Tile('U',1))
        self.assertEqual(len(game.current_player.rack), 2)
        game.descount_tiles_to_player(word, location, orientation)
        self.assertEqual(len(game.current_player.rack), 0)
    
    def test_descount_tiles_to_player_exception(self):
        game = Scrabble(2)
        game.next_turn()
        board = game.board
        word = "Facu"
        location = (4, 7)
        orientation = "H"
        game.current_player.rack = [Tile('A',1), Tile('B',1), Tile('C',1), Tile('D',1)]
        board.grid[4][8] = Cell(letter=Tile('A',1))
        board.grid[4][10] = Cell(letter=Tile('U',1))
        with self.assertRaises(InvalidRackException):
            game.descount_tiles_to_player(word, location, orientation)
  
    def test_convert_wildcard_fine(self):
        game = Scrabble(2)
        game.next_turn()
        game.current_player.rack = [Tile('?', 0)]
        game.convert_wild_card('A')
        self.assertEqual(game.current_player.rack[0].letter, 'A')
        self.assertEqual(game.current_player.rack[0].value, 1)

    def test_convert_wildcard_no_wildcard(self):
        game = Scrabble(2)
        game.next_turn()
        game.current_player.rack = [Tile('A', 1)]
        with self.assertRaises(InvalidWildCardConversion):
            game.convert_wild_card('B')
    
    def test_clean_word_to_use(self):
        game = Scrabble(2)
        word = 'Imaginación'
        self.assertEqual(game.clean_word_to_use(word), 'IMAGINACION')
    
    def test_comprobate_is_an_int_wrong_fine(self):
        game = Scrabble(2)
        string = '0'
        self.assertEqual(game.comprobate_is_an_int(string), 0)

    def test_comprobate_is_an_int_wrong(self):
        game = Scrabble(2)
        string = 'm'
        self.assertEqual(game.comprobate_is_an_int(string), None)
    
    def test_comprobate_is_an_orientation(self):
        game = Scrabble(2)
        orientation = 'm'
        self.assertEqual(game.comprobate_is_an_orientation(orientation), None)
        
    def test_get_current_player_id(self):
        game = Scrabble(2)
        game.next_turn()
        self.assertEqual(game.get_current_player_id(), 1)
if __name__ == '__main__':
    unittest.main()'''