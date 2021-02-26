import tkinter as tk

def create_button(root):
    # 创建一个按钮组件
    # fg 是 foreground的缩写 就是设置前景颜色的意思 command 点击触发键
    say_hello = tk.Button(root, text = "打招呼", fg = "blue", command = eat)
    say_hello.pack()
    return root

def eat():
    print('你吃饭了吗?')

# 创建一个窗口
root = tk.Tk()
app = create_button(root)

# 显示窗口 进入窗口的循环 使其不显示一次就结束 
root.mainloop()

    