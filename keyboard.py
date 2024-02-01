import pygame

class keyboard:

    def __init__(self, keys):
        self.k = keys
        self.running = True
        self.n = 0
        self.sp = False
        self.sg = False

    def get(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_z or event.key == pygame.K_UP:
                    self.k['UP'] = 1
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    self.k['DOWN'] = 1
                if event.key == pygame.K_q or event.key == pygame.K_LEFT:
                    self.k['LEFT'] = 1
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    self.k['RIGHT'] = 1

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_z or event.key == pygame.K_UP:
                    self.k['UP'] = 0
                    self.n =1
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    self.k['DOWN'] = 0
                    self.n =1
                if event.key == pygame.K_q or event.key == pygame.K_LEFT:
                    self.k['LEFT'] = 0
                    self.n =1
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    self.k['RIGHT'] = 0
                    self.n =1

                if event.key == pygame.K_ESCAPE:
                    self.running = False
                if event.key == pygame.K_g:
                    self.sg = not self.sg
                if event.key == pygame.K_p:
                    self.sp = not self.sp
                
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                print("mouse_pos:", pos)
