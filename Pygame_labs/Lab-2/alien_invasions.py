import pygame
import sys
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from time import sleep
from game_stats import GameStats
from button import Button
from bonuses import Bonus
import random
import resources

class AlienInvasion:
    """Класс для управления ресурсами и поведением игры"""

    def __init__(self):
        """Инициализирует и создаёт игровые ресурсы."""
        pygame.init()
        self.settings = Settings()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.stats = GameStats(self)

        self.ship = Ship(self.screen)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.bonuses = pygame.sprite.Group()
        self.effects = {}

        self._create_fleet()

        self.play_button = Button(self, "Play")


    def run_game(self):
        while True:
            keys = pygame.key.get_pressed()
            self._check_events()
            if self.stats.game_active:
                self.ship.update(keys)
                self._update_aliens()
                self._update_bullets()
                self._update_bonuses()
                self._update_effects()
            self._update_screen()
            self.clock.tick(self.settings.fps)

    def _create_fleet(self):
        """Создание флота вторжения"""

        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        available_space_x = self.settings.screen_width - (2 * alien_width)
        numbers_aliens_x = available_space_x // (2* alien_width)

        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)
        for row in range(number_rows):
            for i in range(numbers_aliens_x):
                self._create_alien(i, row)

    def _create_alien(self, i, row):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * i
        alien.rect.x = alien.x
        alien.rect.y = alien_height + 2 * alien_height * row
        self.aliens.add(alien)

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_s:
            if not self.stats.game_active:
                self._save()
        elif event.key == pygame.K_l:
            self._end_level()
            self._load()
        elif event.key == pygame.K_r:
            self._ship_hit()


    def _fire_bullet(self):
        """Создание нового снаряда и включение его в группу bullets"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)


    def _bonus_drop(self, alien):
        new_bonus = Bonus(self, alien)
        if random.randint(1, 20) == 20:
            self.bonuses.add(new_bonus)

    def _update_bonuses(self):
        self.bonuses.update()
        for bonus in self.bonuses.copy():
            if bonus.rect.top >= self.screen.get_height():
                self.bonuses.remove(bonus)
        self._check_ship_bonus_collision()

    def _update_effects(self):
        for effect in self.effects.copy():
            self.effects[effect] -= 1
            if self.effects[effect] <= 0:
                self.effects.pop(effect)

    def _update_screen(self):
        """Обновляет изображения на экране и отображает новый экран."""
        self.screen.fill(self.settings.bg_color)
        self.ship.render()
        for bullet in self.bullets.sprites():
            bullet.render()
        self.aliens.draw(self.screen)
        self.bonuses.draw(self.screen)
        if not self.stats.game_active:
            self.play_button.draw_button()

        pygame.display.flip()


    def _update_bullets(self):
        """Обновляет позиции снарядов и уничтожает старые снаряды."""
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        if self.effects.get("armor_shread", False):
            collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, False, True)
        else:
            collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        if collisions:
            for collision in collisions:
                self._bonus_drop(collisions[collision][0])
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()
            self.settings.level += 1
            self._end_level()

    def _update_aliens(self):
        self._check_fleet_edges()
        self.aliens.update()

        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        self._check_aliens_bottom()

    def _check_fleet_edges(self):
        """Реагирует на достижение пришельцем края экрана."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _ship_hit(self):
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1

            self.aliens.empty()
            self.bullets.empty()

            self._create_fleet()
            self.ship.center_ship()

            sleep(0.5)
        else:
            self.settings.level = 1
            self.stats.reset_stats()
            self._end_level()

    def _check_aliens_bottom(self):
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self._ship_hit()
                break

    def _check_play_button(self, mouse_pos):
        if self.play_button.rect.collidepoint(mouse_pos) and not self.stats.game_active:
            self.stats.game_active = True
            self.aliens.empty()
            self.effects.clear()
            self.bonuses.empty()
            self.bullets.empty()
            self._create_fleet()
            self.ship.center_ship()
            pygame.mouse.set_visible(False)

    def _save(self):
        import json
        data = {"level": self.settings.level, "ships": self.stats.ships_left}
        with open("data.json", "w") as file:
            file.write(json.dumps(data))

    def _load(self):
        import json

        with open("data.json", "r") as file:
            data = json.load(file)
            self.settings.level = data["level"]
            self.stats.ships_left = data["ships"]
            print(data)
            print(self.stats.ships_left)

    def _end_level(self):
        self.stats.game_active = False
        pygame.mouse.set_visible(True)

    def _check_ship_bonus_collision(self):
        collision = pygame.sprite.spritecollideany(self.ship, self.bonuses)
        if collision:
            self.effects[collision.type] = self.settings.boon_time
            self.bonuses.remove(collision)



if __name__ == '__main__':

    ai = AlienInvasion()
    ai.run_game()
