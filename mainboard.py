import pygame
import functions
import property
import player


# Initialize the pygame
pygame.init()

# Creates the screen
width, height = 1050, 600

# Sets the size of the squares
card_length = 97.5
card_breadth = 45

# Setting the colours
white = (255, 255, 255)
black = (0, 0, 0)
yellow = (255, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
light_blue = (0, 0, 100)
maroon = (100, 10, 100)
grey = (160, 160, 160)
orange = (228, 142, 88)

n = 0
player_index = 0
endturn = 0

card_display = 0  # Whether the property is displayed on the screen or not
key = 0  # Variable which is used to carry out different function
place = " "  # Checks the exact place on the board

full_round = [0, 0]  # number of spaces moved
round_complete = 0

start = 0
free_parking = 0
just_visiting = 0
jail = 0
chance1 = 0
chance2 = 0

won = 0
won2 = 0
won3 = 0

clock = pygame.time.Clock()

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Monopoly")
pygame.display.update()


def mainscreen():
    game_exit = False
    while not game_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Checks if the user quit
                game_exit = True

        # Calls this function
        drawing()
        # Updates the screen again and again

        clock.tick(15)


def drawing():
    global key, card_display, full_round, round_complete, free_parking, start, just_visiting, jail, chance1, chance2, \
        endturn, won, won2, won3
    img = pygame.image.load('background.jpg')  # Adds the background
    functions.screen.blit(img, (0, 0))

    pygame.draw.rect(functions.screen, white, [0, 0, height, height])  # Box for the board is sketched
    _font = pygame.font.Font('freesansbold.ttf', 15)

    # player boxes sketched
    pygame.draw.rect(functions.screen, white, [630, 30, 160, 160])  # Dimensions of rectangle 160 x 260
    pygame.draw.rect(functions.screen, white, [830, 30, 160, 160])  # Dimensions of rectangle 160 x 260

    # Messages added to player boxes
    functions.text_in_box("Player 1", _font, blue, 680, 30, 50, 50)  # For player 1
    functions.text_in_box("Cash £ %d" % player.player[0].cash, _font, black, 680, 110, 50, 50)
    functions.text_in_box("Net Worth £ %d" % player.player[0].total_wealth, _font, black, 680, 140, 50, 50)

    functions.text_in_box("Player 2", _font, red, 880, 30, 50, 50)  # For player 2
    functions.text_in_box("Cash £ %d" % player.player[1].cash, _font, black, 880, 110, 50, 50)
    functions.text_in_box("Net Worth £ %d" % player.player[1].total_wealth, _font, black, 880, 140, 50, 50)

    # Creating a box for messages to go
    functions.screen.fill(white, rect=[630, 350, 400, 100])

    # Creating a box for messages to go
    functions.screen.fill(white, rect=[630, 220, 160, 100])

    # Creating a box for messages to go
    functions.screen.fill(white, rect=[630, 480, 400, 100])

    # Images for the board are added
    functions.add_image('go.png', 470, 470)  # bottom right corner
    functions.add_image('gotojail.png', 470, 0)  # top right corner
    functions.add_image('parking.png', 0, 0)  # top left corner
    functions.add_image('jail.png', 0, 470)  # bottom corner
    functions.add_image('chance1.png', 242, 470)  # bottom row
    functions.add_image('chance3.png', 470, 242)  # right column

    button("ROLE DICE", 230, 230, 150, 37.5, blue, red, "roll", black)
    button("END TURN", 230, 320, 150, 37.5, blue, red, "endturn", black)
    functions.message_to_screen("You rolled %d" % n, black, 250, 400, 30)
    functions.text_in_box("Player %r's turn " % (player_index + 1), _font, black, 280, 150, 50, 50)

    # sketching properties on board
    property.street["delhi"].locmaker()
    property.street["mumbai"].locmaker()
    property.street["banglore"].locmaker()
    property.street["newyork"].locmaker()
    property.street["washingtondc"].locmaker()
    property.street["sanfrancisco"].locmaker()
    property.street["london"].locmaker()
    property.street["manchester"].locmaker()
    property.street["oxford"].locmaker()
    property.street["melbourne"].locmaker()
    property.street["canberra"].locmaker()
    property.street["sydney"].locmaker()
    property.street["tokyo"].locmaker()
    property.street["osaka"].locmaker()
    property.street["hiroshima"].locmaker()
    property.street["beijing"].locmaker()
    property.street["hongkong"].locmaker()
    property.street["shanghai"].locmaker()
    property.street["moscow"].locmaker()
    property.street["saintpetersburg"].locmaker()
    property.street["capetown"].locmaker()
    property.street["durban"].locmaker()

    __font = pygame.font.Font('freesansbold.ttf', 15)

    # Winning Conditions
    if player.player[player_index].total_wealth >= 3500:  # if wealth is above £3500
        functions.text_in_box("Player %r Congratulations you have Won!" % (player_index + 1), _font, black, 765, 475,
                              50, 50)
        button("Finish Game", 650, 530, 150, 30, blue, red, "finish", black)  # Button ends the game

    # Losing Conditions
    # if wealth is under £0 or if cash is under -£500
    if player.player[0].total_wealth < 0 or player.player[0].cash <= -500:
        functions.text_in_box("Player 2 Congratulations you have Won!", _font, black, 775, 475, 50, 50)
        button("Finish Game", 650, 530, 150, 30, blue, red, "finish", black)

    if player.player[1].total_wealth < 0 or player.player[1].cash <= -500:
        functions.text_in_box("Player 1 Congratulations you have Won!", _font, black, 775, 475, 50, 50)
        button("Finish Game", 650, 530, 150, 30, blue, red, "finish", black)

    if chance2 == 1:
        chance2 = 0
        card_display = 0
        player.player[player_index].cash -= 150  # Bad Mystery Card
        player.player[player_index].total_wealth -= 150
        key = 9

    if key == 9:
        functions.text_in_box("You have been fined for speeding, pay £150", _font, black, 775, 345, 50, 50)

    if chance1 == 1:
        chance1 = 0
        card_display = 0
        player.player[player_index].cash += 100  # Good Mystery Card
        player.player[player_index].total_wealth += 100
        key = 8

    if key == 8:
        functions.text_in_box("You have won a prize in a beauty contest, collect £100", _font, black, 805, 345, 50, 50)

    if jail == 1:
        jail = 0
        card_display = 0
        player.player[player_index].posx = 50  # Moves it to the Jail square
        player.player[player_index].posy = 540
        player.player[player_index].cash -= 250  # Fines the player for landing on Jail
        player.player[player_index].total_wealth -= 250
        full_round[player_index] -= 14  # As they have moved back to the jail square
        key = 7

    if key == 7:
        functions.text_in_box("You landed on Jail, pay £250", _font, black, 720, 345, 50, 50)

    if just_visiting == 1:
        just_visiting = 0
        card_display = 0
        key = 6

    if key == 6:
        functions.text_in_box("Don't worry you are just visiting Jail", _font, black, 745, 345, 50, 50)

    if start == 1:
        start = 0
        card_display = 0
        key = 5

    if key == 5:
        functions.text_in_box("Here is £200 for passing Go", _font, black, 720, 345, 50, 50)

    if free_parking == 1:
        free_parking = 0
        card_display = 0
        key = 4

    if key == 4:
        functions.text_in_box("You are at Free Parking", _font, black, 700, 345, 50, 50)

    if round_complete == 1:
        player.player[player_index].cash += 200  # Gives the player 200 for passing Go
        player.player[player_index].total_wealth += 200
        full_round[player_index] -= 28  # Starts the lap again
        round_complete = 0

    if card_display == 1:
        property.street[place].card()  # Calls the card function
        rent_paid = property.street[place].rent  # Gets the correct rent value
        if property.street[place].owner is not None and key == 0 and player_index != property.street[place].owner:
            player.player[player_index].cash -= rent_paid  # Pays rent
            player.player[player_index].total_wealth -= rent_paid  # Loses wealth
            player.player[property.street[place].owner].cash += rent_paid  # Collects rent
            player.player[property.street[place].owner].total_wealth += rent_paid  # Gains wealth
            key = 1

        if key == 1:
            functions.text_in_box(
                "You paid rent of £ %d to player %d?" % (rent_paid, property.street[place].owner + 1), __font,
                black, 745, 345, 50, 50)

        if property.street[place].owner is None and key == 0:  # checks if it is not owned
            property.street[place].card()
            functions.text_in_box("Do you want to purchase %r ?" % property.street[place].name, __font, black, 765, 345,
                                  50, 50)
            button("Yes", 650, 400, 80, 30, blue, red, "yes", black)
            button("No", 750, 400, 80, 30, blue, red, "no", black)

        if key == 2:
            property.street[place].card()
            functions.text_in_box("Successfully purchased %r" % property.street[place].name, __font, black, 755, 345,
                                  50, 50)

    player.player[1].draw()
    player.player[0].draw()


def button(msg, x, y, l, h, ac, ic, function, tc):
    global player_index, endturn, n, card_display, key, place, full_round, round_complete
    global start, free_parking, just_visiting, jail, chance1, chance2, won, won2, won3
    _font = pygame.font.Font('freesansbold.ttf', 15)
    pygame.draw.rect(functions.screen, ic, [x, y, l, h])
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x < mouse[0] < x + l and y < mouse[1] < y + h:
        pygame.draw.rect(functions.screen, ac, [x, y, l, h])
        if click[0] == 1:  # checks if the dice is rolled
            if function == "roll":
                n = functions.rolldice()  # rolls the dice

                full_round[player_index] += n  # Adds the value of the dice

                player.player[player_index].movement(n)  # moves the player

                if full_round[player_index] >= 28:  # Checks if it has completed on lap around the board
                    round_complete = 1

                for tplace, tempo in property.street.items():
                    # Checks if the player is on the property
                    if property.street[tplace].x1 == player.player[player_index].posx and \
                            property.street[tplace].y1 == player.player[player_index].posy:
                        card_display = 1  # takes it to that function
                        key = 0
                        place = tplace  # temporary place
                endturn = 0

                # Check if it is at free parking
                if player.player[player_index].posx == 50 and player.player[player_index].posy == 50:
                    free_parking = 1
                endturn = 0

                # Check if it is at Go
                if player.player[player_index].posx == 540 and player.player[player_index].posy == 540:
                    start = 1
                endturn = 0

                # Check if it is at Just Visiting
                if player.player[player_index].posx == 50 and player.player[player_index].posy == 540:
                    just_visiting = 1
                endturn = 0

                # Check if it is at Jail
                if player.player[player_index].posx == 540 and player.player[player_index].posy == 50:
                    jail = 1
                endturn = 0

                # Check if it is at Chance 1
                if player.player[player_index].posx == 274 and player.player[player_index].posy == 540:
                    chance1 = 1
                endturn = 0

                # Check if it is at Chance 2
                if player.player[player_index].posx == 540 and player.player[player_index].posy == 274:
                    chance2 = 1
                endturn = 0

            if function == "endturn" and endturn == 0:
                if player_index == 0:
                    player_index += 1  # Increases the player index, so it's player 2's turn
                elif player_index == 1:
                    player_index -= 1  # Decreases the player index, so it's player 1's turn
                card_display = 0
                endturn = 1

            if function == "yes":
                player.player[player_index].cash -= property.street[place].cost  # Loses money from buying
                property.street[place].owner = player_index  # Assigned to that player
                player.player[player_index].properties.append(place)
                key = 2

            if function == "no":
                card_display = 0

            if function == "finish":
                quit()

    _font = pygame.font.Font('freesansbold.ttf', 20)
    functions.text_in_box(msg, _font, tc, x, y, l, h)
