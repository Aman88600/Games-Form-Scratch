import pygame
import time
import random

pygame.init()

# Game Window
gameDisplay=pygame.display.set_mode((600,400))
white=(255,255,255)
#Battle Ship
battle_ship_x=300
#Battle Ship Gun
fire=0
bullet_x=0
bullet_y=400
i=0
p=0

# Enemy Ship
enemy_ship_x=50
j=0
enemy_ship_exist=[1,1,1,1,1,1,1,1,1,1]

#Enemy Bullet
ship_count=10
enemy_bullet_y=10
active_ship=0
enemy_fire=1
score=0
life=1
battle_ship_info=0

#level
level=1

running=True
while running:
    gameDisplay.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    
    # Battle Ship Movement
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            if battle_ship_x > 0:
                battle_ship_x -=1
        if event.key == pygame.K_RIGHT:
            if battle_ship_x < 570:
                battle_ship_x +=1
    
    #Battle Ship fire
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            fire=1

    #Battle Ship Gun
    if fire ==1:
        while p!=571:
            if battle_ship_x==p:
                bullet_x=battle_ship_x
                bullet_x+=10
            p+=1
        pygame.draw.rect(gameDisplay,white,(bullet_x,bullet_y,10,10))
        bullet_y-=1
        if bullet_y==0:
            fire=0
            bullet_y=400
            p=0
    
    #Enemy Ship
    for j in range(0,10):
        if enemy_ship_exist[j]==1:
            pygame.draw.rect(gameDisplay,white,(enemy_ship_x+j*50,10,30,10))
            pygame.draw.rect(gameDisplay,white,(enemy_ship_x+10+j*50,20,10,10))
    
    
    #Enemy Bullet
    battle_ship_info=battle_ship_x
    ship_count=0
    for j in range(0,10):
        if enemy_ship_exist[j]==1:
            ship_count+=1
    if enemy_fire==1:
        active_ship=random.randint(0,9)
    if enemy_ship_exist[active_ship]==1:
        pygame.draw.rect(gameDisplay,white,(enemy_ship_x+10+active_ship*50,enemy_bullet_y,10,10))
        enemy_bullet_y+=1
        enemy_fire=0
    if enemy_ship_exist[active_ship]==0:
        enemy_fire=1
    if enemy_bullet_y == 400:
        enemy_bullet_y=10
        enemy_fire=1
    if ship_count == 0 or life == 0 :
        break
    if enemy_bullet_y==390:
        for i in range(0,31):
            if enemy_ship_x+10+(active_ship*50)==battle_ship_info+i:
                life-=1


    
    #Score
    if bullet_y==10:
        for j in range(0,10):
            for k in range(0,31):
                if bullet_x == enemy_ship_x+(j*50)+k:
                    if enemy_ship_exist[j]==1:
                        enemy_ship_exist[j]=0
                        score+=1
                        print(score)
                    

    # Battle Ship
    pygame.draw.rect(gameDisplay,white,(battle_ship_x,390,30,10))
    pygame.draw.rect(gameDisplay,white,(battle_ship_x+10,390-10,10,10))

    # Speed Control
    time.sleep(0.008)
    pygame.display.update()

if ship_count == 0:
    print("You Win")
else:
    print("You Lose")