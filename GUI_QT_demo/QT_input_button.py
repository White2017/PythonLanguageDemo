# coding:utf-8
"""
    按钮 / 单行输入框 / 输入对话框 控件
"""
import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtWidgets import QLineEdit  # 单行输入框
from PyQt5.QtWidgets import QInputDialog  # 输入对话框
from PyQt5.QtWidgets import QPushButton  # 按钮


class WindowInput(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 设置窗口的位置、尺寸
        self.setGeometry(300, 300, 290, 150)
        # 设置窗口的标题
        self.setWindowTitle('Input dialog')
        # 添加单行输入框
        self.showLineEdit()
        # 添加按钮
        self.showbtn()

    def showLineEdit(self):
        """
        brief :1.创建单行输入框; 2.设置单行输入框的位置
        :return:None
        """
        self.line_edit = QLineEdit(self)
        self.line_edit.move(130, 22)

    def showbtn(self):
        """
        breif :1.创建按钮; 2.给按钮添加点击事件
        :return: None
        """
        self.btn = QPushButton('button', self)
        self.btn.move(20, 20)
        # 按钮的点击事件
        self.btn.clicked.connect(self.showDialog)

    def showDialog(self):
        """
        breif :1.创建输入对话框； 2.将对话框的文本写入到单行文本框中
        :return:None
        """
        text, ok = QInputDialog.getText(self, 'Input Dialog', 'Enter your emassage:')
        print(ok)

        if text.strip() and ok:
            # 将对话框的文本写入单行文本框中
            self.line_edit.setText(str(text))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window_inout = WindowInput()
    window_inout.show()
    sys.exit(app.exec_())
