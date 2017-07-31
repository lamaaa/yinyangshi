# coding=utf-8

import threading
import time

from GameStatus import *
from Screen import Screen


class Worker(threading.Thread):
    def __init__(self):
        super().__init__()

        self._stop = threading.Event()
        self.cnt = 0
        GameStatus().window.status_changed()
        self.screen = Screen()
        self.do_loop = True

    def stop(self):
        GameStatus().game_stage = GameStage.Stopped
        self._stop.set()

    def stopped(self):
        return self._stop.is_set()

    def quit_on_complete(self):
        self.do_loop = False

    def fight(self):
        GameStatus().current_level = Screen().get_current_level()
        if GameStatus().current_level == 3:
            for key in Screen()._skills.get_all():
                while Screen().have(key, loader=Screen()._skills):
                    if GameStatus().game_stage == GameStage.Stopped:
                        return
                    Screen().click_on(key, loader=Screen()._skills)
                    time.sleep(2)
                    Screen().log('use ' + key)

        GameStatus().cards = []


        while len(GameStatus().cards) < 3:
            if self.stopped():
                return

            if Screen().have('atk_btn'):
                Screen().click_on('atk_btn')
                time.sleep(1)

                Screen().get_cards()

        for i in range(0, 3):
            x, y = GameStatus().cards[i]
            Screen()._click(x, y)
            time.sleep(Screen()._delay)

    def run(self):
        GameStatus().window.status_changed()
        screen = self.screen
        while self.do_loop:
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
            if screen.have('yaoguaifaxian_16'):
                screen.click_on('yaoguaifaxian_16')
            if screen.have('yaoguaifaxian_hard_unactive'):
                screen.click_on('yaoguaifaxian_hard_unactive')
                time.sleep(1)
            if screen.have('yaoguaifaxian_16'):
                screen
            if screen.have('yaoguaifaxian_hard_actived'):
                screen.click_on('yaoguaifaxian_explore', repeat=True)
                while True:
                    if screen.have('boss_fight'):
                        screen.click_on('boss_fight')
                    if screen.have('xiaoguai_fight'):
                        screen.click_on('xiaoguai_fight')
                    if screen.have('shoudong') or screen.have('zidong'):
                        screen.click_on('yaoguaifaxian_win', repeat=True)
                        screen.click_on('yaoguaifaxian_damo', repeat=True)
                        screen.click_on('yaoguaifaxian_damo1', repeat=True)
                    if screen.have('yaoguaifaxian_xiangzi'):
                        screen.click_on('yaoguaifaxian_xiangzi', repeat=True)
                        screen.click_on('yaoguaifaxian_huodejiangli', repeat=False, offset=(350, 350))
                    if screen.have('yaoguaifaxian_right'):
                        if direction == "right":
                            screen.click_on("yaoguaifaxian_right")
                            right_counter += 1
                        elif direction == "left":
                            screen.click_on("yaoguaifaxian_left")
                            left_counter += 1
                    if screen.have('yaoguaifaxian_over'):
                        break

                # GameStatus().game_stage = GameStage.Fighting

            # elif GameStatus().game_stage == GameStage.Fighting:
            #     # attack
            #     # 选3张卡 循环
            #
            #     while not screen.have('jiban'):
            #         if self.stopped():
            #             return
            #
            #         if screen.have('atk_btn'):
            #             self.fight()
            #         elif screen.have('network_error'):
            #             screen.click_on('retry')
            #         else:
            #             time.sleep(0.5)
            #
            #             GameStatus().game_stage = GameStage.AfterFight
            #
            # elif GameStatus().game_stage == GameStage.AfterFight:
            #
            #     # 点击 羁绊
            #     screen.click_on('jiban', repeat=True)
            #
            #     if screen.have('lvup'):
            #         screen.click_on('lvup', repeat=True)
            #
            #     if screen.have('jibanup'):
            #         screen.click_on('jibanup', repeat=True)
            #
            #     # 点击exp
            #     screen.click_on('exp', repeat=True)
            #
            #     if screen.have('lvup'):
            #         screen.click_on('lvup', repeat=True)
            #
            #     screen.click_on('xiayibu')
            #     self.cnt += 1
            #     GameStatus().window.status_changed()
            #     GameStatus().window.add_text("---战斗 %s 完成 历时 %s 秒 ---" % (self.cnt, time.time() - start_time))
            #     GameStatus().game_stage = GameStage.BeforeFight
            #
            # elif GameStatus().game_stage == GameStage.Stopped:
            #     break
            # else:
            #     raise RuntimeError('Unknown Status')
