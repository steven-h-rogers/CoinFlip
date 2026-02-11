import pygame, sys

pygame.init()

screen = pygame.display.set_mode((1000,1000))
clock = pygame.time.Clock()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or running == False:
            print('quitting')
            pygame.quit()
            sys.exit()

    

    pygame.display.flip()
    clock.tick(60)