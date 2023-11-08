# tools.py

from colorama import Fore, Style

class Tools:
    def move_pointer(self, orientation, row, column):
        if orientation == "H":
            column += 1
        elif orientation == "V":
            row += 1
        return row, column
    
    def is_active_and_letter_multiplier(self,cell):
        return cell.status == 'active' and cell.multiplier_type == 'letter'

    def is_active_and_word_multiplier(self,cell):
        return cell.status == 'active' and cell.multiplier_type == 'word'

    def format_placed_word_cell(self, cell):
        return f" {cell.letter.letter} "

    def format_active_cell(self, cell):
        if cell.status == 'active':
            return self.format_cell_contents(cell)

    def format_cell_contents(self, cell):
        if cell.letter is None:
            return self.format_multiplier(cell.multiplier, cell.multiplier_type)
        else:
            return self.format_placed_word_cell(cell)

    def format_multiplier(self, multiplier, multiplier_type):
        if multiplier_type == 'word':
            colors = {2: Fore.LIGHTMAGENTA_EX, 3: Fore.RED}
        elif multiplier_type == 'letter':
            colors = {2: Fore.CYAN, 3: Fore.BLUE}
        else:
            return " - "

        return f"{colors.get(multiplier, '')}{multiplier}{multiplier_type[0].upper()}{Style.RESET_ALL} "
    
    def filter_reapeted_column(self, list_tuples):
        columns = {}
        for row, column in list_tuples:
            if column not in columns:
                columns[column] = (row, column)
        list_tuples = list(columns.values())
        return list_tuples
    
    def filter_reapeted_row(self, list_tuples):
        rows = {}
        for row, column in list_tuples:
            if row not in rows:
                rows[row] = (row, column)
        list_tuples = list(rows.values())
        return list_tuples
