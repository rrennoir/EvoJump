import pygame
from pygame.locals import *
from main import*


#from EvoJump-master import*
pygame.init()

# init pygame, importez chaque module dans pygame.
pg.init()


# Fenêtre de 500 par 400 pixels.
largeur = 500
hauteur = 400
taille_affichage = [largeur, hauteur]
screen = pg.display.set_mode(taille_affichage)

#BOUCLE PRINCIPALE (Acceuil et lancement du mode de jeu)
continuer = 1
while continuer:
    #Chargement et affichage de l'écran d'accueil
    accueil = pg.image.load("background.jpg").convert()
    accueil.blit(accueil, (0,0))

    #Rafraichissement
    pygame.display.flip()

    #On remet ces variables à 1 à chaque tour de boucle
    continuer_jeu = 1
    continuer_accueil = 1
    #BOUCLE D'ACCUEIL
    while continuer_accueil:

        #Limitation de vitesse de la boucle
        pygame.time.Clock().tick(30)

        for event in pygame.event.get():

            #Si l'utilisateur quitte, on met les variables
            #de boucle à 0 pour n'en parcourir aucune et fermer
            if event.type == QUIT and event.type == KEYDOWN and event.key == K_ESCAPE:
                continuer_accueil = 0
                continuer_jeu = 0
                continuer = 0
                #Variable de choix du mode
                choix = 0

            elif event.type == KEYDOWN:

                if event.key == K_a:
                    continuer_accueil = 0	#On quitte l'accueil

    #pour ne pas charger s'il quitte
    if choix != 0:
        #Chargement du fond
        fond = pygame.image.load("background.jpg")
