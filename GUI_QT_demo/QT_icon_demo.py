# coding:utf-8
"""
   修改窗口图标：setWindowIcon
"""
import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QIcon


class WindowIcon(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 设置窗口的位置，尺寸
        self.setGeometry(500, 250, 400, 400)
        # 窗口标题
        self.setWindowTitle('add icon')
        # 修改窗口图标
        self.setWindowIcon(QIcon('./ui_picture/ui-icon.jpg'))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window_icon = WindowIcon()
    window_icon.show()
    sys.exit(app.exec_())
