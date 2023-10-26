from load_file import load_board
from board import *
from player_turn import *

if __name__ == "__main__":
	player1_name = input("Player 1, enter name: ")
	player1_filename = input("%s, enter the file to load ships from: " % player1_name)
	player1_board = Board(load_board(player1_filename), board_type_player)
	player2_name = input("Player 2, enter name: ")
	player2_filename = input("%s, enter the file to load ships from: " % player2_name)
	player2_board = Board(load_board(player2_filename), board_type_player)

	players = [Player(player1_board, player1_name), Player(player2_board, player2_name)]

	print(players[0].ship_board)
	print(players[1].ship_board)

	
	