import pygame, sys
import random
pygame.init()

clock = pygame.time.Clock()

keys = pygame.key.get_pressed()

screen_w, screen_y = 600, 800
screen = pygame.display.set_mode((screen_w, screen_y))

pygame.display.set_caption('Pong')

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

myfont = pygame.font.SysFont('ccoverbyteoffregular.otf', 100)


direction = ('Right','Left')
numbers = [-1,1]
random_direction = random.choice(numbers)


class Player():
    def __init__(self, width = 10, height = 100, x = 590, y = 400, vel = 10):
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
player2 = Player(10, 100, 0, 400, 10)


class ball():
    def __init__(self, random, x = 200, y = 300, radius = 10, h_vel = 5, v_vel = 5, max_h = 790, min_h = 10, start = 0):
        self.x = x
        self.y = y
        self.radius = radius
        self.h_vel = h_vel
        self.v_vel = v_vel
        self.max_h = max_h
        self.min_h = min_h
        self.random = random
        self.start = start



    def draw_circle(self):
        pygame.draw.circle(screen, (255, 255, 255), (self.x, self.y), self.radius)
        self.x += self.h_vel
        self.y += self.v_vel


ball1 = ball(random_direction)



ball_count = 0

score1 = 0
score2 = 0

player1score = myfont.render(f'{score1}', False, (255, 255, 255))
player2score = myfont.render(f'{score2}', False, (255, 255, 255))
ending = myfont.render('', False, (255, 255, 255))

over = False


num_sequence = [ 5, -5, 6, -6]
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



    if ball1.x >= 825 or ball1.x <= -25:
        counter = 0
        if ball1.x >= 800:
            score2 += 1
            player2score = myfont.render(f'{score2}', False, (255, 255, 255))
        if ball1.x <= -10:
            score1 += 1
            player1score = myfont.render(f'{score1}', False, (255, 255, 255))
        if score1 == 10:
            ending = myfont.render('Player 1 WINS!!', False, (255, 255, 255))
            over = True
        if score2 == 10:
            ending = myfont.render('Player 2 WINS!!', False, (255, 255, 255))
            over = True
        ball1.x = 200
        ball1.y = 300
        ball1.v_vel = random.randint(3, 6)


    if ball1.y <= 10:
        ball1.v_vel *= switch
    if ball1.y >= 790:
        ball1.v_vel *= switch


#########################################
#BALL COLLISION WITH PLAYER
    if ball1.x == 580 and ball1.y >= player1.y and ball1.y <= (player1.y + 100):
        ball1.h_vel *= switch
        if keys[pygame.K_DOWN]:
            if ball1.v_vel > 0:
                ball1.v_vel *= switch
            ball1.v_vel -= .5
        if keys[pygame.K_UP]:
            if ball1.v_vel < 0:
                ball1.v_vel *= switch
            ball1.v_vel += .5





    if ball1.x == 20 and ball1.y >= player2.y and (ball1.y + 10) <= (player2.y + 110):
        ball1.h_vel *= switch
        if keys[pygame.K_s]:
            if ball1.v_vel > 0:
                ball1.v_vel *= switch
            ball1.v_vel -= .5
        if keys[pygame.K_w]:
            if ball1.v_vel < 0:
                ball1.v_vel *= switch
            ball1.v_vel += .5



#########################################


    screen.fill((0, 0, 0))

    if keys[pygame.K_SPACE] and counter == 0 and over == False:
        counter = 1
        ball1.h_vel = random.choice(num_sequence)
        ball1.draw_circle()
    if counter == 1:
        ball1.draw_circle()
    screen.blit(player1score, (500, 30))
    screen.blit(player2score, (100, 30))
    player1.draw_rect1()
    player2.draw_rect2()
    if over == True:
        screen.blit(ending, (50, 400))
    pygame.display.flip()
    clock.tick(60)

