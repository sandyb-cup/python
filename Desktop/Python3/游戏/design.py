from tkinter.constants import END
import pygame
import random
import time
pygame.init()


SCREEN_RECT = pygame.Rect(0,0,400,700)

# 定义事件编号
CRECT_ENEMY_EVENT = pygame.USEREVENT + 1
class Base(pygame.sprite.Sprite):
    def __init__(self, image_path, speed):
        super().__init__()
        
        
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.speed = speed         
    
    def update(self, *args):
        self.rect.y += self.speed

class Background(Base):
    def __init__(self, image_path = '/Users/sandy/Desktop/Python3/images/background.png', speed = 2, flag = True):
        super().__init__(image_path, speed) 
        # 0, 0, 0, -700
        # 如果传入的flag是一个false，y的位置设置为 -700
        if not flag:
            self.rect.y = -700
            
    def update(self, *args):
        self.rect.y += self.speed
        
        if self.rect.y > SCREEN_RECT.height:
            self.rect.y = -SCREEN_RECT.height
class Hero(Base):
    def __init__(self, image_path = '/Users/sandy/Desktop/Python3/images/me2.png', speed = 0, flag = True):
        super().__init__(image_path, speed) 
        self.rect.x = SCREEN_RECT.w / 2
        self.rect.y = SCREEN_RECT.height * 5/7
        
        self.bullet_group = pygame.sprite.Group()
        
        self.flag = True
        self.image1 = pygame.image.load("/Users/sandy/Desktop/Python3/images/me1.png")
        self.image2 = pygame.image.load("/Users/sandy/Desktop/Python3/images/me2.png")
    
    def fire(self):
        index = 15
        # 子弹音乐加载
        self.bullet_sound = pygame.mixer.Sound("/Users/sandy/Desktop/Python3/sound/bullet.wav")

        # 设置音乐大小
        self.bullet_sound.set_volume(0.1)
        
        for i in range(3):
            bullet = Bullet()
            bullet.rect.x = self.rect.centerx
            bullet.rect.y = self.rect.centery - 20 - i * index
            self.bullet_group.add(bullet)
            self.bullet_sound.play()
        
        
    def update(self, *args):
        if self.flag:
            self.image = self.image1
            self.flag = False
        else:
            self.image = self.image2
            self.flag = True
            
        self.rect.x += self.speed
        
        if self.rect.x < self.speed:
            self.rect.x = self.speed

        if self.rect.x > SCREEN_RECT.w - self.rect.w:
            self.rect.x = SCREEN_RECT.w - self.rect.w
            
class Bullet(Base):
    def __init__(self):
        super().__init__(image_path="/Users/sandy/Desktop/Python3/cartoon.jpg", speed = -2)
        self.rect.x = SCREEN_RECT.w / 2
        self.rect.y = SCREEN_RECT.height * 5/7
        
        # 释放内存 结束操作
        if self.rect.bottom < 0:
            self.kill()
           
class Enemy(Base):
    def __init__(self, image_path = '/Users/sandy/Desktop/Python3/images/enemy1.png', speed = 0, flag = True):
        speed = random.randint(1, 4)  
        super().__init__(image_path, speed) 
        self.rect.x = random.randint(0, SCREEN_RECT.w - self.rect.w)
        
        self.down_enemy_image_number = 0
        self.activate = True
        # 被摧毁前敌机图片
        self.down_enemy = [
            pygame.image.load("/Users/sandy/Desktop/Python3/images/enemy1_down1.png"),
            pygame.image.load("/Users/sandy/Desktop/Python3/images/enemy1_down2.png"),
            pygame.image .load("/Users/sandy/Desktop/Python3/images/enemy1_down3.png"),
            pygame.image.load("/Users/sandy/Desktop/Python3/images/enemy1_down4.png")
            
                        ]
        
        
        
    def update(self, *args):
        super().update(*args)
        
        # 释放内存 结束操作
        if self.rect.y > SCREEN_RECT.height:
            self.kill()
        if not self.activate:
            if self.down_enemy_image_number >= 3:
                self.enemy_down_sound = pygame.mixer.Sound("/Users/sandy/Desktop/Python3/sound/enemy2_down.wav")

                # 设置音乐大小
                self.enemy_down_sound.set_volume(0.1)
                self.enemy_down_sound.play()
                self.kill()
            self.image = self.down_enemy[self.down_enemy_image_number]
            self.down_enemy_image_number += 1
            # 敌机死亡
            
    # def __del__(self):
    #     # 对象被销毁前自动调用的方法
    #     print("对象被销毁")
        
    