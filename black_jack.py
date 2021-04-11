from enum import Enum
from random import sample


def sum_cards(cards):
    score = 0
    for card in cards:
        score = score + card.value
    return score


class Cards:

    def __init__(self, value, sign, name, decription):
        self.value = value
        self.sign = sign
        self.name = name
        self.description = decription

    def __repr__(self):
        return str(self.description)

    def __str__(self):
        return str(self.description)

    def __int__(self):
        return int(self.value)


class Sign(Enum):
    CLUBS = 1
    DIAMONDS = 2
    HEARTS = 3
    SPADES = 4


class CardName(Enum):
    Two = 2
    Tree = 3
    Four = 4
    Five = 5
    Six = 6
    Seven = 7
    Eight = 8
    Nine = 9
    Ten = 10
    Jack = 11
    Queen = 12
    King = 13
    Ace = 14


class DeckOfCards:
    def __init__(self):
        pass

    two_h = Cards(2, Sign.HEARTS, CardName.Two, "Two of Hearts")
    tree_h = Cards(3, Sign.HEARTS, CardName.Tree, "Tree of Hearts")
    four_h = Cards(4, Sign.HEARTS, CardName.Four, "Four of Hearts")
    five_h = Cards(5, Sign.HEARTS, CardName.Five, "Five of Hearts")
    six_h = Cards(6, Sign.HEARTS, CardName.Six, "Six of Hearts")
    seven_h = Cards(7, Sign.HEARTS, CardName.Seven, "Seven of Hearts")
    eight_h = Cards(8, Sign.HEARTS, CardName.Eight, "Eight of Hearts")
    nine_h = Cards(9, Sign.HEARTS, CardName.Nine, "Nine of Hearts")
    ten_h = Cards(10, Sign.HEARTS, CardName.Ten, "Ten of Hearts")
    jack_h = Cards(10, Sign.HEARTS, CardName.Jack, "Jack of Hearts")
    queen_h = Cards(10, Sign.HEARTS, CardName.Queen, "Queen of Hearts")
    king_h = Cards(10, Sign.HEARTS, CardName.King, "King of Hearts")
    ace_h = Cards(11, Sign.HEARTS, CardName.Ace, "Ace of Hearts")

    two_c = Cards(2, Sign.CLUBS, CardName.Two,  "Two of Clubs")
    tree_c = Cards(3, Sign.CLUBS, CardName.Tree, "Tree of Clubs")
    four_c = Cards(4, Sign.CLUBS, CardName.Four, "Four of Clubs")
    five_c = Cards(5, Sign.CLUBS, CardName.Five, "Five of Clubs")
    six_c = Cards(6, Sign.CLUBS, CardName.Six, "Six of Clubs")
    seven_c = Cards(7, Sign.CLUBS, CardName.Seven, "Seven of Clubs")
    eight_c = Cards(8, Sign.CLUBS, CardName.Eight, "Eight of Clubs")
    nine_c = Cards(9, Sign.CLUBS, CardName.Nine, "Nine of Clubs")
    ten_c = Cards(10, Sign.CLUBS, CardName.Ten, "Ten of Clubs")
    jack_c = Cards(10, Sign.CLUBS, CardName.Jack, "Jack of Clubs")
    queen_c = Cards(10, Sign.CLUBS, CardName.Queen, "Queen of Clubs")
    king_c = Cards(10, Sign.CLUBS, CardName.King, "King of Clubs")
    ace_c = Cards(11, Sign.CLUBS, CardName.Ace, "Ace of Clubs")

    two_s = Cards(2, Sign.SPADES, CardName.Two,  "Two of Spades")
    tree_s = Cards(3, Sign.SPADES, CardName.Tree, "Tree of Spades")
    four_s = Cards(4, Sign.SPADES, CardName.Four, "Four of Spades")
    five_s = Cards(5, Sign.SPADES, CardName.Five, "Five of Spades")
    six_s = Cards(6, Sign.SPADES, CardName.Six, "Six of Spades")
    seven_s = Cards(7, Sign.SPADES, CardName.Seven, "Seven of Spades")
    eight_s = Cards(8, Sign.SPADES, CardName.Eight, "Eight of Spades")
    nine_s = Cards(9, Sign.SPADES, CardName.Nine, "Nine of Spades")
    ten_s = Cards(10, Sign.SPADES, CardName.Ten, "Ten of Spades")
    jack_s = Cards(10, Sign.SPADES, CardName.Jack, "Jack of Spades")
    queen_s = Cards(10, Sign.SPADES, CardName.Queen, "Queen of Spades")
    king_s = Cards(10, Sign.SPADES, CardName.King, "King of Spades")
    ace_s = Cards(11, Sign.SPADES, CardName.Ace, "Ace of Spades")

    two_d = Cards(2, Sign.DIAMONDS, CardName.Two,  "Two of Diamonds")
    tree_d = Cards(3, Sign.DIAMONDS, CardName.Tree, "Tree of Diamonds")
    four_d = Cards(4, Sign.DIAMONDS, CardName.Four, "Four of Diamonds")
    five_d = Cards(5, Sign.DIAMONDS, CardName.Five, "Five of Diamonds")
    six_d = Cards(6, Sign.DIAMONDS, CardName.Six, "Six of Diamonds")
    seven_d = Cards(7, Sign.DIAMONDS, CardName.Seven, "Seven of Diamonds")
    eight_d = Cards(8, Sign.DIAMONDS, CardName.Eight, "Eight of Diamonds")
    nine_d = Cards(9, Sign.DIAMONDS, CardName.Nine, "Nine of Diamonds")
    ten_d = Cards(10, Sign.DIAMONDS, CardName.Ten, "Ten of Diamonds")
    jack_d = Cards(10, Sign.DIAMONDS, CardName.Jack, "Jack of Diamonds")
    queen_d = Cards(10, Sign.DIAMONDS, CardName.Queen, "Queen of Diamonds")
    king_d = Cards(10, Sign.DIAMONDS, CardName.King, "King of Diamonds")
    ace_d = Cards(11, Sign.DIAMONDS, CardName.Ace, "Ace of Diamonds")

    full_deck = [two_h, tree_h, four_h, five_h, six_h, seven_h, eight_h, nine_h, ten_h, jack_h, queen_h, king_h, ace_h,
                 two_c, tree_c, four_c, five_c, six_c, seven_c, eight_c, nine_c, ten_c, jack_c, queen_c, king_c, ace_c,
                 two_s, tree_s, four_s, five_s, six_s, seven_s, eight_s, nine_s, ten_s, jack_s, queen_s, king_s, ace_s,
                 two_d, tree_d, four_d, five_d, six_d, seven_d, eight_d, nine_d, ten_d, jack_d, queen_d, king_d, ace_d]


class Player:

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


deck = DeckOfCards.full_deck

# player1 = Player('Goga')
#
# crup = Croupier()
# shoe = crup.make_a_shoe()

# print(deck)
# print('*'*195)
# print(shoe)
# print('*'*195)


# print(sum_cards(shoe))
# print(sum_cards(DeckOfCards.full_deck))
#
# player1.take_card(shoe)
# player1.take_card(shoe)
# crup.take_card(shoe)


def game():
    name = input("Enter ur name ")
    player = Player(name)

    crup = Croupier()
    shoe = crup.make_a_shoe()
    game_loop = True

    while game_loop:
        if player.sum_score() < 21:
            a = input("PRESS A TO TAKE A CARD")
            if a == 'a'.lower():
                player.take_card(shoe)
                crup.take_card(shoe)
                print('Crup took a card')
                print(f"ur cards  {player.hand} (sum = {player.sum_score()})")
                print(f'{crup.hand} is CRUP   (sum = {crup.sum_score()})')
                a2 = input("Wanna more? press a to take more or press any key if its enough")
                if a2 == "a":
                    continue
                else:
                    if player.sum_score() <= 21 and player.sum_score() > crup.sum_score():
                        print(f"you WIN Ur score is {player.sum_score()} , crup {crup.sum_score}")
                        break
                    else:
                        print(f'LOOSEER Ur score is {player.sum_score()} , crup {crup.sum_score}')
                        break
        else:
            print('LOST SCORE is > 21')
            break

game()


