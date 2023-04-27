import pygame
import functions

# Creates the screen
width, height = 1050, 600

# Creates the squares
card_length = 130
card_breadth = 56

# Setting the colours
white = (255, 255, 255)
black = (0, 0, 0)
yellow = (255, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (50, 255, 50)
dark_blue = (0, 0, 100)
maroon = (100, 10, 100)
new = (10, 100, 100)
new1 = (200, 150, 50)
new2 = (67, 234, 169)
grey = (160, 160, 160)
orange = (230, 120, 50)

tflag = 0

clock = pygame.time.Clock()


class Property:  # creating a class property which will contain all data of properties and their functions
    def __init__(self, name, color, country, locx, locy, cost, x1, y1):
        # initialising every object(property) with its basic information
        self.name = name
        self.color = color
        self.country = country
        self.locx = locx  # x coordinate
        self.locy = locy  # y coordinate
        self.cost = cost
        self.rent = 0.1 * self.cost
        self.owner = None  # initially set to none
        self.x1 = x1  # x coordinate of player on the square
        self.y1 = y1  # y coordinate of player on the square

    def locmaker(self) -> object:  # it creates the respective property on the board
        lfont = pygame.font.Font('freesansbold.ttf', 10)
        if self.locx == card_length / 2:  # creates properties on the left column
            pygame.draw.rect(functions.screen, black, [0, self.locy - card_breadth / 2, card_length, card_breadth],
                             1)
            functions.text_in_box(self.name, lfont, black, 0, self.locy - card_breadth / 2, 0.7 * card_length,
                                  card_breadth)
            functions.screen.fill(self.color,
                                  rect=[0.7 * card_length, self.locy - card_breadth / 2, 0.3 * card_length,
                                        card_breadth])
        elif self.locx == height - card_length / 2:  # creates properties on the right column
            pygame.draw.rect(functions.screen, black,
                             [height - card_length, self.locy - card_breadth / 2, card_length, card_breadth], 1)
            functions.text_in_box(self.name, lfont, black, height - 0.7 * card_length,
                                  self.locy - card_breadth / 2, 0.7 * card_length, card_breadth)
            functions.screen.fill(self.color, rect=[height - card_length, self.locy - card_breadth / 2,
                                                    0.3 * card_length, card_breadth])
        elif self.locy == card_length / 2:  # creates properties on the top row
            pygame.draw.rect(functions.screen, black, [self.locx - card_breadth / 2, 0, card_breadth, card_length],
                             1)
            a = self.name.split(' ')
            temp = 0
            for x in a:
                functions.text_in_box(x, lfont, black, self.locx - card_breadth / 2, temp, card_breadth,
                                      0.35 * card_length)
                temp += 0.35 * card_length
            functions.screen.fill(self.color, rect=[self.locx - card_breadth / 2, 0.7 * card_length, card_breadth,
                                                    0.3 * card_length])

        elif self.locy == height - card_length / 2:  # creates the properties on the bottom row
            pygame.draw.rect(functions.screen, black,
                             [self.locx - card_breadth / 2, height - card_length, card_breadth, card_length], 1)
            functions.text_in_box(self.name, lfont, black, self.locx - card_breadth / 2,
                                  height - 0.7 * card_length, card_breadth, 0.7 * card_length)
            functions.screen.fill(self.color,
                                  rect=[self.locx - card_breadth / 2, height - card_length, card_breadth,
                                        0.3 * card_length])
            pygame.display.update()

    def card(self):  # #this draws the card of the property with the respective details on it
        lfont = pygame.font.Font('freesansbold.ttf', 15)
        functions.text_in_box(self.name, lfont, self.color, 680, 220, 50, 50)
        functions.message_to_screen("Cost: £ %d" % self.cost, black, 650, 270, 20)
        functions.message_to_screen("Rent: £ %d" % self.rent, black, 650, 290, 20)
        pygame.display.update()


# initialising the property objects


street = {"delhi": Property("Delhi", red, "India", 159, card_length / 2, 220, 160, 50),
          "mumbai": Property("Mumbai", red, "India", 216, card_length / 2, 220, 217, 50),
          "banglore": Property("Banglore", red, "India", 273, card_length / 2, 240, 274, 50),
          "newyork": Property("New York", yellow, "America", 330, card_length / 2, 260, 331, 50),
          "washingtondc": Property("Washington D.C.", yellow, "America", 387, card_length / 2, 260, 388, 50),
          "sanfrancisco": Property("San Francisco", yellow, "America", 444, card_length / 2, 280, 445, 50),
          "london": Property("London", grey, "England", height - card_length / 2, 159, 300, 540, 160),
          "manchester": Property("Manchester", grey, "England", height - card_length / 2, 216, 300, 540, 217),
          "oxford": Property("Oxford", grey, "England", height - card_length / 2, 330, 320, 540, 331),
          "moscow": Property("Moscow", dark_blue, "Russia", height - card_length / 2, 387, 350, 540, 388),
          "saintpetersburg": Property("Saint Petersberg", dark_blue, "Russia", height - card_length / 2, 444, 400, 540,
                                      445),
          "melbourne": Property("Melbourne", blue, "Australia", card_length / 2, 159, 200, 50, 160),
          "canberra": Property("Canberra", blue, "Australia", card_length / 2, 216, 180, 50, 217),
          "sydney": Property("Sydney", blue, "Australia", card_length / 2, 273, 180, 50, 274),
          "tokyo": Property("Tokyo", orange, "Japan", card_length / 2, 330, 160, 50, 331),
          "osaka": Property("Osaka", orange, "Japan", card_length / 2, 387, 140, 50, 387),
          "hiroshima": Property("Hiroshima", orange, "Japan", card_length / 2, 444, 140, 50, 445),
          "beijing": Property("Beijing", new, "China", 159, height - card_length / 2, 120, 160, 540),
          "hongkong": Property("Hong Kong", new, "China", 216, height - card_length / 2, 100, 217, 540),
          "shanghai": Property("Shanghai", new, "China", 330, height - card_length / 2, 100, 331, 540),
          "capetown": Property("Cape Town", new2, "SouthAfrica", 387, height - card_length / 2, 60, 388, 540),
          "durban": Property("Durban", new2, "SouthAfrica", 444, height - card_length / 2, 60, 445, 540)
          }
