import pygame

import mainboard
import secondpage
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


def main():
    game_exit = False
    while not game_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # Checks if the user quit
                game_exit = True

        x = 440 # Position
        y1 = 220 # For START
        y2 = 370 # For END
        l = 150 # Length of the button
        h = 37.5 # Height of the button


        img = pygame.image.load('back5.jpg')
        functions.screen.blit(img, (0, 0))



        functions.button("START GAME", x, y1, l, h, blue, red, "screen2", black)
        functions.button("END GAME", x, y2, l, h, blue, red, "quit1", black)

        pygame.display.update()


if __name__ == "__main__":
    main()

