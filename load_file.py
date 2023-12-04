"""
Creston Dorothy
Frank Jilek
August Peterson
CIS 121 Final Project

load_file.py
Here lies the function to load the ship positions from a file
"""

import board
import csv
import os

def load_board(filename):
	# Declaring lists to append to later
	player_board = [] # Will be returned at the end of the function	
	ships = []
	if not os.path.isfile(filename): # Check if filename is valid and return with error value if not
		print("ERROR! \"%s\" is not a valid file!")
		return -1
	with open(filename) as board_file:
		board_reader = csv.reader(board_file, delimiter=',')
		ship_count = 0
		for row in board_reader:
			if ship_count >= 5:
				break
			ship = [ ord(row[0]) - 0x41, int(row[1])-1, int(row[2]) ]
			ships.append(ship)
			ship_count += 1
	# Create a list of 0s to fill the board with initially
	default_board_row = []
	for i in range(0, board.board_width):
		default_board_row.append(0)
	for i in range(0, board.board_height):
		player_board.append(default_board_row.copy())

	ship_num = 1
	for ship in ships:
		max_y = ship[0] + (ship[2] * board.ship_lengths[ship_num])
		max_x = ship[1] + ((ship[2] ^ 1) * board.ship_lengths[ship_num])
		# The math here works out so that the length is multiplied by 1 for one value and multiplied by 0 for the other

		# Check to see if the ship is in bounds
		if ship[0] < 0 or ship[0] > board.board_height \
		  or ship[1] < 0 or ship[1] > board.board_width \
		  or (ship[2] != 0 and ship[2] != 1) \
		  or max_y > board.board_height or max_x > board.board_width:
			print("ERROR! Invalid ship setup (ship out of bounds or invalid direction) (ship %d)" % ship_num)
			return -2

		# Iterate i through the length of the ship to set the values of player_board
		for i in range(0, board.ship_lengths[ship_num]):
			y = ship[0]
			x = ship[1]
			if ship[2] == 0:
				x += i
			else:
				y += i
			if player_board[y][x] != 0:
				print("ERROR! Invalid ship setup (ship colliding) (ship %d)" % ship_num)
				return -2
			player_board[y][x] = ship_num
		ship_num += 1

	return player_board

