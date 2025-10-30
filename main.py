import pygame 
import libs

HEIGHT = 720
WIDTH = 1000

if __name__ == "__main__" :
    pygame.init()
    screen = pygame.display.set_mode((WIDTH,HEIGHT)) 
    caption = pygame.display.set_caption("Mini golf game") 
    clock = pygame.time.Clock() 
    running = True 
    ball = libs.Ball(WIDTH//2,HEIGHT-50)
    level = libs.Level()
    '''Mainloop'''
    while running :
        level.draw(screen)
        ball.draw(screen)
        for event in pygame.event.get():
            '''Stop condition'''
            if event.type == pygame.QUIT :
                running = False
            elif event.type == pygame.KEYDOWN :
                pass
        pygame.display.update()
        clock.tick(60)
    pygame.quit()