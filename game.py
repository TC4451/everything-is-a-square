import pygame

gameHeight = 900
gameWidth = 1600

pygame.init()
gameDisplay = pygame.display.set_mode((gameWidth, gameHeight))
pygame.display.set_caption('Everything-is-a-square')
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
            
    pygame.display.update()
    clock.tick(60)
    