# Импорт модулей
import pygame
import random
import time

# Инициализация Pygame
pygame.init()

# Константы
SCREEN_SIZE = 400
GRID_SIZE = 4
SQUARE_SIZE = SCREEN_SIZE // GRID_SIZE
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GRAY = (200, 200, 200)

# Настройки дисплея
screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
pygame.display.set_caption("Подсветка случайных квадратов")

