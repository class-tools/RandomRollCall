import ctypes
import tkinter as tk
from tkinter.messagebox import showinfo
import random

def Show_About():
    showinfo(title = Lang_Menu_About, message = Lang_Messagebox_Message)

def label_click_handler(events):
    selected = random.randint(1, 49)
    label_obj1['text'] = selected

# Language
syslang = hex(ctypes.windll.kernel32.GetSystemDefaultUILanguage())
Lang_Title = ""
Lang_Menu_About = ""
Lang_Menu_Quit = ""
Lang_Messagebox_Message = ""
if syslang == '0x804':
    Lang_Title = u"随机点名"
    Lang_Menu_About = u"关于"
    Lang_Menu_Quit = u"退出"
    Lang_Messagebox_Message = u"本软件使用 MIT 开源软件协议，开发者为 Yuchen Ren。\nGithub 存储库地址：https://github.com/ren-yc/RandomRollCall"
else:
    Lang_Title = u"RandomRollCall"
    Lang_Menu_About = u"About"
    Lang_Menu_Quit = u"Quit"
    Lang_Messagebox_Message = u"This program uses MIT License, Developer: Yuchen Ren.\nGithub Repo: https://github.com/ren-yc/RandomRollCall"

# Init
root = tk.Tk()

# Menubar
menubar = tk.Menu(root)
root['menu'] = menubar
menubar.add_command(label = Lang_Menu_About, command = Show_About)
menubar.add_command(label = Lang_Menu_Quit, command = root.quit)

# Window
root.title(Lang_Title)
root.geometry("400x400")
root.resizable(width = False, height = False)

# Random
selected = random.randint(1, 49)
label_obj1 = tk.Label(root, text = selected, width = 380, height = 380)
label_obj1.config(font = 'Helvetica -%d bold' % 200)
label_obj1.bind("<Button-1>", label_click_handler)
label_obj1.pack(side = tk.LEFT)
root.mainloop()
