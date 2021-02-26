# -*- conding: utf-8 -*-
# author:Andy
# time:2020/7/29
import tkinter as tk

root = tk.Tk()
root.geometry('300x300+100+100')
# 设置图片为label背景
img1 = tk.PhotoImage(file = '../../images/enemy2.png')

# 所用的组件 第一个参数接收需要绑定的对象
label = tk.Label(root,
                 text = '组件学习',
                 background = '#de5151',# 设置背景颜色为灰色 # 设置显示的文字
                 image = img1, # 需要一个图片对象
                 font = ('宋体', 24),
                 width = '30', # 高度是以文字大小为单位
                 height = '5', #
                )
# 将组件布局到页面
label.pack()

# label2 = tk.Label(root, image = '')
root.mainloop()
