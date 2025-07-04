import pygame
import numpy
import os
from GameMap import Map
from Camera import Camera
from Config import *


class Game:
    def __init__(self):
        pygame.init()
        self.screen = self.setting_window()
        self.clock = pygame.time.Clock()
        self.size_map = MAP_SIZE_CELL
        self.game_map = Map(MAP_SIZE_CELL)

        self.camera = self.create_camera()
        self.fps = FPS

    @staticmethod
    def setting_window():
        screen_info = pygame.display.Info()
        w, h = screen_info.current_w, screen_info.current_h - 60

        screen = pygame.display.set_mode((w, h), pygame.RESIZABLE | pygame.SCALED)
        pygame.display.set_caption("Evolution Simulation")
        return screen

    @staticmethod
    def create_camera():
        screen_info = pygame.display.Info()
        w, h = screen_info.current_w, screen_info.current_h
        camera = Camera(MAP_SIZE_PIX, w, h)
        return camera

    def handle_events(self):
        # Обработка нажатий клавиш, мыши, выхода
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # если нажали ESC
                    return False
                elif event.key == pygame.K_d:
                    for cell in self.game_map.cells_sprite:
                        cell.toggle_border()
        return True

    def camera_move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.camera.move(-CAMERA_SPEED, 0)
        if keys[pygame.K_RIGHT]:
            self.camera.move(CAMERA_SPEED, 0)
        if keys[pygame.K_UP]:
            self.camera.move(0, -CAMERA_SPEED)
        if keys[pygame.K_DOWN]:
            self.camera.move(0, CAMERA_SPEED)
        for sprite in self.game_map.all_sprites:
            if self.camera.rect.colliderect(sprite):
                new_cell = self.camera.apply(sprite.rect)
                self.screen.blit(sprite.image, new_cell)

        new = self.camera.apply(self.game_map.border)
        self.game_map.draw_border_map(self.screen, new)

    def run(self):
        running = True
        while running:
            self.clock.tick(self.fps)  # FPS
            dt = self.clock.tick(self.fps) / 1000
            running = self.handle_events()
            self.camera_move()
            self.game_map.agent_sprite.update(dt)
            pygame.display.flip()

        pygame.quit()
