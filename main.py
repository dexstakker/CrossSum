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


def calc_line(a: int, b: int, c: int, op1: str, op2: str, answer:int) -> tuple[bool, int]:
    # So, we need to calculate the two totals, factoring in the order of precedence
    left = right = None
    total = 0
    if is_quick(op1):
        # Solve the left
        left = calc_part(a, b, op1)
        if left[0] is False:
            return False, 0
        # Solve the right and we're done
        total = calc_part(left[1], c, op2)
        if total[0] is False:
            return False, 0
    else:
        right = calc_part(b, c, op2)
        if right[0] is False:
            return False, 0
        total = calc_part(a, right[1], op1)
        if total[0] is False:
            return False, 0

    return total[1] == answer, total[1]

def calc_line2(a: int, b: int, c: int, op1: str, op2: str, answer:int) -> tuple[bool, int]:
    # So, we need to calculate the two totals, factoring in the order of precedence

    sub = calc_part(a, b, op1)
    if sub[0] is False:
        return False, 0

    total = calc_part(sub[1], c, op2)
    if total[0] is False:
        return False, 0

    return total[1] == answer, total[1]

#def calc_board() -> bool:


# ROW 1
combobox00= ttk.Combobox(win,state="readonly", width=5)
combobox00['values']=('+', '-', '*', '/')
combobox00.current(0)
combobox00.grid(column=0, row=0)

combobox10= ttk.Combobox(win,state="readonly", width=5)
combobox10['values']=('+', '-', '*', '/')
combobox10.current(1)
combobox10.grid(column=1, row=0)

txtvar30 = tk.StringVar()
textbox30 = ttk.Entry(win, textvariable=txtvar30, width=3)
textbox30.grid(column=3, row=0)
txtvar30.set("10") # Set initial text


# ROW 1
combobox01= ttk.Combobox(win,state="readonly", width=5)
combobox01['values']=('+', '-', '*', '/')
combobox01.current(1)
combobox01.grid(column=0, row=1)

combobox11= ttk.Combobox(win,state="readonly", width=5)
combobox11['values']=('+', '-', '*', '/')
combobox11.current(0)
combobox11.grid(column=1, row=1)

combobox21= ttk.Combobox(win,state="readonly", width=5)
combobox21['values']=('+', '-', '*', '/')
combobox21.current(1)
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
txtvar32.set("36") # Set initial text


# ROW 3
combobox03= ttk.Combobox(win,state="readonly", width=5)
combobox03['values']=('+', '-', '*', '/')
combobox03.current(1)
combobox03.grid(column=0, row=3)

combobox13= ttk.Combobox(win,state="readonly", width=5)
combobox13['values']=('+', '-', '*', '/')
combobox13.current(2)
combobox13.grid(column=1, row=3)

combobox23= ttk.Combobox(win,state="readonly", width=5)
combobox23['values']=('+', '-', '*', '/')
combobox23.current(1)
combobox23.grid(column=2, row=3)


# ROW 4
combobox04= ttk.Combobox(win,state="readonly", width=5)
combobox04['values']=('+', '-', '*', '/')
combobox04.current(0)
combobox04.grid(column=0, row=4)

combobox14= ttk.Combobox(win,state="readonly", width=5)
combobox14['values']=('+', '-', '*', '/')
combobox14.current(0)
combobox14.grid(column=1, row=4)

txtvar34 = tk.StringVar()
textbox34 = ttk.Entry(win, textvariable=txtvar34, width=3)
textbox34.grid(column=3, row=4)
txtvar34.set("9") # Set initial text


# ROW 5
txtvar05 = tk.StringVar()
textbox05 = ttk.Entry(win, textvariable=txtvar05, width=3)
textbox05.grid(column=0, row=5)
txtvar05.set("1") # Set initial text

txtvar15 = tk.StringVar()
textbox15 = ttk.Entry(win, textvariable=txtvar15, width=3)
textbox15.grid(column=1, row=5)
txtvar15.set("39") # Set initial text

txtvar25 = tk.StringVar()
textbox25 = ttk.Entry(win, textvariable=txtvar25, width=3)
textbox25.grid(column=2, row=5)
txtvar25.set("0") # Set initial text

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
        res = calc_line2(perm[0], perm[1], perm[2], combobox00.get(), combobox10.get(), int(textbox30.get()))
        if res[0] is False:
            continue

        # 2. Across 2nd line
        res = calc_line2(perm[3], perm[4], perm[5], combobox02.get(), combobox12.get(), int(textbox32.get()))
        if res[0] is False:
            continue

        # 3. Across 3rd line
        res = calc_line2(perm[6], perm[7], perm[8], combobox04.get(), combobox14.get(), int(textbox34.get()))
        if res[0] is False:
            continue

        # 4. Down the 1st column -- Incomplete
        res = calc_line2(perm[0], perm[3], perm[6], combobox01.get(), combobox03.get(), int(textbox05.get()))
        if res[0] is False:
            continue

        # 5. Down the 2nd column
        res = calc_line2(perm[1], perm[4], perm[7], combobox11.get(), combobox13.get(), int(textbox15.get()))
        if res[0] is False:
            continue

        # 6. Down the 3rd column
        res = calc_line2(perm[2], perm[5], perm[8], combobox21.get(), combobox23.get(), int(textbox25.get()))
        if res[0] is False:
            continue

        # If we made it here, then we have a winner
        print("ANSWER: ", perm)

        # If we made it here, then we have a winner
        count += 1
    print("Number of permutations: ", count)

exeButton = ttk.Button(win, text="Do CrossSum", command=analyze_cross_sum)
exeButton.grid(column=6, row=5)

win.mainloop()
