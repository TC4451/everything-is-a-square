import pygame

game_height = 600
game_width = 500

square_size = 30

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
y = game_height / 2

accel = 0.6
deccel = 0.3

x_speed = 0
y_speed = 0

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


    # If a key is pressed, accelerate in the direction of the key
    if left_key:
        x_speed -= accel

    if right_key:
        x_speed += accel

    if up_key:
        y_speed -= accel
    
    if down_key:
        y_speed += accel
    
    # Subtract decceleration
    if x_speed > 0:
        x_speed -= deccel
    elif x_speed < 0:
        x_speed += deccel

    if y_speed > 0:
        y_speed -= deccel
    elif y_speed < 0:
        y_speed += deccel

    # Avoid drift
    if abs(x_speed) < 0.3:
        x_speed = 0
    
    if abs(y_speed) < 0.3:
        y_speed = 0

     # Add speed to square position
    x += x_speed
    y += y_speed

    #Handle hitting walls
    if x < 0:
        x = 0
    elif x > (game_width - square_size):
        x = game_width - square_size
    
    if y < 0:
        y = 0
    elif y > (game_height - square_size):
        y = game_height - square_size

    
    game_display.fill(white)
    draw_square(red, x, y, square_size)

    
    pygame.display.update()
    clock.tick(60)
    