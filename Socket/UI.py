import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    # UI 실행
    def initUI(self):
        self.window_size()

        self.statusBar().showMessage('Ready')
        self.statusBar()

        self.create_menubar(menu_name='하이')
        self.create_menubar()

        self.show()

    # 윈도우 크기
    def window_size(self):
        self.setWindowTitle('chat')
        self.setWindowIcon(QIcon('images/titleicon.png'))
        self.resize(600, 800)
        self.app_position()

    # 윈도우 생성 위치
    def app_position(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def create_menubar(self, menu_name = "생성중"):
        exit_action = QAction(QIcon('images/exit.png'), 'Exit', self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.setStatusTip('Exit App')
        exit_action.triggered.connect(qApp.quit)

        menu_bar = self.menuBar()
        menu_bar.setNativeMenuBar(False)
        file_menu = menu_bar.addMenu(menu_name)
        file_menu.addAction(exit_action)

    # exitAction 함수로 만들기
    # 메뉴버튼 안에 들어갈 것들을 함수화하기.
    # 하이 생성중 둘다 안에 exit이기 떄문에 이걸 수정해야함.
    def action(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
