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
    cursor_pos = 0
    ball = libs.Ball(WIDTH//2,HEIGHT-70)
    level = libs.Level()
    '''Mainloop'''
    while running :
        level.draw(screen)
        ball.draw(screen)
        for event in pygame.event.get():
            '''Stop condition'''
            if event.type == pygame.QUIT :
                running = False
            if event.type == pygame.MOUSEBUTTONUP :
                if event.button == 1 :
                    ball.tension(cursor_pos)
            elif event.type == pygame.MOUSEBUTTONDOWN :
                if event.button == 1 :
                    cursor_pos = pygame.mouse.get_pos() #In prototype
        ball.update_pos()
        ball.collide(level)
        pygame.display.update()
        clock.tick(60)
    pygame.quit()