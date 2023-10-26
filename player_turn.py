from board import *

class Player:
	def __init__(self, in_board):
		self.ship_board = in_board
		self.attack_board = Board(create_empty_board(), board_type_enemy)
		

def player_turn(player_return):
	while True:
		player_input = input(f"{players[current_player]}, enter where you want to move: ")
		#gets the current players input
	
		if gameover:
			#checks to see if someone won
			print(f"{players[current_player]} wins!!!!")
			#whoever's turn it just was wins
			break
	
		current_player = (current_player + 1) % len(players)
		#switches to next player's turn assuming that nobody won
		
	
	
