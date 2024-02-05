import pygame

class item:
    def __init__(self, tilesize, color, texture_path):
        self.item_diamond = [[10,10], [12, 2], [36, 2]]
        self.texture = pygame.image.load(texture_path)
        self.item_health = [[15,19]]
        self.tilesize = tilesize
        self.color = color
        self.offsetX = 0
        self.offsetY = 0
        
        
    def draw_diamond(self, screen):
        for elt in self.item_diamond:
            scaled_texture = pygame.transform.scale(self.texture, (self.tilesize, self.tilesize))
            screen.blit(scaled_texture, (elt[0] * self.tilesize + self.offsetX, elt[1] * self.tilesize + self.offsetY))

    def draw_health_texture(self, screen, texture):
        for elt in self.item_health:
                resized_texture = pygame.transform.scale(texture, (self.tilesize, self.tilesize))
                screen.blit(resized_texture, (elt[0] * self.tilesize + self.offsetX, elt[1] * self.tilesize + self.offsetY))


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