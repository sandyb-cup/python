from design import (Background, Hero, Enemy, Bullet, SCREEN_RECT,CRECT_ENEMY_EVENT)
import pygame
class Game():
    def __init__(self):
        
        # 加载背景音乐
        pygame.mixer.music.load("/Users/sandy/Desktop/Python3/sound/game_music.ogg")

        # 设置音乐大小
        pygame.mixer.music.set_volume(0.1)
        pygame.mixer.music.play(-1)
        
        
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        self.clock = pygame.time.Clock()
        
        self.creat_sprite()
        
        pygame.time.set_timer(CRECT_ENEMY_EVENT,500)
    def creat_sprite(self):
        bg = Background(flag = True)
        bg_flag = Background(flag = False)
        self.bg_group = pygame.sprite.Group()
        
        self.bg_group.add(bg)
        self.bg_group.add(bg_flag)
        
        # 将hero绑定到实例对象
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group()
        self.hero_group.add(self.hero)
        
        enemy = Enemy()
        self.enemy_group = pygame.sprite.Group()
        self.enemy_group.add(enemy)
        
    def update_sprite(self):
        # 创建对象 更新对象 绘制对象
        self.bg_group.update()
        self.bg_group.draw(self.screen)
        
        self.hero_group.update()
        self.hero_group.draw(self.screen)
        
        self.enemy_group.update()
        self.enemy_group.draw(self.screen)
        
        self.hero.bullet_group.update()
        self.hero.bullet_group.draw(self.screen)
        
        # self.enemy_group.add(Enemy())
    
    # 事件监听
    def handle_event(self):
        event_list = pygame.event.get()
        for event in event_list:
            if event in event_list:
                if event.type == pygame.QUIT:
                    print("游戏结束")
                    self.exit_game()
                if event.type == CRECT_ENEMY_EVENT:
                    # 一秒钟创建一个敌机
                    self.enemy_group.add(Enemy())
                    self.hero.fire()
                else:
                    print(" ")
            key_press = pygame.key.get_pressed()
            plan_speed = 5
            if key_press[pygame.K_RIGHT]:
                self.hero.speed += plan_speed 
                
            elif key_press[pygame.K_LEFT]:
                self.hero.speed -= plan_speed
            else:
                self.hero.speed =0
    def handle_collide(self):
        # pygame.sprite.groupcollide(self.hero.bullet_group, self.enemy_group, True, True)  
              
        # pygame.sprite.groupcollide(self.hero_group, self.enemy_group, True, True)  
        
        for enemy in self.enemy_group:
            # 返回碰撞精灵组
            bullets =  pygame.sprite.spritecollide(enemy, self.hero.bullet_group, False)
            
            for bullet in bullets:
                bullet.kill()
            # 返回状态给 敌机
            if bullets:
                enemy.activate = False
                    
        game_over = pygame.sprite.spritecollide(self.hero, self.enemy_group, False)
               
        if game_over:
            print("游戏结束")
            self.exit_game()
    def main(self):
        while True:
            self.clock.tick(50)
            # 更新游戏精灵
            self.update_sprite()
            # 监听游戏事件
            self.handle_event()
            self.handle_collide()
            pygame.display.update()
    
    @staticmethod
    def exit_game():
        pygame.quit()
        exit(0)
if __name__ == "__main__":
    game=Game()
    game.main()
        
    