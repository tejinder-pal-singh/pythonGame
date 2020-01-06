import pygame

# initializing pygame lib
pygame.init()

# setting window parameters
#set_mode method gets args as a tuple
screen = pygame.display.set_mode((800, 600))

#setting display props ie title, icon respectively
pygame.display.set_caption("My First game")
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

#since prog exits when it runs the lines above,
#in order to keep it running, we use while loop
running = True  #flag for window
#moreover entire playground config is done within this loop

#player placement ie car
playerImg = pygame.image.load("car.png")
playerX = 370
playerY = 493

def player():
    #for binding immage with its coordinates
    screen.blit(playerImg, (playerX, playerY))

while running:
    #for coloring the  screen
    screen.fill((192,192,192)) #tuple of rgb val


    #for event handling mainly for closing a window mainly
    for event in pygame.event.get():
        #checking if closed event is occured
        if event.type == pygame.QUIT:
            running = false



    #for displaying the player image
    player()
    #we need to update window once we made changes to our playground
    pygame.display.update()


