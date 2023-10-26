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

	current_player = 0
	while not players[0].ship_board.all_ships_sunk() and not players[1].ship_board.all_ships_sunk():
		opposing_player = (current_player + 1) % 2
		player_turn(players[current_player], players[opposing_player])
		sunk = players[opposing_player].ship_board.check_ships()
		if sunk > 0:
			print("%s sunk %s's %s" % (players[current_player].name, players[opposing_player].name, ship_dict[sunk]) )
		current_player = opposing_player