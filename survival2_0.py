import pygame as pg # au lieu de mettre pygame on met pg pour court et rapide
from random import randint


# toute mes fonctions pour faciliter la lecture du jeu
def player_rex(game_data):

    keys = pg.key.get_pressed()
    for event in pg.event.get():

        if event.type == pg.QUIT:
            game_data["play"] = False
            pg.quit()
            quit()

    # Rect pour rectangle sert à délimiter la zone de limage,
    # sa "hit box" pour voir s'il y a collision.
    if game_data["player"]["in_jump"]:

        game_data["player"]["tick"] -= 1
        if game_data["player"]["tick"] == 0:

            game_data["player"]["rect"] = game_data["player"]["rect"].move(0, 200)
            game_data["player"]["hitbox"] = game_data["player"]["hitbox"].move(0, 200)
            game_data["player"]["in_jump"] = False

    # Si vous appuyez sur SPACE, faites le saut.
    if keys[pg.K_SPACE] and not game_data["player"]["in_jump"]:
        game_data["player"]["rect"] = game_data["player"]["rect"].move(0, -200)
        game_data["player"]["hitbox"] = game_data["player"]["hitbox"].move(0, -200)
        game_data["player"]["in_jump"] = True
        game_data["player"]["tick"] = 50

    return game_data


def obstacle_arrivé(game_data):

    # Crée un obstacle chaque seconde juste à l'extérieur de l'écran.
    if game_data["obstacle"]["tick"] == game_data["obstacle"]["next"]:
        
        game_data["obstacle"]["next"] = randint(1, 4)
        game_data["obstacle"]["list"].append(game_data["obstacle"]["spawn"])
        game_data["obstacle"]["tick"] = 0

    return game_data


def création_objet(largeur, font):

    obstacle = pg.image.load("obstacle.png")
    player = pg.image.load("rex.png")

    game_data = {

        "asset": {
            "fond": pg.image.load("fond.jpg").convert(),
            "obstacle": obstacle,
            "player": player
        },

        "obstacle": {
            "spawn": obstacle.get_rect(topleft=(largeur, 475)),
            "list": [],
            "tick": 0,
            "next": 2
        },

        "player": {
            "hitbox": pg.Rect(150, 450, 130, 130),
            "rect": player.get_rect(topleft=(50, 350)),
            "tick": 0,
            "in_jump": False
        },

        "font": font,
        "tick": 0,
        "score": 0,
        "play": True
    }

    return game_data


def collision(game_data):

    # Mise à jour de la position de l'obstacle et vérification de la collision avec le joueur.
    for index, obstacle_rectangle in enumerate(game_data["obstacle"]["list"]):

        if obstacle_rectangle.colliderect(game_data["player"]["hitbox"]):

            game_data["play"] = False
            return game_data

        game_data["obstacle"]["list"][index] = obstacle_rectangle.move(-11, 0)
        #ici on détermine la position de l'obstacle tant qu'il n'y a pas de collision

    return game_data


def dessiner_image(screen, game_data):

    # Dessiner le fond.
    # Screen.blit pour faire afficher l'image à la position 0.0
    screen.blit(game_data["asset"]["fond"], (0, 0))

    # Dessine le joueur au milieu de l’écran.
    screen.blit(game_data["asset"]["player"], game_data["player"]["rect"])

    # Dessine un obstacle.
    for obstacle_rectangle in game_data["obstacle"]["list"]:
        screen.blit(game_data["asset"]["obstacle"], obstacle_rectangle)

    font = game_data["font"]
    # Créée une surface avec le text.
    text_rect = font.render(str(game_data["score"]), 0, (29, 29, 29), font)

    # Affiche le text a l'écran.
    screen.blit(text_rect, (0, 0))


def jeu(screen, clock, largeur, font): # on rajoute en argument screen et clock pour les utiliser à partir de main

    #c'est un simple appel de fonction qui prend des valeurs en entré(les arguments),
    # qui les/en modifies et qui (les) renvois le résultat.

    game_data = création_objet(largeur, font)

    while game_data["play"]:

        #c'est un simple appel de fonction qui prend des valeurs en entré,
        # qui les modifies et qui renvois le résultat.
        game_data = player_rex(game_data)

        game_data = obstacle_arrivé(game_data)

        game_data = collision(game_data)

        dessiner_image(screen, game_data)

        # Mise à jour de l'affichage.
        screen.blit(screen, (0, 0))
        pg.display.flip()

        # Compter tick.
        if game_data["tick"] > 60:
            game_data["score"] += 1
            game_data["tick"] = 0
            game_data["obstacle"]["tick"] += 1

        game_data["tick"] += 1

        # Mettre le jeu à 60 update par seconde.
        clock.tick(60)

    return game_data["score"]


def accueil(screen, clock, font):

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

                if event.key == pg.K_ESCAPE: #pour quitter 
                    running = False
                    pg.quit()
                    quit()

                if event.key == pg.K_RETURN: #enter
                    return

        clock.tick(30)


def end_screen(screen, score, font):

    screen.fill((0, 0, 0))
    background = pg.image.load("fond.jpg").convert()
    screen.blit(background, (0, 0))

    text_rect = font.render("score: %s" % str(score), 0, (29, 29, 29), font)
    screen.blit(text_rect, (0, 0))

    pg.display.flip()

    waiting = True
    while waiting:
        keys = pg.key.get_pressed()
        for event in pg.event.get():

            if event.type == pg.QUIT:
                return False

        if keys[pg.K_RETURN]:
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
        playing = end_screen(screen, score, font)

    pg.quit()


if __name__ == "__main__":
    main()
