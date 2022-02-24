import pygame
import random

pygame.init()

display_width = 800
display_height = 600
player_size = 60
pillar_width = 60
pillar_gap = 120

clock = pygame.time.Clock()

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Flappy Bird 1.0.0")

red = (255,0,0)
green = (0,255,0) 
blue = (0,0,225)
black = (0,0,0)
bgcolor = (255, 255, 200)

'''
gameIcon = pygame.image.load() #yet to be added
pygame.display.set_icon(gameIcon)
'''

# bird = pygame.image.load('bird.png')
# bird = pygame.transform.scale(bird, (60, 60))

smallText = pygame.font.Font('freesansbold.ttf',15)
largeText = pygame.font.Font('freesansbold.ttf',105)

def fly(x,y,color = blue):
    #gameDisplay.blit(bird,(x,y))
    pygame.draw.rect(gameDisplay,color,[x,y,player_size,player_size])

def scr(score):
    text = smallText.render("SCORE: "+str(score), True, black)
    gameDisplay.blit(text,(10,10))

def start():
    print('game starts here')

def pillar_generator():
    upper_pillar = 200 + random.randint(-150,280)
    lower_pillar = upper_pillar + pillar_gap
    return upper_pillar, lower_pillar

upper_pillar, lower_pillar = pillar_generator()

def pillar(x=200):
    pygame.draw.rect(gameDisplay,green,[x,0,pillar_width,upper_pillar])
    pygame.draw.rect(gameDisplay,green,[x,lower_pillar,pillar_width,display_height - lower_pillar])

def gameLoop():
    start()

    global upper_pillar, lower_pillar

    reduce = 0
    frameRate = 60
    score = 0
    dodged = 0
    bird_position_x = 200
    bird_position_y = 200
    velocity = 0
    jumpVelocity = -250
    gravity = 1000
    time_elapsed = 0
    pillar_position_x = display_width + 100
    pillar_velocity = -100

    gameExit = False
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    velocity = jumpVelocity

        gameDisplay.fill(bgcolor)
    
        #bird auto fall
        if bird_position_y >= -20 and bird_position_y <= display_height - player_size:
            bird_position_y += velocity*(1/frameRate)
            velocity += gravity*(1/frameRate)

        # reduce 1 point on touching top
        if 0 > bird_position_y :
            bird_position_y = 0
            pygame.draw.rect(gameDisplay,red,[0,0,display_width,3])
            if score > 0 and reduce == 0:
                score -= 1      
            reduce = 1
        else:
            reduce = 0 

        # scoring
        if bird_position_x > pillar_position_x:
            if increase == 0:
                score +=1
                dodged += 1
            increase = 1
        else:
            increase = 0 

        # pillar scroll
        time_elapsed += 1/frameRate
        if time_elapsed > (display_width + 4*pillar_width) / -pillar_velocity:
            time_elapsed = 0
            pillar_position_x = display_width + 100
            upper_pillar, lower_pillar = pillar_generator()

        pillar_position_x += (pillar_velocity - dodged) * (1/frameRate)
        pillar(pillar_position_x)
        scr(score)
        fly(bird_position_x,bird_position_y)

        #touch bottom
        if bird_position_y>540:
            text = largeText.render("GAME OVER",True,black)
            gameDisplay.blit(text,(70,200))
            fly(bird_position_x,bird_position_y,red)
            pygame.display.update()
            pygame.time.delay(3000)
            gameLoop()

        pygame.display.update()
        clock.tick(frameRate)

gameLoop()