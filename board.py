"""
board.py
Defines board class and some constant values
"""


board_type_enemy = 0
board_type_player = 1

board_move_invalid = 0
board_move_hit = 1
board_move_miss = 2

board_width = 10
board_height = 10

# 0 0 0 0 1 0 1 1
#         | | | |
#         | +-+-+-- These three bits are the number associated with the ship. 0 means no ship
#         +-- 1 if hit. 0 if not. Can still be 1 even if there's no ship (indicates a miss)
# the board value gets bitwise anded with these values to check if a ship has been hit and to filter out the ship number
board_bit_hit = 8
board_bit_ship = 7


ships_dict = {0 : "", 1 : "Destroyer", 2 : "Submarine", 3 : "Cruiser", 4 : "Battleship", 5 : "Carrier"}

ships_characters = ("~", "D", "S", "U", "B", "C", "@", "@", ".", "X", "X", "X", "X", "X", "X", "X")

class Board:
	def __init__(self, board_list, board_type):
		self.board = board_list
		self.type = board_type
	def __str__(self):
		string = " "
		for i in range(0, board_width):
			string += (" %d" % (i+1))
		string += "\n"
		for y in range(0, board_height):
			string += chr(0x41 + y)
			for x in range(0, board_width):
				string += (" %s" % ships_characters[self.board[y][x]])
			string += "\n"
		return string
				
	def try_hit(self, row, column):
		if row < 0 or row > board_height or column < 0 or column > board_width or self.board[row][column] & board_bit_hit == board_bit_hit:
			return board_move_invalid
		if self.board[row][column] & board_bit_ship != 0:
			self.board[row][column] |= board_bit_hit
			return board_move_hit
		return board_move_miss
