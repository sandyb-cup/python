import pygame
import random
# 初始化pygame模块
bg_rect = pygame.Rect((0, 0, 480, 700))
bg = pygame.image.load('/Users/sandy/Desktop/Python3/images/background.png')
pygame.init() 
class Enemy(pygame.sprite.Sprite): 
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("/Users/sandy/Desktop/Python3/images/enemy1.png")
        self.rect = self.image.get_rect()
        self.speed = self.speed = 1
        self.rect.x = random.randint(0, bg_rect.w - self.rect.w)
    def update(self, *args):
        self.rect.y += self.speed
         
# enemy = Enemy()   
# 创建一个敌机精灵组
enemy_group = pygame.sprite.Group()
# enemy_group.add(enemy)

screen = pygame.display.set_mode((480, 700))



hero_rect = pygame.Rect((120, 350, 20, 20))
hero = pygame.image.load('/Users/sandy/Desktop/Python3/images/me2.png')

clock = pygame.time.Clock()
i = 0
while True:
    """
    游戏循环 英雄位置发生改变，然后把英雄绘制到屏幕对象 更新显示对象
    """
    clock.tick(30)
    
    screen.blit(bg, bg_rect) 
    # hero_rect.y -= 2
    screen.blit(hero, hero_rect)
    clock.tick(30)
    event_info = pygame.event.get()
    
    # 更新敌机对象的位置
    # screen.blit(enemy.image, enemy.rect)
    # enemy.update()
    enemy = Enemy()
    enemy_group.add(enemy)
    enemy_group.update() # 调用每一个精灵 update方法
    enemy_group.draw(screen) # 将每一个精灵 绘制到背景里面
    
    
    pygame.display.update()
    # 记录键盘事件
    # for i in event_info:
    #     if i == pygame.QUIT:
    #         pygame.quit()
    # 专门处理事件的方法,获取的是一个列表
    key_press = pygame.key.get_pressed()

    