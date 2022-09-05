'''
Random Roll Call Main Source File 2.0.0
This source code file is under MIT License.
Copyright (c) 2022 Class Tools Develop Team
Contributors: ren-yc
'''
# Modules
import os
import sys
import json
import random
import tkinter
import webbrowser
from time import sleep
from tkinter.messagebox import showerror, showinfo
from tkinter.simpledialog import askinteger, askstring

# Variables
RUNNING = False
VERSION = '2.0.0'
TK_ROOT = tkinter.Tk()
SUPPORT_LANG = ['en-US', 'zh-CN']
BASE_DIR = os.path.dirname(__file__)

# Error
def ERRNO1():
	showerror(title = 'Fatal Error', message = '[Errno 2] Cannot read language file data.')
	print('FATAL ERROR: [Errno 2] Cannot read language file data.')

def ERRNO2():
	showerror(title = 'Error', message = '[Errno 3] Number out of range. (0 < min or max < 100000 and min < max)')
	print('ERROR: [Errno 3] Number out of range. (0 < min or max < 100000 and min < max)')

# Read
def Read_Settings():
	global Settings_Dict
	try:
		with open(os.path.join(BASE_DIR, './settings.json'), 'r', encoding = 'utf-8') as f:
			Settings_Dict = json.load(f)
	except (FileNotFoundError, json.decoder.JSONDecodeError):
		Settings_Dict['Language'] = 'en-US'
		Settings_Dict['Min'] = 1
		Settings_Dict['Max'] = 49

def Read_Language():
	global Language_Dict
	try:
		with open(os.path.join(BASE_DIR, './lang/' + Settings_Dict['Language'] + '.json'), 'r', encoding = 'utf-8') as f:
			Language_Dict = json.load(f)
	except (FileNotFoundError, json.decoder.JSONDecodeError):
		ERRNO1()
		TK_ROOT.quit()
		sys.exit(1)

# Update Settings
def update():
	with open(os.path.join(BASE_DIR, './settings.json'), 'w', encoding = 'utf-8') as f:
		json.dump(Settings_Dict, f, indent = '\t')

# Dialog
def Ask_MIN():
	tmp = askinteger(title = Language_Dict['Ask_Min_Message'], prompt = Language_Dict['Ask_Min_Message'], initialvalue = Settings_Dict['Min'])
	if tmp is None:
		return
	if tmp <= 0 or tmp >= Settings_Dict['Max']:
		ERRNO2()
		return
	Settings_Dict['Min'] = tmp
	update()

def Ask_MAX():
	tmp = askinteger(title = Language_Dict['Ask_Max_Message'], prompt = Language_Dict['Ask_Max_Message'], initialvalue = Settings_Dict['Max'])
	if tmp is None:
		return
	if tmp >= 100000 or tmp <= Settings_Dict['Min']:
		ERRNO2()
		return
	Settings_Dict['Max'] = tmp
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
	if Settings_Dict['Language'] == 'zh-CN':
		webbrowser.open('https://github.com/class-tools/RandomRollCall/blob/master/README.zh-CN.md')
	else:
		webbrowser.open('https://github.com/class-tools/RandomRollCall/blob/master/README.md')

def Show_About():
	showinfo(title = Language_Dict['About'], message = Language_Dict['About_Message1'] + VERSION + Language_Dict['About_Message2'] + Language_Dict['Version'])

def Ask_Lang():
	tmp = askstring(title = Language_Dict['Switch_Lang'], prompt = Language_Dict['Switch_Info'])
	if tmp is None:
		return
	if not tmp in SUPPORT_LANG:
		showerror(title = Language_Dict['Error'], message = Language_Dict['Switch_Lang_Error'])
	else:
		Settings_Dict['Language'] = tmp
		update()
		showinfo(title = Language_Dict['Warn'], message = Language_Dict['Reopen'])
		TK_ROOT.quit()
		sys.exit(0)

# Init
def Set_Window():
	global Language_Dict
	TK_ROOT.title(Language_Dict['Title'])
	TK_ROOT.geometry('400x400')
	TK_ROOT.resizable(width = False, height = False)
	TK_ROOT.iconbitmap('RRC.ico')

def Set_Menubar():
	global Language_Dict
	menubar = tkinter.Menu(TK_ROOT)
	TK_ROOT['menu'] = menubar
	settingsmenu = tkinter.Menu(menubar, tearoff = False)
	settingsmenu.add_command(label = Language_Dict['Ask_Min_Message'], command = Ask_MIN)
	settingsmenu.add_command(label = Language_Dict['Ask_Max_Message'], command = Ask_MAX)
	settingsmenu.add_command(label = Language_Dict['Switch_Lang'], command = Ask_Lang)
	menubar.add_cascade(label = Language_Dict['Settings'], menu = settingsmenu)
	menubar.add_command(label = Language_Dict['Help'], command = Show_Help)
	menubar.add_command(label = Language_Dict['About'], command = Show_About)
	menubar.add_command(label = Language_Dict['Quit'], command = TK_ROOT.quit)

# Events
def click(events):
	global RUNNING
	if RUNNING == False:
		RUNNING = True
		while RUNNING == True:
			selected = random.randint(Settings_Dict['Min'], Settings_Dict['Max'])
			big_num_label.config(font = 'Helvetica -%d bold' % FrontSize(selected))
			big_num_label['text'] = selected
			big_num_label.update()
			sleep(0.01)
	else:
		RUNNING = False

# Mainloop
def main():
	global big_num_label
	big_num_label = tkinter.Label(TK_ROOT, text = Language_Dict['Window_Info'], width = 380, height = 380)
	big_num_label.config(font = 'Helvetica -%d bold' % 100)
	big_num_label.bind('<Button-1>', click)
	big_num_label.pack(side = tkinter.LEFT)
	TK_ROOT.mainloop()

if __name__ == '__main__':
	Read_Settings()
	Read_Language()
	Set_Window()
	Set_Menubar()
	main()
