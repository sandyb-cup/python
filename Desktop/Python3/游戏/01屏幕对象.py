import pygame

# 初始化pygame模块
pygame.init() # 需要显示内存  

# 获取屏幕对象

screen = pygame.display.set_mode((480, 700))

# 把窗口显示到屏幕
bg = pygame.image.load('/Users/sandy/Desktop/Python3/woman_face.jpeg')
screen.blit(bg, (0, 0))

# 使绘制的内容显示到屏幕
pygame.display.update()

input('输入内容:')

screen.quit()


# 使用英雄的位置信息创建一个矩形对象 来控制英雄
hero_rect = pygame.Rect( )


# 英雄对象
bg = pygame.image.load('/Users/sandy/Desktop/Python3/woman_face.jpeg')
screen.blit(bg, hero_rect)