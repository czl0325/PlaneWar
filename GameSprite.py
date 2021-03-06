import random
import pygame

# 游戏窗口的尺寸
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
# 创建敌机的事件
CREATE_ENEMY_EVENT = pygame.USEREVENT
# 英雄发射子弹事件
HERO_FIRE_EVENT = pygame.USEREVENT + 1


class GameSprite(pygame.sprite.Sprite):
    def __init__(self, image_name, speed=1):
        super().__init__()
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self, *args):
        self.rect.y += self.speed


class Background(GameSprite):
    def __init__(self, is_alt=False):
        super().__init__("./images/background.png")
        if is_alt:
            self.rect.y = -self.rect.height

    def update(self, *args):
        super().update()
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.bottom = 0


class Enemy(GameSprite):
    def __init__(self):
        super().__init__("./images/enemy1.png")
        self.rect.bottom = 0
        self.speed = random.randint(2, 5)
        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0, max_x)

    def update(self, *args):
        super().update()
        if self.rect.y >= SCREEN_RECT.height:
            self.kill()

    def __del__(self):
        pass


class Hero(GameSprite):
    def __init__(self):
        super().__init__("./images/hero.png")
        self.rect.bottom = SCREEN_RECT.height - 10
        self.rect.centerx = SCREEN_RECT.centerx
        self.speed = 0
        self.bullets = pygame.sprite.Group()

    def update(self, *args):
        self.rect.x += self.speed
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.right > SCREEN_RECT.width:
            self.rect.right = SCREEN_RECT.width

    def fire(self):
        bullet = Bullet()
        bullet.rect.bottom = self.rect.y
        bullet.rect.centerx = self.rect.centerx
        self.bullets.add(bullet)


class Bullet(GameSprite):
    def __init__(self):
        super().__init__("./images/bullet1.png", -3)

    def update(self, *args):
        super().update()
        if self.rect.bottom <= 0:
            self.kill()