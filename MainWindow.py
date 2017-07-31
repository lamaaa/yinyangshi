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

        self.toolBar = self.addToolBar('')

        GameStatus().window = self

        loop_action = QAction(QIcon('./images/ui/loop.png'), 'Loop', self)
        loop_action.triggered.connect(self.start_loop)

        continue_action = QAction(QIcon('./images/ui/continue.png'), 'Continue', self)
        continue_action.triggered.connect(self.continue_loop)

        once_action = QAction(QIcon('./images/ui/one.jpg'), 'Once', self)
        once_action.triggered.connect(self.quit_on_complete)

        exit_action = QAction(QIcon('./images/ui/exit.png'), 'Exit', self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.triggered.connect(self.stop_loop)

        inspect_action = QAction(QIcon('./images/ui/inspect.jpg'), 'Inspect', self)
        inspect_action.triggered.connect(self.inspect)

        self.toolBar.addAction(loop_action)
        self.toolBar.addAction(continue_action)
        self.toolBar.addAction(once_action)
        self.toolBar.addAction(exit_action)
        self.toolBar.addAction(inspect_action)

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

    def start_loop(self):
        if self.worker is not None and not self.worker.stopped():
            return

        self.worker = Worker()
        GameStatus().game_stage = GameStage.BeforeFight
        self.worker.start()

    def continue_loop(self):
        if self.worker is not None and not self.worker.stopped():
            return

        self.worker = Worker()
        GameStatus().game_stage = GameStage.Fighting
        self.worker.start()

    def stop_loop(self):
        if self.worker is None:
            return
        self.worker.stop()

    def quit_on_complete(self):
        if self.worker is None:
            return
        self.worker.quit_on_complete()

    def inspect(self):
        Screen().get_cards()
