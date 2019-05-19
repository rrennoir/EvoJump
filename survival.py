import pygame as pg # au lieu de mettre pygame on met pg pour court et rapide
from random import randint

def jeu(screen, clock, largeur, hauteur): # on rajoute en argument screen et clock pour les utiliser à partir de main

    # créer le fond
    fond = pg.image.load("fond.jpg").convert()

    # Créer un joueur rect = rectangle
    player = pg.image.load("rex.png")
    player_rect = player.get_rect(topleft=(50, 350)) #topleft en haut à gauche 

    # Créer un obstacle
    obstacle_image = pg.image.load("obstacle.png")
    obstacle_rect = obstacle_image.get_rect(topleft=(largeur, 475))

    next_obstacle = 2 

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
#rect pour rectangle sert à délimiter la zone de limage, sa "hit box" pour voir s'il y a collision 
        if in_jump:
            jump_tick -= 1
            if jump_tick == 0:
                player_rect = player_rect.move(0, 200)
                in_jump = False

        # Si vous appuyez sur SPACE, faites le saut.
        if keys[pg.K_SPACE] and not in_jump:
            player_rect = player_rect.move(0, -200)
            in_jump = True
            jump_tick = 90

        # Crée un obstacle chaque seconde juste à l'extérieur de l'écran.
        if obstacle_tick == next_obstacle: # ici on détermine le nombre de seconde
            next_obstacle = randint(1,5)
            obstacle_rect_list.append(obstacle_rect)
            obstacle_tick = 0

        # Mise à jour de la position de l'obstacle et vérification de la collision avec le joueur.
        for index, obstacle_rectangle in enumerate(obstacle_rect_list):

            if obstacle_rectangle.colliderect(player_rect):
                return

            obstacle_rect_list[index] = obstacle_rectangle.move(-6, 0) 
            #ici on détermine la position de l'obstacle tant qu'il n'y a pas de collision

        #dessiner le fond
        screen.blit(fond, (0,0)) #screen.blit pour faire afficher léimage à la position 0.0

        # Dessine le joueur au milieu de l’écran.
        screen.blit(player, player_rect)

        # Dessine un obstacle.
        for obstacle_rectangle in obstacle_rect_list:
            screen.blit(obstacle_image, obstacle_rectangle)

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


def accueil(screen, clock):

    

    # Remplace ce que avait sur la surface par du noir.
    screen.fill((0, 0, 0))

    # Charge une image et la converti a la bonne taille.
    background = pg.image.load("menu.jpg").convert()

    # Place l'image sur la surface.
    screen.blit(background, (0, 0))

    # Met a jour la surface afficher a l'écran.
    pg.display.flip()

    running = True
    while running:

        for event in pg.event.get():

            if event.type == pg.QUIT:
                running = False
                pg.quit()
                quit()

            if event.type == pg.KEYDOWN:

                if event.key == pg.K_ESCAPE:
                    running = False
                    pg.quit()
                    quit()

                if event.key == pg.K_RETURN:
                    return

        clock.tick(30)


def main(): #gere tous jeu + acceuil = global mais en mieux 

    pg.init() # init pygame, importez chaque module dans pygame.
    
    icone = pg.image.load("icone.jpg")

    # Fenêtre de 1200 par 600 pixels.
    largeur = 1200
    hauteur = 600
    taille_affichage = [largeur, hauteur]

    screen = pg.display.set_mode(taille_affichage)
    pg.display.set_icon(icone)
    # Définir le titre de la fenêtre
    pg.display.set_caption("Jump")
    clock = pg.time.Clock()

    accueil(screen, clock)
    jeu(screen, clock, largeur, hauteur)


if __name__ == "__main__":
    main()
