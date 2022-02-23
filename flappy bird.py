import pygame

pygame.init()

display_width = 800
display_height = 600

clock = pygame.time.Clock()

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Flappy Bird 1.0.0")

'''
gameIcon = pygame.image.load() #yet to be added
pygame.display.set_icon(gameIcon)
'''

bird = {}
tower = {}

score = 0

gameExit = False
while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE: #jump
                print('spacebar pressed')

    gameDisplay.fill((255,255,200))
    pygame.display.update()
    clock.tick(60)