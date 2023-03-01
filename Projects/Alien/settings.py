class Settings:
    """储存游戏中所有设置的类"""

    def __init__(self):
        """初始化游戏的设置"""
        # 屏幕设置
        self.screen_wigth = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.ship_speed = 1.5