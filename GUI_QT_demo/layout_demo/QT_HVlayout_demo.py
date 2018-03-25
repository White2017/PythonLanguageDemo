# coding:utf-8
"""
   水平布局：QHBoxLayout
   垂直布局：QVBoxLayout
   布局的嵌套：setLayout
   布局中添加控件：addWidget
"""
import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtWidgets import QPushButton  # 按钮
from PyQt5.QtWidgets import QHBoxLayout  # 水平放置控件的布局类
from PyQt5.QtWidgets import QVBoxLayout  # 垂直放置控件的布局类


class WindowLayout(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 设置窗体的位置 和 尺寸
        self.setGeometry(350, 250, 400, 300)
        # 创建OK按钮
        self.ok_button = QPushButton('OK')
        # 创建Cancel按钮
        self.cancel_button = QPushButton('cancel')

        self.HVLayout()

    def HVLayout(self):
        # 创建一个水平布局对象
        h_box = QHBoxLayout()
        # 添加伸展系数，按钮将被挤到右侧
        h_box.addStretch(1)
        # h_box水平布局对象，添加OK按钮
        h_box.addWidget(self.ok_button)
        # h_box水平布局对象，添加Cancel按钮
        h_box.addWidget(self.cancel_button)

        # 创建一个垂直布局对象
        v_box = QVBoxLayout()
        # 添加伸展系数，按钮将被挤到窗体底部
        v_box.addStretch(1)
        # 将水平布局h_box置于垂直布局v_box内
        v_box.addLayout(h_box)

        # 将v_box设置为窗体的主布局
        self.setLayout(v_box)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window_layout = WindowLayout()
    window_layout.show()
    sys.exit(app.exec_())
