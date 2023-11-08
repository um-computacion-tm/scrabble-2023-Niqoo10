#main.py 

from Game.scrabble import Scrabble, InvalidWordException, InvalidWildCardConversion, InvalidRackException

class Main:
    def __init__(self):
        print('¡BIENVENIDO!')
        self.player_count = self.get_player_count()
        self.game = Scrabble(self.player_count)
        self.board = self.game.get_board()

    def valid_player_count(self,player_count):
        try:
            count = int(player_count)
            return 2 <= count <= 4
        except ValueError:
            return False
            
    def get_player_count(self):
        while True:
            player_count = input('JUGADORES (2-4): ')
            if self.valid_player_count(player_count) is True:
                return int(player_count)
            print('JUGADORES INCORRECTOS (2-4)')

    def show_board(self):
        print('\n  |' + ''.join([f' {str(row_index).rjust(2)} ' for row_index in range(len(self.board.grid))]))
        for row_index, row in enumerate(self.board.grid):
            print(
                str(row_index).rjust(2) +
                '| ' +
                ' '.join([repr(cell) for cell in row])
            )
    
    def show_rack(self):
        return ' '.join(f'[{tile.letter}]' for tile in self.game.current_player.rack)
    
    def take_turn(self):
        print(f'TUS FICHAS: {self.show_rack()}')
        while True:
            action = input('SELECCIONA --> JUGAR(1) / PASAR(2) / PUNTUACION(3): ')
            action = self.game.comprobate_is_an_int(action)
            if action == 1:
                self.player_play()
                break
            elif action == 2:
                break
            elif action == 3:
                self.show_scores()
    
    def player_play(self):
        actions = {1: self.place_word, 2: self.reorganize, 3: self.exchange_tiles, 4: self.change_wildcard_to_tile, 5: self.quite_game }
        while True:
            action = input('SELECCIONA --> COLOCAR(1) / REORGANIZAR(2) / INTERCAMBIAR(3) / CONVERTIR COMODÍN(4) / PASAR(5) ')
            action = self.game.comprobate_is_an_int(action)
            action_function = actions.get(action)
            if action_function is None:
                print('VALOR INVALIDO, INTENTA NUEVAMENTE')
            elif self.player_action(action_function):
                break

    
    def player_action(self, action_function):
        if action_function is not None:
            action_result = action_function()
            if action_result == 'finish':
                return True

    def quite_game(self):
        return 'finish'
    
    def show_scores(self):
        sorted_players = sorted(self.game.players, key=lambda player: player.score, reverse=True) #Sorted es una función para ordenar listas
        #Los parametros de sorted es para que ordene por el atributo score y de manera descendente
        print("Puntajes de los jugadores:")
        for _, player in enumerate(sorted_players, start=1):
            print(f"Jugador {player.id}: Puntaje = {player.score}")
    
    def place_word(self):
        while True:
            try:
                word, location, orientation = self.get_word_location_orientation()
                if word == '0':
                    break
                self.validate_and_put_word(word, location, orientation)
                return 'finish'
            except (InvalidWordException, InvalidRackException) as e:
                print(f'Error: {e}')
                validate = input('PRESIONA CUALQUIER TECLA PARA CONTINUAR: ')
                if validate == '0':
                    break
    
    def get_word_location_orientation(self):
        while True:
            word = input('INGRESE LA PALABRA / (0) PASAR: ')
            word = self.game.clean_word_to_use(word)
            if word == '0':
                return word, None, None
            location_x = input('INGRESE LA FILA (0-14): ')
            location_x = self.game.comprobate_is_an_int(location_x)
            location_y = input('INGRESE LA COLUMNA (0-14): ')
            location_y = self.game.comprobate_is_an_int(location_y)
            location = (location_x, location_y)
            orientation = input('INGRESE ORIENTACIÓN (V/H): ')
            orientation = orientation.strip().upper()
            orientation = self.game.comprobate_is_an_orientation(orientation)
            return word, location, orientation
    
    def validate_and_put_word(self, word, location, orientation):
        if self.game.validate_word(word, location, orientation):
            self.game.descount_tiles_to_player(word, location, orientation)
            self.game.calculate_score(word, location, orientation)
            self.game.put_word(word, location, orientation)
            

    def exchange_tiles(self):
        print('(0) SALIR')
        while True:
            amount = input("¿CUANTAS FICHAS QUIERES CAMBIAR? (1-7): ")
            amount = self.game.comprobate_is_an_int(amount)
            numbers = [1, 2, 3, 4, 5, 6, 7]
            if amount in numbers:
                self.convert_tiles_in_another_tile(amount, numbers)
                return 'finish'
            elif amount == 0:
                break
            else: 
                print('VALOR INVALIDO, INTENTA NUEVAMENTE')
    
    def convert_tiles_in_another_tile(self, amount, numbers):
        for i in range(amount):
            index = input("ELIJE LAS FICHAS PARA CAMBIAR UNA A UNA (1-7): ")
            index = self.game.comprobate_is_an_int(index)
            if index in numbers:
                self.game.current_player.exchange_tiles(index, self.game.bagtiles)
            elif index == 0:
                break
            else:
                print('VALOR INVALIDO, INTENTA NUEVAMENTE')

    def reorganize(self):
        while True:
            self.game.shuffle_rack()
            print(f'{self.show_rack()}')
            organize = input("APRETA CUALQUIER TECLA O (0 PARA TERMINAR): ")
            organize = organize.strip().upper()
            if organize == "0":
                break
    
    def change_wildcard_to_tile(self):
        while True:
            try:
                if self.convert_wildcard_into_tile():
                    break
            except InvalidWildCardConversion as e:
                print(f'Error: {e}')
    
    def convert_wildcard_into_tile(self):
        new_letter = input('SELECCIONE LA LETRA DEL COMODIN (0 para terminar): ')
        new_letter= new_letter.strip().upper()
        alphabet = ['A', 'B', 'C', 'CH', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'LL', 'M', 'N','Ñ', 'O', 'P', 'Q', 'R', 'RR', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']
        if new_letter in alphabet:
            self.game.convert_wild_card(new_letter)
            print('COMODIN CAMBIADO')
            return True
        elif new_letter == '0':
            return True
        else:
            print('VALOR INVALIDO, INTENTA NUEVAMENTE')
            return False
    
    def get_tiles_to_full_rack(self):
        amount_tiles_needed = 7 - len(self.game.current_player.rack)
        if amount_tiles_needed == 0:
            return
        elif amount_tiles_needed > 0:
            self.game.put_tiles_in_rack(amount_tiles_needed)

    def play_game(self):
        print('¡QUE EMPIECE EL JUEGO!')
        self.game.put_initial_tiles_bag()
        self.game.put_tiles_in_rack()        
        while not self.game.game_over():
            self.game.next_turn()
            self.show_board()
            player_number = self.game.get_current_player_id()
            print(f'TURNO DEL JUGADOR {player_number}')
            self.take_turn()
            self.get_tiles_to_full_rack()
        print('¡JUEGO TERMINADO!')
        self.show_scores()


if __name__ == "__main__":
    main = Main()
    main.play_game()