import pygame
import numpy as np


class Camera:
    def __init__(self, size_map, screen_width, screen_height):
        self.width, self.height = size_map  # ширина и высота карты в пикселях
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.x = 0  # смещение камеры по X
        self.y = 0  # смещение камеры по Y
        self.rect = pygame.Rect(self.x, self.y, self.screen_width, self.screen_height)

    def move(self, dx, dy):
        self.x += dx  # сдвинуть камеру по горизонтали
        self.y += dy  # сдвинуть камеру по вертикали

        # ограничить движение камеры по X, чтобы не уйти за левый и правый край карты
        self.x = max(0, min(self.x, self.width - self.screen_width))
        # ограничить движение камеры по Y, чтобы не уйти за верхний и нижний край карты
        self.y = max(0, min(self.y, self.height - self.screen_height))

        self.rect.topleft = (self.x, self.y)

    def apply(self, rect):
        # Возвращает новый rect с учётом камеры
        return rect.move(-self.x, -self.y)
