import pygame as pg


def main():

    # init pygame, import every module in pygame.
    pg.init()

    # Setup window of 500 by 400 pixel.
    width = 500
    height = 400
    display_size = [width, height]
    screen = pg.display.set_mode(display_size)

    # Set the windows title
    pg.display.set_caption("Jump")

    clock = pg.time.Clock()

    # Create player rect.
    player_size = 20
    player_rect = pg.Rect(width / 2, height / 2, player_size, player_size)

    obstacle_rect_list = []
    tick = 0
    in_jump = False
    jump_tick = 0
    obstacle_tick = 0
    play = True
    while play:

        screen.fill((0, 0, 0))

        keys = pg.key.get_pressed()
        for event in pg.event.get():

            if event.type == pg.QUIT:
                play = False
                pg.quit()
                quit()

        if in_jump:
            jump_tick -= 1
            if jump_tick == 0:
                player_rect = player_rect.move(0, 50)
                in_jump = False

        # If SPACE is pressed made the jump.
        if keys[pg.K_SPACE] and not in_jump:
            player_rect = player_rect.move(0, -50)
            in_jump = True
            jump_tick = 90

        # Spawn a obstacle every seconde just out side of the screen.
        if obstacle_tick == 3:

            obstacle_tick = 0
            obstacle_rect = pg.Rect(width, height / 2, 20, 20)
            obstacle_rect_list.append(obstacle_rect)

        # Update obstacle position and check for colision with the player.
        for index, obstacle_rect in enumerate(obstacle_rect_list):
            if obstacle_rect.colliderect(player_rect):
                print("LOST")
                return
            obstacle_rect_list[index] = obstacle_rect.move(-1, 0)

        # Draw player on the middle of the screen.
        pg.draw.rect(screen, (255, 255, 255), player_rect)

        # Draw obstacle.
        for obstacle in obstacle_rect_list:
            pg.draw.rect(screen, (255, 0, 0), obstacle)

        # Update display.
        screen.blit(screen, (0, 0))
        pg.display.flip()

        # Count tick.
        if tick > 60:
            tick = 0
            obstacle_tick += 1
        tick += 1

        # Set the game to 60 update per second.
        clock.tick(60)


if __name__ == "__main__":
    main()
