# coding=utf-8

import threading
import time

from GameStatus import *
from Screen import Screen
from ImageLoader import ImageLoader


class Worker(threading.Thread):
    def __init__(self, imagesPath):
        super().__init__()

        self._stop = threading.Event()
        self.cnt = 0
        GameStatus().window.status_changed()
        self.screen = Screen()
        self.do_loop = True
        self.imagesPath = imagesPath

    def stop(self):
        GameStatus().game_stage = GameStage.Stopped
        self._stop.set()

    def stopped(self):
        return self._stop.is_set()

    def run(self):
        GameStatus().window.status_changed()
        screen = self.screen
        yaoguaifaxain_loader = ImageLoader(self.imagesPath + "yaoguaifaxian/")
        while self.do_loop:
            while GameStatus().game_stage == GameStage.Yaoguaifaxian:
                time.sleep(3)
                left_counter = 0
                right_counter = 0
                direction = "right"

                if left_counter == 10:
                    left_counter = 0
                    direction = "right"
                if right_counter == 10:
                    right_counter = 0
                    direction = "left"
                if screen.have('yaoguaifaxian_16', loader=yaoguaifaxain_loader):
                    screen.click_on('yaoguaifaxian_16', loader=yaoguaifaxain_loader)
                if screen.have('yaoguaifaxian_hard_unactive', loader=yaoguaifaxain_loader):
                    screen.click_on('yaoguaifaxian_hard_unactive', loader=yaoguaifaxain_loader)
                    time.sleep(1)
                if screen.have('yaoguaifaxian_16', loader=yaoguaifaxain_loader):
                    screen.click_on('yaoguaifaxian_16', loader=yaoguaifaxain_loader)
                if screen.have('yaoguaifaxian_hard_actived', loader=yaoguaifaxain_loader):
                    screen.click_on('yaoguaifaxian_explore', repeat=True, loader=yaoguaifaxain_loader)
                    time.sleep(3)
                    while True:
                        if screen.have('yaoguaifaxian_unlock', loader=yaoguaifaxain_loader):
                            screen.click_on('yaoguaifaxian_unlock', loader=yaoguaifaxain_loader)
                        if screen.have('yaoguaifaxian_boss_fight', loader=yaoguaifaxain_loader):
                            screen.click_on('yaoguaifaxian_boss_fight', loader=yaoguaifaxain_loader)
                            time.sleep(2)
                        if screen.have('yaoguaifaxian_xiaoguai_fight', loader=yaoguaifaxain_loader):
                            screen.click_on('yaoguaifaxian_xiaoguai_fight', loader=yaoguaifaxain_loader)
                            time.sleep(2)
                        if screen.have('shoudong', loader=yaoguaifaxain_loader) or screen.have('zidong', loader=yaoguaifaxain_loader) or screen.have('zhunbei', loader=yaoguaifaxain_loader):
                            while True:
                                if screen.have('zhunbei', loader=yaoguaifaxain_loader):
                                    screen.click_on('zhunbei', repeat=True, loader=yaoguaifaxain_loader)
                                if screen.have('shoudong', loader=yaoguaifaxain_loader):
                                    screen.click_on('shoudong', repeat=True, loader=yaoguaifaxain_loader)
                                if screen.have('yaoguaifaxian_win', loader=yaoguaifaxain_loader):
                                    screen.click_on('yaoguaifaxian_win', repeat=True, loader=yaoguaifaxain_loader)
                                    screen.click_on('yaoguaifaxian_damo', repeat=True, loader=yaoguaifaxain_loader)
                                    screen.click_on('yaoguaifaxian_damo1', repeat=True, loader=yaoguaifaxain_loader)
                                    break
                                elif screen.have('yaoguaifaxian_lose', loader=yaoguaifaxain_loader):
                                    screen.click_on('yaoguaifaxian_lose', repeat=True, loader=yaoguaifaxain_loader)
                                    break
                        if screen.have('yaoguaifaxian_xiangzi', loader=yaoguaifaxain_loader):
                            screen.click_on('yaoguaifaxian_xiangzi', repeat=True, loader=yaoguaifaxain_loader)
                            screen.click_on('yaoguaifaxian_huodejiangli', repeat=False, loader=yaoguaifaxain_loader, offset=(-350, 350))
                        if screen.have('yaoguaifaxian_right', loader=yaoguaifaxain_loader):
                            if direction == "right":
                                screen.click_on("yaoguaifaxian_right", loader=yaoguaifaxain_loader)
                                time.sleep(1.5)
                                right_counter += 1
                            elif direction == "left":
                                screen.click_on("yaoguaifaxian_left", loader=yaoguaifaxain_loader)
                                time.sleep(1.5)
                                left_counter += 1
                        if screen.have('yaoguaifaxian_over', loader=yaoguaifaxain_loader):
                            break

