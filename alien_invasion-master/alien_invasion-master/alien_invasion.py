# -*- coding: utf-8 -*

import game_functions
import pygame
from settings import Settings
from ship import Ship


def run_game():
    pygame.init()  # 初始化pygame
    ai_settings = Settings()  # 创建设置实例
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
    )  # 设置屏幕
    pygame.display.set_caption("Alien Invasion")  # 设置标题
    ship = Ship(ai_settings, screen)  # 创建飞船实例

    # 开始游戏的主循环
    while True:
        game_functions.check_events(ship)  # 检测按键事件
        ship.update()  # 更新飞船位置
        game_functions.update_screen(ai_settings, screen, ship)  # 更新屏幕


run_game()
