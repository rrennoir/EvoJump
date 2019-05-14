import pygame as pg # au lieu de mettre pygame on met pg pour court et rapide

def main():

    # init pygame, importez chaque module dans pygame.
    pg.init()

    # Fenêtre de 500 par 400 pixels.
    width = 500
    height = 400
    display_size = [width, height]
    screen = pg.display.set_mode(display_size)

    # Définir le titre de la fenêtre
    pg.display.set_caption("Jump")

    clock = pg.time.Clock()

    # Créer un joueur rect = rectangle
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

        # Si vous appuyez sur SPACE, faites le saut.
        if keys[pg.K_SPACE] and not in_jump:
            player_rect = player_rect.move(0, -50)
            in_jump = True
            jump_tick = 90

        # Crée un obstacle chaque seconde juste à l'extérieur de l'écran.
        if obstacle_tick == 3: # ici on détermine le nombre de seconde

            obstacle_tick = 0
            obstacle_rect = pg.Rect(width, height / 2, 20, 20)
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


if __name__ == "__main__":
    main()
