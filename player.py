import pygame
import functions

# Initialize the pygame
pygame.init()

# Creates the screen
width = 1050
height = 600

# Creates the squares
card_length: float = 97.5
card_breadth = 45

# Setting the colours
white = (255, 255, 255)
black = (0, 0, 0)
yellow = (255, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)

clock = pygame.time.Clock()

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Monopoly")
pygame.display.update()


# player class declared
class Player:
    def __init__(self, color, no):  # each player initialised with its data
        self.cash = 1500  # Starting cash
        self.posx = 540  # So that it starts on the Go square
        self.posy = 540
        self.total_wealth = 1500  # Starting wealth
        self.properties = []  # Initially nothing is there
        self.color = color
        self.no = no
        self.released = 1  # For the jail function which will be implemented later

    def draw(self):  # function to draw circular player on the board
        _font = pygame.font.Font('freesansbold.ttf', 20)
        pygame.draw.circle(functions.screen, self.color, [int(self.posx), int(self.posy)], 20)  # circle
        textSurface = _font.render(self.no, True, black)
        textRect = textSurface.get_rect()
        textRect.center = (self.posx, self.posy)
        screen.blit(textSurface, textRect)
        pygame.display.update()

    def movement(self, n):  # for controlling the movement of player on the board
        while n > 0:  # Whilst the number on the dice is above 1
            # specifying different movements at different positions
            if self.posx == 540 and self.posy == 540:  # If at GO moves to durban
                self.posx -= 95
            elif 161 < self.posx < 446 and self.posy == 540:  # Between Durban and Beijing
                self.posx -= 57
            elif self.posx == 160 and self.posy == 540:  # If at Beijing move to Just Visiting
                self.posx -= 110
            elif self.posx == 50 and self.posy == 540:  # If at Just Visiting move to Hiroshima
                self.posy -= 95
            elif self.posx == 50 and 161 < self.posy < 446:  # Between Hiroshima and Melbourne
                self.posy -= 57
            elif self.posx == 50 and self.posy == 160:  # If at Melbourne move to Free Parking
                self.posy -= 110
            elif self.posx == 50 and self.posy == 50:  # If at Free Parking move to Dehli
                self.posx += 110
            elif 159 < self.posx < 444 and self.posy == 50:  # Between Dehli and San Fransisco
                self.posx += 57
            elif self.posx == 445 and self.posy == 50:  # If at San Fransisco move to Jail
                self.posx += 95
            elif self.posx == 540 and self.posy == 50:  # If at Jail move to London
                self.posy += 110
            elif self.posx == 540 and 159 < self.posy < 444:  # Between London and Saint Petersburg
                self.posy += 57
            elif self.posx == 540 and self.posy == 445:  # If at Saint Petersburg move to GO
                self.posy += 95

            n -= 1  # Minus 1 from the number rolled on the dice


player = [Player(blue, '1'), Player(red, '2')]  # initialising player objects
