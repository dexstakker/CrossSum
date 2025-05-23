
#Import Tkinter library
import tkinter as tk
from tkinter import *
from tkinter import ttk
#Create an instance of Tkinter frame or window
win= tk.Tk()
#Set the geometry of tkinter frame
win.geometry("750x250")


# ROW 1
combobox00= ttk.Combobox(win,state="readonly", width=5)
combobox00['values']=('+', '-', '*', '/')
combobox00.current(0)
combobox00.grid(column=0, row=0)

combobox10= ttk.Combobox(win,state="readonly", width=5)
combobox10['values']=('+', '-', '*', '/')
combobox10.current(2)
combobox10.grid(column=1, row=0)

txtvar30 = tk.StringVar()
textbox30 = ttk.Entry(win, textvariable=txtvar30, width=3)
textbox30.grid(column=3, row=0)
txtvar30.set("0") # Set initial text


# ROW 1
combobox01= ttk.Combobox(win,state="readonly", width=5)
combobox01['values']=('+', '-', '*', '/')
combobox01.current(0)
combobox01.grid(column=0, row=1)

combobox11= ttk.Combobox(win,state="readonly", width=5)
combobox11['values']=('+', '-', '*', '/')
combobox11.current(2)
combobox11.grid(column=1, row=1)

combobox21= ttk.Combobox(win,state="readonly", width=5)
combobox21['values']=('+', '-', '*', '/')
combobox21.current(2)
combobox21.grid(column=2, row=1)


# ROW 2
combobox02= ttk.Combobox(win,state="readonly", width=5)
combobox02['values']=('+', '-', '*', '/')
combobox02.current(0)
combobox02.grid(column=0, row=2)

combobox12= ttk.Combobox(win,state="readonly", width=5)
combobox12['values']=('+', '-', '*', '/')
combobox12.current(2)
combobox12.grid(column=1, row=2)

txtvar32 = tk.StringVar()
textbox32 = ttk.Entry(win, textvariable=txtvar32, width=3)
textbox32.grid(column=3, row=2)
txtvar32.set("0") # Set initial text


# ROW 3
combobox03= ttk.Combobox(win,state="readonly", width=5)
combobox03['values']=('+', '-', '*', '/')
combobox03.current(0)
combobox03.grid(column=0, row=3)

combobox13= ttk.Combobox(win,state="readonly", width=5)
combobox13['values']=('+', '-', '*', '/')
combobox13.current(2)
combobox13.grid(column=1, row=3)

combobox23= ttk.Combobox(win,state="readonly", width=5)
combobox23['values']=('+', '-', '*', '/')
combobox23.current(2)
combobox23.grid(column=2, row=3)


# ROW 4
combobox04= ttk.Combobox(win,state="readonly", width=5)
combobox04['values']=('+', '-', '*', '/')
combobox04.current(0)
combobox04.grid(column=0, row=4)

combobox14= ttk.Combobox(win,state="readonly", width=5)
combobox14['values']=('+', '-', '*', '/')
combobox14.current(2)
combobox14.grid(column=1, row=4)

txtvar34 = tk.StringVar()
textbox34 = ttk.Entry(win, textvariable=txtvar34, width=3)
textbox34.grid(column=3, row=4)
txtvar34.set("0") # Set initial text


# ROW 5


win.mainloop()