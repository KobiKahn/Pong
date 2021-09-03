import pygame, sys
import random
pygame.init()

clock = pygame.time.Clock()

keys = pygame.key.get_pressed()

screen_w, screen_y = 600, 800
screen = pygame.display.set_mode((screen_w, screen_y))

pygame.display.set_caption('Pong')

# image = pygame.image.load('Pong_ball.png')
#
# ball = screen.blit(image, (x, y))

counter = 0

player1_downcollide = False
player1_upcollide = False

player2_downcollide = False
player2_upcollide = False

ball_x = 300
ball_y = 400

switch = -1

horizontal_vel = 5
vert_vel = 5

over = False

direction = ('Right','Left')
random_direction = [random.randint(0, 1)]


############################################
# WHEN DOING BALL COLLISION WITH SIDES MAKE
# IT SO WHEN BALL HITS RIGHT SIDE VARIABLE
# BECOMES LEFT AND THE VARIABLE HAS TO BE
# RIGHT WHEN IT COLLIDES RIGHT AND OPP.
############################################

class Player():
    def __init__(self, width = 20, height = 100, x = 580, y = 400, vel = 20):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.vel = vel



    def draw_rect1(self):
        player1 = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(screen, (255,255,255), player1)

    def draw_rect2(self):
        player2 = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(screen, (255,255,255), player2)


    def move_up(self):
        self.y -= self.vel
    def move_down(self):
        self.y += self.vel



player1 = Player()
player2 = Player(20, 100, 0, 400, 20)


class ball():
    def __init__(self, random, x = 200, y = 300, radius = 10, vel = 5, max_h = 790, min_h = 10, max_w = 610, min_w = -10 ):
        self.x = x
        self.y = y
        self.radius = radius
        self.vel = vel
        self.max_h = max_h
        self.min_h = min_h
        self.max_w = max_w
        self.min_w = min_w
        self.random = random

    def draw_circle(self):
        self.x += self.vel
        self.y += self.vel
        pygame.draw.circle(screen, (255, 255, 255), (self.x, self.y), self.radius)

ball1 = ball(random_direction)

if keys[pygame.K_1] and over == True:
    over = False


while not over:
    if over == True:
        counter = 0
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
###########################################
# PLAYER 1 COLLISION
    if player1.y >= 800:
        player1.y = -90

    if player1.y <= -100:
        player1.y = 800


# PLAYER 2 COLLISION
    if player2.y >= 800:
        player2.y = -90

    if player2.y <= -100:
        player2.y = 800


#########################################
    # PLAYER1 MOVEMENT

    if keys[pygame.K_DOWN]:
        player1.move_down()

    if keys[pygame.K_UP]:
        player1.move_up()

    # PLAYER2 MOVEMENT

    if keys[pygame.K_s]:
        player2.move_down()

    if keys[pygame.K_w]:
        player2.move_up()
 ########################################



    if ball1.x >= 800:
        over = True
    if ball1.x <= 0:
        over = True

    if ball1.y <= 15:
        vert_vel *= switch
    if ball1.y >= 785:
        vert_vel *= switch

#########################################

    # if ball.x - player1.x

    screen.fill((0, 0, 0))

    if keys[pygame.K_SPACE] and counter == 0:
        counter = 1
        ball1.draw_circle()
    if counter == 1:
        ball1.draw_circle()
    player1.draw_rect1()
    player2.draw_rect2()

    pygame.display.flip()
    clock.tick(60)

