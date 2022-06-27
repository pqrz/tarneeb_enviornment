import random
import numpy as np

card_value_dict = {'A': 14, 
 'K': 13,
 'Q': 12,
 'J': 11
}

def get_card_value(card_name):
	#import pdb; pdb.set_trace()
	#return card_value_dict.get(card_name[0], int(card_name[0]) )
	return card_name.cardId()

def get_highest_card(card_name_list):
	highest_card = ''
	highest_value = 0
	for card_name in card_name_list:
		card_value = get_card_value(card_name)
		if highest_value <= card_value:
			highest_value = card_value
			highest_card = card_name
	return highest_card
	

class Player:
	def __init__(self, name, max_card_strategy):
		self.name = name
		self.quiver = []
		self.wins = 0
		self.max_card_strategy = max_card_strategy
	def __repr__(self):
		return self.name + ": " + str(self.hand) + "\t" + str(self.quiver)
	def setHand(self, cards):
		self.hand = cards
	def clearHand(self):
		self.hand = []
	def filterCardsByType(self, cType):
		nh = []
		for c in self.hand:
			if(c.type == cType):
				nh.append(c)
		return nh

	def playCard(self, cards = []):
		crd = self.chooseCard(self.hand)
		if(len(cards) > 0):
			fh = self.filterCardsByType(cards[0].type)
			if(len(fh) > 0):
				if self.max_card_strategy and (self.name == 'p0'):
					crd = self.chooseCard_max(fh)
				else:
					crd = self.chooseCard(fh)
		self.hand.pop(self.hand.index(crd))
		return crd

	def chooseCard(self, ligalCards):
		return random.choice(ligalCards)

	def chooseCard_max(self, fh):
		return get_highest_card(fh)
		#import pdb; pdb.set_trace()

	def handToArray(self):
		ret = np.zeros(52)
		for c in self.hand:
			ret[c.cardId()] = 1
		return ret

	def win(self, tour):
		self.wins += 1

	def getScoreTarneeb(self):
		return self.wins