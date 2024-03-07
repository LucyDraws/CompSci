# !/usr/bin/python
# -*- coding: utf-8 -*-
import datetime
import os
import random
import threading
import pygame

pygame.init()

screen_height = 600 
screen_width = 1100
screen = pygame.display.set_mode((screen_width, screen_height))


pygame.display.set_caption("Chrome Dino Runner")


Icon = pygame.image.load("assets/DinoWallpaper.png")
pygame.display.set_icon(Icon)


Run = [
    pygame.image.load(os.path.join("assets/Dino", "DinoRun1.png")),
    pygame.image.load(os.path.join("assets/Dino", "DinoRun2.png")),
 ]
Jump = pygame.image.load(os.path.join("assets/Dino", "DinoJump.png"))
                   
Duck = [
    pygame.image.load(os.path.join("assets/Dino", "DinoDuck1.png")),
    pygame.image.load(os.path.join("assets/Dino", "DinoDuck2.png")),]


Small_Cactus = [
    pygame.image.load(os.path.join("assets/Cactus", "SmallCactus1.png")),
    pygame.image.load(os.path.join("assets/Cactus", "SmallCactus2.png")),
    pygame.image.load(os.path.join("assets/Cactus", "SmallCactus3.png")),
]

Large_Cactus = [
    pygame.image.load(os.path.join("assets/Cactus", "LargeCactus1.png")),
    pygame.image.load(os.path.join("assets/Cactus", "LargeCactus2.png")),
    pygame.image.load(os.path.join("assets/Cactus", "LargeCactus3.png")),
]

Bird = [
     pygame.image.load(os.path.join("assets/Bird", "Bird1.png")),
    pygame.image.load(os.path.join("assets/Bird", "Bird2.png")),
]

Cloud = pygame.image.load(os.path.join("assets/Other", "Cloud.png"))


BG = pygame.image.load(os.path.join("assets/Other", "Track.png"))


Font_Color = (0,0,0)

class Dino:
    x_pos = 80
    y_pos = 310
    y_pos_duck = 340
    jump_velocity = 8.5

    def __init__(self):
        self.duck_img = Duck
        self.run_img = Run
        self.jump_img = Jump

        self.dino_duck = False
        self.dino_run = True
        self.dino_jump = False

        self.step_index = 0
        self.jump_vel = self.jump_velocity
        self.image = self.run_img[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.x_pos
        self.dino_rect.y = self.y_pos
    
    def update(self, input):
        if self.dino_duck:
            self.duck()
        if self.dino_run:
            self.run()
        if self.dino_jump:
            self.jump()
        if self.step_index >= 10:
            self.step_index = 0
        if (input[pygame.K_UP] or input[pygame.K_SPACE] and not self.dino_jump):
            self.dino_duck = False
            self.dino_run = False
            self.dino_jump = True
        elif (input[pygame.K_DOWN] and not self.dino_jump):
            self.dino_duck = True
            self.dino_run = False
            self.dino_jump = False
        elif not (self.dino_jump or input[pygame.K_DOWN]):
            self.dino_duck = False
            self.dino_jump = False
            self.dino_run = True
    
    def duck(self):
        self.image = self.duck_img[self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.x_pos
        self.dino_rect.y = self.y_pos_duck
        self.step_index += 1
        

    def run(self):
        self.image = self.run_img[self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.x_pos
        self.dino_rect.y = self.y_pos
        self.step_index += 1

    def jump(self):
        self.image = self.jump_img
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8
        if self.jump_vel < -self.jump_velocity:
            self.dino_jump = False
            self.jump_vel = self.jump_velocity

    def draw(self, SCREEN):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))

class clouds:
    def __init__(self):
        self.x = screen_width + random.randint(800, 1000)
        self.y = random.randint(50, 100)
        self.image = Cloud
        self.width = self.image.get_width()
        

    def update(self):
        self.x -= game_speed
        if self.x < -self.width:
            self.x = screen_width + random.randint(2500, 3000)
            self.y = random.randint(50, 100)


    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

class obstacle:
    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect()
        self.rect.x = screen_width
        
    
    def update(self,):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            obstacles.pop()
    
    def draw(self, SCREEN):
        SCREEN.blit(self.image[self.type], self.rect)

class small_cactus(obstacle):
    def __init__(self, image):
        self.type = random.randint(0,2)
        super().__init__(image, self.type)
        self.rect.y = 325

class large_cactus(obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 300

class bird(obstacle):
    bird_heights = [250, 290, 320]

    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = random.choice(self.bird_heights)
        self.index = 0


    def draw(self, screen):
        if self.index >= 9:
            self.index = 0
        screen.blit(self.image[self.index // 5], self.rect)
        self.index += 1

def main():
    global game_speed, x_bg, y_bg, points, obstacles
    run = True
    clock = pygame.time.Clock()
    player = Dino()
    cloud = clouds()
    game_speed = 20
    x_bg = 0
    y_bg = 380
    points = 0
    font = pygame.font.Font("freesansbold.ttf", 20)
    obstacles = []
    death_count = 0
    pause = False

    def score():
        global points, game_speed
        points += 1
        if points % 100 == 0:
            game_speed += 1
        current_time = datetime.datetime.now().hour
        with open("score.txt", "r") as f:
            score = (f.read())
            score_ints = [int(x) for x in score.split()]
            highscore = max(score_ints)
            if points > highscore:
                highscore = points
            text = font.render("High Score: "+ str(highscore) + "  Points: " + str(points), True, Font_Color)
        text_rect = text.get_rect()
        text_rect.center = (900, 40)
        screen.blit(text, text_rect)
    def bg():
        global x_bg, y_bg
        width = BG.get_width()
        screen.blit(BG, (x_bg, y_bg))
        screen.blit(BG, (width + x_bg, y_bg))
        if x_bg <= -width:
            screen.blit(BG, (width + x_bg, y_bg))
            x_bg = 0
        x_bg -= game_speed

    def Pause():
        nonlocal pause
        pause = True
        font = pygame.font.Font("freesansbold.ttf", 30)
        text = font.render("Game Paused, press "u" to unpause", True, Font_Color)
        text_rect = text.get_rect()
        text_rect.center = (screen_width // 2, screen_height // 3)
        screen.blit(text, text_rect)
        pygame.display.update()
        while pause:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_u:
                    unpause()

    def unpause():
        nonlocal pause, run
        pause = False
        run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                run = False
                pause()

        current_time = datetime.datetime.now().hour
        if 7 < current_time < 19:
            screen.fill((255, 255, 255))
        else:
            screen.fill((0, 0, 0))
        user_input = pygame.key.get_pressed()

        player.draw(screen)
        player.update(user_input)

        if len(obstacles) == 0:
            if random.randint(0,2) == 0:
                obstacles.append(small_cactus(Small_Cactus))
            elif random.randint(0,2) == 1:
                obstacles.append(large_cactus(Large_Cactus))
            elif random.randint(0,2) == 2:
                obstacles.append(bird(Bird))
        
        for obstacle in obstacles:
            obstacle.draw(screen)
            obstacle.update()
            if player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(2000)
                death_count += 1
                menu(death_count)

        bg()

        cloud.draw(screen)
        cloud.update()
        score()
        clock.tick(30)
        pygame.display.update()

def menu(death_count):
    global points
    global Font_Color
    run = True
    while run:
        time = datetime.datetime.now().hour
        if 7 < time < 19:
            Font_Color = (0,0,0)
            screen.fill((255,255,255))
        else:
            Font_Color = (255,255,255)
            screen.fill(128,128,128)
        font = pygame.font.Font("freesansbold.ttf", 30)

        if death_count == 0:
            text = font.render("Press any Key to Start", True, Font_Color)
        elif death_count > 0:
            text = font.render("Press any Key to Restart", True, Font_Color)
            score = font.render("Your Score: " + str(points), True, Font_Color)
            score_rect = score.get_rect()
            score_rect.center = (screen_width // 2, screen_height // 2 + 50)
            screen.blit(score, score_rect)
            f = open("score.txt", "a")
            f.write(str(points)+ "\n")
            f.close()
            with open("text.txt", "r") as f:
                score = (f.read())
                score_int =[int(x) for x in score.split()]
            highscore = max(score_int)
            highscore_text = font.render("High Score : ", str(highscore), True, Font_Color)
            highscore_rect = highscore_text.get_rect()
            highscore_rect.center(screen_width // 2, screen_height // 2 + 100)
            screen.blit(highscore_text, highscore_rect)
        text_rect = text.get_rect()
        screen.blit(Run[0], (screen_width // 2 - 20, screen_height // 2 - 140))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.display.quit()
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                main()

start = threading.Thread(target = menu(death_count=0),daemon= True)
start.start()
