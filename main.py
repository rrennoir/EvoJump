import pygame as pg


def main():

    # init pygame, import every module in pygame.
    pg.init()

     # Setup window of 500 by 400 pixel.
    display_size = [500, 400]
    screen = pg.display.set_mode(display_size)

    # Set the windows title
    pg.display.set_caption("Jump")

    clock = pg.time.Clock()

    play = True
    while play:

        screen.fill((0, 0, 0))

        keys = pg.key.get_pressed()
        for event in pg.event.get():

            if event.type == pg.QUIT:
                play = False
                pg.quit()
                quit()

    screen.blit(screen, (0, 0))
    pg.display.flip()

    # Set the game to 60 update per second.
    clock.tick(60)


if __name__ == "__main__":
    main()