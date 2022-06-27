# from Cards.Card import CardValue
from Card import CardValue
# from Cards.Card import CardType
from Card import CardType
# from Cards.Card import Card
from Card import Card
import random
import numpy as np

class StandarDeck:
	def __init__(self):
		self.cards = []
		for i in CardValue:
			for j in CardType:
				self.cards.append(Card(i, j))
				#print(Card(i, j), Card(i, j).cardId())
		random.shuffle(self.cards)

	def distripute(self, n):
		ret = []
		for i in range(n):
			ret.append(self.cards.pop(0))
		return ret

	def winner (self, playedCards, tarneeb = None):
		wincard = playedCards[0]
		#import pdb; pdb.set_trace()
		winId = 0
		for i in range(1, len(playedCards)):
			if(wincard.largerThan(playedCards[i]) == False):
				wincard = playedCards[i]
				winId = i
			if (playedCards[i].type._value_ != playedCards[0].type._value_):
				if (playedCards[i].type._value_ == tarneeb):
					wincard = playedCards[i]
					winId = i
					break
		#print(wincard)
		self.cards.append(playedCards)
		return winId

def cardstoArray(cards, val = 1):
	ret = np.zeros(52)
	for c in cards:
		ret[c.cardId()] = val
	return ret