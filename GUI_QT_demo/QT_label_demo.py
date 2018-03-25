# coding:utf-8
"""
   label标签的作用：作为一个占位符，可以显示不可编辑的文本或图片，也可放置一个gif动画，
                   纯文本、链接或富文本可以显示在标签上
   label标签的使用：通过move实现绝对布局
"""
import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtWidgets import QLabel  # Label标签
from PyQt5.QtGui import QFont  # 设置字体
from PyQt5.QtGui import QPixmap  # 设置Qlabel为一个Pixmap


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
        label_1 = QLabel(self)
        label_1.setText('这是一个文本标签')
        label_1.move(15, 10)

        # label_2
        label_2 = QLabel(self)
        # 超链接文本
        label_2.setText("<a href='http://pyqt.sourceforge.net/Docs/PyQt5/index.html_file'>python GUI</a>")
        # 表示能够访问该超链接
        label_2.setOpenExternalLinks(True)
        label_2.move(35, 40)

        # label_3
        label_3 = QLabel(self)
        label_3.setToolTip('这是一张图片标签')
        # 将标签填充为图片
        label_3.setPixmap(QPixmap('./ui_picture/ui-icon.jpg'))
        label_3.move(55, 70)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window_lable = WindowLable()
    window_lable.show()
    sys.exit(app.exec_())
