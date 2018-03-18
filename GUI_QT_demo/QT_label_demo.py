# coding:utf-8
"""
   label标签的使用：通过move实现绝对布局
"""
import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtWidgets import QLabel  # Label标签
from PyQt5.QtGui import QFont


class WindowLable(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 设置字体样式
        self.setFont(QFont('microsoft yahei', 10))
        # 设置窗体位置 和 尺寸
        self.setGeometry(350, 250, 400, 350)
        self.showLable()

    def showLable(self):
        """
        :brief  创建三个label标签，并通过move方法，改变标签的绝对位置
        :return: None
        """
        # label_1：one：标签的内容， self: 表示label标签属于WindowLable这个对象
        label_1 = QLabel('one', self)
        label_1.move(15, 10)
        # label_2
        label_2 = QLabel('two', self)
        label_2.move(35, 40)
        # label_3
        label_3 = QLabel('three', self)
        label_3.move(55, 70)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window_lable = WindowLable()
    window_lable.show()
    sys.exit(app.exec_())
