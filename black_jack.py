from enum import Enum
from random import sample
import pygame
from pygame.sprite import RenderUpdates
from pygame.locals import *
import sys
import os
from UIElement import UIElement
from cards import DeckOfCards

pygame.init()
fps = 30
fpsClock = pygame.time.Clock()

BLUE = (106, 159, 181)
width, height = 900, 800
BG_IMG = pygame.image.load(os.path.join("imgs", "sukno.png"))

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Basic Pygame Template')


def main():
    scale = 0.42
    hand1_angle = -47
    hand2_angle = -30

    hand1_x_y = (30, 310)
    hand2_x_y = (140, 388)


    screen.fill(BLUE)
    screen.blit(BG_IMG, (0, screen.get_height()/2 - BG_IMG.get_height()/2))

    screen.blit(pygame.transform.rotozoom(DeckOfCards.six_d.img, hand2_angle, scale), hand2_x_y)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        fpsClock.tick(fps)


def sum_cards(cards):
    score = 0
    for card in cards:
        score = score + card.value
    return score


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


def game():
    # name = input("Enter ur name ")
    player = Player("name")

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
                    if 21 >= player.sum_score() > crup.sum_score():
                        print(f"you WIN Ur score is {player.sum_score()} , crup {crup.sum_score}")
                        break
                    else:
                        print(f'LOOSEER Ur score is {player.sum_score()} , crup {crup.sum_score}')
                        break
        else:
            print('LOST SCORE is > 21')
            break


if __name__ == "__main__":
    main()
