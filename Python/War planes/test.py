from plane_sprites import *
import pygame

pygame.init()

# 创建游戏的窗口 480 * 700
screen = pygame.display.set_mode((480, 700))

# 绘制背景图像
# 1> 加载图像数据
bg = pygame.image.load("./images/background.png")
# 2> blit 绘制图像
screen.blit(bg, (0, 0))
# 3> update 更新屏幕显示
# pygame.display.update()

# 绘制英雄的飞机
hero = pygame.image.load("./images/me1.png")
screen.blit(hero, (200, 500))
pygame.display.update()

# 创建时钟对象
clock = pygame.time.Clock()

# 定义rect记录飞机的初始位置
hero_rect = pygame.Rect(150, 300, 102, 126)

# 创建敌机的精灵
enemy = GameSprite("./images/enemy1.png")
enemy1 = GameSprite("./images/enemy1.png", 2)

# 创建敌机的精灵组
enemy_group = pygame.sprite.Group(enemy, enemy1)

while True:
    # 可以指定循环体内部的代码执行的频率
    clock.tick(60)
    # 捕获事件
    # event_list = pygame.event.get()
    # if len(event_list) > 0:
    #     print(event_list)

    # 监听事件
    for event in pygame.event.get():
        # 判断事件类型是否是退出事件
        if event.type == pygame.QUIT:
            print("游戏退出...")
            # quit 卸载所有的模块
            pygame.quit()
            # exit() 直接终止当前正在执行的程序
            exit()
    # 修改飞机的位置
    hero_rect.y -= 1
    # 判断飞机的位置
    if hero_rect.y + hero_rect.height <= 0:
        hero_rect.y = 700

    # 调用bilt方法绘制图像
    screen.blit(bg, (0, 0))
    screen.blit(hero, hero_rect)

    # 让精灵组调用两个方法
    # update-让组中的所有精灵更新位置
    enemy_group.update()
    #  draw-在screen上绘制所有的精灵
    enemy_group.draw(screen)
    # 调用update方法更新显示
    pygame.display.update()

    # event = pygame.event.poll()
    # if event.type == pygame.QUIT:
    #     pygame.quit()
    #     exit()

pygame.quit()
