import pygame
from pygame.sprite import RenderUpdates
import sys
import os
from UIElement import UIElement, GameState, Button
from players import Player, Croupier

pygame.init()
fps = 5
fpsClock = pygame.time.Clock()

transparent = (0, 0, 0, 0)
BG_RGB = (224, 150, 116)
BG_RGB2 = (230, 150, 122)
WHITE = (255, 255, 255)
BLUE = (106, 159, 181)
width, height = 900, 800
BG_IMG = pygame.image.load(os.path.join("imgs", "sukno.png"))

scale = 0.42

player_hand_draw = []

angles = [-43, -31, -16, 0, 16, 31, 43]
coordinates = [(24, 312), (130, 390), (255, 442), (400, 468), (520, 440), (630, 380), (720, 305)]

crup_angles = [-13, -8, -3, 0, 3, 8, 13]
crup_coordinates = [(245, 100), (290, 115), (340, 125), (390, 125), (420, 124), (450, 110), (490, 95)]


crup_hand_draw = []
crup_hand_open = []


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
            game_state = title_screen(screen, game_state, player)

        if game_state == GameState.GAME:
            game_state = play_level(screen, game_state, player, shoe, crup)

        if game_state == GameState.QUIT:
            pygame.quit()
            return

        # pygame.display.update()
        fpsClock.tick(fps)


def title_screen(screen, game_state, player):
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

    return screens_loop(screen, buttons, game_state, player)


def screens_loop(screen, buttons, game_state, player):
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
                player.clear()

        screen.blit(BG_IMG, (0, 0))

        if game_state == GameState.TITLE:
            Player.clear(player)
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
    game_stop = True
    while True:
        clock = pygame.time.Clock()
        clock.tick(30)
        mouse_up = False


        btn_take_card = Button(
            color=BG_RGB2,
            x=width/2-300,
            y=screen.get_height() - 130,
            width=200,
            height=60,
            text=""
        )

        btn_stop = Button(
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
                # BTN    TAKE CARD
                if btn_take_card.isOver(pos) and game_stop:

                    if 6 > player.count:
                        print(not bool(btn_stop.pressed))
                        print('Game ', game_stop)
                        player.take_card(shoe)
                        crup.take_card(shoe)

                        player_card = draw(player.hand[player.count], angles[player.count], coordinates[player.count])

                        crup_card = draw_hidden(crup.hand[crup.count], crup_angles[crup.count],
                                                crup_coordinates[crup.count])

                        crup_card2 = draw(crup.hand[crup.count], crup_angles[crup.count],
                                                crup_coordinates[crup.count])

                        player_hand_draw.append(player_card)
                        crup_hand_draw.append(crup_card)
                        crup_hand_open.append(crup_card2)

                        print('Player', player.score)
                        print('Crup', crup.score)
                print('"player count is"', player.count)
                # BTN STOP
                if btn_stop.isOver(pos):
                    btn_stop.pressed = True
                    game_stop = False

                    crup_hand_draw.clear()

                    if 21 >= player.score > crup.score:
                        print('Player', player.hand)
                        print("WIN")
                        print('Crup', crup.hand)
                    elif crup.score > 21 >= player.score:
                        print('Player', player.hand)
                        print("WIN")
                        print('Crup', crup.hand)
                    elif player.score == crup.score:
                        print('Draw')
                    else:
                        print('Crup', crup.score, 'Player', player.score)
                        print('Player Hand', player.hand)
                        print("LOST")
                        print('Crup Hand', crup.hand)
                mouse_up = True
        if game_state == GameState.GAME:

            screen.fill(BG_RGB)
            screen.blit(BG_IMG, (0, screen.get_height() / 2 - BG_IMG.get_height() / 2))
            btn_take_card.draw(screen, True)
            btn_stop.draw(screen, True)
            buttons.draw(screen)

            # draw cards
            for card in player_hand_draw:
                screen.blit(card[0], card[1])

            for card in crup_hand_open:
                screen.blit(card[0], card[1])

            for card in crup_hand_draw:
                screen.blit(card[0], card[1])

        for button in buttons:
            ui_action = button.update(pygame.mouse.get_pos(), mouse_up)
            if ui_action is not None:
                return ui_action

        pygame.display.flip()
        pygame.display.update()


def sum_cards(cards):
    score = 0
    for card in cards:
        score = score + card.value
    return score


def draw(card, angle, coordinate):
    return pygame.transform.rotozoom(card.img, angle, 0.26), coordinate


def draw_hidden(card, angle, coordinate):
    return pygame.transform.rotozoom(card.hidden, angle, 0.27), coordinate


if __name__ == "__main__":
    main()
