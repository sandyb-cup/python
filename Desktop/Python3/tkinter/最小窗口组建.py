import tkinter as tk
root = tk.Tk()
root.title("hello python")

# 创建一个标签 把标签绑定到root中
text_text = tk.Label(root, text = "你好")

# 将内容贴到 root中
text_text.pack()
root.mainloop() 