"""
board.py
Defines board class and some constant values
"""


# Constants
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



ship_dict = {0 : "", 1 : "Destroyer", 2 : "Submarine", 3 : "Cruiser", 4 : "Battleship", 5 : "Carrier"}
ship_lengths = (0, 2, 3, 3, 4, 5)
ship_characters = ("~", "D", "S", "U", "B", "C", "@", "@", ".", "X", "X", "X", "X", "X", "X", "X")

class Board:
	sunk_ships = [0, False, False, False, False, False]
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
				string += (" %s" % ship_characters[self.board[y][x]])
			string += "\n"
		return string
				
	def try_hit(self, row, column):
		
		# Check if hit is out of bounds or if the space was already hit
		if row < 0 or row >= board_height or column < 0 or column >= board_width or self.board[row][column] & board_bit_hit == board_bit_hit:
			return board_move_invalid
		# Set the board to be hit on this spot (ship data stays intact)
		self.board[row][column] |= board_bit_hit
		# Check if there's a ship on the space
		if self.board[row][column] & board_bit_ship != 0:
			return board_move_hit
		# Nothing was hit. Miss
		return board_move_miss

	def all_ships_sunk(self):
		return self.sunk_ships[1] and self.sunk_ships[2] and self.sunk_ships[3] and self.sunk_ships[4] and self.sunk_ships[5]

	def check_ships(self):
		# Check the ships that have been sunk by counting ship spaces that aren't hit
		# Returns either that no ships have been hit or the ship that has been sunk this turn
		# Should be run after every turn
		ship_spots_left = {0 : 0, 1 : 0, 2 : 0, 3 : 0, 4 : 0, 5 : 0}
		ship_sunk = 0
		for y in range(0, board_height):
			for x in range(0, board_width):
				if self.board[y][x] & board_bit_hit == 0 and self.board[y][x] & board_bit_ship > 0:
					ship_spots_left[self.board[y][x]] += 1
		for ship in ship_spots_left.keys():
			if ship == 0:
				continue
			if ship_spots_left[ship] == 0:
				if self.sunk_ships[ship] == False:
					# We can guarantee that the only ship that was sunk this turn is this one
					ship_sunk = ship
				self.sunk_ships[ship] = True
		return ship_sunk


def create_empty_board():
	empty_list = []
	empty_row = []
	for i in range(0,board_width):
		empty_row.append(0)
	for i in range(0,board_height):
		empty_list.append(empty_row.copy())
	return empty_list