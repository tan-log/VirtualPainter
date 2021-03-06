from PyQt5.QtWidgets import QMainWindow, QWidget, QTabWidget, QVBoxLayout, QLabel, QFrame
from PyQt5.QtGui import QFont
from subscribe import Subscribe
from analyse import Analyse
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        MainWindow.setFixedSize(self,1700,950)
        self.init()

    def init(self):
        font = QFont()
        font.setPointSize(35)
        title = QLabel('可协作式画板')
        title.setFont(font)
        line = QFrame(self)
        line.setFrameShape(QFrame.HLine)
        line.setFrameShadow(QFrame.Plain)
        self.subscribe = Subscribe(self)
        self.analyse = Analyse(self)
        self.topic=""
        tab = QTabWidget(self)
        tab.addTab(self.subscribe, MainWindow.tr(self, '订阅'))
        tab.addTab(self.analyse, MainWindow.tr(self, '绘制'))
        tab.setStyleSheet("QTabWidget:pane {border-top:0px;background: transparent;}"
                          "QTabWidget::tab-bar{alignment:center;}")

        layout = QVBoxLayout()
        layout.addWidget(title, 0, Qt.AlignHCenter)
        layout.addWidget(line)
        layout.addWidget(tab)
        widget = QWidget(self)
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        self.setWindowTitle('可协作式画板')
        self.show()
