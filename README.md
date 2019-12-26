# PlaneWar
飞机大战游戏，使用python的pygame开发



### pygame开发步骤

##### 1. init初始化

```
# 1. 创建游戏的窗口
self.screen = pygame.display.set_mode(SCREEN_RECT.size)
# 2. 创建游戏的时钟
self.clock = pygame.time.Clock()
```

##### 2. 游戏循环

```
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
```