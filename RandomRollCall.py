import webbrowser
import random
import yaml
import os
import sys
import tkinter as tk
from time import sleep
from tkinter.messagebox import showerror, showinfo
from tkinter.simpledialog import askinteger, askstring

# Init
root = tk.Tk()
supported_lang = ["en-Us", "zh-Hans"]
running = False

# Error
def errno_1():
    showerror(title = "Fatal Error", message = "[Errno 1] Cannot read settings file data.")
    print("FATAL ERROR: [Errno 1] Cannot read settings file data.")

def errno_2():
    showerror(title = "Fatal Error", message = "[Errno 2] Cannot read language file data.")
    print("FATAL ERROR: [Errno 2] Cannot read language file data.")

def errno_3():
    showerror(title = "Error", message = "[Errno 3] Number out of range. (0 < min or max < 100000 and min < max)")
    print("ERROR: [Errno 3] Number out of range. (0 < min or max < 100000 and min < max)")

# Yaml + Language
yamlSettingsPath = os.path.join("", "settings.yml")
try:
    SettingsFile = open(yamlSettingsPath, 'r', encoding = 'utf-8')
    dicSettings = yaml.load(SettingsFile.read(), Loader = yaml.FullLoader)
    default_Lang = dicSettings['Language']
    minnum = dicSettings['Min']
    maxnum = dicSettings['Max']
    if minnum == None or maxnum == None:
        raise TypeError
    version = dicSettings['Version']
    SettingsFile.close()
except:
    errno_1()
    root.quit()
    sys.exit(1)
try:
    yamlPath = os.path.join("", "lang/" + default_Lang + ".yml")
    file = open(yamlPath, 'r', encoding = 'utf-8')
    dic = yaml.load(file.read(), Loader = yaml.FullLoader)
    Lang_Title = dic['Title']
    Lang_Menu_Settings = dic['Settings']
    Lang_Menu_Help = dic['Help']
    Lang_Menu_About = dic['About']
    Lang_Menu_Quit = dic['Quit']
    Lang_Menu_MIN = dic['Ask_Min_Message']
    Lang_Menu_MAX = dic['Ask_Max_Message']
    Lang_Menu_Lang = dic['Switch_Lang']
    Lang_Switch = dic['Switch_Info']
    Lang_Messagebox_Message1 = dic['About_Message1']
    Lang_Messagebox_Message2 = dic['About_Message2']
    Lang_Warn = dic['Warn']
    Lang_Please_Reopen = dic['Reopen']
    Lang_Error = dic['Error']
    Lang_Switch_Error_Message = dic['Switch_Lang_Error']
    Lang_Window_Info = dic['Window_Info']
    Lang_Version = dic['Version']
    file.close()
except:
    errno_2()
    root.quit()
    sys.exit(1)

# Update Settings
def update():
    SettingsFile = open(yamlSettingsPath, 'w', encoding = 'utf-8')
    data = {"Language" : default_Lang, "Min" : minnum, "Max" : maxnum, "Version" : version}
    yaml.dump(data = data, stream = SettingsFile, allow_unicode = True, sort_keys = False)

# Dialog
def Ask_MIN():
    global minnum
    tmp = askinteger(title = Lang_Menu_MIN, prompt = Lang_Menu_MIN)
    if tmp == None:
        return
    if tmp <= 0 or tmp >= maxnum:
        errno_3()
        return
    minnum = tmp
    update()

def Ask_MAX():
    global maxnum
    tmp = askinteger(title = Lang_Menu_MAX, prompt = Lang_Menu_MAX)
    if tmp == None:
        return
    if tmp >= 100000 or tmp <= minnum:
        errno_3()
        return
    maxnum = tmp
    update()

def FrontSize(tmp):
    length = len(str(tmp))
    if length <= 3:
        return 200
    elif length == 4:
        return 150
    elif length == 5:
        return 100
    else:
        return 50

# Menubar
def Show_Help():
    if default_Lang == "zh-Hans":
        webbrowser.open("https://github.com/class-tools/RandomRollCall/blob/master/README.zh-Hans.md")
    else:
        webbrowser.open("https://github.com/class-tools/RandomRollCall/blob/master/README.md")

def Show_About():
    showinfo(title = Lang_Menu_About, message = Lang_Messagebox_Message1 + version + Lang_Messagebox_Message2 + Lang_Version)

def Ask_Lang():
    tmp = askstring(title = Lang_Menu_Lang, prompt = Lang_Switch)
    if tmp == None:
        return
    if not tmp in supported_lang:
        showerror(title = Lang_Error, message = Lang_Switch_Error_Message)
    else:
        global default_Lang
        default_Lang = tmp
        update()
        showinfo(title = Lang_Warn, message = Lang_Please_Reopen)
        root.quit()
        sys.exit(0)

menubar = tk.Menu(root)
root['menu'] = menubar
settingsmenu = tk.Menu(menubar, tearoff = False)
settingsmenu.add_command(label = Lang_Menu_MIN, command = Ask_MIN)
settingsmenu.add_command(label = Lang_Menu_MAX, command = Ask_MAX)
settingsmenu.add_command(label = Lang_Menu_Lang, command = Ask_Lang)
menubar.add_cascade(label = Lang_Menu_Settings, menu = settingsmenu)
menubar.add_command(label = Lang_Menu_Help, command = Show_Help)
menubar.add_command(label = Lang_Menu_About, command = Show_About)
menubar.add_command(label = Lang_Menu_Quit, command = root.quit)

# Window
root.title(Lang_Title)
root.geometry("400x400")
root.resizable(width = False, height = False)
root.iconbitmap("RandomRollCall.ico")

# Mainloop
def click(events):
    global running
    if running == False:
        running = True
        while running == True:
            selected = random.randint(minnum, maxnum)
            big_num_label.config(font = 'Helvetica -%d bold' % FrontSize(selected))
            big_num_label['text'] = selected
            big_num_label.update()
            sleep(0.01)
    else:
        running = False

# Show
big_num_label = tk.Label(root, text = Lang_Window_Info, width = 380, height = 380)
big_num_label.config(font = 'Helvetica -%d bold' % 100)
big_num_label.bind("<Button-1>", click)
big_num_label.pack(side = tk.LEFT)
root.mainloop()
