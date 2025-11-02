import pygame 

class Ball :
    def __init__(self,x,y):
        self.image = pygame.image.load(fr'C:\Users\ponsg\MiniGolf-Game\Assets\ball.png')
        self.dimension = (100,100)
        self.x = x-50
        self.y = y-50
        self.dx = 0
        self.dy = 0
    def distance(self, x2, y2):
        '''Return distance beetween the ball and a point'''
        return (((x2-self.x)**2)+((y2-self.y)**2))**0.5
    def tension(self):
        '''Calcul acceleration of the ball'''
        cursor_pos = pygame.mouse.get_pos()
        self.dx = (self.x+25 - cursor_pos[0])/10
        self.dy = (self.y+25 - cursor_pos[1])/10
        if self.dx > 30 :
            self.dx = 30
        elif self.dx < -30 :
            self.dx = -30
        if self.dy > 30 :
            self.dy = 30
        elif self.dy < -30 :
            self.dy = -30
    def update_pos(self):
        '''Update postion of the ball'''
        self.x += self.dx
        self.y += self.dy
        if self.x >= 600-50 or self.x <= 0 :
            self.dx *= -1
        elif self.y >= 720-50 or self.y <= 0 :
            self.dy *= -1
        self.dx *= 0.98
        self.dy *= 0.98

    def collide(self,level) :
        '''Verify collision beetween elements of level and the ball'''
        distance_hole_ball = self.distance(level.hole_pos[0],level.hole_pos[1])
        if distance_hole_ball-25 <= 15 and self.image.get_width()>1:
            self.dx = 0
            self.dy = 0
            self.image = pygame.transform.scale(self.image,(self.image.get_width()*0.98,self.image.get_height()*0.98))

    def draw(self,surface) :
        surface.blit(self.image,(self.x,self.y))

class Level :
    def __init__(self):
        self.main_bg = pygame.image.load(fr'C:\Users\ponsg\MiniGolf-Game\Assets\main_bg.png')
        self.main_bg = pygame.transform.scale(self.main_bg,(1000,1000))
        self.hole = pygame.image.load(fr'C:\Users\ponsg\MiniGolf-Game\Assets\golf_hole.png')
        self.barrier = pygame.image.load(fr'C:\Users\ponsg\MiniGolf-Game\Assets\barrière.png')
        self.barrier = pygame.transform.scale(self.barrier,(100,100))
        self.hole_pos = (1000/2-50,100)
        self.barrier_pos = []
    def level_update(self):
        pass
    def draw(self,surface):
        surface.blit(self.main_bg,(0,0))
        surface.blit(self.hole,self.hole_pos)
        for pos in self.barrier_pos :
            surface.blit(self.barrier,pos)

class Info :
    def __init__(self):
        self.info_side = pygame.image.load(fr'C:\Users\ponsg\MiniGolf-Game\Assets\info_side.png')
        self.info_side = pygame.transform.scale(self.info_side,(400,800))
        self.level_label = []
        self.level_number = 0
        self.right_arrow = pygame.image.load(fr'C:\Users\ponsg\MiniGolf-Game\Assets\right_arrow.png')
        self.left_arrow = pygame.transform.rotate(self.right_arrow,180)
        for i in range(1,2):
            label = pygame.image.load(fr'C:\Users\ponsg\MiniGolf-Game\Assets\level{i}_label.png')
            self.level_label.append(pygame.transform.scale(label,(150,75)))
    def draw(self, surface):
        surface.blit(self.info_side,(600,0))
        surface.blit(self.level_label[self.level_number],(725,50))
        surface.blit(self.right_arrow,(900,75))