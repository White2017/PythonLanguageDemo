# coding:utf-8
"""
   QGridLayout: 网格布局(多行多列)
"""
import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtWidgets import QPushButton, QGridLayout


class WindowGridLayOut(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 设置窗体标题
        self.setWindowTitle('Calculator')
        # 设置窗体位置
        self.move(300, 150)
        # 创建网格布局对象
        grid_layout = QGridLayout()
        # 按钮名称：5*4
        button_names = ['Calculator', 'Back', '', 'Close',
                        '7', '8', '9', '/',
                        '4', '5', '6', '*',
                        '1', '2', '3', '-',
                        '0', '.', '=', '+']

        # 按钮的位置：5*4
        button_positions = [(i, j) for i in range(5) for j in range(4)]

        for button_position, button_name in zip(button_positions, button_names):
            if button_name == "":
                continue
            # 创建按钮
            button = QPushButton(button_name)
            # 将按钮添加到网格布局中: *button_position：按钮在网格布局中的位置
            grid_layout.addWidget(button, *button_position)

        # 将网格布局(grid_layout)设置为窗体的主布局
        self.setLayout(grid_layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window_gridlayout = WindowGridLayOut()
    window_gridlayout.show()
    sys.exit(app.exec_())
