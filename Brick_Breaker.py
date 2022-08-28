from sys import platlibdir
import pygame
import time

pygame.init()

# Create Screen

gameDisplay=pygame.display.set_mode((600,400))

white=(255,255,255)

#plate
plate_x=100
running=True

# ball
ball_x=200
ball_y=200
ball_x_vel=1
ball_y_vel=1
i=0


#points
point_x=[]
point_y=10
point_exist=[1,1,1,1,1,1,1,1,1,1]
i=0
while i!=10:
    point_x.append(i)
    i+=1

# score
score=0

while running:
    gameDisplay.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Plate movement
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            if plate_x > 0:
                plate_x-=1
        if event.key == pygame.K_RIGHT:
            if plate_x <500:
                plate_x+=1

    #ball movement
    if ball_x_vel == 1:
        ball_x+=1
    elif ball_x_vel == -1:
        ball_x-=1
    if ball_y_vel == 1:
        ball_y-=1
    elif ball_y_vel == -1:
        ball_y+=1
    
    #ball bounce
    if ball_x == 600:
        ball_x_vel = -1
    elif ball_x == 0:
        ball_x_vel = 1
    if ball_y == 0:
        ball_y_vel = -1
    i=0
    if ball_y == 380:
        if ball_y_vel == -1:
            while i!=101:
                if ball_x == plate_x+i:
                    ball_y_vel = 1
                i+=1

    if ball_y == 400:
        ball_x=200
        ball_y=200
        ball_y_vel=1
        break


    # speed control
    time.sleep(0.008)

    #score
    i=0
    j=0
    if ball_y==30:
        for i in range(0,10):
            for j in range(0,21):
                if ball_x == 100+(point_x[i]*30)+j:
                    if point_exist[i]==1:
                        point_exist[i]=0
                        ball_y_vel=-1
                        score+=1
                        print(score)

    #points
    i=0
    while i!=10:
        if point_exist[i]==1:
            pygame.draw.rect(gameDisplay,white,(100+point_x[i]*30,point_y,20,20))
        i+=1
    if score == 10:
        break

    #ball
    pygame.draw.rect(gameDisplay,white,(ball_x,ball_y,10,10))
    # Plate
    pygame.draw.rect(gameDisplay,white,(plate_x,390,100,10))
    pygame.display.update()
if score ==10:
    print("You Win")
else:
    print("You Lose")