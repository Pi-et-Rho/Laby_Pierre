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
from chargeur import Loader
import fight

# pygame setup
pygame.init()

level = "data/laby-03.ini"

data = Loader(level)

offsetX = 0
offsetY = 0

#constantes
tilesize = data.tilesize # taille d'une tuile IG
size = (data.sizex, data.sizey) # taille du monde
fps = 30 # fps du jeu
player_speed = 150 # vitesse du joueur
next_move = 0 #tic avant déplacement
player_health = 100

# color
read = read_color_parameters()
read.readColors("colorLaby.ini")
color = read.c



laby = Labyrinthe(size[0], size[1])
laby.matrice = data.map
laby.setAD()
laby.load_wall_texture(r"Textures\Stone_Bricks.png", tilesize)
laby.load_ground_texture(r"Textures\Ground.png", tilesize)
laby.load_water_texture(r"Textures\Blue_Concrete.png", tilesize)
laby.load_lava_texture(r"Textures\Orange_Concrete.png", tilesize)

grid = Grid(size[0], size[1], tilesize)
grid.set_color(color["grid_color"])

screen = pygame.display.set_mode((1280, 800))

clock = pygame.time.Clock()
running = True
dt = 0

show_grid = True
show_pos = False

keys= { "UP":0 , "DOWN":0, "LEFT":0, "RIGHT":0 , "QUIT":0}
alien_direction = random.choice(['UP', 'Down', 'LEFT', 'RIGHT'])

player_pos = Pos(laby.start[0],laby.start[1])
player_head_texture = pygame.image.load(r"Textures\Player.png")
health_item_texture = pygame.image.load(r"Textures\Heal.png")
items1 = item(tilesize, color["item_color"], r"Textures\Diamonds.png")
items2 = item(tilesize, color["item_color"], r"Textures\Diamonds.png")
items3 = item(tilesize, color["item_color"], r"Textures\Diamonds.png")

aliens = []
for elt in data.monsters:
    aliens.append(alien(tilesize, color["alien_color"], r"Textures\Alien.png"))
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
        
        if laby.hit_water(new_x, new_y):
            kb.n -= player_speed // 2

        if laby.hit_lava(new_x, new_y):
            player_health -= 10 
            print("Ouch! Health:", player_health)
            if player_health <= 0:
                print("Game Over! Player ran out of health.")

        if kb.sp:
            print("pos: ",[player_pos.x, player_pos.y])
            
        if items1.get_diamond(player_pos.x, player_pos.y):
            print("Validé")
        if items2.get_health(player_pos.x, player_pos.y):
            print("Soigné")
            player_health = 100

            
        if kb.sp:
            print("pos: ", [player_pos.x, player_pos.y])
            
        #déplacement des aliens
        for elt in aliens:
            elt.update_position(laby)
            elt.check_collision_with_player(player_pos)

            if elt.check_collision_with_player(player_pos):
                fightResult = fight.calculate_fight()

                if fightResult == "party_1":
                    aliens.pop(aliens.index(elt))
                else:
                    player_health-=10
        #collision avec alien)
        
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

    
    player_head_texture_resized = pygame.transform.scale(player_head_texture, (tilesize, tilesize))
    screen.blit(player_head_texture_resized, (player_pos.x * tilesize + offsetX, player_pos.y * tilesize + offsetY))
    items1.draw_diamond(screen)
    items2.draw_health_texture(screen, health_item_texture)
    items1.set_offset(offsetX, offsetY)
    items2.set_offset(offsetX, offsetY)
    for elt in aliens:
        elt.draw(screen)
        elt.set_offset(offsetX, offsetY)

    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(10, 10, 200, 20))
    pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(10, 10, player_health * 2, 20))
    
    # affichage des modification du screen_view
    pygame.display.flip()
    # gestion fps
    dt = clock.tick(fps)

pygame.quit()