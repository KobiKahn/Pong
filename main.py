import pygame, sys

pygame.init()

clock = pygame.time.Clock()




screen_w, screen_y = 600, 800
screen = pygame.display.set_mode((screen_w, screen_y))

pygame.display.set_caption('Pong')

# image = pygame.image.load('Pong_ball.png')
#
# ball = screen.blit(image, (x, y))



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
    def __init__(self, x = 200, y = 300, width = 20, height = 20, vel = 5, max_h = 790, min_h = 10, max_w = 610, min_w = -10):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = vel
        self.max_h = max_h
        self.min_h = min_h
        self.max_w = max_w
        self.min_w = min_h


while True:

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

    # if ball_x >= 585:
    #     over = True
    # if ball_x <= 10:
    #     over = True
    #
    # if ball_y <= 0:
    #     vert_vel *= switch
    # if ball_y >= 785:
    #     vert_vel *= switch



    screen.fill((0, 0, 0))
    player1.draw_rect1()
    player2.draw_rect2()

    pygame.display.flip()
    clock.tick(60)

