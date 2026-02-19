import pygame
from pygame.sprite import Sprite
import random
import resources

bonuses = ["armor_shread"]

class Bonus(Sprite):
    def __init__(self, ai_game, alien):
        """Инициализирует пришельца и задаёт его начальную позицию"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.type = random.choice(bonuses)
        self.image = pygame.image.load(resources.armor_shread)
        self.rect = self.image.get_rect()

        self.rect.midbottom = alien.rect.midbottom

        self.y = float(self.rect.y)

    def update(self):
        self.y += self.settings.bullet_speed
        self.rect.y = self.y
