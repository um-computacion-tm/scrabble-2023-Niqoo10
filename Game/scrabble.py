# scrabble.py

from Game.board import Board
from Game.player import Player
from Game.bagtiles import BagTiles
from Game.models import Miscellaneos
from Game.dictionary import Dictionary
from Game.wordconverter import Converter
import random
import uuid

class InvalidWordException(Exception):
    pass

class InvalidRackException(Exception):
    pass

class InvalidWildCardConversion(Exception):
    pass

class Scrabble:
    def __init__(self,player_count):
        self.board = Board()
        self.bagtiles = BagTiles()
        self.gameid = str(uuid.uuid4())
        self.players = []
        for index in range(player_count):
            self.players.append(Player(id=index + 1))
        self.current_player = None
        self.turn = 0
        self.dict = Dictionary()
            
    def playing(self):
        return True
    
    def next_turn(self):
        if self.current_player is None:
            self.current_player = self.players[0]
        elif self.current_player == self.players[-1]:
            self.current_player = self.players[0]
        else:
            player_turn = self.players.index(self.current_player) + 1
            self.current_player = self.players[player_turn]
        self.turn += 1

    def validate_word(self, word, location, orientation):
        if not self.dict.verify_word(word):
            raise InvalidWordException('Su palabra no existe en el diccionario')
        if not self.board.validate_word_inside_board(word, location, orientation):
            raise InvalidWordException('Su palabra excede el tablero')
        if not self.board.validate_word_place_board(word, location, orientation):
            raise InvalidWordException('Su palabra no se cruza con ninguna palabra valida')
        if not self.board.validate_words_around(word, location, orientation):
            raise InvalidWordException('Su palabra forma palabras invalidas')
        return True
    
    def calculate_score(self, word, location, orientation):
        converter = Converter()
        misc = Miscellaneos()
        residual_words = []
        self.board.validate_words_around(word, location, orientation, residual_words)
        new_word = converter.word_to_cells(word, location, orientation, self.board)
        score = misc.calculate_word_value(new_word)
        self.current_player.score += score
        if len(residual_words) > 0:
            for word in residual_words:
                residual_word_in_cells = converter.word_to_false_cells(word)
                score = misc.calculate_word_value(residual_word_in_cells)
                self.current_player.score += score
           
    def get_board(self):
        return self.board
    
    def put_word(self, word, location, orientation):
        self.board.put_words_board(word, location, orientation)

    def show_amount_tiles_bag(self):
        return len(self.bagtiles.tiles)
      
    def shuffle_rack(self):
        random.shuffle(self.current_player.rack)
    
    def game_over(self):
        if len(self.bagtiles.tiles) == 0:
            return True
        return False
    
    def put_tiles_in_rack(self, amount=7):
        bag = self.bagtiles
        if self.turn == 0:
            for i in range(len(self.players)):
                self.players[i].get_tiles(amount, bag)
        elif amount < len(bag.tiles):
            self.current_player.get_tiles(amount, bag)
        else:
            self.current_player.get_tiles(len(bag.tiles), bag)
        
    def descount_tiles_to_player(self, word, location, orientation):
        misc = Miscellaneos()
        tiles_required = misc.tiles_needed_to_form_word(word, location, orientation, self.board)
        if not self.current_player.has_letters(tiles_required):
            raise InvalidRackException('No tienes las fichas suficientes')
        for letter in tiles_required:
            tile_to_remove = next(tile for tile in self.current_player.rack if tile.letter == letter.letter)
            self.current_player.rack.remove(tile_to_remove)

    def put_initial_tiles_bag(self):
        self.bagtiles.initial_tiles()
    
    def convert_wild_card(self, new_letter):
        bag = BagTiles()
        if self.current_player.has_wildcard() is True:
            index = self.current_player.find_wildcard()
            wildcard = self.current_player.rack[index]
            matching_tile = next((t for t in bag.tiles if t.letter == new_letter), None)
            if matching_tile.letter == new_letter:
                wildcard.convert_tile(new_letter, matching_tile.value)
        else:
            raise InvalidWildCardConversion('No tienes un comodin en tu rack')
    
    def clean_word_to_use(self, word):
        dic = Dictionary()
        word = dic.remove_accents(word)
        word = word.strip().upper()
        return word
    
    def comprobate_is_an_int(self, string):
        try:
            return int(string)
        except ValueError:
            return None

    def comprobate_is_an_orientation(self, orientation):
        real_orientation = ['H', 'V']
        if orientation in real_orientation:
            return orientation
        else:
            return None
    
    def get_current_player_id(self):
        return self.current_player.id
