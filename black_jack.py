import pygame
from pygame.sprite import RenderUpdates
# from pygame.locals import *
import sys
import os
from UIElement import UIElement, GameState
from cards import DeckOfCards, Hand
from players import Player, Croupier

pygame.init()
fps = 30
fpsClock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLUE = (106, 159, 181)
width, height = 900, 800
BG_IMG = pygame.image.load(os.path.join("imgs", "sukno.png"))

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Basic Pygame Template')

scale = 0.42
hand1 = Hand(-43, (24, 312))
hand2 = Hand(-31, (130, 390))
hand3 = Hand(-16, (255, 442))
hand4 = Hand(0, (400, 468))
hand5 = Hand(16, (520, 440))
hand6 = Hand(31, (630, 380))
hand7 = Hand(43, (720, 305))

def title_screen(screen, game_state):
    start_btn = UIElement(
        center_position=(width / 2, 400),
        font_size=30,
        bg_rgb=BLUE,
        text_rgb=WHITE,
        text="Start",
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

        if game_state == GameState.LOST:

            screen.blit(BG_IMG, (0, 0))

        for button in buttons:
            ui_action = button.update(pygame.mouse.get_pos(), mouse_up)
            if ui_action is not None:
                return ui_action

        buttons.draw(screen)
        pygame.display.flip()

def main():
    game_state = GameState.TITLE


    # screen.blit(BG_IMG, (0, screen.get_height()/2 - BG_IMG.get_height()/2))

    hand1.draw(DeckOfCards.five_c, screen)
    hand2.draw(DeckOfCards.ten_d, screen)
    hand3.draw(DeckOfCards.six_d, screen)
    hand4.draw(DeckOfCards.six_d, screen)
    hand5.draw(DeckOfCards.ace_c, screen)
    hand5.draw(DeckOfCards.jack_c, screen)
    hand6.draw(DeckOfCards.six_d, screen)
    hand7.draw(DeckOfCards.six_d, screen)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if game_state == GameState.TITLE:
            game_state = title_screen(screen, game_state)

        # if game_state == GameState.GAME:
        #     game_state = play_level(screen, game_state, score)
        #
        # if game_state == GameState.LOST:
        #     game_state = game_over_screen(screen, game_state, score)

        if game_state == GameState.QUIT:
            pygame.quit()
            return

        pygame.display.update()
        fpsClock.tick(fps)


def sum_cards(cards):
    score = 0
    for card in cards:
        score = score + card.value
    return score


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
