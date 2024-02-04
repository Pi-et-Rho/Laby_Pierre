import pygame

class item:
    def __init__(self, tilesize, color):
        self.item_diamond = [[10,10], [12, 2], [36, 2]]
        self.item_health = [[15,19]]
        self.tilesize = tilesize
        self.color = color
        self.offsetX = 0
        self.offsetY = 0
        
        
    def draw_diamond(self, screen):
        for elt in self.item_diamond:
            pygame.draw.polygon(screen,self.color,((elt[0]*self.tilesize + (self.tilesize/2) + self.offsetX, elt[1]*self.tilesize + self.offsetY), (elt[0]*self.tilesize + self.offsetX, elt[1]*self.tilesize  + (self.tilesize/2) + self.offsetY), (elt[0]*self.tilesize + (self.tilesize/2) + self.offsetX, elt[1]*self.tilesize  + self.tilesize + self.offsetY),  (elt[0]*self.tilesize + self.tilesize + self.offsetX, elt[1]*self.tilesize + (self.tilesize/2) + self.offsetY)))

    def draw_health(self, screen, cross_thickness):
        for elt in self.item_health:
            pixel_x = elt[0] * self.tilesize + self.tilesize // 2 + self.offsetX
            pixel_y = elt[1] * self.tilesize + self.tilesize // 2 + self.offsetY

            pygame.draw.line(screen, self.color, (pixel_x - self.tilesize // 2, pixel_y), (pixel_x + self.tilesize // 2, pixel_y), cross_thickness)
            pygame.draw.line(screen, self.color, (pixel_x, pixel_y - self.tilesize // 2), (pixel_x, pixel_y + self.tilesize // 2), cross_thickness)

    def set_offset(self, x, y):
        self.offsetX = x
        self.offsetY = y

    def get_diamond(self, player_x, player_y):
        for elt in self.item_diamond:
            if (player_x, player_y) == (elt[0], elt[1]):
                self.item_diamond.remove(elt)
                return True
        return False
    
    def get_health(self, player_x, player_y):
        for elt in self.item_health:
            if (player_x, player_y) == (elt[0], elt[1]):
                self.item_health.remove(elt)
                return True
        return False