from board import *

class Player:
	boards = [0,0]
	def __init__(self, board1, board2):
		board[0] = board1
		board[1] = board2 
		

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
		
	
	
