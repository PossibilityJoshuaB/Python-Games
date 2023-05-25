#Intialization
import pygame
pygame.init()

#dimensions and screen
screen = pygame.display.set_mode((700, 700))
x = 0
y = 0
width = 20
height = 20
red = (191, 22, 0)
font = pygame.font.SysFont(None, 40)

# #drawing objects
# #do not touch rects
# rect1 = pygame.draw.rect(screen, red, (90, 90, 100, 100))
# rect2 = pygame.draw.rect(screen, red, (380, 190, 140, 140))
# # touch rect
# grect = pygame.draw.rect(screen, (22, 191, 0), (500, 500, 120, 120))

#speed of movement
vel = 1

running = True
while running:
    #game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #remember keys pressed
    keys = pygame.key.get_pressed()
    #which direction to move
    #left
    if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and x>0:
        x -= vel
    #right
    if (keys[pygame.K_d] or keys[pygame.K_RIGHT])and x<700-width:
        x += vel
    #up
    if (keys[pygame.K_w] or keys[pygame.K_UP])and y>0:
        y -= vel
    #down
    if (keys[pygame.K_s] or keys[pygame.K_DOWN]) and y<700-height:
        y += vel

    
    #screen stuff
    screen.fill((0,0, 10))


    #drawing objects
    #moving
    player = pygame.draw.rect(screen, (0,22,191), (x, y, width, height))
    #do not touch rects
    rect1 = pygame.draw.rect(screen, red, (90, 90, 100, 100))
    rect2 = pygame.draw.rect(screen, red, (380, 190, 120, 120))
    rect3 = pygame.draw.rect(screen, red, (90, 370, 200, 200))
    # touch rect
    grect = pygame.draw.rect(screen, (22, 191, 0), (500, 500, 120, 120))

    #game over
    if player.colliderect(rect1) or player.colliderect(rect2) or player.colliderect(rect3):
        gameend = pygame.draw.rect(screen, (100, 100, 100), (0, 0, 700, 700))
        text = font.render("FAILED. Click space to try again")
        # screen.blit(gameend, text)
        if keys[pygame.K_SPACE]:
            screen.blit(screen, (rect1, rect2, rect3, player, grect))
    elif player.colliderect(grect):
        gamewin = pygame.draw.rect(screen, (100, 100, 100), (0, 0, 700, 700))
        wintext = font.render("Well done. Click space to play again")
        # screen.blit(gamewin, wintext)
        if keys[pygame.K_SPACE]:
            screen.blit(screen, (rect1, rect2, rect3, player, grect))

    #display update
    pygame.display.update()

pygame.quit()
quit()