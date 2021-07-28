import pygame
import time

pygame.init()
pygame.mixer.init()

#Colors
black = (0,0,0)
white = (255,255,255) 

#Creating game window
screen_width = 1100
screen_hight = 650
screen = pygame.display.set_mode((screen_width, screen_hight))
pygame.display.set_caption("Monster Hunter Game created by Pratham Rathod")

#import images 
welcome_img = pygame.image.load("Gallary\welcome text.png")
welcome_img = pygame.transform.scale(welcome_img,(screen_width,screen_hight))

back_ground_img = pygame.image.load("Gallary\\bg.png")
back_ground_img = pygame.transform.scale(back_ground_img,(screen_width+10,screen_hight+10))

base_img = pygame.image.load("Gallary\\base.png")
base_img = pygame.transform.scale(base_img,(screen_width,100))

dino1 = pygame.image.load("Gallary\\dino.png")
dino1 = pygame.transform.scale(dino1,(210,170))

dino2 = pygame.image.load("Gallary\\dino2.png")
dino2 = pygame.transform.scale(dino2,(210,170))

dino3 = pygame.image.load("Gallary\\dino3.png") 
dino3 = pygame.transform.scale(dino3,(210,170))

dino_dead = pygame.image.load("Gallary\\dino2.png")
dino_dead = pygame.transform.scale(dino_dead,(210,170))
dino_dead = pygame.transform.rotate(dino_dead,160)

blood = pygame.image.load("Gallary\\blood.png")
blood = pygame.transform.scale(blood,(210,170))

hunter = pygame.image.load("Gallary\hunter.png")
hunter = pygame.transform.scale(hunter,(155,120))

game_over_img = pygame.image.load("Gallary\\game over.png")
game_over_img = pygame.transform.scale(game_over_img,(screen_width-50,screen_hight-50))

#Welcome window
def Welcome():
    pygame.mixer.music.load("Gallary\music.mp3")
    pygame.mixer.music.play()
    screen.fill(white)
    screen.blit(back_ground_img, (0,0))
    screen.blit(welcome_img, (0,0))
    screen.blit(base_img, (0,550))
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    pygame.mixer.music.load("Gallary\Starting_music.mp3")
                    pygame.mixer.music.play()
                    Main_Game()
                    
#Main game loop
def Main_Game():
    #Useful veriables for game
    game_over = False
    jump = False
    game_start = False
    bg_x = 0
    bg_y = 0
    base_x = 0
    base_y = 550
    dino_x = 80
    dino_y = 400
    velocity_x = 0
    bg_speed = 6
    hunter_x = 1200
    hunter_y = 450
    bg_count = 0
    score = 0

    font = pygame.font.SysFont(None,100,bold=10)
    # dino walking and hunter
    dino = [dino2,dino2,dino2,dino3,dino3,dino3,dino3,dino1,dino_dead]
    walk = 0
    while not game_over:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    quit()
                if event.key == pygame.K_SPACE:
                    velocity_x = bg_speed
                    game_start = True
                    if dino_y > 350:
                        jump = True
                        pygame.mixer.music.load("Gallary\swoosh.wav")
                        pygame.mixer.music.play()
                        pygame.mixer.music.load("Gallary\Animal_Bark_And_Growl.mp3")
                        pygame.mixer.music.play()
                        bg_speed += 0.1

        base_x -= velocity_x
        screen.fill(white)

        #Set background and infinet base     
        if game_start == True:
            if bg_count == 20:
                bg_y -= 2
                bg_x -= 2
                bg_count = 0

            if bg_count == 15:
                bg_y = 0
                bg_x =0
            bg_count += 1
        
        if base_x < -1099:
            base_x = 0

        #hunter image
        hunter_x -= velocity_x
        if hunter_x < -50:
            hunter_x = 1100
        
        #moving dino
        walk += 1
        if walk > 6:
            walk = 0
        
        #dino jump
        if 401 > dino_y > 100:
            if jump:
                walk = 1
                dino_y -= 10
                
                
        else:
            jump = False
            

        if dino_y < 400:
            if not jump:
                walk = 4
                dino_y += 10
        
        #game over
        if dino_x > hunter_x - 145 and dino_y > hunter_y - 90:
            bg_speed = 0
            pygame.mixer.music.load("Gallary\Big_Gun_Shots_Close.mp3")
            pygame.mixer.music.play()
            
            walk = 8
            game_over = True
        elif dino_x > hunter_x - 145:
            score += 1
        #score
        score_screen = font.render("Your Score : "+str(score),True,black)
        over_score = font.render(str(score),True,black)

        #bliting images 
        screen.blit(back_ground_img, [bg_x,bg_y])
        screen.blit(base_img, [base_x,base_y])
        screen.blit(base_img, [base_x+screen_width,base_y])
        screen.blit(hunter, [hunter_x,hunter_y])
        screen.blit(score_screen, [400,0])
        if not game_start:
            screen.blit(dino[7], [dino_x,dino_y])
        
        if game_start:
            screen.blit(dino[walk], [dino_x,dino_y])

        if game_over:
            screen.blit(blood,[dino_x,dino_y])
            screen.blit(game_over_img,[0,0])
            screen.blit(over_score, [700,370])
        
        pygame.display.update()

Welcome()
