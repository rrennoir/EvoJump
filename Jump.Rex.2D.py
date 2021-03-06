import pygame as pg # au lieu de mettre pygame on met pg plus court et rapide
from random import randint

# toute mes fonctions pour faciliter la lecture du jeu
def player_rex(play, player_rect, player_hitbox, in_jump, jump_tick):

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
            player_hitbox = player_hitbox.move(0, 200)
            in_jump = False

    # Si vous appuyez sur SPACE, faites le saut.
    if keys[pg.K_SPACE] and not in_jump:
        player_rect = player_rect.move(0, -200)
        player_hitbox = player_hitbox.move(0, -200)
        in_jump = True
        jump_tick = 50

    return play, player_rect, player_hitbox, in_jump, jump_tick

def obstacle_arrivé(next_obstacle, obstacle_tick, obstacle_rect_list, obstacle_rect):
    # Crée un obstacle chaque seconde juste à l'extérieur de l'écran.
    if obstacle_tick == next_obstacle: # ici on détermine le nombre de seconde
        next_obstacle = randint(1, 4)
        obstacle_rect_list.append(obstacle_rect)
        obstacle_tick = 0
    return obstacle_rect, next_obstacle, obstacle_tick, obstacle_rect_list

def création_objet(largeur):

    # créer le fond
    fond = pg.image.load("fond.jpg").convert()

    # Créer un joueur rect = rectangle
    player = pg.image.load("rex.png")
    player_rect = player.get_rect(topleft=(50, 350)) #topleft en haut à gauche/ pour sa position
    player_hitbox = pg.Rect(150, 450, 130, 130)

    # Créer un obstacle
    obstacle_image = pg.image.load("obstacle.png")
    obstacle_rect = obstacle_image.get_rect(topleft=(largeur, 475))

    return fond, player, player_rect, obstacle_image, obstacle_rect, player_hitbox

def collision(play, obstacle_rect_list, player_hitbox):

    # Mise à jour de la position de l'obstacle et vérification de la collision avec le joueur.
    for index, obstacle_rectangle in enumerate(obstacle_rect_list):

        if obstacle_rectangle.colliderect(player_hitbox):
            play = False

            return play, obstacle_rect_list

        obstacle_rect_list[index] = obstacle_rectangle.move(-11, 0) 
        #ici on détermine la position de l'obstacle tant qu'il n'y a pas de collision

    return play, obstacle_rect_list

def dessiner_image(fond, player, player_rect, obstacle_rect_list, screen, obstacle_image, temps, font):
    #ppour positionner un objet sur l'écran, nous avons besoin de la fonction blit()
    #dessiner le fond
    screen.blit(fond, (0, 0)) #screen.blit pour faire afficher l'image à la position 0.0

    # Dessine le joueur au milieu de l’écran.
    screen.blit(player, player_rect)

    # Dessine un obstacle.
    for obstacle_rectangle in obstacle_rect_list:
        screen.blit(obstacle_image, obstacle_rectangle)

    text_rect = font.render(str(temps), 0, (29, 29, 29), font) # str pour mettre en string le temps
    screen.blit(text_rect, (0, 0))

def jeu(screen, clock, largeur, font): # on rajoute en argument screen et clock pour les utiliser à partir de main

    #c'est un simple appel de fonction qui prend des valeurs en entré(les arguments),
    # qui les/en modifies et qui (les) renvois le résultat.

    fond, player, player_rect, obstacle_image, obstacle_rect, player_hitbox = création_objet(largeur)

    next_obstacle = 2

    obstacle_rect_list = []

    tick = 0
    in_jump = False
    jump_tick = 0
    obstacle_tick = 0
    play = True
    temps = 0
    while play:

        #c'est un simple appel de fonction qui prend des valeurs en entré,
        # qui les modifies et qui renvois le résultat.
        play, player_rect, player_hitbox, in_jump, jump_tick = player_rex(play, player_rect, player_hitbox, in_jump, jump_tick)

        obstacle_rect, next_obstacle, obstacle_tick, obstacle_rect_list = obstacle_arrivé(next_obstacle, obstacle_tick, obstacle_rect_list, obstacle_rect)

        play, obstacle_rect_list = collision(play, obstacle_rect_list, player_hitbox)

        dessiner_image(fond, player, player_rect, obstacle_rect_list, screen, obstacle_image, temps, font)

        # Mise à jour de l'affichage.
        screen.blit(screen, (0, 0))
        pg.display.flip()

        # Compter tick.
        if tick > 60:
            temps += 1
            tick = 0
            obstacle_tick += 1

        tick += 1

        # Mettre le jeu à 60 update par seconde.
        clock.tick(60)

    return temps

def accueil(screen, clock, font):

    # Remplace ce que avait sur la surface par du noir.
    screen.fill((0, 0, 0))

    # Charge une image et la converti a la bonne taille.
    fond_fin = pg.image.load("menu.jpg").convert()

    # Place l'image sur la surface.
    screen.blit(fond_fin, (0, 0))

    # Met a jour la surface afficher a l'écran.
    pg.display.flip()

    running = True
    while running:

        for event in pg.event.get():

            if event.type == pg.QUIT: # quitter avec la croix rouge en haut à doite
                running = False
                pg.quit()
                quit()

            if event.type == pg.KEYDOWN:

                if event.key == pg.K_ESCAPE: # ou échap pour quitter 
                    running = False
                    pg.quit()
                    quit()

                if event.key == pg.K_RETURN: # touche enter pour jouer
                    return

        clock.tick(30)

def ecran_fin(screen, score, font):

    screen.fill((0, 0, 0))
    fond_fin = pg.image.load("ecran_fin.jpg").convert()
    screen.blit(fond_fin, (0, 0))

    text_rect = font.render("score: %s" % str(score), 0, (29, 29, 29), font) #
    screen.blit(text_rect, (0, 0))

    pg.display.flip()

    att_touche = True # ici on attend que le joueur appuie sur une touche pour relancer une game
    while att_touche:
        keys = pg.key.get_pressed()
        for event in pg.event.get():

            if event.type == pg.QUIT: # soit il peut quitter 
                return False

        if keys[pg.K_RETURN]: # soit comme depuis le menu il peut lancer un game en apuyant sur ENTRER
            return True

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
    pg.display.set_caption("Jump.Rex.2D")

    font = pg.font.SysFont("Comic Sans MS", 35) #ici on créé la police, on la choisi + taille
    clock = pg.time.Clock()

    accueil(screen, clock, font)

    playing = True
    while playing:

        score = jeu(screen, clock, largeur, font)
        playing = ecran_fin(screen, score, font)

    pg.quit()


if __name__ == "__main__":
    main()
