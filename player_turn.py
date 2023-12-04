from board import *
"""
Creston Dorothy
Frank Jilek
August Peterson
CIS 121 Final Project

player_turn.py
Contains the function executed in the main game loop
"""

class Player:
	# Initialize with a board of ships & a name
	def __init__(self, in_board, name):
		self.ship_board = in_board
		self.attack_board = Board(create_empty_board(), board_type_enemy)
		self.name = name

def is_not_letter(character):
	return ord(character) > ord('Z') or ord(character) < ord('A')

def is_not_number(character):
	return ord(character) > ord('9') or ord(character) < ord('0')

def player_turn(player1, player2):
	print(f"{player1.name}'s turn. Press enter to continue...")
	input()
	print(player1.attack_board)
	print(player1.ship_board)
	valid_move = False
	hit = 0
	row = 0
	column = 0
	# Keep getting player input until they enter a valid move
	while not valid_move:
		player_input = input(f"{player1.name} Attack: ")
		# Check for invalid inputs (string too long/short; not formatted correctly)
		if len(player_input) < 2 or len(player_input) > 3:
			valid_move = False
			print("Invalid input")
			continue
		if is_not_letter(player_input[0]): 
			valid_move = False
			print("Invalid input")
			continue
		caught = False
		for i in range(1, len(player_input)):
			if is_not_number(player_input[i]):
				valid_move = False
				caught = True
				print("Invalid input")
				break
		if caught:
			continue
		# subtract 'A' from the input to convert letters to numbers starting from 0
		row = ord(player_input[0]) - ord('A')
		# convert the end of the string to a number
		column = int(player_input[1:len(player_input)])-1
		# Check bounds
		if column < 0 or column >= board_width or row < 0 or row >= board_height:
			valid_move = False
			print("Invalid location")
			continue
		hit = player2.ship_board.try_hit(row, column)
		# Check if spot was hit already
		if hit == board_move_invalid:
			valid_move = False
			print("Spot has already been attacked")
		else:
			valid_move = True
	if hit == board_move_hit:
		player1.attack_board.board[row][column] = 9
		print("Hit!")
	else:
		player1.attack_board.board[row][column] = 8
		print("Miss!")
