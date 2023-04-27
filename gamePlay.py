import pygame

import firstpage
import secondpage
import mainboard

# Initialize the pygame
pygame.init()

# Creates the screen
width, height = 1050, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Monopoly")
pygame.display.update()

# Setting the colours
white = (255, 255, 255)
black = (0, 0, 0)
yellow = (255, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)

firstpage.main()

pygame.quit()

quit()
