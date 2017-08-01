from enum import Enum

from Singleton import *


class GameStage(Enum):
    Stopped = 4
    Yaoguaifaxian = 1
    Yunhun_dashe = 2


class GameStatus(metaclass=Singleton):
    def __init__(self):
        self.game_stage = None
        self.current_level = None
        self.cards = []
        self.window = None
        self.y = 989.0
        self.use_Droid4X = False
