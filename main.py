import pygame


from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

# Инициализация
pygame.init()

# Настройка окна рисования
# Определите константы для ширины и высоты экрана
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 300

# Создайте экранный объект
# Размер определяется постоянными параметрами SCREEN_WIDTH и SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))