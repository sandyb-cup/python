# -*- conding: utf-8 -*-
# author:Andy
# time:2020/7/29
import sys
from PyQt5 import QtCore, QtGui, QtWigats

app = QtWigats.QApplication(sys.argv) # 创建一个app
widgetHello = QtWigats.QWidget()

widgetHello.resize(280, 150) # 设置窗口大小

widgetHello.setWindowTitle("Dome_2")

LabHello = QtWigats.QLabel(widgetHello) # 创建标签 夫容器为widgetHello
LabHello.setText("hello world pyQt5")

font = QtGui.QFont() # 设置字体大小
font.setBold(True) # 设置字体为粗体

LabHello.setFont(font) # 设置字体为LabHEllo字体

size = LabHello.sizeHint() # 获取LabHello合适大小
LabHello.setGeometry(70, 60, size.width(), size.height())

widgetHello.show() #显示对话框

sys.exit(app.exec_()) # 应用程序运行