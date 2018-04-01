# coding:utf-8  fxb_qzyx@163.com
"""
   日历控件的使用：calendar
"""
import sys

from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtWidgets import QVBoxLayout, QLabel
from PyQt5.QtWidgets import QCalendarWidget  # 日期控件类
from PyQt5.QtCore import QDate


class WindowCalendar(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QT Calendar')
        self.resize(400, 350)

        # 创建日期控件对象
        self.calendar = QCalendarWidget(self)
        # 设置日历控件的日期最大/最小范围
        self.calendar.setMinimumDate(QDate(1900, 1, 1))
        self.calendar.setMaximumDate(QDate(5000, 1, 1))
        # 获取当前选定的时间
        date = self.calendar.selectedDate()
        # 给选定的日期绑定函数
        self.calendar.clicked[QDate].connect(self.showDate)

        # 创建标签对象
        self.label = QLabel()
        # 将当前时间显示到标签中
        self.label.setText(date.toString("yyyy-MM-dd dddd"))
        # 设置日历控件显示网格
        self.calendar.setGridVisible(True)
        # 创建垂直布局对象
        v_layout = QVBoxLayout()

        # 向垂直布局对象中添加控件
        v_layout.addWidget(self.calendar)
        v_layout.addWidget(self.label)

        # 将垂直布局对象添加到主控件中
        self.setLayout(v_layout)

    def showDate(self, selected_date):
        """
        :brief 接收传递的日期，并显示在标签中
        :param selected_date: 选定的日期
        :return: None
        """
        self.label.setText(selected_date.toString("yyyy-MM-dd dddd"))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window_calendar = WindowCalendar()
    window_calendar.show()
    sys.exit(app.exec_())
