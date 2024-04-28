"""
Function:
    其他工具函数

"""
import sys
import pygame

'''退出程序'''


def QuitGame(use_pygame=True):
    if use_pygame: pygame.quit()
    sys.exit()
