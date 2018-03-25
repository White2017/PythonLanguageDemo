# coding:utf-8  fxb_qzyx@163.com
"""
   多行文本框的使用：QTextEdit
"""
import sys

from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtWidgets import QPushButton, QVBoxLayout
from PyQt5.QtWidgets import QTextEdit  # 多行文本框
from threading import Thread


class WindowTextEdit(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('多行文本框-QTextEdit')
        self.resize(450, 450)
        # 垂直布局对象
        H_layout = QVBoxLayout()
        # 多行文本框
        self.text_edit = QTextEdit()
        # 按钮1
        btn_1 = QPushButton('显示一般文本')
        btn_1.clicked.connect(self.show_text)
        # 按钮2
        btn_2 = QPushButton('显示网页文本')
        btn_2.clicked.connect(self.show_html_test)

        # 垂直布局对象添加控件
        H_layout.addWidget(self.text_edit)
        H_layout.addWidget(btn_1)
        H_layout.addWidget(btn_2)

        self.setLayout(H_layout)

    def show_text(self):
        """显示普通文本"""
        self.text_edit.setPlainText("显示普通文本\n多行文本框")

    def show_html_test(self):
        """显示网页文本"""
        self.text_edit.setHtml("<font color='gray' size='6'>网页版文本框<br/>多行文本框</font>")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window_textedit = WindowTextEdit()
    window_textedit.show()
    sys.exit(app.exec_())
