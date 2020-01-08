import pygame
from pygame import mixer
import random
import math
# initializing pygame lib
pygame.init()

xAxis = 800
yAxis = 600

# setting window parameters
# set_mode method gets args as a tuple
screen = pygame.display.set_mode((xAxis, yAxis))
# background
background = pygame.image.load("background.png")
mixer.music.load("background.wav")
mixer.music.play(-1)

# setting display props ie title, icon respectively
pygame.display.set_caption("My First game")
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)


# since prog exits when it runs the lines above,
# in order to keep it running, we use while loop
running = True  # flag for window
# moreover entire playground config is done within this loop

# player placement 
playerImg = pygame.image.load("spaceship.png")
playerX = 370
playerY = 493
movementX = 0
speed = 5
minBoundary = 0
maxBoundary = xAxis - 66

# enemies
enemiesCount = 10
enemyImg = []
enemyX = []
enemyY = []
enemySpeedX = []
enemySpeedY = []
for i in range(enemiesCount):
    enemyImg.append(pygame.image.load("alien.png"))
    enemyX.append(random.randint(0, 730))
    enemyY.append(random.randint(0, 200))
    enemySpeedX.append(random.randint(1, 4))
    enemySpeedY.append(random.randint(1, 1))

# bullet
bulletImg = pygame.image.load("bullet.png")
bulletX = 0
bulletY = 493
bulletSpeedY = 10
bulletState = "ready"

# score
scoreVal = 0
font = pygame.font.Font("freesansbold.ttf", 22)
scoreX = 660
scoreY = 559

# game over
fontGameOver = pygame.font.Font("freesansbold.ttf", 40)
fontll = pygame.font.Font("freesansbold.ttf", 18)



def score(scoreX, scoreY):
    score = font.render("Score: "+ str(scoreVal), True, (255, 255, 255))
    screen.blit(score, (scoreX, scoreY))


def gameOver():
    gameOver = fontGameOver.render("GAME OVER", True, (255, 255, 255))
    connectMe = fontll.render(
        "connect me on Linkedin: https://www.linkedin.com/in/tejinder-singh-34014a163/", True, (240,240,240))
    screen.blit(gameOver, (280, 280))
    screen.blit(connectMe, (60, 330))



def player(playerX, playerY):
    # for binding immage with its coordinates
    screen.blit(playerImg, (playerX, playerY))


def enemy(enemyX, enemyY, i):
    # for binding immage with its coordinates
    screen.blit(enemyImg[i], (enemyX[i], enemyY[i]))


def bullet(bulletX, bulletY):
    global bulletState
    bulletState = "firing"
    # for binding immage with its coordinates
    screen.blit(bulletImg, (bulletX+16, bulletY+10))


def isCollision(enemyX, enemyY, bulletX, bulletY):
    dist = math.sqrt(math.pow(enemyX - bulletX, 2) +
                     (math.pow(enemyY - bulletY, 2)))
    if dist < 32:
        return True
    return False


while running:

    # for coloring the  screena
    screen.fill((192, 192, 192))  # tuple of rgb val
    screen.blit(background, (0, 0))

    # for event handling including closing a window
    for event in pygame.event.get():
        # checking if closed event is occured
        if event.type == pygame.QUIT:
            running = false
        # checking if any key is pressed ie for movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                movementX = -speed
            if event.key == pygame.K_RIGHT:
                movementX = speed
            if event.key == pygame.K_SPACE:
                if bulletState is "ready":
                    firingSound = mixer.Sound("laser.wav")
                    firingSound.play()
                    bulletX = playerX
                    bullet(bulletX, bulletY)
        # for stopping the movement
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                movementX = 0

    playerX += movementX

    # setting boundaries for player
    if playerX <= minBoundary:
        playerX = minBoundary
    elif playerX > maxBoundary:
        playerX = maxBoundary

    for i in range(enemiesCount):
        if enemyY[i] > 430:
            for j in range(enemiesCount):
                enemyY[j] = 2000  
            gameOver()
            break

        enemyX[i] += enemySpeedX[i]  # enemy position change
        # for incomingCar
        if enemyX[i]+64 > xAxis or enemyX[i] < 0:
            print("cleared")
            enemySpeedX[i] = -enemySpeedX[i]
            enemyY[i] += 60

        # for colliding
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            collisionSound = mixer.Sound("explosion.wav")
            bulletY = 493
            collisionSound.play()
            scoreVal += 1
            bulletState = "ready"
            enemyX[i] = random.randint(0, 730)
            enemyY[i] = random.randint(0, 200)
            enemySpeedX[i] = random.randint(1, 4)
            enemySpeedY[i] = random.randint(1, 1)
        enemy(enemyX, enemyY, i)

    if bulletY < 0:
        bulletY = 493
        bulletState = "ready"
    if bulletState is "firing":
        bullet(bulletX, bulletY)
        bulletY -= bulletSpeedY

    # for displaying the player and enemy
    player(playerX, playerY)
    score(scoreX, scoreY)
    # we need to update window once we made changes to our playground
    pygame.display.update()
