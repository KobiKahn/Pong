import pygame, sys

pygame.init()

clock = pygame.time.Clock()

x = 200
y = 300

screen_w, screen_y = 600, 800
screen = pygame.display.set_mode((screen_w, screen_y))

pygame.display.set_caption('Pong')

image = pygame.image.load('Pong_ball.jpg')

ball = screen.blit(image, (x, y))

player1 = pygame.Rect(580, 400, 20, 100)

player2 = pygame.Rect(0, 400, 20, 100)



player1_downcollide = False
player1_upcollide = False

player2_downcollide = False
player2_upcollide = False

ball_x = 300
ball_y = 400

switch = -1

horizontal_vel = 5
vert_vel = 5

over = True

############################################
# WHEN DOING BALL COLLISION WITH SIDES MAKE
# IT SO WHEN BALL HITS RIGHT SIDE VARIABLE
# BECOMES LEFT AND THE VARIABLE HAS TO BE
# RIGHT WHEN IT COLLIDES RIGHT AND OPP.
############################################

while True:


    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    if player1.y >= 700:
        player1_downcollide = True
    else:
        player1_downcollide = False
    if player1.y <= 0:
        player1_upcollide = True
    else:
        player1_upcollide = False

    if player2.y >= 700:
        player2_downcollide = True
    else:
        player2_downcollide = False
    if player2.y <= 0:
        player2_upcollide = True
    else:
        player2_upcollide = False


    if player1_downcollide == False:
        if keys[pygame.K_DOWN]:
            player1.y += 20
    if player1_upcollide == False:
        if keys[pygame.K_UP]:
            player1.y -= 20

    if player2_downcollide == False:
        if keys[pygame.K_s]:
            player2.y += 20
    if player2_upcollide == False:
        if keys[pygame.K_w]:
            player2.y -= 20
    if ball_x >= 585:
        over = True
    if ball_x <= 10:
        over = True
        
    if ball_y <= 0:
        vert_vel *= switch
    if ball_y >= 785:
        vert_vel *= switch





    screen.fill((0, 0, 0))

    ball


    pygame.draw.rect(screen, (255, 255, 255), player1)
    pygame.draw.rect(screen, (255, 255, 255), player2)

    pygame.display.flip()
    clock.tick(60)

