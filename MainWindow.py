# coding=utf-8

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QAction, QTextBrowser

from GameStatus import GameStatus, GameStage
from Screen import Screen
from worker import Worker


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.worker = None
        self.statusBar().showMessage('ready')
        self.resize(250, 150)
        self.move(300, 300)
        self.setWindowTitle('刷起来')
        self.setWindowIcon(QIcon('icon.ico'))
        self.imagesPath = "./images/tp14/"
        self.toolBar = self.addToolBar('')

        GameStatus().window = self

        yaoguaifaxian_action = QAction(QIcon('./images/ui/yaoguaifaxian.jpg'), '妖怪发现', self)
        yaoguaifaxian_action.triggered.connect(self.yaoguaifaxian)

        exit_action = QAction(QIcon('./images/ui/exit.png'), '停止', self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.triggered.connect(self.stop_loop)


        self.toolBar.addAction(yaoguaifaxian_action)
        self.toolBar.addAction(exit_action)

        txt = QTextBrowser()
        txt.setContentsMargins(5, 5, 5, 5)
        self.setCentralWidget(txt)
        self.show()

    def add_text(self, text):
        self.centralWidget().append(text)
        sb = self.centralWidget().verticalScrollBar()
        sb.setValue(sb.maximum())
        print(text)

    def closeEvent(self, *args, **kwargs):
        self.stop_loop()
        print("关闭程序")

    def status_changed(self):
        if self.worker is None:
            self.statusBar().showMessage("就绪。")
        elif self.worker.stopped():
            self.statusBar().showMessage("已停止。")
        else:
            self.statusBar().showMessage("当前次数： " + str(self.worker.cnt))

    def yaoguaifaxian(self):
        if self.worker is not None and not self.worker.stopped():
            return

        self.worker = Worker(self.imagesPath)
        GameStatus().game_stage = GameStage.Yaoguaifaxian
        self.worker.start()

    def stop_loop(self):
        if self.worker is None:
            return
        self.worker.stop()

