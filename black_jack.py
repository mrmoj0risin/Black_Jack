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
BG_RGB2 = (230, 156, 122)
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

hands = [hand1, hand2, hand3, hand4, hand5, hand6, hand7]
x = []

angles = [-43, -31, -16, 0, 16, 31, 43]
coordinates = [(24, 312), (130, 390), (255, 442), (400, 468), (520, 440), (630, 380), (720, 305)]


def main():
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Black Jack v 0.1')

    game_state = GameState.GAME

    player = Player("name")

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if game_state == GameState.TITLE:
            game_state = title_screen(screen, game_state)

        if game_state == GameState.GAME:
            game_state = play_level(screen, game_state, player)
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


def play_level(screen, game_state, player):

    return_btn = UIElement(
        center_position=(width - 80, screen.get_height()-30),
        font_size=17,
        bg_rgb=BG_RGB,
        text_rgb=WHITE,
        text="To main menu",
        action=GameState.TITLE,
    )
    take_card = UIElement(

        center_position=(width/2, height-100),
        font_size=25,
        bg_rgb=BG_RGB,
        text_rgb=WHITE,
        text="Take card",
        action=GameState.GAME,

    )

    buttons = RenderUpdates(return_btn, take_card)

    return game_loop(screen, buttons, game_state, player)


def game_loop(screen, buttons, game_state, player):
    while True:
        clock = pygame.time.Clock()
        clock.tick(30)
        mouse_up = False

        crup = Croupier()
        shoe = crup.make_a_shoe()

        btn = Button(
            color=BG_RGB2,
            x=screen.get_width()/2-90,
            y=screen.get_height() - 130,
            width=200,
            height=60,
            text=""
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
                    print(player.count)
                mouse_up = True
        if game_state == GameState.GAME:

            screen.fill(BG_RGB)
            screen.blit(BG_IMG, (0, screen.get_height() / 2 - BG_IMG.get_height() / 2))
            btn.draw(screen)

            if 7 > player.count >= 0:
                i = player.count
                s = pygame.transform.rotozoom(player.hand[player.count].img, angles[i], 0.26), coordinates[i]
                # print(s)
                x.append(s)





            # hand2.draw(DeckOfCards.ten_d, screen)
            # hand3.draw(DeckOfCards.six_d, screen)
            # hand4.draw(DeckOfCards.six_d, screen)
            # hand5.draw(DeckOfCards.ace_c, screen)
            # hand5.draw(DeckOfCards.jack_c, screen)
            # hand6.draw(DeckOfCards.six_d, screen)
            # hand7.draw(DeckOfCards.six_d, screen)

        for button in buttons:
            ui_action = button.update(pygame.mouse.get_pos(), mouse_up)
            if ui_action is not None:
                return ui_action

        buttons.draw(screen)
        for i in x:
            screen.blit(i[0], i[1])
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
