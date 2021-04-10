from enum import Enum
from random import randrange, shuffle,sample


class Cards:

    def __init__(self, value, sign, name):
        self.value = value
        self.sign = sign
        self.name = name

    def __repr__(self):
        return str(self.name)

    def __str__(self):
        return str(self.name)

    def __int__(self):
        return int(self.value)


class Sign(Enum):
    CLUBS = 1
    DIAMONDS = 2
    HEARTS = 3
    SPADES = 4


class DeckOfCards:
    def __init__(self):
        pass

    two_h = Cards(2, Sign.HEARTS, "Two of Hearts")
    tree_h = Cards(3, Sign.HEARTS, "Tree of Hearts")
    four_h = Cards(4, Sign.HEARTS, "Four of Hearts")
    five_h = Cards(5, Sign.HEARTS, "Five of Hearts")
    six_h = Cards(6, Sign.HEARTS, "Six of Hearts")
    seven_h = Cards(7, Sign.HEARTS, "Seven of Hearts")
    eight_h = Cards(8, Sign.HEARTS, "Eight of Hearts")
    nine_h = Cards(9, Sign.HEARTS, "Nine of Hearts")
    ten_h = Cards(10, Sign.HEARTS, "Ten of Hearts")
    jack_h = Cards(10, Sign.HEARTS, "Jack of Hearts")
    queen_h = Cards(10, Sign.HEARTS, "Queen of Hearts")
    king_h = Cards(10, Sign.HEARTS, "King of Hearts")
    ace_h = Cards(11, Sign.HEARTS, "Ace of Hearts")

    two_c = Cards(2, Sign.CLUBS, "Two of Clubs")
    tree_c = Cards(3, Sign.CLUBS, "Tree of Clubs")
    four_c = Cards(4, Sign.CLUBS, "Four of Clubs")
    five_c = Cards(5, Sign.CLUBS, "Five of Clubs")
    six_c = Cards(6, Sign.CLUBS, "Six of Clubs")
    seven_c = Cards(7, Sign.CLUBS, "Seven of Clubs")
    eight_c = Cards(8, Sign.CLUBS, "Eight of Clubs")
    nine_c = Cards(9, Sign.CLUBS, "Nine of Clubs")
    ten_c = Cards(10, Sign.CLUBS, "Ten of Clubs")
    jack_c = Cards(10, Sign.CLUBS, "Jack of Clubs")
    queen_c = Cards(10, Sign.CLUBS, "Queen of Clubs")
    king_c = Cards(10, Sign.CLUBS, "King of Clubs")
    ace_c = Cards(11, Sign.CLUBS, "Ace of Clubs")

    two_s = Cards(2, Sign.SPADES, "Two of Spades")
    tree_s = Cards(3, Sign.SPADES, "Tree of Spades")
    four_s = Cards(4, Sign.SPADES, "Four of Spades")
    five_s = Cards(5, Sign.SPADES, "Five of Spades")
    six_s = Cards(6, Sign.SPADES, "Six of Spades")
    seven_s = Cards(7, Sign.SPADES, "Seven of Spades")
    eight_s = Cards(8, Sign.SPADES, "Eight of Spades")
    nine_s = Cards(9, Sign.SPADES, "Nine of Spades")
    ten_s = Cards(10, Sign.SPADES, "Ten of Spades")
    jack_s = Cards(10, Sign.SPADES, "Jack of Spades")
    queen_s = Cards(10, Sign.SPADES, "Queen of Spades")
    king_s = Cards(10, Sign.SPADES, "King of Spades")
    ace_s = Cards(11, Sign.SPADES, "Ace of Spades")

    two_d = Cards(2, Sign.DIAMONDS, "Two of DiamondsDIAMONDS")
    tree_d = Cards(3, Sign.DIAMONDS, "Tree of Diamonds")
    four_d = Cards(4, Sign.DIAMONDS, "Four of Diamonds")
    five_d = Cards(5, Sign.DIAMONDS, "Five of Diamonds")
    six_d = Cards(6, Sign.DIAMONDS, "Six of Diamonds")
    seven_d = Cards(7, Sign.DIAMONDS, "Seven of Diamonds")
    eight_d = Cards(8, Sign.DIAMONDS, "Eight of Diamonds")
    nine_d = Cards(9, Sign.DIAMONDS, "Nine of Diamonds")
    ten_d = Cards(10, Sign.DIAMONDS, "Ten of Diamonds")
    jack_d = Cards(10, Sign.DIAMONDS, "Jack of Diamonds")
    queen_d = Cards(10, Sign.DIAMONDS, "Queen of Diamonds")
    king_d = Cards(10, Sign.DIAMONDS, "King of Diamonds")
    ace_d = Cards(11, Sign.DIAMONDS, "Ace of Diamonds")

    full_deck = [two_h, tree_h, four_h, five_h, six_h, seven_h, eight_h, nine_h, ten_h, jack_h, queen_h, king_h, ace_h,
                 two_c, tree_c, four_c, five_c, six_c, seven_c, eight_c, nine_c, ten_c, jack_c, queen_c, king_c, ace_c,
                 two_s, tree_s, four_s, five_s, six_s, seven_s, eight_s, nine_s, ten_s, jack_s, queen_s, king_s, ace_s,
                 two_d, tree_d, four_d, five_d, six_d, seven_d, eight_d, nine_d, ten_d, jack_d, queen_d, king_d, ace_d]


deck = DeckOfCards


def sum_cards(cards):
    sum = 0
    for card in cards:
        sum = sum + card.value
    return sum


class Player:
    hand = []
    score = sum_cards(hand)

    def take_card(self, card):
        self.hand.append(card)


class Croupier(Player):
    shoe = []

    def make_a_shoe(self):
        fulldeck = DeckOfCards.full_deck
        shuffle(fulldeck)

        for card in fulldeck:
            self.shoe.append(card)

        return self.shoe


player1 = Player()

crup = Croupier()
shoe = crup.make_a_shoe()
print(shoe)


x = 0
player1.take_card(shoe[x])
player1.take_card(shoe[2])
print(sum_cards(shoe))


print(player1.hand, player1.score)
