import pygame
import mainboard
import functions

# Initialize the pygame
pygame.init()

# Creates the screen
width, height = 1050, 600

# Setting the colours
white = (255, 255, 255)
black = (0, 0, 0)
yellow = (255, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)

def screen2():
    game_exit = False
    while not game_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True

        functions.screen.fill(black)
        img = pygame.image.load('background.jpg')
        functions.screen.blit(img, (0, 0))


        functions.message_to_screen("Number of players : 2", red, 37.5, 75,40)
        functions.message_to_screen("Winning Amount : £3500", red, 37.5, 150,40)
        functions.message_to_screen("If cash drops under -£500 you are bankrupt", red, 37.5, 225, 40)
        functions.message_to_screen("If wealth drops under £0 you are bankrupt", red, 37.5, 300, 40)
        functions.message_to_screen("Enjoy the Game!", red, 37.5, 375, 40)

        functions.button("NEXT", 800, 450, 150, 37.5, blue, red, "next", black)


        pygame.display.update()