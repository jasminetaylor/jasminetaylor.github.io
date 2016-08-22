"""
 Pygame base template for opening a window

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/vRB_983kUMc
"""

import pygame
import random



# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (127, 127, 127)
 
colors = ["BLACK", "WHITE", "GREEN", "RED", "BLUE", "GREY" ]
list = len(colors)-1
#random_color = random.randint(0,(list[6]))

pygame.init()


Font = pygame.font.Font(None, 25)

# Set the width and height of the screen [width, height]
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Ball Game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()


possible_ball_colors = [BLACK, WHITE, GREEN, RED, BLUE, GREY]
x_speed = random.randint(-10, 10)
y_speed = random.randint(-10, 10)
x_location = int(SCREEN_WIDTH/2)
y_location = int(SCREEN_HEIGHT/2)
ball_size = random.randint(10,30)
# BOUNCING BALL CLASS CODE  

class BouncingBall(): 

    # CONSTRUCTOR METHOD 
    def __init__(self, x_location, y_location, x_speed, y_speed, ball_size):  
    # Attributes of the bouncing ball 
        self.x_location = x_location
        self.y_location = y_location  
        self.x_speed = x_speed
        self.y_speed = y_speed 
        self.ball_size = ball_size 
        
    # BALL METHODS 
    # Flash and Bounce: The actions the ball can perform 
    def flashBounce(self, screen, colors, screen_width, screen_height):

        ball_color = random.choice(colors) # This is outside because of variable scoping.

        if self.x_location >= screen_width - self.ball_size or self.x_location < self.ball_size:
            self.x_speed = self.x_speed * -1

        if self.y_location >= screen_height - self.ball_size or self.y_location < self.ball_size:
            self.y_speed = self.y_speed * -1

        self.x_location += self.x_speed 
        self.y_location += self.y_speed 

        pygame.draw.circle(screen, ball_color, [self.x_location, self.y_location], self.ball_size)
    
ball_click =[]
ball = BouncingBall(x_location, y_location, x_speed, y_speed, ball_size)

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("Here!")
            pos = pygame.mouse.get_pos()
            ball_click.append(BouncingBall(pos[0],pos[1],20,20,30))
            

    # --- Game logic should go here
    #Text = font.render("End Game", True, BLACK)
    #screen.blit(Text, [100,100])
    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(GREEN) 
    
    # --- Drawing code should go here
    for ball in ball_click:
        ball.flashBounce(screen, possible_ball_colors, SCREEN_WIDTH, SCREEN_HEIGHT)
    
    
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE


