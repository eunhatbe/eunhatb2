import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.windowSize()

        self.statusBar().showMessage('Ready')
        self.statusBar()

        self.createMenuBar(menu_name='하이')
        self.createMenuBar()

        self.show()

    def windowSize(self):
        self.setWindowTitle('chat')
        self.setWindowIcon(QIcon('images/titleicon.png'))
        self.resize(600, 800)
        self.appPosition()

    def appPosition(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def createMenuBar(self, menu_name = "생성중"):
        exitAction = QAction(QIcon('images/exit.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit App')
        exitAction.triggered.connect(qApp.quit)

        menuBar = self.menuBar()
        menuBar.setNativeMenuBar(False)
        fileMenu = menuBar.addMenu(menu_name)
        fileMenu.addAction(exitAction)

    # exitAction 함수로 만들기
    # 메뉴버튼 안에 들어갈 것들을 함수화하기.
    # 하이 생성중 둘다 안에 exit이기 떄문에 이걸 수정해야함.
    def Action(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
