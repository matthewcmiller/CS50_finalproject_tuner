import pygame
import random

def display(note, cents):
    # initalize pygame
    pygame.init()

    # set colors
    black = (0, 0, 0)
    red = (255, 0, 0)
    green = (0, 255, 0)
    

    # set display dimensions
    display_width = 800
    display_height = 600


    # create display
    display_screen = pygame.display.set_mode((display_width,display_height))
    pygame.display.set_caption('Tuner')

    # choose font
    note_font = pygame.font.SysFont('arial', 64, bold = True)

    message_font = pygame.font.SysFont('arial', 32, italic = True)

    cents_font = pygame.font.SysFont('arial', 32)

    symbol_font = pygame.font.SysFont('arial', 64)

    # running = True
    # while running:
    
    # fill screen
    display_screen.fill(black)
    
    # choose text to display
    # note = random.choice(['C1', 'C#7', 'D2', 'D#4', 'E5'])
    # cents = random.choice([3, 50, 44, -13, -24, 37])

    if cents < -5:
        color = red
        statement = 'up!'
    elif cents > 5:
        color = red
        statement = 'down!'
    else:
        color = green
        statement = 'good!'
    
    # render text
    notetext = note_font.render(note, True, color)
    statementtext = message_font.render(statement, True, color)
    centstext = cents_font.render(str(cents) + ' c', True, color) 
    plus = symbol_font.render('+', True, red)
    minus = symbol_font.render('-', True, red)

    # create objects
    noterect = notetext.get_rect()
    noterect.center = (display_width / 2, display_height / 2)
    messagerect = statementtext.get_rect()
    messagerect.center = (display_width / 2,(display_height / 2) - 100)
    centsrect = centstext.get_rect()
    centsrect.center = (display_width / 2,(display_height / 2) + 100)
    plusrect = plus.get_rect()
    plusrect.center = ((display_width / 2) + 100, display_height / 2)
    minusrect = minus.get_rect()
    minusrect.center = ((display_width / 2) - 100, display_height / 2)

    # blit text onto objects
    display_screen.blit(notetext, noterect)
    display_screen.blit(statementtext, messagerect)
    display_screen.blit(centstext, centsrect)
    
    # only blit +/- if pitch is sharp/flat
    if cents < -5:
        display_screen.blit(minus, minusrect)
    elif cents > 5:
        display_screen.blit(plus, plusrect)

    # stop running if user quits the window
    # for event in pygame.event.get():
    #    if event.type == pygame.QUIT:
    #        running = False
    
    pygame.display.flip()

    # pygame.quit()
    return
    
