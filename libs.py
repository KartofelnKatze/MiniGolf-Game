import pygame 

class Ball :
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.image = pygame.image.load(fr'C:\Users\ponsg\MiniGolf-Game\Assets\ball.png')
        self.dimension = self.image.get_rect()
    def draw(self,surface) :
        surface.blit(self.image,(self.x,self.y))
class Level :
    def __init__(self):
        self.main_bg = pygame.image.load(fr'C:\Users\ponsg\MiniGolf-Game\Assets\main_bg.png')
        self.main_bg = pygame.transform.scale(self.main_bg,(1000,1000))
    def draw(self,surface):
        surface.blit(self.main_bg,(0,0))