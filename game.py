import asyncio
from pygame import *
from random import randint
import time as tid

async def main():
    # Initialize Pygame
    init()

    # Game Constants
    WIDTH, HEIGHT = 800, 400
    FPS = 60
    GRAVITY = 0.5
    JUMP_STRENGTH = -10

    # Colors
    WHITE = (255, 255, 255)

    # Load assets
    player_img = image.load("assets/img/player.png")
    background_img = image.load("assets/img/background.png")
    tree_img = image.load("assets/img/tree.png")

    rand_tree_pos = (randint(0, 790), randint(225,235))
    tree_positions = [rand_tree_pos]

    # Scale assets
    player_img = transform.scale(player_img, (50, 50))
    tree_img = transform.scale(tree_img, (70, 100))
    tree_counter_img = transform.scale(tree_img, (35, 40))
    background_img = transform.scale(background_img, (WIDTH, HEIGHT))

    # Initilize font
    text_font = font.SysFont('Arial', 36)
    def draw_text(text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        screen.blit(img, (x, y))

    # Initilize counter
    tree_counter = 0

    # Game Variables
    player_x = 0
    player_y = 290
    player_speed = 5
    player_velocity_y = 0
    is_jumping = False
    ground_level = 290

    # Create game window
    screen = display.set_mode((WIDTH, HEIGHT))
    display.set_caption("Tree Collecting")

    # Game Loop
    clock = time.Clock()
    running = True
    visible_tree = True

    while running:
        clock.tick(FPS)
        
        for evnt in event.get():
            if evnt.type == QUIT:
                running = False

        keys = key.get_pressed()
        if keys[K_RIGHT]:
            player_x += player_speed
        elif keys[K_LEFT]:
            player_x -= player_speed

        if keys[K_UP] and not is_jumping:
            player_velocity_y = JUMP_STRENGTH
            is_jumping = True

        player_velocity_y += GRAVITY
        player_y += player_velocity_y
        if player_y >= ground_level:
            player_y = ground_level
            is_jumping = False

        screen.blit(background_img, (0, 0))
        for pos in tree_positions:
            if pos[0] in range(player_x-5, player_x+5) and not player_y < pos[1]:
                visible_tree = False
                tree_positions.append((randint(-10, 790), randint(225, 260)))
                tid.sleep(0.05)
                tree_positions.remove(pos)
                tree_counter += 1
            elif visible_tree: 
                screen.blit(tree_img, pos)
            else:
                visible_tree = True

        screen.blit(tree_counter_img, (0,0))
        screen.blit(player_img, (player_x, player_y))
        draw_text(f"{tree_counter}", text_font, (255, 255, 255), 35, 5)

        if player_x > WIDTH:
            player_x = -30
        if player_x < -30:
            player_x = WIDTH + player_speed

        display.flip()

        # Yield to browser so it doesn’t freeze
        await asyncio.sleep(0)

    quit()

# Run the async game loop
asyncio.run(main())
