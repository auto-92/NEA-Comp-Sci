import pygame
import pgzrun

#creates the track and positions it
track = Actor('green_track')
track.pos = 0,0
track.bottomleft = 0,500

#determines the width and height of the game window
WIDTH = 1000
HEIGHT = 500

#green track colour = (42, 149, 14, 255) (R, G, B, A)

#displays and draws everything onto the screen
def draw():
    #screen.fill((0, 50, 200))    #fills the background of the screen with an rgb colour
    screen.blit('red_sky_background', (0,0))    #'blits' the background onto the screen
    track.draw()    #draws the track on the screen

#updates the screen a 60 times a second, scrolls track
def update():
    track_scrolling()

#function that makes the track actor 'scroll' across the screen when right key pressed
def track_scrolling():
    if track.right > 1000:
        if keyboard[keys.RIGHT]:
            track.right -= 5