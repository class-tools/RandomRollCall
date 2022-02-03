import webbrowser
import ctypes
import tkinter as tk
from tkinter.messagebox import showinfo
from tkinter.simpledialog import askinteger
import random

def Show_Help():
    if Lang_Help == True:
        webbrowser.open("https://github.com/ren-yc/RandomRollCall/blob/master/README.zh-Hans.md")
    else:
        webbrowser.open("https://github.com/ren-yc/RandomRollCall/blob/master/README.md")

def Show_About():
    showinfo(title = Lang_Menu_About, message = Lang_Messagebox_Message)

def label_click_handler(events):
    selected = random.randint(minnum, maxnum)
    label_obj1['text'] = selected

# Language
syslang = hex(ctypes.windll.kernel32.GetSystemDefaultUILanguage())
Lang_Title = ""
Lang_Menu_Settings = ""
Lang_Menu_Help = ""
Lang_Menu_About = ""
Lang_Menu_Quit = ""
Lang_Menu_MIN = ""
Lang_Menu_MAX = ""
Lang_Messagebox_Message = ""
Lang_Help = False
if syslang == '0x804':
    Lang_Title = u"随机点名"
    Lang_Menu_Settings = u"设置"
    Lang_Menu_Help = u"帮助"
    Lang_Menu_About = u"关于"
    Lang_Menu_Quit = u"退出"
    Lang_Menu_MIN = u"设置最小学号"
    Lang_Menu_MAX = u"设置最大学号"
    Lang_Messagebox_Message = u"本软件使用 MIT 开源软件协议，开发者为 Yuchen Ren。\nGithub 存储库地址：https://github.com/ren-yc/RandomRollCall"
    Lang_Help = True
else:
    Lang_Title = u"RandomRollCall"
    Lang_Menu_Settings = u"Settings"
    Lang_Menu_Help = u"Help"
    Lang_Menu_About = u"About"
    Lang_Menu_Quit = u"Quit"
    Lang_Menu_MIN = u"Edit minimum student number"
    Lang_Menu_MAX = u"Edit maximum student number"
    Lang_Messagebox_Message = u"This program uses MIT License, Developer: Yuchen Ren.\nGithub Repo: https://github.com/ren-yc/RandomRollCall"
    Lang_Help = False

# Init
root = tk.Tk()
minnum = 1
maxnum = 49

# Min and MAX

def Ask_MIN():
    global minnum
    minnum = askinteger(title = Lang_Menu_MIN, prompt = Lang_Menu_MIN)

def Ask_MAX():
    global maxnum
    maxnum = askinteger(title = Lang_Menu_MAX, prompt = Lang_Menu_MAX)

# Menubar
menubar = tk.Menu(root)
root['menu'] = menubar
settingsmenu = tk.Menu(menubar, tearoff = False)
settingsmenu.add_command(label = Lang_Menu_MIN, command = Ask_MIN)
settingsmenu.add_command(label = Lang_Menu_MAX, command = Ask_MAX)
menubar.add_cascade(label = Lang_Menu_Settings, menu = settingsmenu)
menubar.add_command(label = Lang_Menu_Help, command = Show_Help)
menubar.add_command(label = Lang_Menu_About, command = Show_About)
menubar.add_command(label = Lang_Menu_Quit, command = root.quit)

# Window
root.title(Lang_Title)
root.geometry("400x400")
root.resizable(width = False, height = False)

# Random
selected = random.randint(minnum, maxnum)
label_obj1 = tk.Label(root, text = selected, width = 380, height = 380)
label_obj1.config(font = 'Helvetica -%d bold' % 200)
label_obj1.bind("<Button-1>", label_click_handler)
label_obj1.pack(side = tk.LEFT)
root.mainloop()
