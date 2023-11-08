# test_main.py

from main import Main
from Game.tile import Tile
from Game.cell import Cell
import unittest
from unittest.mock import patch
from io import StringIO
import io
import sys
from unittest.mock import call
from Game.scrabble import InvalidWordException, InvalidWildCardConversion, Scrabble

class TestMain(unittest.TestCase):
    def setUp(self):
        self.main_output = StringIO()
        self.real_stdout = sys.stdout
        sys.stdout = self.main_output

    def tearDown(self):
        sys.stdout = self.real_stdout

    @patch('builtins.input', side_effect=['2'])   
    def test_valid_player_count(self,mock_input):
        main = Main()
        number = "2"
        self.assertEqual(main.valid_player_count(number), True)

    @patch('builtins.input', side_effect=['3'])
    def test_valid_player_count_error(self, mock_input):
        main = Main()
        number = "name"
        self.assertEqual(main.valid_player_count(number), False)
    
    @patch('builtins.input', side_effect=['2'])
    def test_next_turn_main(self, mock_input):
        main = Main()
        self.assertEqual(main.game.turn, 0)
        main.game.next_turn()
        self.assertEqual(main.game.turn, 1)
    
    @patch('builtins.input', side_effect=['2', '1', '2'])
    def test_convert_tiles_in_another_tile(self, mock_input):
        main = Main()
        main.game.players[0].rack = [Tile('H', 4), Tile('O',1), Tile('L',1), Tile('A',1)]
        main.game.next_turn()
        numbers = [1, 2, 3, 4, 5, 6, 7]
        main.convert_tiles_in_another_tile(2, numbers)
        self.assertEqual(len(main.game.players[0].rack), 4)
    
    @patch('builtins.print')
    @patch('builtins.input', side_effect=['2', 'd', '0'])
    def test_convert_tiles_in_another_tile_wrong(self, mock_input, mock_print):
        main = Main()
        numbers = [1, 2, 3, 4, 5, 6, 7]
        main.convert_tiles_in_another_tile(4, numbers)
        expected_output = [
            call('Bienvenido'),
            call('Valor invalido, intente de nuevo'),]
        mock_print.assert_has_calls(expected_output, any_order=False)
        
    @patch('builtins.input', side_effect=['2', '2', '1', '3'])
    def test_exchange_tiles(self, mock_input):
        main = Main()
        main.game.players[0].rack = [Tile('H', 4), Tile('O',1), Tile('L',1), Tile('A',1)]
        main.game.next_turn()
        main.exchange_tiles()
        self.assertEqual(len(main.game.players[0].rack), 4)
    
    @patch('builtins.input', side_effect=['2', '1', '7'])
    def test_exchange_tiles_final_limit_index(self, mock_input):
        main = Main()
        main.game.players[0].rack = [Tile('H', 4), Tile('O',1), Tile('L',1), Tile('A',1), Tile('H', 4), Tile('O',1), Tile('L',1)]
        main.game.next_turn()
        main.exchange_tiles()
        self.assertEqual(len(main.game.players[0].rack), 7)

    @patch('builtins.input', side_effect=['2', '1', '0'])
    def test_exchange_tiles_initial_limit_index(self, mock_input):
        main = Main()
        main.game.players[0].rack = [Tile('H', 4), Tile('O',1), Tile('L',1), Tile('A',1), Tile('H', 4), Tile('O',1), Tile('L',1)]
        main.game.next_turn()
        main.exchange_tiles()
        self.assertEqual(len(main.game.players[0].rack), 7)

    @patch('builtins.print')
    @patch('builtins.input', side_effect=['2', 'd', '0'])
    def test_exchange_tiles_exit(self, mock_input, mock_print):
        main = Main()
        main.game.next_turn()
        main.exchange_tiles()
        expected_output = [
            call('Bienvenido'),
            call('Puedes apretar 0 para salir'),
            call('Valor invalido, intente de nuevo'),
        ]
        mock_print.assert_has_calls(expected_output, any_order=False)
    
    
    @patch('builtins.input', side_effect=['2', 'x', '0'])
    def test_reorganize(self, mock_input):
        main = Main()
        main.game.players[0].rack = [Tile('H', 4), Tile('O',1), Tile('L',1), Tile('A',1)]
        main.game.next_turn()
        self.assertEqual(len(main.game.players[0].rack), 4)
        main.reorganize()
        self.assertEqual(len(main.game.players[0].rack), 4)
   
    @patch('builtins.print')
    @patch('builtins.input', side_effect=['2'])
    def test_show_board(self, mock_input, mock_print):
        main = Main()
        #Se crea una matriz 2x2 para que sea más fácil de testear
        main.board.grid = [ 
            [Cell(), Cell()],
            [Cell(), Cell()]
        ]
        main.show_board()
        #Se crea una variable de lo que se espera que escriba en pantalla
        expected_output = [ 
            call('\n  |  0   1 '),
            call(' 0|  -   - '),
            call(' 1|  -   - ')
        ]
        mock_print.assert_has_calls(expected_output, any_order=False) #Se compara lo que se espera con lo que realmente imprimio
    
    @patch('builtins.print')
    @patch('builtins.input', side_effect=['2', '3', '2'])
    def test_take_turn_show_scores_and_pass_turn(self, mock_input, mock_print):
        main = Main()
        main.game.next_turn()
        main.game.current_player.rack = [Tile('A', 1), Tile('B', 1)]
        main.game.current_player.score = 16
        main.take_turn()
        expected_output = [
            call('Bienvenido'),
            call('Tú mano actual es: [A] [B]'),
            call('Puntajes de los jugadores:'),
            call('Jugador 1: Puntaje = 16'),
            call('Jugador 2: Puntaje = 0')
        ]
        mock_print.assert_has_calls(expected_output, any_order=False)
    
    @patch.object(Main, 'player_play', return_value=('hola', (7,7), 'H'))
    @patch('builtins.print')
    @patch('builtins.input', side_effect=['2', '1'])
    def test_take_turn_player_play(self, mock_input, mock_print, mock_object):
        main = Main()
        main.game.next_turn()
        player = main.game.current_player
        player.rack = [Tile('H', 4), Tile('O', 1), Tile('L', 1), Tile('A', 1)]
        main.take_turn()

    
    @patch('builtins.print')
    @patch('builtins.input', side_effect=['4'])
    def test_show_scores(self, mock_input, mock_print):
        main = Main()
        main.game.players[0].score = 90
        main.game.players[1].score = 172
        main.game.players[2].score = 78
        main.game.players[3].score = 134
        main.show_scores()
        expected_output = [
            call("Bienvenido"),
            call("Puntajes de los jugadores:"),
            call("Jugador 2: Puntaje = 172"),
            call("Jugador 4: Puntaje = 134"),
            call("Jugador 1: Puntaje = 90"),
            call("Jugador 3: Puntaje = 78")
        ]
        mock_print.assert_has_calls(expected_output, any_order=False)
    
    @patch('builtins.print')
    @patch('builtins.input', side_effect=['2', '5'])
    def test_player_play(self, mock_input, mock_print):
        main = Main()
        main.player_play()
        expected_output = [
            call("Bienvenido"),]
        mock_print.assert_has_calls(expected_output, any_order=False)
        
    @patch('builtins.print')
    @patch('builtins.input', side_effect=['2', '7', '5'])
    def test_player_play_incorret_way(self, mock_input, mock_print):
        main = Main()
        main.player_play()
        expected_output = [
            call("Bienvenido"),
            call('Valor invalido, intente de nuevo'),]
        mock_print.assert_has_calls(expected_output, any_order=False)
    
    @patch('builtins.input', side_effect=['2', 'hola', '7', '7', 'H'])
    def test_get_word_location_orientation(self, mock_input):
        main = Main()
        word, location, orientation = main.get_word_location_orientation()
        self.assertEqual(word, 'HOLA')
        self.assertEqual(location, (7,7))
        self.assertEqual(orientation, 'H')

    @patch('builtins.input', side_effect=['2', '0'])
    def test_get_word_location_orientation_return(self, mock_input):
        main = Main()
        word, location, orientation = main.get_word_location_orientation()
        self.assertEqual(word, '0')
        self.assertEqual(location, None)
        self.assertEqual(orientation, None)

    @patch.object(Main, 'get_word_location_orientation', return_value=('HOLA', (7,7), 'H'))
    @patch('builtins.input', side_effect=['2'])
    def test_placed_word(self, *args):
        main = Main()
        main.game.next_turn()
        player = main.game.current_player
        player.rack = [Tile('H', 4), Tile('O', 1), Tile('L', 1), Tile('A', 1)]
        main.place_word()
        self.assertEqual(len(player.rack), 0)
        self.assertEqual(player.score, 14)
        self.assertEqual(main.board.grid[7][7].letter.letter, 'H')
        self.assertEqual(main.board.grid[7][8].letter.letter, 'O')
        self.assertEqual(main.board.grid[7][9].letter.letter, 'L')
        self.assertEqual(main.board.grid[7][10].letter.letter, 'A')
    
    @patch.object(Main, 'get_word_location_orientation', return_value=('0', None, None))
    @patch('builtins.print')
    @patch('builtins.input', side_effect=['2', '0'])
    def test_placed_word_break(self, mock_input, mock_print, mock_object):
        main = Main()
        main.game.next_turn()
        player = main.game.current_player
        #player.rack = [Tile('H', 4), Tile('O', 1), Tile('L', 1), Tile('A', 1)]
        main.place_word()
        #expected_output = [
        #    call("Bienvenido"),
        #    call('Error: Su palabra no se cruza con ninguna palabra valida'),]
        #mock_print.assert_has_calls(expected_output, any_order=False)

    @patch.object(Main, 'get_word_location_orientation', return_value=('hola', (6,6), 'H'))
    @patch('builtins.print')
    @patch('builtins.input', side_effect=['2', '0',])
    def test_placed_word_exception(self, mock_input, mock_print, mock_object):
        main = Main()
        main.game.next_turn()
        player = main.game.current_player
        player.rack = [Tile('H', 4), Tile('O', 1), Tile('L', 1), Tile('A', 1)]
        main.place_word()
        expected_output = [
            call("Bienvenido"),
            call('Error: Su palabra no se cruza con ninguna palabra valida'),]
        mock_print.assert_has_calls(expected_output, any_order=False)

    @patch('builtins.input', side_effect=['2'])
    def test_get_tiles_to_full_rack(self, mock_input):
        main = Main()
        main.game.next_turn()
        main.game.current_player.rack = [Tile('A', 1), Tile('B', 1)]
        self.assertEqual(len(main.game.current_player.rack), 2)
        main.get_tiles_to_full_rack()
        self.assertEqual(len(main.game.current_player.rack), 7)
    
    @patch('builtins.input', side_effect=['2'])
    def test_get_tiles_to_full_rack_with_7_tiles_in_rack(self, mock_input):
        main = Main()
        main.game.next_turn()
        main.game.current_player.rack = [Tile('A', 1), Tile('B', 1), Tile('A', 1), Tile('B', 1), Tile('A', 1), Tile('B', 1), Tile('C', 1)]
        self.assertEqual(len(main.game.current_player.rack), 7)
        main.get_tiles_to_full_rack()
        self.assertEqual(len(main.game.current_player.rack), 7)
    
    @patch('builtins.input', side_effect=['2', 'A'])
    def test_change_wildcard_to_tile_true(self, mock_input):
        main = Main()
        main.game.next_turn()
        main.game.current_player.rack = [Tile('?', 0), Tile('B', 1)]
        main.change_wildcard_to_tile()
        self.assertEqual(main.game.current_player.rack[0].letter, 'A' )
    
    @patch('builtins.print')
    @patch('builtins.input', side_effect=['2', 'AB', 'A'])
    def test_change_wildcard_to_tile_second_try(self, mock_input, mock_print):
        main = Main()
        main.game.next_turn()
        main.game.current_player.rack = [Tile('?', 0), Tile('B', 1)]
        main.change_wildcard_to_tile()
        expected_output = [
            call('Bienvenido'),
            call('Valor invalido, intente de nuevo'),
            call('Se ha cambiado con exito')]
        mock_print.assert_has_calls(expected_output, any_order=False)
    
    @patch('builtins.print')
    @patch('builtins.input', side_effect=['2', 'A', '0'])
    def test_change_wildcard_exception(self, mock_input, mock_print):
        main = Main()
        main.game.next_turn()
        main.game.current_player.rack = [Tile('B', 1)]
        main.change_wildcard_to_tile()
        expected_output = [
            call('Bienvenido'),
            call('Error: No tienes un comodin en tu rack'),]
        mock_print.assert_has_calls(expected_output, any_order=False)
    
    @patch.object(Scrabble, 'put_initial_tiles_bag')
    @patch.object(Scrabble, 'put_tiles_in_rack')
    @patch.object(Scrabble, 'game_over', side_effect=[False, True])
    @patch.object(Scrabble, 'next_turn')
    @patch.object(Scrabble, 'get_current_player_id', return_value=(1))
    @patch.object(Main, 'show_board')
    @patch.object(Main, 'take_turn', return_value=('2'))
    @patch.object(Main, 'get_tiles_to_full_rack')
    @patch.object(Main, 'show_scores')
    @patch('builtins.print')
    @patch('builtins.input', side_effect=['2', 'A', '0'])
    def test_play_game(self, mock_input, mock_print, *args):
        Main().play_game()