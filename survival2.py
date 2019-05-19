import pygame as pg # au lieu de mettre pygame on met pg pour court et rapide

def jeu(screen, clock, largeur, hauteur): # on rajoute en argument screen et clock... pour les utiliser à partir de main

    

    # Créer un joueur rect = rectangle
    player_size = 20
    player_rect = pg.Rect(largeur / 2, hauteur / 2, player_size, player_size)

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

        # Si vous appuyez sur SPACE, faites le saut.
        if keys[pg.K_SPACE] and not in_jump:
            player_rect = player_rect.move(0, -50)
            in_jump = True
            jump_tick = 90

        # Crée un obstacle chaque seconde juste à l'extérieur de l'écran.
        if obstacle_tick == 3: # ici on détermine le nombre de seconde

            obstacle_tick = 0
            obstacle_rect = pg.Rect(largeur, hauteur / 2, 20, 20)
            obstacle_rect_list.append(obstacle_rect)

        # Mise à jour de la position de l'obstacle et vérification de la collision avec le joueur.
        for index, obstacle_rect in enumerate(obstacle_rect_list):
            if obstacle_rect.colliderect(player_rect):
                print("LOST")
                return
            obstacle_rect_list[index] = obstacle_rect.move(-1, 0)

        # Dessine le joueur au milieu de l’écran.
        pg.draw.rect(screen, (255, 255, 255), player_rect)

        # Dessine un obstacle.
        for obstacle in obstacle_rect_list:
            pg.draw.rect(screen, (255, 0, 0), obstacle)

        # Mise à jour de l'affichage.
        screen.blit(screen, (0, 0))
        pg.display.flip()

        # Compter tick.
        if tick > 60:
            tick = 0
            obstacle_tick += 1
        tick += 1

        # Mettre le jeu à 60 update par seconde.
        clock.tick(60)


def accueil(screen, clock, largeur, hauteur):

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


def main(): #gere tous jeu + acceuil = global mais en mieux 

    pg.init() # init pygame, importez chaque module dans pygame.
    # Fenêtre de 500 par 400 pixels.
    largeur = 500
    hauteur = 400
    taille_affichage = [largeur, hauteur]
    screen = pg.display.set_mode(taille_affichage)
    # Définir le titre de la fenêtre
    pg.display.set_caption("Jump")
    clock = pg.time.Clock()


    accueil(screen, clock, largeur, hauteur)
    jeu(screen, clock, largeur, hauteur)

if __name__ == "__main__":
    main()
