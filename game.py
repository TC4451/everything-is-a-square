import pygame
import math

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

player_x = game_width / 2
player_y = game_height / 2

previous_x = player_x
previous_y = player_y

accel = 0.6
deccel = 0.3

x_speed = 0
y_speed = 0

map = [
    [0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0],
    [0, 1, 0, 1, 1, 0],
    [0, 0, 0, 0, 0, 0]
    ]


pygame.init()
game_display = pygame.display.set_mode((game_width, game_height))
pygame.display.set_caption('Everything-is-a-square')
clock = pygame.time.Clock()

def draw_square(color, x, y, size):
        pygame.draw.rect(game_display, color, [x, y, size, size])

def draw_map(map):
    for y, row in enumerate(map):
        for x, block in enumerate(row):
            if block == 1:
                x_pos = x * 100
                y_pos = y * 100
                draw_square(black, x_pos, y_pos, 100)
                
def highlight_block():
    block_index_x = math.floor(player_x / 100)
    block_index_y = math.floor(player_y / 100)
    draw_square(green, block_index_x * 100, block_index_y * 100, 100)
    # draw_square(red, block_index_x * 100, (block_index_y - 1) * 100, 100)
    # draw_square(red, (block_index_x - 1) * 100, block_index_y * 100, 100)
    
    # top right block
    draw_square(red, (block_index_x + 1) * 100, (block_index_y - 1) * 100, 100)
    # bottom left block
    draw_square(red, (block_index_x - 1) * 100, (block_index_y + 1) * 100, 100)
    # bottom right block
    draw_square(red, (block_index_x + 1) * 100, (block_index_y + 1) * 100, 100)

def check_collision():
    global player_x
    global player_y
    global x_speed
    global y_speed
    # need global because we are updating a global varaible

    block_index_x = math.floor(previous_x / 100)
    block_index_y = math.floor(previous_y / 100)    
    left_block_x_index = block_index_x - 1
    top_block_y_index = block_index_y - 1
    right_block_x_index = block_index_x + 1
    bottom_block_y_index = block_index_y + 1
    # print(f"block index y is {block_index_y}, left_block_x_index is {left_block_x_index}, map[block_index_y][left_block_x_index] is {map[block_index_y][left_block_x_index]}")
    
    # checking the left block
    if map[block_index_y][left_block_x_index] == 1:
        if player_x < block_index_x * 100:
            player_x = block_index_x * 100
            x_speed = 0
    
    # checking the top block
    if map[top_block_y_index][block_index_x] == 1:
        if player_y < block_index_y * 100:
            player_y = block_index_y * 100
            y_speed = 0

    # checking the right block
    if map[block_index_y][right_block_x_index] == 1:
        if player_x >= right_block_x_index * 100 - square_size:
            player_x = right_block_x_index * 100 - square_size
            x_speed = 0
    
    
    # checking the bottom block
    if map[bottom_block_y_index][block_index_x] == 1:
        if player_y >= bottom_block_y_index * 100 - square_size:
            player_y = bottom_block_y_index * 100 - square_size
            y_speed = 0

            
    # checking the top right corner
    if map[top_block_y_index][right_block_x_index] == 1: 
        if player_y < block_index_y * 100:
            if player_x >= right_block_x_index * 100 - square_size:
                player_y = block_index_y * 100
                y_speed = 0
    
    # checking the bottom left corner
    if map[bottom_block_y_index][left_block_x_index] == 1: 
        if player_y >= bottom_block_y_index * 100 - square_size:
            if player_x < block_index_x * 100:
                player_x = block_index_x * 100
                x_speed = 0 

    # checking the bottom right corner
    if map[bottom_block_y_index][right_block_x_index] == 1: 
        if player_y > bottom_block_y_index * 100 - square_size:
            if player_x >= right_block_x_index * 100 - square_size:
                # checks if moving right
                if previous_x <= right_block_x_index * 100 - square_size:
                    player_x = right_block_x_index * 100 - square_size
                    x_speed = 0 
                # checks if moving down
                if previous_y <= bottom_block_y_index * 100 - square_size:
                    player_y = bottom_block_y_index * 100 - square_size
                    y_speed = 0
        # print(f"player_y:{player_y} previous_y: {previous_y} bottom_block_y_index * 100 - square_size: {bottom_block_y_index * 100 - square_size}")

while True:
    
    # Handle key presses
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
    if abs(x_speed) < deccel:
        x_speed = 0
    
    if abs(y_speed) < deccel:
        y_speed = 0

    previous_x = player_x
    previous_y = player_y

    # Add speed to player position
    player_x += x_speed
    player_y += y_speed

    # Handle hitting walls
    if player_x < 0:
        player_x = 0
    elif player_x > (game_width - square_size):
        player_x = game_width - square_size
    
    if player_y < 0:
        player_y = 0
    elif player_y > (game_height - square_size):
        player_y = game_height - square_size

    
    check_collision()
    
    # Background
    game_display.fill(white)

    # Draw the blocks
    draw_map(map)

    # helped with debugging collision
    # highlight_block()

    # Draw player square
    draw_square(red, player_x, player_y, square_size)

    
    pygame.display.update()
    clock.tick(60)
    