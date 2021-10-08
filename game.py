import pygame

game_height = 900
game_width = 1600

red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 200, 0)
blue = pygame.Color(0, 0, 255)
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)

left_key = False
right_key = False
up_key = False 
down_key = False

x = game_width / 2

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
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                left_key = True
            elif event.key == pygame.K_RIGHT:
                right_key = True
            elif event.key == pygame.K_UP:
                up_key = True
            elif event.key == pygame.K_DOWN:
                down_key = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                left_key = False
            elif event.key == pygame.K_RIGHT:
                right_key = False
            elif event.key == pygame.K_UP:
                up_key = False
            elif event.key == pygame.K_DOWN:
                down_key = False


    if left_key:
        x -= 1
    

    game_display.fill(white)
    draw_square(red, x, 20, 30)

    
    pygame.display.update()
    clock.tick(60)
    