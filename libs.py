import pygame 
import time
import pandas

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
    
    def tension(self,info):
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
        info.score -= 1

    def update_pos(self):
        '''Update postion of the ball'''
        self.x += self.dx
        self.y += self.dy
        if self.x >= 550 or self.x <= 0 :
            self.dx *= -1
        elif self.y >= 670 or self.y <= 0 :
            self.dy *= -1
        self.dx *= 0.98
        self.dy *= 0.98

    def collide(self,level,info) :
        '''Verify collision beetween elements of level and the ball'''
        distance_hole_ball = self.distance(level.hole_pos[0],level.hole_pos[1])
        if distance_hole_ball-25 <= 15 and self.image.get_width()>1:
            self.dx = 0
            self.dy = 0
            self.image = pygame.transform.scale(self.image,(self.image.get_width()*0.98,self.image.get_height()*0.98))
            df = pandas.read_csv('info.csv')
            if info.score == -1 :
                info.highscore = 1
                df["highscore"].values[0] = 1
            elif info.score > info.highscore or info.score == 0 :
                info.highscore = info.score
                df["highscore"].values[0] = info.score 
            df.to_csv('info.csv')
            
        for coor in level.barrier_pos :
            if self.distance(coor[0]+25,coor[1]+25) <= 50:
                if self.x > coor[0] and self.x < coor[0]+50 :
                    print("high pass")
                    self.dy *= -1
                elif self.y > coor[1]+50 and self.y < coor[1] :
                    print('side pass')
                    self.dx *= -1 # Protoype

    def draw(self,surface) :
        '''Draw the ball on the screen'''
        surface.blit(self.image,(self.x,self.y))

    def reset(self):
        self.__init__(300,650)

class Level :
    def __init__(self):
        self.main_bg = pygame.image.load(fr'C:\Users\ponsg\MiniGolf-Game\Assets\main_bg.png')
        self.main_bg = pygame.transform.scale(self.main_bg,(1000,1000))
        self.hole = pygame.image.load(fr'C:\Users\ponsg\MiniGolf-Game\Assets\golf_hole.png')
        self.barrier = pygame.image.load(fr'C:\Users\ponsg\MiniGolf-Game\Assets\barrière.png')
        self.barrier = pygame.transform.scale(self.barrier,(100,100))
        self.hole_pos = (1000/2-50,100)
        self.barrier_pos = []
        self.ball_pos = ()

    def draw(self,surface):
        surface.blit(self.main_bg,(0,0))
        surface.blit(self.hole,self.hole_pos)
        for pos in self.barrier_pos :
            surface.blit(self.barrier,pos)
            pygame.draw.circle(surface,(255,0,0),(pos[0]+50,pos[1]+50),10)

class Info :
    def __init__(self):
        self.level_list = []
        self.level_index = 0
        self.chronometer = Timer()
        self.chronometer.start()
        self.chronometer.update()
        try :
            player_info = pandas.read_csv("info.csv") 
            self.player_info = player_info
            self.highscore = self.player_info["highscore"].values[0]
        except FileNotFoundError :
            print('Fichier introuvable')
        self.score = 0
        self.text_font = pygame.font.Font(None, 40)
        self.info_side = pygame.image.load(fr'C:\Users\ponsg\MiniGolf-Game\Assets\info_side.png')
        self.info_side = pygame.transform.scale(self.info_side,(400,800))
        self.level_label = []
        self.right_arrow = pygame.image.load(fr'C:\Users\ponsg\MiniGolf-Game\Assets\right_arrow.png')
        self.left_arrow = pygame.transform.rotate(self.right_arrow,180)
        for i in range(1,3):
            label = pygame.image.load(fr'C:\Users\ponsg\MiniGolf-Game\Assets\level{i}_label.png')
            self.level_label.append(pygame.transform.scale(label,(150,75)))

    def switch_levels(self,ball):
        '''Method to switch beetween levels'''
        cursor_pos =  pygame.mouse.get_pos()
        if self.distance(cursor_pos,(925,90)) < 25  and self.level_index < len(self.level_list)-1:
            self.level_index += 1
            ball.reset()
            self.chronometer.start()
        elif self.distance(cursor_pos,(700,90)) < 25 and self.level_index >= 1:
            self.level_index -= 1
            ball.reset()
            self.chronometer.start()
        return self.level_list[self.level_index]
    
    def draw(self, surface):
        '''Draw all elements of the info bar'''
        self.chronometer.update()
        self.score_render = self.text_font.render(f"Score : {self.score}",True,(255,255,255))
        if self.highscore == 1:
            self.highscore = "Hole in one"
        self.highscore_render = self.text_font.render(f"Highscore : {str(self.highscore)}",True,(255,255,255))
        self.text_render = self.text_font.render(f"Chrono : {str(self.chronometer.time_passed)}", True,(255,255,255))
        surface.blit(self.info_side,(600,0))
        surface.blit(self.level_label[self.level_index],(725,50))
        surface.blit(self.right_arrow,(900,65))
        surface.blit(self.left_arrow,(650,65))
        surface.blit(self.text_render,(725,200))
        surface.blit(self.highscore_render,(710,300))
        surface.blit(self.score_render,(725, 400))
    
    def distance(self,coor : tuple , coor2 : tuple):
        '''Return distance beetween two entity'''
        return (((coor2[0]-coor[0])**2)+((coor2[1]-coor[1])**2))**0.5

class Timer :
    def __init__(self):
        self.initial = None
        self.current = None
        self.time_passed = None
    
    def start(self):
        '''Start the chronometer'''
        self.initial = time.time()

    def update(self):
        '''Update time'''
        self.current = time.time()
        self.time_passed = round(self.current - self.initial)
        
    def convert(self):
        '''Convert the litteral time in human reading capable time'''
        hour = round(self.time_passed() / 3600)
        minute = round(self.time_passed / 60)
        #In prototype

class Start_Menu:
    def __init__(self):
        self.play_img = pygame.image.load('Assets\play.png')
        self.settings_img = pygame.image.load('Assets\settings.png')
        self.quit_img = pygame.image.load('Assets\quit.png')
        self.bg = pygame.image.load('Assets\main_bg')
        self.bg = pygame.transform.scale(self.bg,(1000,1000))
        self.bg_move = 0
    
    def draw(self,surface):
        surface.blit(self.play_img,(400,200))
        surface.blit(self.settings_img,(400,300))
        surface.blit(self.quit_img,(400,400))
        surface.blit(self.bg,(-10+self.bg_move,0))
        if self.bg_move < 10 :
            self.bg_move += 1
        else :
            self.bg_move = 0