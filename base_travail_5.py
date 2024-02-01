# Example file showing a circle moving on screen
import pygame 
import random
from labyrinthe import Labyrinthe
from grid import Grid
from utils import Pos
from read_colors import read_color_parameters
from keyboard import keyboard
from item import item
from alien import alien

# pygame setup
pygame.init()

offsetX = 0
offsetY = 0

#constantes
tilesize = 32 # taille d'une tuile IG
size = (40, 25) # taille du monde
fps = 30 # fps du jeu
player_speed = 150 # vitesse du joueur
next_move = 0 #tic avant déplacement

# color
read = read_color_parameters()
read.readColors("color.ini")
color = read.c

read = read_color_parameters()
read.readColors("color.ini")
color = read.c

level = "data/laby-03.dat"

laby = Labyrinthe(size[0], size[1])
laby.load_from_file(level)
laby.set_color(color["wall_color"])

grid = Grid(size[0], size[1], tilesize)
grid.set_color(color["grid_color"])

screen = pygame.display.set_mode((1900, 1000))

clock = pygame.time.Clock()
running = True
dt = 0

show_grid = True
show_pos = False

keys= { "UP":0 , "DOWN":0, "LEFT":0, "RIGHT":0 }
alien_direction = random.choice(['UP', 'Down', 'LEFT', 'RIGHT'])

player_pos = Pos(laby.start[0],laby.start[1])
items = item(tilesize, color["item_color"])
aliens = alien(tilesize, color["alien_color"])
alien_move_counter = 0

kb = keyboard(keys)

#tour de boucle, pour chaque FPS
while kb.running:

    kb.get()
    keys = kb.k
    kb.n += dt

    if kb.n>0:
        new_x, new_y = player_pos.x, player_pos.y
        if keys['UP'] == 1:
            new_y -=1
        elif keys['DOWN'] == 1:
            new_y += 1
        elif keys['LEFT'] == 1:
            new_x -=1
        elif keys['RIGHT'] == 1:
            new_x += 1

        # vérification du déplacement du joueur                                    
        if not laby.hit_box(new_x, new_y):
            player_pos.x, player_pos.y = new_x, new_y
            kb.n -= player_speed
            laby.hit_finish(player_pos.x, player_pos.y)

        if kb.sp:
            print("pos: ",[player_pos.x, player_pos.y])
            
        if items.get_item(player_pos.x, player_pos.y):
            print("Validé")
            
        if kb.sp:
            print("pos: ", [player_pos.x, player_pos.y])
            
        #déplacement des aliens
        aliens.update_position(laby)
        #collision avec alien
        aliens.check_collision_with_player(player_pos)
        
        alien_move_counter += 1
        if alien_move_counter >= 2:
            alien_direction = random.choice(['UP', 'DOWN', 'LEFT', 'RIGHT'])
            alien_move_counter = 0

    #
    # affichage des différents composants graphique
    #
    screen.fill(color["ground_color"])

    laby.draw(screen, tilesize)
    laby.set_offset(offsetX, offsetY)

    if kb.sg:
        grid.draw(screen)
    grid.displayExit(screen, color["exit_color"], laby.finish[0], laby.finish[1])
    grid.set_offset(offsetX, offsetY)


    pygame.draw.rect(screen, color["player_color"], pygame.Rect(player_pos.x * tilesize + offsetX, player_pos.y * tilesize + offsetY, tilesize, tilesize))
    items.draw(screen)
    items.set_offset(offsetX, offsetY)
    aliens.draw(screen)
    aliens.set_offset(offsetX, offsetY)
    
    # affichage des modification du screen_view
    pygame.display.flip()
    # gestion fps
    dt = clock.tick(fps)

pygame.quit()