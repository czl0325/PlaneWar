import pygame
from GameSprite import *

class PlaneGame(object):
    def __init__(self):
        # 1. 创建游戏的窗口
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        # 2. 创建游戏的时钟
        self.clock = pygame.time.Clock()
        # 3. 调用私有方法，精灵和精灵组的创建
        self.__create_sprites()
        # 4. 设置定时器事件 - 创建敌机　1s
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)

    def __create_sprites(self):
        bg1 = Background()
        bg2 = Background(True)
        self.back_group = pygame.sprite.Group(bg1, bg2)
        # 创建敌机的精灵组
        self.enemy_group = pygame.sprite.Group()
        # 创建英雄的精灵和精灵组
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)

    def __event_handler(self):
        for event in pygame.event.get():
            # 判断是否退出游戏
            if event.type == pygame.QUIT:
                PlaneGame.__game_over(self)
            elif event.type == CREATE_ENEMY_EVENT:
                enemy = Enemy()
                self.enemy_group.add(enemy)

        # 使用键盘提供的方法获取键盘按键 - 按键元组
        keys_pressed = pygame.key.get_pressed()
        # 判断元组中对应的按键索引值 1
        if keys_pressed[pygame.K_RIGHT]:
            self.hero.speed = 5
        elif keys_pressed[pygame.K_LEFT]:
            self.hero.speed = -5
        else:
            self.hero.speed = 0

    def __check_collide(self):
        pass

    def __update_sprites(self):
        # 背景图精灵组刷新
        self.back_group.update()
        self.back_group.draw(self.screen)
        # 敌机精灵组刷新
        self.enemy_group.update()
        self.enemy_group.draw(self.screen)
        # 英雄精灵组刷新
        self.hero_group.update()
        self.hero_group.draw(self.screen)

    def start_game(self):
        while True:
            # 1. 设置刷新帧率
            self.clock.tick(60)
            # 2. 事件监听
            self.__event_handler()
            # 3. 碰撞检测
            self.__check_collide()
            # 4. 更新/绘制精灵组
            self.__update_sprites()
            # 5. 更新显示
            pygame.display.update()

    @staticmethod
    def __game_over(self):
        pygame.quit()
        exit()

if __name__ == '__main__':
    game = PlaneGame()
    game.start_game()