# -*- coding: utf-8 -*-
"""
@Time ： 2022/12/17 15:09
@Auth ： gw
@File ：main.py
@IDE ：PyCharm
"""
import warnings

if __name__ == '__main__':
    from core import *
else:
    from .core import *
warnings.filterwarnings('ignore')

'''Python实用工具集'''


class Games():
    def __init__(self, **kwargs):
        for key, value in kwargs.items(): setattr(self, key, value)
        self.supported_games = self.initialize()

    '''执行程序'''

    def execute(self, game_type=None, config={}):
        assert game_type in self.supported_games, 'unsupport game_type %s...' % game_type
        client = self.supported_games[game_type](**config)
        client.run()

    '''初始化'''

    def initialize(self):
        supported_games = {
            'footballGame': FootballGame,
        }
        return supported_games

    '''获得游戏信息'''

    def getallsupported(self):
        all_supports = {}
        for key, value in self.supported_games.items():
            all_supports[value.game_type] = key
        return all_supports

    '''str'''

    def __str__(self):
        return 'games made by python'


'''run'''
if __name__ == '__main__':
    games_client = Games()
    games_client.execute('footballGame')
