#initialization
import pygame
import sys
pygame.init()

#screen and color setup
screen = pygame.display.set_mode((700, 700))
color_light = (0, 50, 100)
color_dark = (0, 10, 90)
color = (255, 255, 255)

#store screen width and height
width = screen.get_width()
height = screen.get_height()

#writing text
font = pygame.font.SysFont(None, 35)
text = font.render("Close", True, color)

#game loop
running = True
while running:
    #mouse position
    mouse = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #if mouse click on rect, then open image
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if width/2-100 <= mouse[0] <= width/2+100 and height/2-20 <= mouse[1] <= height/2+20:
                img = pygame.image.load("C:\\Joshua\\3161LogoinBlack-Gold.png")
                
                screen.blit(img, (300, 300))
    #screen background
    screen.fill((255, 255, 255))
    #if mouse over, darken, else stay same
    if width/2-100 <= mouse[0] <= width/2+100 and height/2-20 <= mouse[1] <= height/2+20:
        pygame.draw.rect(screen, color_dark, (width/2-100, height/2-20, 200, 40))
    else:
        pygame.draw.rect(screen, color_light, (width/2-100, height/2-20, 200, 40))

    #put text on button
    screen.blit(text, (width/2-70, height/2-10))
    #refresh the screen
    pygame.display.update()
pygame.quit()
quit()