import pygame
from pygame.sprite import RenderUpdates
# from pygame.locals import *
import sys
import os
from UIElement import UIElement, GameState, Button
from cards import DeckOfCards, Hand
from players import Player, Croupier

pygame.init()
fps = 30
fpsClock = pygame.time.Clock()

BG_RGB = (224, 150, 116)
BG_RGB2 = (230, 150, 122)
WHITE = (255, 255, 255)
BLUE = (106, 159, 181)
width, height = 900, 800
BG_IMG = pygame.image.load(os.path.join("imgs", "sukno.png"))

scale = 0.42

hand1 = Hand(-43, (24, 312))
hand2 = Hand(-31, (130, 390))
hand3 = Hand(-16, (255, 442))
hand4 = Hand(0, (400, 468))
hand5 = Hand(16, (520, 440))
hand6 = Hand(31, (630, 380))
hand7 = Hand(43, (720, 305))

player_hand_coordinates = [hand1, hand2, hand3, hand4, hand5, hand6, hand7]
player_hand_draw = []

angles = [-43, -31, -16, 0, 16, 31, 43]
coordinates = [(24, 312), (130, 390), (255, 442), (400, 468), (520, 440), (630, 380), (720, 305)]


crup_hand1 = Hand(-13, (250, 100))
crup_hand2 = Hand(-8, (290, 115))
crup_hand3 = Hand(-3, (340, 125))
crup_hand4 = Hand(0, (390, 125))
crup_hand5 = Hand(3, (420, 124))
crup_hand6 = Hand(8, (450, 114))
crup_hand7 = Hand(13, (490, 100))

crup_hand_draw = []


def main():
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Black Jack v 0.1')

    game_state = GameState.GAME

    player = Player("name")
    crup = Croupier()
    shoe = crup.make_a_shoe()

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if game_state == GameState.TITLE:
            game_state = title_screen(screen, game_state)

        if game_state == GameState.GAME:
            game_state = play_level(screen, game_state, player, shoe, crup)
        #
        # if game_state == GameState.LOST:
        #     game_state = game_over_screen(screen, game_state, score)

        if game_state == GameState.QUIT:
            pygame.quit()
            return

        pygame.display.update()
        fpsClock.tick(fps)


def title_screen(screen, game_state):
    start_btn = UIElement(
        center_position=(width / 2, 400),
        font_size=30,
        bg_rgb=BLUE,
        text_rgb=WHITE,
        text="Start new game",
        action=GameState.GAME,
    )
    quit_btn = UIElement(
        center_position=(width / 2, 480),
        font_size=30,
        bg_rgb=BLUE,
        text_rgb=WHITE,
        text="Quit",
        action=GameState.QUIT,
    )

    buttons = RenderUpdates(start_btn, quit_btn)

    return screens_loop(screen, buttons, game_state)


def screens_loop(screen, buttons, game_state):
    """ Handles game loop until an action is return by a button in the
        buttons sprite renderer.
    """
    while True:
        mouse_up = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True
        screen.blit(BG_IMG, (0, 0))

        if game_state == GameState.TITLE:
            screen.fill(BLUE)

        for button in buttons:
            ui_action = button.update(pygame.mouse.get_pos(), mouse_up)
            if ui_action is not None:
                return ui_action

        buttons.draw(screen)
        pygame.display.flip()


def play_level(screen, game_state, player, shoe, crup):

    return_btn = UIElement(
        center_position=(width - 80, screen.get_height()-30),
        font_size=17,
        bg_rgb=BG_RGB,
        text_rgb=WHITE,
        text="To main menu",
        action=GameState.TITLE,
    )
    take_card = UIElement(

        center_position=(width/2-200, height-100),
        font_size=25,
        bg_rgb=BG_RGB,
        text_rgb=WHITE,
        text="Take card",
        action=GameState.GAME,

    )

    buttons = RenderUpdates(return_btn, take_card)

    return game_loop(screen, buttons, game_state, player, shoe, crup)


def game_loop(screen, buttons, game_state, player, shoe, crup):
    while True:
        clock = pygame.time.Clock()
        clock.tick(30)
        mouse_up = False

        btn = Button(
            color=BG_RGB2,
            x=width/2-300,
            y=screen.get_height() - 130,
            width=200,
            height=60,
            text=""
        )

        btn2 = Button(
            color=BG_RGB2,
            x=width/2+96,
            y=screen.get_height() - 130,
            width=200,
            height=60,
            text="Stop"
        )

        # Catching events
        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:
                pass
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                pos = pygame.mouse.get_pos()
                if btn.isOver(pos):
                    player.take_card(shoe)
                    crup.take_card(shoe)
                    print(crup.hand)
                if btn2.isOver(pos):
                    if player.sum_score() > crup.sum_score():
                        print("WIN")
                    else:
                        print("LOSER")
                mouse_up = True
        if game_state == GameState.GAME:

            screen.fill(BG_RGB)
            screen.blit(BG_IMG, (0, screen.get_height() / 2 - BG_IMG.get_height() / 2))
            btn.draw(screen, True)
            btn2.draw(screen, True)

            if 7 > player.count >= 0:
                player_card = pygame.transform.rotozoom(player.hand[player.count].img, angles[player.count], 0.26),\
                                                                                               coordinates[player.count]
                crup_card = pygame.transform.rotozoom(crup.hand[crup.count].img, angles[crup.count], 0.26), \
                                                                                               coordinates[crup.count]

                player_hand_draw.append(player_card)

        for button in buttons:
            ui_action = button.update(pygame.mouse.get_pos(), mouse_up)
            if ui_action is not None:
                return ui_action

        buttons.draw(screen)
        # crup_hand1.draw_hidden(DeckOfCards.six_d, screen)
        # crup_hand2.draw_hidden(DeckOfCards.six_d, screen)
        # crup_hand3.draw_hidden(DeckOfCards.six_d, screen)
        # crup_hand4.draw_hidden(DeckOfCards.six_d, screen)
        # crup_hand5.draw_hidden(DeckOfCards.six_d, screen)
        # crup_hand6.draw_hidden(DeckOfCards.six_d, screen)
        # crup_hand7.draw_hidden(DeckOfCards.six_d, screen)

        # draw cards
        for card in player_hand_draw:
            screen.blit(card[0], card[1])
        pygame.display.flip()
        pygame.display.update()


def sum_cards(cards):
    score = 0
    for card in cards:
        score = score + card.value
    return score


# def game():
#     # name = input("Enter ur name ")
#     player = Player("name")
#
#     crup = Croupier()
#     shoe = crup.make_a_shoe()
#     game_loop = True
#
#     while game_loop:
#         if player.sum_score() < 21:
#             a = input("PRESS A TO TAKE A CARD")
#             if a == 'a'.lower():
#                 player.take_card(shoe)
#                 crup.take_card(shoe)
#                 print('Crup took a card')
#                 print(f"ur cards  {player.hand} (sum = {player.sum_score()})")
#                 print(f'{crup.hand} is CRUP   (sum = {crup.sum_score()})')
#                 a2 = input("Wanna more? press a to take more or press any key if its enough")
#                 if a2 == "a":
#                     continue
#                 else:
#                     if 21 >= player.sum_score() > crup.sum_score():
#                         print(f"you WIN Ur score is {player.sum_score()} , crup {crup.sum_score}")
#                         break
#                     else:
#                         print(f'LOOSEER Ur score is {player.sum_score()} , crup {crup.sum_score}')
#                         break
#         else:
#             print('LOST SCORE is > 21')
#             break
#

if __name__ == "__main__":
    main()
