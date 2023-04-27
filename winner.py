import pygame
import functions
import mainboard
import player

# Initialize the pygame
pygame.init()

# Creates the screen
width, height = 1050, 600

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Monopoly")
pygame.display.update()


def winner_screen():
    game_exit = False
    while not game_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True

        img = pygame.image.load('background.jpg')
        functions.screen.blit(img, (0, 0))


def won():
    # Winning Conditions
    if player.player[player_index].total_wealth >= 3500:  # if wealth is above £3500
        functions.screen.fill(black)
        functions.message_to_screen("Player %r Congratulations you have Won " % player_index, red, 250, 400,
                                    30)

    # Losing Conditions
    if player.player[0].total_wealth < 0:  # if wealth is under £0
        functions.screen.fill(black)
        functions.message_to_screen("Player 2 Congratulations you have Won ", red, 250, 400, 30)
    elif player.player[1].total_wealth < 0:  # if wealth is under £0
        functions.screen.fill(black)
        functions.message_to_screen("Player 1 Congratulations you have Won ", red, 250, 400, 30)
    elif player.player[0].cash <= -500:  # if cash is under -£500
        functions.screen.fill(black)
        functions.message_to_screen("Player 2 Congratulations you have Won ", red, 250, 400, 30)
    elif player.player[1].cash <= -500:  # if cash is under -£500
        functions.screen.fill(black)
        functions.message_to_screen("Player 1 Congratulations you have Won ", red, 250, 400, 30)
