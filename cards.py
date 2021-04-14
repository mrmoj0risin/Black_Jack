import pygame
from enum import Enum
import os


def transform_card(cards_img):
    return pygame.transform.scale(cards_img,
                                  (int(cards_img.get_size()[0]),
                                   int(cards_img.get_size()[1])))


class Cards:

    def __init__(self, value, sign, name, description, img):
        self.value = value
        self.sign = sign
        self.name = name
        self.description = description
        self.img = img

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

    cards_imgs = [pygame.image.load(os.path.join("imgs/cards", "Ten of Diamonds.png")),

                  ]

    two_h = Cards(2, Sign.HEARTS, CardName.Two, "Two of Hearts", transform_card(cards_imgs[0]))
    tree_h = Cards(3, Sign.HEARTS, CardName.Tree, "Tree of Hearts", transform_card(cards_imgs[0]))
    four_h = Cards(4, Sign.HEARTS, CardName.Four, "Four of Hearts", transform_card(cards_imgs[0]))
    five_h = Cards(5, Sign.HEARTS, CardName.Five, "Five of Hearts", transform_card(cards_imgs[0]))
    six_h = Cards(6, Sign.HEARTS, CardName.Six, "Six of Hearts", transform_card(cards_imgs[0]))
    seven_h = Cards(7, Sign.HEARTS, CardName.Seven, "Seven of Hearts", transform_card(cards_imgs[0]))
    eight_h = Cards(8, Sign.HEARTS, CardName.Eight, "Eight of Hearts", transform_card(cards_imgs[0]))
    nine_h = Cards(9, Sign.HEARTS, CardName.Nine, "Nine of Hearts", transform_card(cards_imgs[0]))
    ten_h = Cards(10, Sign.HEARTS, CardName.Ten, "Ten of Hearts", transform_card(cards_imgs[0]))
    jack_h = Cards(10, Sign.HEARTS, CardName.Jack, "Jack of Hearts", transform_card(cards_imgs[0]))
    queen_h = Cards(10, Sign.HEARTS, CardName.Queen, "Queen of Hearts", transform_card(cards_imgs[0]))
    king_h = Cards(10, Sign.HEARTS, CardName.King, "King of Hearts", transform_card(cards_imgs[0]))
    ace_h = Cards(11, Sign.HEARTS, CardName.Ace, "Ace of Hearts", transform_card(cards_imgs[0]))

    two_c = Cards(2, Sign.CLUBS, CardName.Two, "Two of Clubs", transform_card(cards_imgs[0]))
    tree_c = Cards(3, Sign.CLUBS, CardName.Tree, "Tree of Clubs", transform_card(cards_imgs[0]))
    four_c = Cards(4, Sign.CLUBS, CardName.Four, "Four of Clubs", transform_card(cards_imgs[0]))
    five_c = Cards(5, Sign.CLUBS, CardName.Five, "Five of Clubs", transform_card(cards_imgs[0]))
    six_c = Cards(6, Sign.CLUBS, CardName.Six, "Six of Clubs", transform_card(cards_imgs[0]))
    seven_c = Cards(7, Sign.CLUBS, CardName.Seven, "Seven of Clubs", transform_card(cards_imgs[0]))
    eight_c = Cards(8, Sign.CLUBS, CardName.Eight, "Eight of Clubs", transform_card(cards_imgs[0]))
    nine_c = Cards(9, Sign.CLUBS, CardName.Nine, "Nine of Clubs", transform_card(cards_imgs[0]))
    ten_c = Cards(10, Sign.CLUBS, CardName.Ten, "Ten of Clubs", transform_card(cards_imgs[0]))
    jack_c = Cards(10, Sign.CLUBS, CardName.Jack, "Jack of Clubs", transform_card(cards_imgs[0]))
    queen_c = Cards(10, Sign.CLUBS, CardName.Queen, "Queen of Clubs", transform_card(cards_imgs[0]))
    king_c = Cards(10, Sign.CLUBS, CardName.King, "King of Clubs", transform_card(cards_imgs[0]))
    ace_c = Cards(11, Sign.CLUBS, CardName.Ace, "Ace of Clubs", transform_card(cards_imgs[0]))

    two_s = Cards(2, Sign.SPADES, CardName.Two, "Two of Spades", transform_card(cards_imgs[0]))
    tree_s = Cards(3, Sign.SPADES, CardName.Tree, "Tree of Spades", transform_card(cards_imgs[0]))
    four_s = Cards(4, Sign.SPADES, CardName.Four, "Four of Spades", transform_card(cards_imgs[0]))
    five_s = Cards(5, Sign.SPADES, CardName.Five, "Five of Spades", transform_card(cards_imgs[0]))
    six_s = Cards(6, Sign.SPADES, CardName.Six, "Six of Spades", transform_card(cards_imgs[0]))
    seven_s = Cards(7, Sign.SPADES, CardName.Seven, "Seven of Spades", transform_card(cards_imgs[0]))
    eight_s = Cards(8, Sign.SPADES, CardName.Eight, "Eight of Spades", transform_card(cards_imgs[0]))
    nine_s = Cards(9, Sign.SPADES, CardName.Nine, "Nine of Spades", transform_card(cards_imgs[0]))
    ten_s = Cards(10, Sign.SPADES, CardName.Ten, "Ten of Spades", transform_card(cards_imgs[0]))
    jack_s = Cards(10, Sign.SPADES, CardName.Jack, "Jack of Spades", transform_card(cards_imgs[0]))
    queen_s = Cards(10, Sign.SPADES, CardName.Queen, "Queen of Spades", transform_card(cards_imgs[0]))
    king_s = Cards(10, Sign.SPADES, CardName.King, "King of Spades", transform_card(cards_imgs[0]))
    ace_s = Cards(11, Sign.SPADES, CardName.Ace, "Ace of Spades", transform_card(cards_imgs[0]))

    two_d = Cards(2, Sign.DIAMONDS, CardName.Two, "Two of Diamonds", transform_card(cards_imgs[0]))
    tree_d = Cards(3, Sign.DIAMONDS, CardName.Tree, "Tree of Diamonds", transform_card(cards_imgs[0]))
    four_d = Cards(4, Sign.DIAMONDS, CardName.Four, "Four of Diamonds", transform_card(cards_imgs[0]))
    five_d = Cards(5, Sign.DIAMONDS, CardName.Five, "Five of Diamonds", transform_card(cards_imgs[0]))
    six_d = Cards(6, Sign.DIAMONDS, CardName.Six, "Six of Diamonds", transform_card(cards_imgs[0]))
    seven_d = Cards(7, Sign.DIAMONDS, CardName.Seven, "Seven of Diamonds", transform_card(cards_imgs[0]))
    eight_d = Cards(8, Sign.DIAMONDS, CardName.Eight, "Eight of Diamonds", transform_card(cards_imgs[0]))
    nine_d = Cards(9, Sign.DIAMONDS, CardName.Nine, "Nine of Diamonds", transform_card(cards_imgs[0]))
    ten_d = Cards(10, Sign.DIAMONDS, CardName.Ten, "Ten of Diamonds", transform_card(cards_imgs[0]))
    jack_d = Cards(10, Sign.DIAMONDS, CardName.Jack, "Jack of Diamonds", transform_card(cards_imgs[0]))
    queen_d = Cards(10, Sign.DIAMONDS, CardName.Queen, "Queen of Diamonds", transform_card(cards_imgs[0]))
    king_d = Cards(10, Sign.DIAMONDS, CardName.King, "King of Diamonds", transform_card(cards_imgs[0]))
    ace_d = Cards(11, Sign.DIAMONDS, CardName.Ace, "Ace of Diamonds", transform_card(cards_imgs[0]))

    full_deck = [two_h, tree_h, four_h, five_h, six_h, seven_h, eight_h, nine_h, ten_h, jack_h, queen_h, king_h, ace_h,
                 two_c, tree_c, four_c, five_c, six_c, seven_c, eight_c, nine_c, ten_c, jack_c, queen_c, king_c, ace_c,
                 two_s, tree_s, four_s, five_s, six_s, seven_s, eight_s, nine_s, ten_s, jack_s, queen_s, king_s, ace_s,
                 two_d, tree_d, four_d, five_d, six_d, seven_d, eight_d, nine_d, ten_d, jack_d, queen_d, king_d, ace_d]