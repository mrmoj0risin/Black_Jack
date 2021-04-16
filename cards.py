import pygame
from enum import Enum
import os


def transform_card(cards_img):
    return pygame.transform.scale(cards_img,
                                  (int(cards_img.get_size()[0]),
                                   int(cards_img.get_size()[1])))


class Cards:

    def __init__(self, value, sign, name, description, img, hidden):
        self.value = value
        self.sign = sign
        self.name = name
        self.description = description
        self.img = img
        self.hidden = hidden

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

    cards_imgs = [pygame.image.load(os.path.join("imgs/cards", "2_Hearts.png")),
                  pygame.image.load(os.path.join("imgs/cards", "3_Hearts.png")),
                  pygame.image.load(os.path.join("imgs/cards", "4_Hearts.png")),
                  pygame.image.load(os.path.join("imgs/cards", "5_Hearts.png")),
                  pygame.image.load(os.path.join("imgs/cards", "6_Hearts.png")),
                  pygame.image.load(os.path.join("imgs/cards", "7_Hearts.png")),
                  pygame.image.load(os.path.join("imgs/cards", "8_Hearts.png")),
                  pygame.image.load(os.path.join("imgs/cards", "9_Hearts.png")),
                  pygame.image.load(os.path.join("imgs/cards", "10_Hearts.png")),
                  pygame.image.load(os.path.join("imgs/cards", "J_Hearts.png")),
                  pygame.image.load(os.path.join("imgs/cards", "Queen_Hearts.png")),
                  pygame.image.load(os.path.join("imgs/cards", "King_Hearts.png")),
                  pygame.image.load(os.path.join("imgs/cards", "Ace_Hearts.png")),

                  pygame.image.load(os.path.join("imgs/cards", "2_Clubs.png")),
                  pygame.image.load(os.path.join("imgs/cards", "3_Clubs.png")),
                  pygame.image.load(os.path.join("imgs/cards", "4_Clubs.png")),
                  pygame.image.load(os.path.join("imgs/cards", "5_Clubs.png")),
                  pygame.image.load(os.path.join("imgs/cards", "6_Clubs.png")),
                  pygame.image.load(os.path.join("imgs/cards", "7_Clubs.png")),
                  pygame.image.load(os.path.join("imgs/cards", "8_Clubs.png")),
                  pygame.image.load(os.path.join("imgs/cards", "9_Clubs.png")),
                  pygame.image.load(os.path.join("imgs/cards", "10_Clubs.png")),
                  pygame.image.load(os.path.join("imgs/cards", "J_Clubs.png")),
                  pygame.image.load(os.path.join("imgs/cards", "Queen_Clubs.png")),
                  pygame.image.load(os.path.join("imgs/cards", "King_Clubs.png")),
                  pygame.image.load(os.path.join("imgs/cards", "Ace_Clubs.png")),

                  pygame.image.load(os.path.join("imgs/cards", "2_Spades.png")),
                  pygame.image.load(os.path.join("imgs/cards", "3_Spades.png")),
                  pygame.image.load(os.path.join("imgs/cards", "4_Spades.png")),
                  pygame.image.load(os.path.join("imgs/cards", "5_Spades.png")),
                  pygame.image.load(os.path.join("imgs/cards", "6_Spades.png")),
                  pygame.image.load(os.path.join("imgs/cards", "7_Spades.png")),
                  pygame.image.load(os.path.join("imgs/cards", "8_Spades.png")),
                  pygame.image.load(os.path.join("imgs/cards", "9_Spades.png")),
                  pygame.image.load(os.path.join("imgs/cards", "10_Spades.png")),
                  pygame.image.load(os.path.join("imgs/cards", "J_Spades.png")),
                  pygame.image.load(os.path.join("imgs/cards", "Queen_Spades.png")),
                  pygame.image.load(os.path.join("imgs/cards", "King_Spades.png")),
                  pygame.image.load(os.path.join("imgs/cards", "Ace_Spades.png")),

                  pygame.image.load(os.path.join("imgs/cards", "2_Diamonds.png")),
                  pygame.image.load(os.path.join("imgs/cards", "3_Diamonds.png")),
                  pygame.image.load(os.path.join("imgs/cards", "4_Diamonds.png")),
                  pygame.image.load(os.path.join("imgs/cards", "5_Diamonds.png")),
                  pygame.image.load(os.path.join("imgs/cards", "6_Diamonds.png")),
                  pygame.image.load(os.path.join("imgs/cards", "7_Diamonds.png")),
                  pygame.image.load(os.path.join("imgs/cards", "8_Diamonds.png")),
                  pygame.image.load(os.path.join("imgs/cards", "9_Diamonds.png")),
                  pygame.image.load(os.path.join("imgs/cards", "10_Diamonds.png")),
                  pygame.image.load(os.path.join("imgs/cards", "J_Diamonds.png")),
                  pygame.image.load(os.path.join("imgs/cards", "Queen_Diamonds.png")),
                  pygame.image.load(os.path.join("imgs/cards", "King_Diamonds.png")),
                  pygame.image.load(os.path.join("imgs/cards", "Ace_Diamonds.png")),
                  ]
    
    hidden_img = pygame.image.load(os.path.join("imgs/cards", "Skin.png"))
    
    two_h = Cards(2, Sign.HEARTS, CardName.Two, "Two of Hearts", transform_card(cards_imgs[0]), transform_card(hidden_img))
    tree_h = Cards(3, Sign.HEARTS, CardName.Tree, "Tree of Hearts", transform_card(cards_imgs[1]), transform_card(hidden_img))
    four_h = Cards(4, Sign.HEARTS, CardName.Four, "Four of Hearts", transform_card(cards_imgs[2]), transform_card(hidden_img))
    five_h = Cards(5, Sign.HEARTS, CardName.Five, "Five of Hearts", transform_card(cards_imgs[3]), transform_card(hidden_img))
    six_h = Cards(6, Sign.HEARTS, CardName.Six, "Six of Hearts", transform_card(cards_imgs[4]), transform_card(hidden_img))
    seven_h = Cards(7, Sign.HEARTS, CardName.Seven, "Seven of Hearts", transform_card(cards_imgs[5]), transform_card(hidden_img))
    eight_h = Cards(8, Sign.HEARTS, CardName.Eight, "Eight of Hearts", transform_card(cards_imgs[6]), transform_card(hidden_img))
    nine_h = Cards(9, Sign.HEARTS, CardName.Nine, "Nine of Hearts", transform_card(cards_imgs[7]), transform_card(hidden_img))
    ten_h = Cards(10, Sign.HEARTS, CardName.Ten, "Ten of Hearts", transform_card(cards_imgs[8]), transform_card(hidden_img))
    jack_h = Cards(10, Sign.HEARTS, CardName.Jack, "Jack of Hearts", transform_card(cards_imgs[9]), transform_card(hidden_img))
    queen_h = Cards(10, Sign.HEARTS, CardName.Queen, "Queen of Hearts", transform_card(cards_imgs[10]), transform_card(hidden_img))
    king_h = Cards(10, Sign.HEARTS, CardName.King, "King of Hearts", transform_card(cards_imgs[11]), transform_card(hidden_img))
    ace_h = Cards(11, Sign.HEARTS, CardName.Ace, "Ace of Hearts", transform_card(cards_imgs[12]), transform_card(hidden_img))

    two_c = Cards(2, Sign.CLUBS, CardName.Two, "Two of Clubs", transform_card(cards_imgs[13]), transform_card(hidden_img))
    tree_c = Cards(3, Sign.CLUBS, CardName.Tree, "Tree of Clubs", transform_card(cards_imgs[14]), transform_card(hidden_img))
    four_c = Cards(4, Sign.CLUBS, CardName.Four, "Four of Clubs", transform_card(cards_imgs[15]), transform_card(hidden_img))
    five_c = Cards(5, Sign.CLUBS, CardName.Five, "Five of Clubs", transform_card(cards_imgs[16]), transform_card(hidden_img))
    six_c = Cards(6, Sign.CLUBS, CardName.Six, "Six of Clubs", transform_card(cards_imgs[17]), transform_card(hidden_img))
    seven_c = Cards(7, Sign.CLUBS, CardName.Seven, "Seven of Clubs", transform_card(cards_imgs[18]), transform_card(hidden_img))
    eight_c = Cards(8, Sign.CLUBS, CardName.Eight, "Eight of Clubs", transform_card(cards_imgs[19]), transform_card(hidden_img))
    nine_c = Cards(9, Sign.CLUBS, CardName.Nine, "Nine of Clubs", transform_card(cards_imgs[20]), transform_card(hidden_img))
    ten_c = Cards(10, Sign.CLUBS, CardName.Ten, "Ten of Clubs", transform_card(cards_imgs[21]), transform_card(hidden_img))
    jack_c = Cards(10, Sign.CLUBS, CardName.Jack, "Jack of Clubs", transform_card(cards_imgs[22]), transform_card(hidden_img))
    queen_c = Cards(10, Sign.CLUBS, CardName.Queen, "Queen of Clubs", transform_card(cards_imgs[23]), transform_card(hidden_img))
    king_c = Cards(10, Sign.CLUBS, CardName.King, "King of Clubs", transform_card(cards_imgs[24]), transform_card(hidden_img))
    ace_c = Cards(11, Sign.CLUBS, CardName.Ace, "Ace of Clubs", transform_card(cards_imgs[25]), transform_card(hidden_img))

    two_s = Cards(2, Sign.SPADES, CardName.Two, "Two of Spades", transform_card(cards_imgs[26]), transform_card(hidden_img))
    tree_s = Cards(3, Sign.SPADES, CardName.Tree, "Tree of Spades", transform_card(cards_imgs[27]), transform_card(hidden_img))
    four_s = Cards(4, Sign.SPADES, CardName.Four, "Four of Spades", transform_card(cards_imgs[28]), transform_card(hidden_img))
    five_s = Cards(5, Sign.SPADES, CardName.Five, "Five of Spades", transform_card(cards_imgs[29]), transform_card(hidden_img))
    six_s = Cards(6, Sign.SPADES, CardName.Six, "Six of Spades", transform_card(cards_imgs[30]), transform_card(hidden_img))
    seven_s = Cards(7, Sign.SPADES, CardName.Seven, "Seven of Spades", transform_card(cards_imgs[31]), transform_card(hidden_img))
    eight_s = Cards(8, Sign.SPADES, CardName.Eight, "Eight of Spades", transform_card(cards_imgs[32]), transform_card(hidden_img))
    nine_s = Cards(9, Sign.SPADES, CardName.Nine, "Nine of Spades", transform_card(cards_imgs[33]), transform_card(hidden_img))
    ten_s = Cards(10, Sign.SPADES, CardName.Ten, "Ten of Spades", transform_card(cards_imgs[34]), transform_card(hidden_img))
    jack_s = Cards(10, Sign.SPADES, CardName.Jack, "Jack of Spades", transform_card(cards_imgs[35]), transform_card(hidden_img))
    queen_s = Cards(10, Sign.SPADES, CardName.Queen, "Queen of Spades", transform_card(cards_imgs[36]), transform_card(hidden_img))
    king_s = Cards(10, Sign.SPADES, CardName.King, "King of Spades", transform_card(cards_imgs[37]), transform_card(hidden_img))
    ace_s = Cards(11, Sign.SPADES, CardName.Ace, "Ace of Spades", transform_card(cards_imgs[38]), transform_card(hidden_img))

    two_d = Cards(2, Sign.DIAMONDS, CardName.Two, "Two of Diamonds", transform_card(cards_imgs[39]), transform_card(hidden_img))
    tree_d = Cards(3, Sign.DIAMONDS, CardName.Tree, "Tree of Diamonds", transform_card(cards_imgs[40]), transform_card(hidden_img))
    four_d = Cards(4, Sign.DIAMONDS, CardName.Four, "Four of Diamonds", transform_card(cards_imgs[41]), transform_card(hidden_img))
    five_d = Cards(5, Sign.DIAMONDS, CardName.Five, "Five of Diamonds", transform_card(cards_imgs[42]), transform_card(hidden_img))
    six_d = Cards(6, Sign.DIAMONDS, CardName.Six, "Six of Diamonds", transform_card(cards_imgs[43]), transform_card(hidden_img))
    seven_d = Cards(7, Sign.DIAMONDS, CardName.Seven, "Seven of Diamonds", transform_card(cards_imgs[44]), transform_card(hidden_img))
    eight_d = Cards(8, Sign.DIAMONDS, CardName.Eight, "Eight of Diamonds", transform_card(cards_imgs[45]), transform_card(hidden_img))
    nine_d = Cards(9, Sign.DIAMONDS, CardName.Nine, "Nine of Diamonds", transform_card(cards_imgs[46]), transform_card(hidden_img))
    ten_d = Cards(10, Sign.DIAMONDS, CardName.Ten, "Ten of Diamonds", transform_card(cards_imgs[47]), transform_card(hidden_img))
    jack_d = Cards(10, Sign.DIAMONDS, CardName.Jack, "Jack of Diamonds", transform_card(cards_imgs[48]), transform_card(hidden_img))
    queen_d = Cards(10, Sign.DIAMONDS, CardName.Queen, "Queen of Diamonds", transform_card(cards_imgs[49]), transform_card(hidden_img))
    king_d = Cards(10, Sign.DIAMONDS, CardName.King, "King of Diamonds", transform_card(cards_imgs[50]), transform_card(hidden_img))
    ace_d = Cards(11, Sign.DIAMONDS, CardName.Ace, "Ace of Diamonds", transform_card(cards_imgs[51]), transform_card(hidden_img))

    full_deck = [two_h, tree_h, four_h, five_h, six_h, seven_h, eight_h, nine_h, ten_h, jack_h, queen_h, king_h, ace_h,
                 two_c, tree_c, four_c, five_c, six_c, seven_c, eight_c, nine_c, ten_c, jack_c, queen_c, king_c, ace_c,
                 two_s, tree_s, four_s, five_s, six_s, seven_s, eight_s, nine_s, ten_s, jack_s, queen_s, king_s, ace_s,
                 two_d, tree_d, four_d, five_d, six_d, seven_d, eight_d, nine_d, ten_d, jack_d, queen_d, king_d, ace_d]


class Hand:
    def __init__(self, angle, coordinates):
        self.angle = angle
        self.coordinates = coordinates

    def draw(self, card, screen):

        return screen.blit(pygame.transform.rotozoom(card.img, self.angle, 0.26), self.coordinates)

    def draw_hidden(self, card, screen):

        return screen.blit(pygame.transform.rotozoom(card.hidden, self.angle, 0.26), self.coordinates)
