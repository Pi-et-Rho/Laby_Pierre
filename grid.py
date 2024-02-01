import pygame

class Grid:
    def __init__(self, x, y, tilesize):
        self.x = x
        self.y = y
        self.tilesize = tilesize
        self.offsetX = 0
        self.offsetY = 0

    def set_color(self, v):
        self.color = v

    def set_offset(self, x, y):
        self.offsetX = x
        self.offsetY = y

    def draw(self, screen):
        for i in range(1,self.x):
            pygame.draw.line(screen,self.color, (self.tilesize*i, 0), (self.tilesize*i, self.tilesize*self.x) )
        for i in range(0,self.y):
            pygame.draw.line(screen, self.color, (0, self.tilesize*i), (self.tilesize*self.x, self.tilesize*i) )

    def displayExit(self, screen, color, x, y):
        pygame.draw.line(screen, color, (self.tilesize*x + self.offsetX, self.tilesize*y + self.offsetY), (self.tilesize*x + self.offsetX + self.tilesize, self.tilesize*y + self.offsetY + self.tilesize), 3)
        pygame.draw.line(screen, color, (self.tilesize*x + self.offsetX, self.tilesize*y + self.offsetY + self.tilesize), (self.tilesize * x + self.offsetX + self.tilesize, self.tilesize * y + self.offsetY), 3)