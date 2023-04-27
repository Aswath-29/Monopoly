import pygame
import mainboard
import secondpage
import random

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

a = 0

clock = pygame.time.Clock()


def add_image(link, x, y):
    img = pygame.image.load(link)
    screen.blit(img, [x, y])
    pygame.display.update()


def button(msg, x, y, l, h, ac, ic, function, tc):
    pygame.draw.rect(screen, ic, [x, y, l, h])
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x < mouse[0] < x + l and y < mouse[1] < y + h:  # Checks if the button is pressed
        pygame.draw.rect(screen, ac, [x, y, l, h])
        if click[0] == 1:
            if function == "screen2":
                secondpage.screen2()
            if function == "quit1":
                quit()
            if function == "next":
                mainboard.mainscreen()
    _font = pygame.font.Font('freesansbold.ttf', 20)
    text_in_box(msg, _font, tc, x, y, l, h)


def text_in_box(text, font, tc, x, y, l, h):
    textSurface = font.render(text, True, tc)
    textRect = textSurface.get_rect()
    textRect.center = (x + l / 2, y + h / 2)
    screen.blit(textSurface, textRect)


def message_to_screen(msg, color, x, y, s):
    font = pygame.font.SysFont(None, s)
    screen_text = font.render(msg, True, color)
    screen.blit(screen_text, [x, y])


def rolldice():  # Dice function
    global a
    a = random.randrange(1, 7)  # Makes it random
    return a
