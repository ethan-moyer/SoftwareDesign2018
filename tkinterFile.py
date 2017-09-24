from tkinter import *
from tkinter import ttk
from tkinter import messagebox
root = Tk()
s = ttk.Style()
s.theme_use("vista")

mainwindow = ttk.Frame(root)
mainwindow.pack()

def showAbout():
    messagebox.showinfo("About", "Made by Ethan Moyer and Albert Zhang\n\nEmulators Used: \nNestopia(http://nestopia.sourceforge.net/)\nSnes9X(http://www.snes9x.com/)\nMupen64(http://mupen64.emulation64.com/)\nDolphin(https://dolphin-emu.org/)\nPCSX2(https://pcsx2.net/)")

menuBar = Menu(root)
menuBar.add_command(label="About", command=showAbout)
menuBar.add_command(label="Quit!", command=root.quit)

b1 = ttk.Button(root, text="Hello World")
b1.pack(padx=50, pady=50)

root.config(menu=menuBar)
root.mainloop()