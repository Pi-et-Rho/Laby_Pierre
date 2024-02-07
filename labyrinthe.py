import pygame
from read_colors import read_color_parameters
from utils import convert_data

class Labyrinthe :
    # constructeur
    def __init__(self, sizeX, sizeY):
        """sizeX, sizeY désignent la taille du labyrinthe sur l'axe (x,y)"""
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.version = ""
        self.author = ""
        self.start = ""
        self.finish = ""
        self.end = False
        #attention création d'une matrice en Y X
        self.matrice = [[0]* self.sizeX for _ in range(self.sizeY)]
        self.offsetX = 0
        self.offsetY = 0
        read = read_color_parameters()
        read.readColors("colorLaby.ini")
        self.colors = read.c

    def set_color(self, v):
        """Fixe la couleur pour dessiner les murs"""
        self.color = v

    def load_wall_texture(self, texture_path, tilesize):
        self.wall_texture = pygame.image.load(texture_path)
        self.wall_texture = pygame.transform.scale(self.wall_texture, (tilesize, tilesize))

    def load_ground_texture(self, texture_path, tilesize):
        self.ground_texture = pygame.image.load(texture_path)
        self.ground_texture = pygame.transform.scale(self.ground_texture, (tilesize, tilesize))

    def load_water_texture(self, texture_path, tilesize):
        self.water_texture = pygame.image.load(texture_path)
        self.water_texture = pygame.transform.scale(self.water_texture, (tilesize, tilesize))

    def load_lava_texture(self, texture_path, tilesize):
       self.lava_texture = pygame.image.load(texture_path)
       self.lava_texture = pygame.transform.scale(self.lava_texture, (tilesize, tilesize))

    def set_offset(self, x, y):
        self.offsetX = x
        self.offsetY = y

    def display_on_console(self):
        """Sortie console du labyrinthe"""
        for j in range(self.sizeY):
            for i in range(self.sizeX):
                # rappel: matrice en Y,X
                print(self.matrice[j][i], end = "")
            print()
        #print(self.matrice)

    def get_matrice(self):
        """renvoie la matrice associée au labyrinthe"""
        return self.matrice
    
    def getXY(self, i,j):
        """Renvoie la case (i,j) du labyrinthe sur l'axe (x,y)"""
        return self.matrice[j][i]

    def setXY(self, i,j,v):
        """Modifie par v la case (i,j) sur l'axe (x,y)"""
        self.matrice[j][i] = v
    
    def getSize(self):
        """Renvoie la taille (x,y) du labyrinthe"""
        return (self.sizeX, self.sizeY)
    
    def wall_destroy(self, i,j):
        """Détruit un mur du labyrinthe en (i,j) sur l'axe (x,y)"""
        self.matrice[j][i]=0

    def load_from_file(self, filename):
        """Charge un labyrinthe d'un fichier texte"""
        with open(filename) as file:
            #lecture du cartouche du labyrinthe
            # 1) vérification du type de fichier
            firstline = file.readline()
            firstline = firstline.rstrip()
            firstline = firstline.split(',')
            if firstline[0] != "map":
                print("mauvais fichier")
                return
            self.version = firstline[1]
            self.author = firstline[2]
            # 2) vérification de la taille du labyrinthe
            snd_line = file.readline()
            snd_line = snd_line.rstrip()
            snd_line = snd_line.split(',')            
            if int(snd_line[0])!=self.sizeX or int(snd_line[1])!=self.sizeY:
                print("dimensions non cohérentes")
                return
            #lecture des données du labyrinthe
            lines = [line.rstrip() for line in file]
        #print(lines)
        for i in range(len(lines)):
            tmp = lines[i]
            tmp_list = tmp.split(',')
            for j in range(len(tmp_list)):
                    tmp_list[j]= convert_data(tmp_list[j])
            #print(tmp_list)
            self.matrice[i]=tmp_list

        self.setAD()
    
    def setAD(self):
        for i in range(len(self.matrice)):
            for j in range(len(self.matrice[i])):
                if self.matrice[i][j] == 100:
                    self.start = [j, i]
                if self.matrice[i][j] == 101:
                    self.finish = [j, i]
        print(self.start, self.finish)

    def hit_finish(self, x, y):
        if x==self.finish[0] and y==self.finish[1] and self.end == False:
            print("Vous êtes arrivés à la sortie !")
            self.end = True

    def hit_box(self, x, y):
        """indique si l'élément (x,y) est un mur"""
        if x>=self.sizeX or x<0 or y<0 or y>=self.sizeY:
            return 1
        return self.matrice[y][x] == 1
    
    def hit_water(self, x, y):
        """indique si l'élément (x,y) est de l'eau"""
        if x >= self.sizeX or x < 0 or y < 0 or y >= self.sizeY:
            return 1
        return self.matrice[y][x] == 102
    
    def hit_lava(self, x, y):
        """indique si l'élément (x,y) est de la lave"""
        if x >= self.sizeX or x < 0 or y < 0 or y >= self.sizeY:
            return 1
        return self.matrice[y][x] == 103

    def draw(self, screen, tilesize):
        for j in range(self.sizeY):
            for i in range(self.sizeX):
                if self.matrice[j][i] == 1:
                    screen.blit(self.wall_texture, (i * tilesize + self.offsetX, j * tilesize + self.offsetY))
                elif self.matrice[j][i] == 0:
                    screen.blit(self.ground_texture, (i * tilesize + self.offsetX, j * tilesize + self.offsetY))
                elif self.matrice[j][i] == 102:
                    screen.blit(self.water_texture, (i * tilesize + self.offsetX, j * tilesize + self.offsetY))
                elif self.matrice[j][i] == 103:
                    screen.blit(self.lava_texture, (i * tilesize + self.offsetX, j * tilesize + self.offsetY))