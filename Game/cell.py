from Game.tile import Tile
from Game.tools import Tools

class Cell:
    def __init__(self, multiplier=1, multiplier_type='', letter=None, status='active'):
        self.multiplier = multiplier
        self.multiplier_type = multiplier_type
        self.letter = letter
        self.status = status
        self.original_state = {'multiplier': multiplier, 'multiplier_type': multiplier_type, 'letter': letter, 'status': 'active'}
    def add_letter(self,letter:Tile):
        self.letter = letter
    def calculate_value(self):
        if self.letter is None:
            return 0
        if self.multiplier_type == 'letter':
            return self.letter.value * self.multiplier
        if self.multiplier_type == 'word':
            return self.letter.value
    def deactive_cell(self):
        self.status = 'desactive'
    def reset_cell(self):
        self.letter = self.original_state.get('letter')
        self.status = self.original_state.get('status')
        self.multiplier = self.original_state.get('multiplier')
        self.multiplier_type = self.original_state.get('multiplier_type')
    def __repr__(self):
        tool = Tools()
        if self.status == "active":
            return tool.format_active_cell(self)
        else:
            return tool.format_cell_contents(self)
