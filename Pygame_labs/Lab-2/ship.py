import pygame

import resources


class Ship():
    """Класс управления кораблём."""

    def __init__(self, screen):
        """Инициализирует корабль и задаёт его начальную позицию"""

        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.image = pygame.image.load(resources.spaceship)
        self.rect = self.image.get_rect()
        self.center_ship()
        self.speed = 3
    def update(self, keys):
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if self.rect.right < self.screen_rect.right:
            self.rect.x += self.speed
        if self.rect.left > 0:
            self.rect.x -= self.speed

    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

    def render(self):
        """Рисует корабль в текущей позиции"""
        self.screen.blit(self.image, self.rect)
