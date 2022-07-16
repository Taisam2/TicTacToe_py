import pygame as pg,sys
from pygame.locals import *
import time

#initialize global variables
XO = 'x'
winner = None
draw = False
width = 400
height = 400
white = (255, 255, 255)
line_color = (10, 10, 10)

#TicTacToe 3x3 board
TTT = [[None]*3, [None]*3, [None]*3]

#initializing pgame window
pg.init()
fps =30
CLOCK = pg.time.Clock()
screen = pg.display.set_mode((width, height+100), 0, 32)
pg.display.set_caption('Tic Tac Toe')

#loading the images
opening = pg.image.load('tic_tac_toe.png')
x_img = pg.image.load('tic_tac_toe.png')
o_img = pg.image.load('tic_tac_toe.png')

#resizing the images
x_img = pg.transform.scale(x_img, (80,80))
o_img = pg.transform.scale(o_img, (80,80))
opening = pg.transform.scale(opening, (width, height+100))

def game_opening():
    screen.blit(opening, (0, 0))
    pg.display.update()
    time.sleep(1)
    screen.fill(white)

game_opening()