# libraries required
import pygame
import time
import random

pygame.init()

# Create Game Window

gameDisplay=pygame.display.set_mode((600,400))

white=(255,255,255)

# snake head
snake_x=100
snake_y=100

# Snake Movement
snake_up=0
snake_down=0
snake_left=0
snake_right=1

# Snake Food
food_x=200
food_y=200
snake_food_reallocation=0
score=0

# Snake Body
body_x=[]
body_y=[]

running=True

while running:
    gameDisplay.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #key pres
    if event.type == pygame.KEYDOWN:
        if snake_down==0:   
            if event.key == pygame.K_UP:
                snake_up=1
                snake_down=0
                snake_left=0
                snake_right=0
        if snake_up==0:   
            if event.key == pygame.K_DOWN:
                snake_up=0
                snake_down=1
                snake_left=0
                snake_right=0
        if snake_right==0:   
            if event.key == pygame.K_LEFT:
                snake_up=0
                snake_down=0
                snake_left=1
                snake_right=0
        if snake_left==0:   
            if event.key == pygame.K_RIGHT:
                snake_up=0
                snake_down=0
                snake_left=0
                snake_right=1

    # Body movement
    i=score
    body_x.append(0)
    body_y.append(0)
    body_x[0]=snake_x
    body_y[0]=snake_y
    while i!=0:
        body_x[i]=body_x[i-1]
        body_y[i]=body_y[i-1]
        i-=1


    # Snake Movement
    if snake_up==1:
        snake_y-=10
    if snake_down==1:
        snake_y+=10
    if snake_left==1:
        snake_x-=10
    if snake_right==1:
        snake_x+=10

    # Snake eats the food
    for i in range(0,10):
        if snake_x==food_x+i or snake_x+10==food_x+i:
            for i in range(0,10):
                if snake_y==food_y+i or snake_y+10==food_y+i:
                    snake_food_reallocation=1
                    score+=1

    # Snake food movement
    if snake_food_reallocation==1:
        food_x=random.randint(20,570)
        food_y=random.randint(20,370)
        snake_food_reallocation=0


    # Boundary Condition
    if snake_x==0 or snake_x==590:
        break
    if snake_y ==0 or snake_y==390:
        break

    # Tail condition
    break_loop=0
    for i in range(0,score):
        if snake_x==body_x[i] and snake_y==body_y[i]:
            break_loop=1

    if break_loop==1:
        break

    # Snake head
    pygame.draw.rect(gameDisplay,white,(snake_x,snake_y,10,10))

    #Snake food
    pygame.draw.rect(gameDisplay,white,(food_x,food_y,10,10))

    #Snake Body
    for i in range(0,score):
        pygame.draw.rect(gameDisplay,white,(body_x[i],body_y[i],10,10))

    # Boundary
    pygame.draw.rect(gameDisplay,white,(0,0,10,400))
    pygame.draw.rect(gameDisplay,white,(590,0,10,400))
    pygame.draw.rect(gameDisplay,white,(0,390,600,10))
    pygame.draw.rect(gameDisplay,white,(0,0,600,10))
    # Speed control
    time.sleep(0.08)
    pygame.display.update()

print("Game Over")
print("Score=",score)