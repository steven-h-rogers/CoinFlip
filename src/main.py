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
        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    print('flip')    

    

    pygame.display.flip()
    clock.tick(60)