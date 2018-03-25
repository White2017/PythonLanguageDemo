# coding:utf-8  fxb_qzyx@163.com
"""
   表格布局：QFormLayout
"""
import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtWidgets import QFormLayout  # 表格布局类
from PyQt5.QtWidgets import QLabel, QLineEdit


class WindowFormLayout(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Form Layout')
        self.resize(400, 400)
        form_layout = QFormLayout()
        # 创建标签
        title = self.createLabel('标题')
        author = self.createLabel('作者')
        comment = self.createLabel('评论')
        label_lst = [title, author, comment]

        # 创建单行文本框
        title_edit = QLineEdit()
        author_edit = QLineEdit()
        comment_edit = QLineEdit()
        edit_lst = [title_edit, author_edit, comment_edit]

        label_edit_lst = list(zip(label_lst, edit_lst))

        for label_edit in label_edit_lst:
            # 逐行添加标签 和 单行文本框
            form_layout.addRow(*label_edit)

        # 将表单布局添加为主布局
        self.setLayout(form_layout)

    def createLabel(self, label_name):
        """
        :brief :创建标签
        :param label_name:标签名
        :return: 返回标签对象
        """
        return QLabel(label_name)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window_formlayout = WindowFormLayout()
    window_formlayout.show()
    sys.exit(app.exec_())
