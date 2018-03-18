# coding:utf-8
"""
   窗口的居中显示
"""
import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtWidgets import QDesktopWidget  # 桌面窗口类


class WindowCenter(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('窗口居中显示')
        self.resize(500, 450)
        self.center()

    def center(self):
        # 获取桌面屏幕对象
        screen = QDesktopWidget().screenGeometry()

        window_size = self.geometry()  # 获取客户区窗体对象(client area)

        # 获得包含边框的窗体对象(验证时，其实不包含边框, 即：和geometry()的效果一样 )
        # window_size = self.frameGeometry()

        center_width = (screen.width() - window_size.width()) / 2
        center_height = (screen.height() - window_size.height()) / 2
        self.move(center_width, center_height)

        print(self.geometry())
        print(self.frameGeometry())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window_center = WindowCenter()
    window_center.show()
    sys.exit(app.exec_())
