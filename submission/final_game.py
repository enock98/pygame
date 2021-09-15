# In this example.py you will learn how to make a very simple game using the pygame library.
# One of the best ways of learning to program is by writing games.
# Pygame is a collection of modules in one package.
# You will need to install pygame.
# To do so:
# 1) open the command line interface on your computer,
# 2) cd to the directory that this task is located in,
# 3) follow the instructions here: https://www.pygame.org/wiki/GettingStarted
# 4) if you need help using pip, see here: https://projects.raspberrypi.org/en/projects/using-pip-on-windows

import pygame # Imports a game library that lets you use specific functions in your program.
import random # Import to generate random numbers. 

# Initialize the pygame modules to get everything started.

pygame.init() 

# The screen that will be created needs a width and a height.

screen_width = 1040
screen_height = 680
screen = pygame.display.set_mode((screen_width,screen_height)) # This creates the screen and gives it the width and height specified as a 2 item sequence.


# This creates the player and gives it the image found in this folder (similarly with the enemy image). 

player = pygame.image.load("player.png")                     # Changed image to player
enemy = pygame.image.load("monster.png")                 
enemy1 = pygame.image.load("monster.png")                    # Added another enemy
enemy2 = pygame.image.load("monster.png")                    # Added another enemy
enemy3 = pygame.image.load("monster.png")                    # Added another enemy
prize = pygame.image.load("prize.png")                       # Added prize 

# Get the width and height of the images in order to do boundary detection (i.e. make sure the image stays within screen boundaries or know when the image is off the screen).

image_height = player.get_height()
image_width = player.get_width()
enemy_height = enemy.get_height()
enemy_width = enemy.get_width()
enemy1_height = enemy1.get_height()                          # Height dimension added for enemy1
enemy1_width = enemy1.get_width()                            # Width dimension added for enemy1
enemy2_height = enemy2.get_height()                          # Height dimension added for enemy2
enemy2_width = enemy2.get_width()                            # Width dimension added for enemy2
enemy3_height = enemy3.get_height()                          # Height dimension added for enemy3
enemy3_width = enemy3.get_width()                            # Width dimension added for enemy3
prize_height = prize.get_height()                            # Height dimension added for prize
prize_width = prize.get_width()                              # Width dimension added for prize


print("This is the height of the player image: " +str(image_height))
print("This is the width of the player image: " +str(image_width))

# Store the positions of the player and enemy as variables so that you can change them later. 

playerXPosition = 30
playerYPosition = 100

# Make the enemy start off screen and at a random y position.

enemyXPosition =  screen_width
enemyYPosition =  random.randint(0, screen_height - enemy_height)
enemy1XPosition =  screen_width + 2 * enemy1_width
enemy1YPosition =  random.randint(0, screen_height - enemy1_height)
enemy2XPosition =  screen_width + 2 * enemy2_width
enemy2YPosition =  random.randint(0, screen_height - enemy2_height)
enemy3XPosition =  screen_width + 2  * enemy3_width
enemy3YPosition =  random.randint(0, screen_height - enemy3_height)

# The prize position captured below. 

prizeXPosition =   screen_width + 2  * prize_width
prizeYPosition =   random.randint(0, screen_height - prize_height)

# This checks if the up or down key is pressed.
# Right now they are not so make them equal to the boolean value (True or False) of False. 
# Boolean values are True or False values that can be used to test conditions and test states that are binary, i.e. either one way or the other. 

keyUp= False
keyDown = False
keyRight = False 
keyLeft = False

# This is the game loop.
# In games you will need to run the game logic over and over again.
# You need to refresh/update the screen window and apply changes to 
# represent real time game play. 

while 1: # This is a looping structure that will loop the indented code until you tell it to stop(in the event where you exit the program by quitting). In Python the int 1 has the boolean value of 'true'. In fact numbers greater than 0 also do. 0 on the other hand has a boolean value of false. You can test this out with the bool(...) function to see what boolean value types have. You will learn more about while loop structers later. 

    screen.fill(0) # Clears the screen.
    screen.blit(player, (playerXPosition, playerYPosition))# This draws the player image to the screen at the postion specfied. I.e. (100, 50).
    screen.blit(enemy, (enemyXPosition, enemyYPosition))
    screen.blit(enemy1, (enemy1XPosition, enemy1YPosition))
    screen.blit(enemy2, (enemy2XPosition, enemy2YPosition))
    screen.blit(enemy3, (enemy3XPosition, enemy3YPosition))
    screen.blit(prize, (prizeXPosition, prizeYPosition))
    
    pygame.display.flip()# This updates the screen. 
    
    # This loops through events in the game.
    
    for event in pygame.event.get():
    
        # This event checks if the user quits the program, then if so it exits the program. 
        
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

        # This event checks if the user press a key down.
        
        if event.type == pygame.KEYDOWN:
        
            # Test if the key pressed is the one we want.
            
            if event.key == pygame.K_UP: # pygame.K_UP represents a keyboard key constant. 
                keyUp = True
            if event.key == pygame.K_DOWN:
                keyDown = True
            if event.key == pygame.K_RIGHT: 
                keyRight = True
            if event.key == pygame.K_LEFT:
                keyLeft = True
                       
        
        # This event checks if the key is up(i.e. not pressed by the user).
        
        if event.type == pygame.KEYUP:
        
            # Test if the key released is the one we want.
            
            if event.key == pygame.K_UP:
                keyUp = False
            if event.key == pygame.K_DOWN:
                keyDown = False
            if event.key == pygame.K_RIGHT:
                keyRight = False
            if event.key == pygame.K_LEFT:
                keyLeft = False
                                                
    # After events are checked for in the for loop above and values are set,
    # check key pressed values and move player accordingly.
    
    # The coordinate system of the game window(screen) is that the top left corner is (0, 0).
    # This means that if you want the player to move down you will have to increase the y position. 
    
    if keyUp == True:
        if playerYPosition > 0 : # This makes sure that the user does not move the player above the window.
            playerYPosition -= 1
    if keyDown == True:
        if playerYPosition < screen_height - image_height:# This makes sure that the user does not move the player below the window.
            playerYPosition += 1
    if keyLeft == True:
        if playerXPosition > 0:
            playerXPosition -= 1 
    if keyRight == True:
        if playerXPosition < screen_width - image_width:
            playerXPosition += 1  
    
    # Check for collision of the enemy with the player.
    # To do this we need bounding boxes around the images of the player and enemy.
    # We the need to test if these boxes intersect. If they do then there is a collision.
    
    # Bounding box for the player:
    
    playerBox = pygame.Rect(player.get_rect())
    playerBox.top = playerYPosition
    playerBox.left = playerXPosition
    
    # Bounding box for the enemy:
    
    enemyBox = pygame.Rect(enemy.get_rect())
    enemyBox1 = pygame.Rect(enemy1.get_rect())
    enemyBox2 = pygame.Rect(enemy2.get_rect())
    enemyBox.top = enemyYPosition
    enemyBox.left = enemyXPosition
    enemyBox1.top = enemy1YPosition
    enemyBox1.left = enemy1XPosition
    enemyBox2.top = enemy2YPosition
    enemyBox2.left = enemy2XPosition

    # Bounding box for the prize:

    prizeBox = pygame.Rect(prize.get_rect())
    prizeBox.top = prizeYPosition
    prizeBox.left = prizeXPosition
    
    # The following updates the playerBox position to the player's position,
    # in effect making the box stay around the player image. 
     
    # Test collision of the boxes:
    
    if playerBox.colliderect(enemyBox)or playerBox.colliderect(enemyBox1) or playerBox.colliderect(enemyBox2):
    
        # Display losing status to the user: 
        
        print("You Lose!")
       
        # Quite game and exit window: 
        
        pygame.quit()
        exit(0)

        
    if playerBox.colliderect(prizeBox):
    
        # Display winning status to the user: 
        
        print("You Win!")
       
        # Quite game and exit window: 
        
        pygame.quit()
        exit(0)

        
    # If the enemy is off the screen the user wins the game:
    
    if enemyXPosition < 0 - enemy_width:
    
        # Display losing status to the user: 
        
        print("You Lose!")
        
        # Quite game and exit window: 

        pygame.quit()       
        exit(0)

     
    # Make enemy approach the player.
    
    enemyXPosition -= 0.15
    enemy1XPosition -= 0.40
    enemy2XPosition -= 0.30
    prizeXPosition -=0.15
    
    # ================The game loop logic ends here. =============

# Hi Imraan, please be so kind to check again. I run the code and the program executes perfectly.
# Checked it now 20 times, I kid you not, just to make sure. Hishaam was here to check and confirm as well, it runs 100% on my machine, no issues.
# Asked the other students here to check as well, no issues.

# I have to apologize for my mistake, i didn't mention that you should be looking in the "MyCapstone" folder for the task. It should work now.


  
