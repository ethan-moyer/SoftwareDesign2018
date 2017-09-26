from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
from tkinter import filedialog
import os

root = Tk()
s = ttk.Style()
s.theme_use("vista")
mainwindow = ttk.Frame(root)
mainwindow.grid(row=0, column=0)

def showAbout():
    messagebox.showinfo("About", "Made by Ethan Moyer and Albert Zhang\n\nEmulators Used: \nNestopia(http://nestopia.sourceforge.net/)\nSnes9X(http://www.snes9x.com/)\nMupen64(http://mupen64.emulation64.com/)\nDolphin(https://dolphin-emu.org/)\nPCSX2(https://pcsx2.net/)")

def setDirectory(snes9xlocation):
    dirname = filedialog.askdirectory()
    print(dirname,"/file.exe")
    folderContents = os.listdir(dirname)
    snes9xlocation = dirname + "/snes9x-x64.exe"
    os.system(snes9xlocation)
    for item in folderContents:
        listbox.insert(END, item)

def openPathWindow():
    t = tk.Toplevel(root)
    t.wm_title("Set Directories")
    directoryButton = ttk.Button(t, text="Set Directory", command=setDirectory).grid(row=0, column=0)

def showList2():
    listbox2.grid_forget()

def onselect(evt):
    # Note here that Tkinter passes an event object to onselect()
    w = evt.widget
    index = int(w.curselection()[0])
    value = w.get(index)
    print('You selected item %d: "%s"' % (index, value))

menuBar = Menu(root)
settingsmenu = Menu(menuBar, tearoff=0)
settingsmenu.add_command(label="Set Directories", command=openPathWindow)
menuBar.add_cascade(label="Settings", menu=settingsmenu)

menuBar.add_command(label="About", command=showAbout)
menuBar.add_command(label="Quit!", command=root.quit)

nameLabel = tk.Label(mainwindow, text="The Rom Box", font=("Arial", 20)).grid(row=0, column=0)

listbox = tk.Listbox(mainwindow)
listbox.grid(row=1, column=0)
listbox.bind('<<ListboxSelect>>', onselect)


listbox2 = tk.Listbox(mainwindow)
listbox2.grid(row=1, column=0)
for item in ["1", "2", "3"]:
    listbox2.insert(END, item)

b1 = ttk.Button(mainwindow, text="List 1", command=showList2).grid(row=1, column=1)
b2 = ttk.Button(mainwindow, text="List 2", command=showList2).grid(row=2, column=1)

root.config(menu=menuBar)
root.mainloop()