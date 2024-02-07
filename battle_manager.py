import pygame
from read_colors import read_color_parameters
from keyboard import keyboard

class BattleManager:

    def __init__(self, player, enemy, screenSizeX, screenSizeY, colorsFile):
        self.p = player
        self.e = enemy
        self.x = screenSizeX
        self.y = screenSizeY
        colors = read_color_parameters()
        self.c = colors.readColors(colorsFile)
        self.screen = 0
        self.f = True
        self.keys = { "UP":0 , "DOWN":0, "LEFT":0, "RIGHT":0, "QUIT":0}
        self.kb = keyboard(self.keys)
        self.setup_pygame()

    
    def setup_pygame(self):
        pygame.init()

        self.screen = pygame.display.set_mode((self.x,self.y))

        clock = pygame.time.Clock()

        self.mainloop()

    def mainloop(self):
        while self.f == True:
            self.screen.fill(self.c["ground_color"])

            self.kb.get()

            if self.keys["QUIT"] == 1:
                self.f = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.f = False


            pygame.display.flip()
        pygame.quit()


game = BattleManager("", "", 800, 600, "colorFight.ini")
    