import pygame
import random

# Инициализация Pygame
pygame.init()

# Константы
SCREEN_SIZE = 300
GRID_SIZE = 3
SQUARE_SIZE = SCREEN_SIZE // GRID_SIZE
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GRAY = (200, 200, 200)

# Настройки дисплея
screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
pygame.display.set_caption("Нажми на правильный квадрат")