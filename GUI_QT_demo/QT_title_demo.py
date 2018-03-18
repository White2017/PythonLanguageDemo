# coding:utf-8
"""
   通过pyqt5创建GUI程序，并添加窗口标题
"""
import sys
from PyQt5.QtWidgets import QWidget, QApplication


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("first GUI")
        # 设置窗口尺寸
        self.resize(450, 500)


if __name__ == "__main__":
    # 创建应用
    app = QApplication(sys.argv)
    # 实例化窗体对象
    my_window = MyWindow()
    # 显示窗口
    my_window.show()
    # 监听窗口的事件，直到退出
    sys.exit(app.exec_())
