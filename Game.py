# from Cards.StandarDeck import StandarDeck
from StandarDeck import StandarDeck
from Player import Player
import random
import sys

#def distripute(players):
	#for i in range(4):
	#	 players[i].setHand(standardeck.distripute(13))
	#	 #print(players[i])


if len(sys.argv)>=2: 
	max_card_strategy = True
else:
	max_card_strategy = False


def simulate_one_game():
	standardeck = StandarDeck()
	#tarneeb = None
	tarneeb = random.choice(["club", "diamond", "heart", "spade"])
	
	players = []
	for i in range(4):
		players.append(Player("p" + str(i), max_card_strategy) )
	
	#distripute(players)
	for i in range(4):
		players[i].setHand(standardeck.distripute(13))
	
	winner = 0
	#for j in range(2):
	j = 0
	while len(players[0].hand) > 0:
		j += 1
		#print(str(j) + "----------------------------------------------------------------------------")
		tour = []
		for i in range(4):
			tour.append(players[(i + winner)%4].playCard(tour))
			#print(tour)
		winner = (standardeck.winner(tour, tarneeb) + winner)%4
		players[winner].win(tour)
		#for i in range(4):
		#	print(players[i])

	best_player = ''
	best_score	= 0
	for i in range(4):
		#print(players[i].name, ": ", players[i].getScoreTarneeb())
		if best_score < players[i].getScoreTarneeb():
			#best_player = players[i].name
			best_score = players[i].getScoreTarneeb()
	
	best_player = random.choice([players[i].name for i in range(4) if players[i].getScoreTarneeb()==best_score])
	return best_player


def simulate_multiple_game(n):
	player_dict = {}
	for i in range(n):
		best_player = simulate_one_game()
		#print(best_player)
		player_dict[best_player] = player_dict.get(best_player, 0) + 1 
		#print('-'*50)
	for key, value in player_dict.items():
		player_dict[key] = value / n
	print(player_dict)

	
simulate_multiple_game(10_000)




