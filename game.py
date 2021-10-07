import pygame

game_height = 900
game_width = 1600

red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 200, 0)
blue = pygame.Color(0, 0, 255)
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)


pygame.init()
game_display = pygame.display.set_mode((game_width, game_height))
pygame.display.set_caption('Everything-is-a-square')
clock = pygame.time.Clock()

def draw_square(color, x, y, size):
        pygame.draw.rect(game_display, color, [x, y, size, size])


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    draw_square(red, 20, 20, 30)

    pygame.display.update()
    clock.tick(60)
    