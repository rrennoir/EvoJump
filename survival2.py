import pygame as pg


def accueil(screen):

    background = pg.image.load("background.jpg").convert()
    screen.blit(background, (0, 0))
    pg.display.flip()

    running = True
    while running:

        for event in pg.event.get():

            if event.type == pg.QUIT:
                running = False
                quit()

            if event.type == pg.KEYDOWN:

                if event.key == pg.K_ESCAPE:
                    running = False
                    quit()

                if event.key == pg.K_RETURN:
                    print("Sort d'accueil")
                    return

        pg.time.Clock().tick(30)


def main():

    pg.init()

    largeur = 500
    hauteur = 400
    taille_affichage = [largeur, hauteur]
    screen = pg.display.set_mode(taille_affichage)

    accueil(screen)


if __name__ == "__main__":
    main()
