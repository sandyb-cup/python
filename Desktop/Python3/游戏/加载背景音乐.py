import pygame

pygame.init()

# 加载背景音乐
pygame.mixer.music.load("/Users/sandy/Desktop/Python3/sound/game_music.ogg")

# 设置音乐大小
pygame.mixer.music.set_volume(0.1)
pygame.display.set_mode((500, 700))
pygame.mixer.music.play(-1)
while True:
    pygame.display.update()
