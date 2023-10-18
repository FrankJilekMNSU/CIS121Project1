players = ["Player 1", "Player 2"]

current_player = 0
#Initialization of players

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
		
	
	
