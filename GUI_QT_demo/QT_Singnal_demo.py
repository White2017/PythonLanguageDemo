# coding:utf-8  fxb_qzyx@163.com
"""
   1.pyqt自定义信号槽：pyqtSignal
   补充说明：QApplication.processEvents()
        1.processEvents：事件处理程序，其作用是刷新页面；
        2.常见用法：若存在阻塞主线程的代码，则可使用该语句来实时刷新界面，让界面看起来很流畅。
"""
import sys
from threading import Thread
import time
from PyQt5.QtGui import QTextCursor
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtWidgets import QPushButton, QTextEdit, QVBoxLayout
from PyQt5.QtCore import QObject, pyqtSignal  # 自定义信号槽的类


class CustomSignal(QObject):
    sin_out = pyqtSignal(str)

    def write(self, data_str):
        """将数据发送到控件"""
        self.sin_out.emit(data_str)  # 将字符串数据data_str发送出去


class WindowDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        # 将print的信息重定向
        sys.stdout = CustomSignal(sin_out=self.wirteDataToTextEdit)
        sys.stderr = CustomSignal(sin_out=self.wirteDataToTextEdit)

    def wirteDataToTextEdit(self, text):
        """将text的内容写入到多行文本框(text_edit)中"""
        # 获取多行文本指针对象
        cursor_obj = self.text_edit.textCursor()
        # 将文本指针移动到文本末尾
        cursor_obj.movePosition(QTextCursor.End)
        # 在文本末尾插入数据
        cursor_obj.insertText(text)

        # 将插入文本后的文本指针对象重新赋值给text_ddit(手动更新)
        # The QTextEdit's textCursor() method returns a COPY of its cursor,
        # not the real one so we have to set it with setTextCursor() method.
        self.text_edit.setTextCursor(cursor_obj)

    def initUI(self):
        self.setWindowTitle('pysingnal')
        self.resize(550, 500)
        # 创建垂直布局对象
        v_layout = QVBoxLayout()
        # 创建多行文本框
        self.text_edit = QTextEdit()
        # 创建开始按钮
        self.start_btn = QPushButton('start')
        self.start_btn.clicked.connect(self.showData)
        # 将控件添加到垂直布局对象中
        v_layout.addWidget(self.text_edit)
        v_layout.addWidget(self.start_btn)
        # 添加为主布局
        self.setLayout(v_layout)

    def showData(self):
        """创建线程，调用打印数据的方法 """
        # 创建线程
        t = Thread(target=self.printData)
        t.start()

    def printData(self):
        """打印数据 """
        for i in range(100):
            print(i)
            time.sleep(1)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window_demo = WindowDemo()
    window_demo.show()
    sys.exit(app.exec())
