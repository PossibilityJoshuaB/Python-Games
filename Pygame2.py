#Intialization
import pygame
pygame.init()

#dimensions and screen
screen = pygame.display.set_mode((700, 700))
x = 200
y = 200
width = 20
height = 20

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
    # if (keys[pygame.K_l]) and vel <= 10:
    #     vel += 1
    # if (keys[pygame.K_j]) and vel >= 0.5:
    #     vel -= 0.5

    
    #screen stuff
    screen.fill((0,0, 10))


    #drawing object
    pygame.draw.rect(screen, (0,22,191), (x, y, width, height))

    #display update
    pygame.display.update()

pygame.quit()
quit()