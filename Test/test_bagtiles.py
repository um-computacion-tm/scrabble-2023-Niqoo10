# test_bagtiles.py

import unittest
from Game.bagtiles import BagTiles
from Game.tile import Tile

class TestBagTiles(unittest.TestCase):
    # Método de configuración que se ejecuta antes de cada prueba
    def setUp(self):
        # Crear una instancia de la clase BagTiles para cada prueba
        self.bag = BagTiles()

    # Prueba: Tomar un número positivo de fichas del saco
    def test_take_positive(self):
        # Llamar al método take para tomar 3 fichas
        tiles = self.bag.take(3)
        # Verificar que se tomaron exactamente 3 fichas
        self.assertEqual(len(tiles), 3)
        # Verificar que la cantidad de fichas restantes en el saco es 27
        self.assertEqual(len(self.bag.tiles), 27)

    # Prueba: Intentar tomar más fichas de las que hay disponibles
    def test_take_negative(self):
        # Intentar tomar 30 fichas del saco (que inicialmente contiene 28)
        tiles = self.bag.take(30)
        # Verificar que solo se tomaron las 28 fichas disponibles
        self.assertEqual(len(tiles), 28)
        # Verificar que el saco está vacío (0 fichas restantes)
        self.assertEqual(len(self.bag.tiles), 0)

    # Prueba: Agregar una lista de fichas al saco
    def test_put(self):
        # Crear una lista de fichas
        tiles = [Tile('A', 1), Tile('B', 3)]
        # Llamar al método put para agregar las fichas al saco
        self.bag.put(tiles)
        # Verificar que el número total de fichas en el saco es 30
        self.assertEqual(len(self.bag.tiles), 30)

    # Prueba: Agregar una ficha con una cantidad específica al saco
    def test_put_amount(self):
        # Crear una ficha 'C' con valor 2
        tile = Tile('C', 2)
        # Llamar al método put para agregar 2 fichas 'C' al saco
        self.bag.put(tile, amount=2)
        # Verificar que el número total de fichas en el saco es 30
        self.assertEqual(len(self.bag.tiles), 30)

    # Prueba: Obtener el valor de una ficha por su letra
    def test_get_value_for_letter(self):
        # Llamar al método get_value_for_letter para obtener el valor de la ficha 'A'
        value = self.bag.get_value_for_letter('A')
        # Verificar que el valor obtenido es 1
        self.assertEqual(value, 1)

    # Prueba: Inicializar el saco con fichas siguiendo una distribución predefinida
    def test_initial_tiles(self):
        # Llamar al método initial_tiles para inicializar el saco
        self.bag.initial_tiles()
        # Verificar que el número total de fichas en el saco es 100
        self.assertEqual(len(self.bag.tiles), 100)

    # Prueba: Convertir una ficha a una nueva letra y valor
    def test_convert_tile(self):
        # Crear una ficha 'A' con valor 1
        tile = Tile('A', 1)
        # Llamar al método convert_tile para cambiarla a 'B' con valor 3
        tile.convert_tile('B', 3)
        # Verificar que la letra de la ficha es 'B'
        self.assertEqual(tile.letter, 'B')
        # Verificar que el valor de la ficha es 3
        self.assertEqual(tile.value, 3)

# Si se ejecuta este archivo directamente, se inicia el conjunto de pruebas
if __name__ == '__main__':
    unittest.main()
