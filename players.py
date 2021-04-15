from random import sample
from cards import DeckOfCards


class Player:
    count = -1

    def __init__(self, name, hand=None, score=0):
        self.name = name
        self.score = score
        if hand is None:
            hand = []
        self.hand = hand

    def sum_score(self):
        self.score = 0
        for i in self.hand:
            # print('card is ', i.value)
            self.score = self.score + i.value
            # print("Inside ",self.score)
        # print("Out ", self.score)

        return self.score

    def take_card(self, shoe):
        self.hand.append(shoe.pop(0))
        self.count += 1
        return self.count



class Croupier(Player):

    shoe = []

    def __init__(self):
        super().__init__(name="Croupier")

    def make_a_shoe(self):
        # Почему то при создании нового крупье, перемешанная коложа такая же как и у первого
        shuffled_deck = sample(DeckOfCards.full_deck, len(DeckOfCards.full_deck))

        for card in shuffled_deck:
            self.shoe.append(card)

        return self.shoe

