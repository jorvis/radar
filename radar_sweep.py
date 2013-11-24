#!/usr/bin/env python3

"""
Owen wants this:
http://www.youtube.com/watch?v=a-BoIObTgQI&t=0m46s

Things which might help later:
- Antialiased rings / filled circles:
  http://abarry.org/antialiased-rings-filled-circles-in-pygame/
"""

# Import a library of functions called 'pygame'
import pygame
import pygame.gfxdraw
import math
 
# Initialize the game engine
pygame.init()
 
# Define the colors we will use in RGB format
background_color    = [   46, 48,  47 ]
sweep_color         = [ 241, 255, 255 ]
outer_border_color  = [  71,  74,  84 ]
outer_circle_color  = [ 113, 125, 150 ]
inner_border_color  = [  83,  93, 117 ]
inner_circle_color  = [ 164, 180, 211 ]

# Set the height and width of the screen
screen_width = 600
screen_height = 600
outer_border_width = 12
inner_border_width = 9

screen = pygame.display.set_mode((screen_width,screen_height))
midpoint = [ int(screen_width/2), int(screen_height/2) ]
radius = midpoint[0]
sweep_length = radius - outer_border_width
 
my_clock = pygame.time.Clock()
 
#Loop until the user clicks the close button.
done = False
angle = 0
sweep_interval = .005
sweep_speed = sweep_interval

while done==False:
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                pass
            
            elif event.key == pygame.K_RIGHT:
                pass
            
            elif event.key == pygame.K_UP:
                # no upper bounds on speed
                sweep_speed += sweep_interval
                
            elif event.key == pygame.K_DOWN:
                # slow it down, or stop
                sweep_speed -= sweep_interval
                if sweep_speed < 0:
                    sweep_speed = 0
                
    # Set the screen background
    screen.fill(background_color)
 
    # Draw the main circle
    pygame.gfxdraw.aacircle(screen, midpoint[0], midpoint[1], radius, outer_border_color)
    pygame.gfxdraw.filled_ellipse(screen, midpoint[0], midpoint[1], radius, radius, outer_border_color)

    pygame.gfxdraw.aacircle(screen, midpoint[0], midpoint[1], radius - outer_border_width, outer_circle_color)
    pygame.gfxdraw.filled_ellipse(screen, midpoint[0], midpoint[1], radius - outer_border_width, radius - outer_border_width, outer_circle_color)

    # Calculate the x,y for the end point of our 'sweep' based on the current angle
    x = sweep_length * math.sin(angle) + int(screen_width/2)
    y = sweep_length * math.cos(angle) + int(screen_height/2)
 
    # Draw the line from the center at 145, 145 to the calculated end spot
    pygame.draw.line(screen, sweep_color, midpoint, [x,y], 1)

    # now draw the things that layer over the sweep
    inner_circle_radius = int(radius/3)
    pygame.gfxdraw.aacircle(screen, midpoint[0], midpoint[1], inner_circle_radius, inner_border_color)
    pygame.gfxdraw.filled_ellipse(screen, midpoint[0], midpoint[1], inner_circle_radius, inner_circle_radius, inner_border_color)

    pygame.gfxdraw.aacircle(screen, midpoint[0], midpoint[1], inner_circle_radius - inner_border_width, inner_circle_color)
    pygame.gfxdraw.filled_ellipse(screen, midpoint[0], midpoint[1], inner_circle_radius - inner_border_width, inner_circle_radius - inner_border_width, inner_circle_color)

    # do the distortion lines
    #if angle > 0 and angle < 280:
        #pygame.draw.line(screen, sweep_color, midpoint, [sweep_length * ,y], 1)
    myfont = pygame.font.SysFont("monospace", 12)
    label = myfont.render("Sweep endpoint: [x:{0:.2f},y:{1:.2f}]".format(x,y), 1, (200,200,200))
    screen.blit(label, (100, 100))
    
    # Increase the angle by 0.05 radians
    angle = angle + sweep_speed
 
    # If we have done a full sweep, reset the angle to 0
    pi = 3.141592653
    if angle > 2*pi:
        angle = angle - 2*pi
 
    # Update the display, wait out the clock tick
    pygame.display.update()
    my_clock.tick(60)

    ##########
    ## random notes
    # I don't see a difference with an anti-aliased line
    #pygame.draw.aaline(screen, sweep_color, midpoint, [x,y])

    # To really make this perform better, keep track of dirty rectangles later and only update those:
    #   "Dirty rect animation" - http://www.pygame.org/docs/tut/newbieguide.html
    
 

pygame.quit()
