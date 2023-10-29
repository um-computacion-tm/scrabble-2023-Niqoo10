# tools.py

from colorama import Fore, Style

class Tools:
    def move_pointer(self, orientation, row, column):
        # Mueve el puntero en la dirección especificada.
        if orientation == "H":
            column += 1
        elif orientation == "V":
            row += 1
        return row, column

    def is_active_and_letter_multiplier(self, cell):
        # Verifica si una celda está activa y tiene un multiplicador de letra.
        return cell.status == 'active' and cell.multiplier_type == 'letter'

    def is_active_and_word_multiplier(self, cell):
        # Verifica si una celda está activa y tiene un multiplicador de palabra.
        return cell.status == 'active' and cell.multiplier_type == 'word'

    def format_placed_word_cell(self, cell):
        # Formatea una celda con una letra colocada.
        return f" {cell.letter.letter} "

    def format_active_cell(self, cell):
        # Formatea una celda activa.
        if cell.status == 'active':
            return self.format_cell_contents(cell)

    def format_cell_contents(self, cell):
        # Formatea el contenido de una celda.
        if cell.letter is None:
            return self.format_multiplier(cell.multiplier, cell.multiplier_type)
        else:
            return self.format_placed_word_cell(cell)

    def format_multiplier(self, multiplier, multiplier_type):
        # Formatea el multiplicador de la celda.
        if multiplier_type == 'word':
            colors = {2: Fore.LIGHTMAGENTA_EX, 3: Fore.RED}
        elif multiplier_type == 'letter':
            colors = {2: Fore.CYAN, 3: Fore.BLUE}
        else:
            return " - "

        return f"{colors.get(multiplier, '')}{multiplier}{multiplier_type[0].upper()}{Style.RESET_ALL} "

    def filter_repeated_column(self, list_tuples):
        # Filtra las columnas repetidas en una lista de tuplas.
        columns = {}
        for row, column in list_tuples:
            if column not in columns:
                columns[column] = (row, column)
        list_tuples = list(columns.values())
        return list_tuples

    def filter_repeated_row(self, list_tuples):
        # Filtra las filas repetidas en una lista de tuplas.
        rows = {}
        for row, column in list_tuples:
            if row not in rows:
                rows[row] = (row, column)
        list_tuples = list(rows.values())
        return list_tuples


'''from colorama import Fore, Style

class Tools:
    def move_pointer(self, orientation, row, column):
        # Mueve un puntero en una dirección (H para horizontal, V para vertical).
        if orientation == "H":
            column += 1
        elif orientation == "V":
            row += 1
        return row, column

    def is_active_and_multiplier(self, cell, multiplier_type):
        # Verifica si una celda es activa y tiene un tipo de multiplicador específico ('word' o 'letter').
        return cell.status == 'active' and cell.multiplier_type == multiplier_type

    def format_placed_word_cell(self, cell):
        # Formatea una celda con una letra colocada.
        return f" {cell.letter.letter} "

    def format_active_cell(self, cell):
        # Formatea una celda activa (llama a format_cell_contents para el contenido).
        if cell.status == 'active':
            return self.format_cell_contents(cell)

    def format_cell_contents(self, cell):
        # Formatea el contenido de una celda (multiplicador o letra colocada).
        if cell.letter is None:
            return self.format_multiplier(cell.multiplier, cell.multiplier_type)
        else:
            return self.format_placed_word_cell(cell)

    def format_multiplier(self, multiplier, multiplier_type):
        # Formatea un multiplicador con colores según su tipo ('word' o 'letter').
        multiplier_colors = {
            'word': {2: Fore.LIGHTMAGENTA_EX, 3: Fore.RED},
            'letter': {2: Fore.CYAN, 3: Fore.BLUE},
        }

        colors = multiplier_colors.get(multiplier_type, {})
        return f"{colors.get(multiplier, '')}{multiplier}{multiplier_type[0].upper()}{Style.RESET_ALL} "

    def filter_repeated(self, list_tuples, key_index):
        # Filtra las tuplas duplicadas en una lista basándose en un índice clave.
        unique_values = {}
        result = []

        for item in list_tuples:
            key = item[key_index]
            if key not in unique_values:
                unique_values[key] = item
                result.append(item)

        return result'''
