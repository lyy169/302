import sys

import pygame


# 导入模块sys和pygame。模块pygame包含开发游戏所需的功能。玩家退出时，我们将使用模块sys中的工具来退出游戏


class AlienInvasion:
    """管理游戏资源和行为的类"""

    def __init__(self):
        """初始化游戏并创建游戏资源"""
        pygame.init()  # 初始化背景设置

        self.screen = pygame.display.set_mode((1200, 800))  # 创建一个显示窗口,将这个显示窗口赋给属性self.screen，让这个类中的所有方法都能够使用它
        pygame.display.set_caption("Alien Invasion")

        # 设置背景色
        self.bg_color = (230, 230, 230)

    def run_game(self):
        """开始游戏的主循环"""
        while True:
            # 监视键盘和鼠标事件

            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # 当玩家单击游戏窗口的关闭按钮时，将检测到pygame.QUIT事件，进而调用sys.exit()来退出游戏
                    sys.exit()

            # 每次循环时都重绘屏幕。
            self.screen.fill(self.bg_color)

            # 让最近绘制的屏幕可见
            pygame.display.flip()  # 每次执行while循环时都绘制一个空屏幕，并擦去旧屏幕，使得只有新屏幕可见


if __name__ == '__main__':
    # 创建游戏实例并运行游戏
    ai = AlienInvasion()
    ai.run_game()

# 在这个文件末尾，创建一个游戏实例并调用run_game()。这些代码放在一个if代码块中，仅当直接运行该文件时，它们才会执行。
# 如果此时运行alien_invasion.py，将看到一个空的Pygame窗口。
