import pygame
# 初始化pygame模块
pygame.init() # 需要显示内存  

# 获取屏幕对象

screen = pygame.display.set_mode((480, 700))

bg_rect = pygame.Rect((0, 0, 480, 700))
# 把窗口显示到屏幕
bg = pygame.image.load('/Users/sandy/Desktop/Python3/green.jpg')

# 使绘制的内容显示到屏幕
# pygame.display.update()



# 使用英雄的位置信息创建一个矩形对象 来控制英雄
hero_rect = pygame.Rect((120, 350, 20, 20))
# 英雄对象
hero = pygame.image.load('/Users/sandy/Desktop/Python3/QQ.png')

clock = pygame.time.Clock()
i = 0
while True:
    """
    游戏循环 英雄位置发生改变，然后把英雄绘制到屏幕对象 更新显示对象
    """
    # 屏幕刷新频率
    clock.tick(30)
    
    screen.blit(bg, bg_rect) 
    hero_rect.y -= 2
    screen.blit(hero, hero_rect)
    clock.tick(30)
    event_info = pygame.event.get()
    pygame.display.update()
    # 记录键盘事件
    # for i in event_info:
    #     if i == pygame.QUIT:
    #         pygame.quit()
    # 专门处理事件的方法,获取的是一个列表
    key_press = pygame.key.get_pressed()
    print(key_press)

    