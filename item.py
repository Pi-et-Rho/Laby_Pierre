import pygame

class item:
    def __init__(self, tilesize, color):
        self.item = [[10,10], [12, 2], [36, 2]]
        self.tilesize = tilesize
        self.color = color
        self.offsetX = 0
        self.offsetY = 0
        
        
    def draw(self, screen):
        for elt in self.item:
            pygame.draw.polygon(screen,self.color,((elt[0]*self.tilesize + (self.tilesize/2) + self.offsetX, elt[1]*self.tilesize + self.offsetY), (elt[0]*self.tilesize + self.offsetX, elt[1]*self.tilesize  + (self.tilesize/2) + self.offsetY), (elt[0]*self.tilesize + (self.tilesize/2) + self.offsetX, elt[1]*self.tilesize  + self.tilesize + self.offsetY),  (elt[0]*self.tilesize + self.tilesize + self.offsetX, elt[1]*self.tilesize + (self.tilesize/2) + self.offsetY)) )

    def set_offset(self, x, y):
        self.offsetX = x
        self.offsetY = y

    def get_item(self, player_x, player_y):
        for elt in self.item:
            if (player_x, player_y) == (elt[0], elt[1]):
                self.item.remove(elt)
                return True
        return False
