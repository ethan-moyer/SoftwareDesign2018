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
mainwindow.pack()

def showAbout():
    messagebox.showinfo("About", "Made by Ethan Moyer and Albert Zhang\n\nEmulators Used: \nNestopia(http://nestopia.sourceforge.net/)\nSnes9X(http://www.snes9x.com/)\nMupen64(http://mupen64.emulation64.com/)\nDolphin(https://dolphin-emu.org/)\nPCSX2(https://pcsx2.net/)")

def setDirectory():
    dirname = filedialog.askdirectory()
    print(dirname,"/file.exe")
    folderContents = os.listdir(dirname)
    os.system(dirname + "/snes9x-x64.exe")

    for item in folderContents:
        listbox.insert(END, item)
def openPathWindow():
    t = tk.Toplevel(root)
    t.wm_title("Set Directories")
    directoryButton = ttk.Button(t, text="Set Directory", command=setDirectory)
    directoryButton.pack(padx=20, pady=10)

menuBar = Menu(root)
settingsmenu = Menu(menuBar, tearoff=0)
settingsmenu.add_command(label="Set Directories", command=openPathWindow)
menuBar.add_cascade(label="Settings", menu=settingsmenu)

menuBar.add_command(label="About", command=showAbout)
menuBar.add_command(label="Quit!", command=root.quit)

nameLabel = tk.Label(mainwindow, text="The Rom Box", font=("Arial", 20))
nameLabel.pack()

listbox = tk.Listbox(root)
listbox.pack(padx=50)

b1 = ttk.Button(root, text="Hello World")
b1.pack()

root.config(menu=menuBar)
root.mainloop()