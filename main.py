from typing import List
# Code to solve CrossSum problems keyed in via the UI laid out below
import itertools
import tkinter as tk
from tkinter import *
from tkinter import ttk
import operator
#Create an instance of Tkinter frame or window
win= tk.Tk()
#Set the geometry of tkinter frame
win.geometry("750x250")

ops = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '**': operator.pow,
    '%': operator.mod,
}

def is_quick(s: str) -> bool:
    if s == '/' or s == '*':
        return True
    else:
        return False

def calc_part(part1: int, part2: int, op:str) -> tuple[bool, int]:
    if op == '/' and int(part1) % int(part2) != 0:
        return False, 0

    return True, ops[op](int(part1), int(part2))


def calc_line2(a: int, b: int, c: int, op1: str, op2: str, answer:int) -> tuple[bool, int]:
    # So, we need to calculate the two totals, factoring in the order of precedence

    sub = calc_part(a, b, op1)
    if sub[0] is False:
        return False, 0

    total = calc_part(sub[1], c, op2)
    if total[0] is False:
        return False, 0

    return total[1] == answer, total[1]

entry_style = ttk.Style()

entry_style.configure('style.TEntry', fieldbackground="black", foreground="white")

# ROW 1
textbox00 = ttk.Entry(win, width=3, style='style.TEntry')
textbox00.grid(column=0, row=0)
textbox00.insert(index=0, string="")

combobox10= ttk.Combobox(win,state="readonly", width=5)
combobox10['values']=('+', '-', '*', '/')
combobox10.current(0)
combobox10.grid(column=1, row=0)

textbox20 = ttk.Entry(win, width=3, style='style.TEntry')
textbox20.grid(column=2, row=0)
textbox20.insert(index=0, string="")

combobox30= ttk.Combobox(win,state="readonly", width=5)
combobox30['values']=('+', '-', '*', '/')
combobox30.current(0)
combobox30.grid(column=3, row=0)

textbox40 = ttk.Entry(win, width=3, style='style.TEntry')
textbox40.grid(column=4, row=0)
textbox40.insert(index=0, string="")

txtvar50 = tk.StringVar()
textbox50 = ttk.Entry(win, textvariable=txtvar50, width=3)
textbox50.grid(column=5, row=0)
txtvar50.set("0") # Set initial text


# ROW 1
combobox01= ttk.Combobox(win,state="readonly", width=5)
combobox01['values']=('+', '-', '*', '/')
combobox01.current(0)
combobox01.grid(column=0, row=1)

combobox21= ttk.Combobox(win,state="readonly", width=5)
combobox21['values']=('+', '-', '*', '/')
combobox21.current(0)
combobox21.grid(column=2, row=1)

combobox41= ttk.Combobox(win,state="readonly", width=5)
combobox41['values']=('+', '-', '*', '/')
combobox41.current(0)
combobox41.grid(column=4, row=1)


# ROW 2
textbox02 = ttk.Entry(win, width=3, style='style.TEntry')
textbox02.grid(column=0, row=2)
textbox02.insert(index=0, string="")

combobox12= ttk.Combobox(win,state="readonly", width=5)
combobox12['values']=('+', '-', '*', '/')
combobox12.current(0)
combobox12.grid(column=1, row=2)

textbox22 = ttk.Entry(win, width=3, style='style.TEntry')
textbox22.grid(column=2, row=2)
textbox22.insert(index=0, string="")

combobox32= ttk.Combobox(win,state="readonly", width=5)
combobox32['values']=('+', '-', '*', '/')
combobox32.current(0)
combobox32.grid(column=3, row=2)

textbox42 = ttk.Entry(win, width=3, style='style.TEntry')
textbox42.grid(column=4, row=2)
textbox42.insert(index=0, string="")

txtvar52 = tk.StringVar()
textbox52 = ttk.Entry(win, textvariable=txtvar52, width=3)
textbox52.grid(column=5, row=2)
txtvar52.set("0") # Set initial text


# ROW 3
combobox03= ttk.Combobox(win,state="readonly", width=5)
combobox03['values']=('+', '-', '*', '/')
combobox03.current(0)
combobox03.grid(column=0, row=3)

combobox23= ttk.Combobox(win,state="readonly", width=5)
combobox23['values']=('+', '-', '*', '/')
combobox23.current(0)
combobox23.grid(column=2, row=3)

combobox43= ttk.Combobox(win,state="readonly", width=5)
combobox43['values']=('+', '-', '*', '/')
combobox43.current(0)
combobox43.grid(column=4, row=3)


# ROW 4
textbox04 = ttk.Entry(win, width=3, style='style.TEntry')
textbox04.grid(column=0, row=4)
textbox04.insert(index=0, string="")

combobox14 = ttk.Combobox(win,state="readonly", width=5)
combobox14['values']=('+', '-', '*', '/')
combobox14.current(0)
combobox14.grid(column=1, row=4)

textbox24 = ttk.Entry(win, width=3, style='style.TEntry')
textbox24.grid(column=2, row=4)
textbox24.insert(index=0, string="")

combobox34= ttk.Combobox(win,state="readonly", width=5)
combobox34['values']=('+', '-', '*', '/')
combobox34.current(0)
combobox34.grid(column=3, row=4)

textbox44 = ttk.Entry(win, width=3, style='style.TEntry')
textbox44.grid(column=4, row=4)
textbox44.insert(index=0, string="")

txtvar54 = tk.StringVar()
textbox54 = ttk.Entry(win, textvariable=txtvar54, width=3)
textbox54.grid(column=5, row=4)
txtvar54.set("0") # Set initial text


# ROW 5
txtvar05 = tk.StringVar()
textbox05 = ttk.Entry(win, textvariable=txtvar05, width=3)
textbox05.grid(column=0, row=5)
txtvar05.set("0") # Set initial text

txtvar25 = tk.StringVar()
textbox25 = ttk.Entry(win, textvariable=txtvar25, width=3)
textbox25.grid(column=2, row=5)
txtvar25.set("0") # Set initial text

txtvar45 = tk.StringVar()
textbox45 = ttk.Entry(win, textvariable=txtvar45, width=3)
textbox45.grid(column=4, row=5)
txtvar45.set("0") # Set initial text

def analyze_cross_sum():
    print("analyze_cross_sum()")
    # Generate all permutations of numbers 1 to 9
    numbers = list(range(1, 10))
    permutations = list(itertools.permutations(numbers))

    # Example: print the total number and first 5 permutations
    count = 1
    for perm in permutations:
        # Step through each and exercise the tests against it
        # 1. Across top line
        res = calc_line2(perm[0], perm[1], perm[2], combobox10.get(), combobox30.get(), int(textbox50.get()))
        if res[0] is False:
            continue

        # 2. Across 2nd line
        res = calc_line2(perm[3], perm[4], perm[5], combobox12.get(), combobox32.get(), int(textbox52.get()))
        if res[0] is False:
            continue

        # 3. Across 3rd line
        res = calc_line2(perm[6], perm[7], perm[8], combobox14.get(), combobox34.get(), int(textbox54.get()))
        if res[0] is False:
            continue

        # 4. Down the 1st column -- Incomplete
        res = calc_line2(perm[0], perm[3], perm[6], combobox01.get(), combobox03.get(), int(textbox05.get()))
        if res[0] is False:
            continue

        # 5. Down the 2nd column
        res = calc_line2(perm[1], perm[4], perm[7], combobox21.get(), combobox23.get(), int(textbox25.get()))
        if res[0] is False:
            continue

        # 6. Down the 3rd column
        res = calc_line2(perm[2], perm[5], perm[8], combobox41.get(), combobox43.get(), int(textbox45.get()))
        if res[0] is False:
            continue

        # If we made it here, then we have a winner
        print("ANSWER: ", perm)
        textbox00.insert(0, str(perm[0]))
        textbox20.insert(0, str(perm[1]))
        textbox40.insert(0, str(perm[2]))
        textbox02.insert(0, str(perm[3]))
        textbox22.insert(0, str(perm[4]))
        textbox42.insert(0, str(perm[5]))
        textbox04.insert(0, str(perm[6]))
        textbox24.insert(0, str(perm[7]))
        textbox44.insert(0, str(perm[8]))

        # Print a formatted version of the grid
        i = 0
        while i < 3:
            t = (i * 3)
            print(perm[t+0], " ", perm[t+1], " ", perm[t+2])
            i += 1
        print()
    print("For loop finished")

exeButton = ttk.Button(win, text="Do CrossSum", command=analyze_cross_sum)
exeButton.grid(column=6, row=5)

win.mainloop()
