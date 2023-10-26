from board import *

class Player:
	def __init__(self, in_board, name):
		self.ship_board = in_board
		self.attack_board = Board(create_empty_board(), board_type_enemy)
		self.name = name
		

def player_turn(player1, player2):
	print(f"{player1.name}'s turn. Press any key to continue...")
	input()
	print(player1.ship_board)
	print(player1.attack_board)
	valid_move = False
	hit = 0
	row = 0
	column = 0
	while not valid_move:
		player_input = input(f"{player1.name} Attack: ")
		if len(player_input) < 2 or len(player_input) > 3:
			valid_move = False
			print("Invalid input")
		row = ord(player_input[0]) - 0x41
		column = int(player_input[1:len(player_input)])-1
		if column < 0 or column > board_width or row < 0 or row > board_height:
			valid_move = False
			print("Invalid location")
			continue
		hit = player2.ship_board.try_hit(row, column)
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