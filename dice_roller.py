#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
D&D Dice Roller with roll modifiers
"""

# Built-in/Generic Imports
import random
# Libs
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

__author__ = 'Marcello Lamonaca'
__copyright__ = 'Copyright 2019, Marcello Lamonaca'
__credits__ = ['Marcello Lamonaca']
__license__ = 'MIT'
__version__ = '0.2.2'
__maintainer__ = 'Marcello Lamonaca'
__email__ = ''
__status__ = 'dev'


random.seed()  # initialize pseudo-random numbers


def DX(rolls_num, dice_sides, modifier):
    """roll dice with arbitrary number of sides
        INPUTS:
        - number of rolls
        - number of sides
        - roll modifier (applied after dices rolls)"""

    # modifier is StringVar to accept empty entry fields
    try:
        modifier = int(modifier)
    except ValueError:
        modifier = 0

    # sums result of gen-exp that generates randint between 1 and dice_sides roll_num-times
    result = sum(random.randint(1, dice_sides) for i in range(rolls_num)) + modifier
    if result <= 0:
        return 1
    else:
        return result


def D4_roll():
    """calls DX with dice_sides = 4"""
    roll_result.set(DX(D4_rolls.get(), 4, D4_modifier_var.get()))


def D6_roll():
    """calls DX with dice_sides = 6"""
    roll_result.set(DX(D6_rolls.get(), 6, D6_modifier_var.get()))


def D8_roll():
    """calls DX with dice_sides = 8"""
    roll_result.set(DX(D8_rolls.get(), 8, D8_modifier_var.get()))


def D10_roll():
    """calls DX with dice_sides = 10"""
    roll_result.set(DX(D10_rolls.get(), 10, D10_modifier_var.get()))


def D12_roll():
    """calls DX with dice_sides = 12"""
    roll_result.set(DX(D12_rolls.get(), 12, D12_modifier_var.get()))


def D20_roll():
    """calls DX with dice_sides = 20"""
    roll_result.set(DX(D20_rolls.get(), 20, D20_modifier_var.get()))


def D100_roll():
    """calls DX with dice_sides = 100"""
    roll_result.set(DX(D100_rolls.get(), 100, D100_modifier_var.get()))


def DX_roll():
    """calls DX with a user inserted number of sides"""
    try:
        roll_result.set(DX(DX_rolls.get(), DX_sides.get(), DX_modifier_var.get()))
    except:
        messagebox.showerror(title='ERROR', message='the number of sides must be an integer')


if __name__ == '__main__':
    root = tk.Tk()
    root.title('Dice Roller')
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    root.resizable(False, False)

    # FRAME FOR INPUTS
    input_frame = ttk.Frame(root, borderwidth=3, relief='solid')
    input_frame.grid(column=0, row=0, padx=6, pady=6, sticky=(tk.N, tk.S, tk.E, tk.W))

    # PADDING SETTINGS
    entry_padx = (3, 6)
    label_padx = (6, 3)
    std_pady = 6
    button_padx = 6

    roll_result = tk.IntVar()

    # D4 INPUT AND BUTTON
    D4_label = ttk.Label(input_frame, text='D4')
    D4_label.grid(column=1, row=1, padx=label_padx, pady=std_pady)
    D4_rolls = tk.IntVar()
    D4_spinbox = ttk.Spinbox(input_frame, from_=1, to=100, textvariable=D4_rolls, wrap=True)
    D4_spinbox.grid(column=2, row=1, padx=entry_padx, pady=std_pady)
    D4_result = tk.IntVar()
    D4_modifier_label = ttk.Label(input_frame, text='MODIFIER')
    D4_modifier_label.grid(column=3, row=1, padx=label_padx)
    D4_modifier_var = tk.StringVar()
    D4_modifier_entry = ttk.Entry(input_frame, textvariable=D4_modifier_var)
    D4_modifier_entry.grid(column=4, row=1, padx=entry_padx)
    D4_button = ttk.Button(input_frame, text='ROLL', command=D4_roll)
    D4_button.grid(column=10, row=1, padx=button_padx, pady=std_pady)

    # D6 INPUT AND BUTTON
    D6_label = ttk.Label(input_frame, text='D6')
    D6_label.grid(column=1, row=2, padx=label_padx, pady=std_pady)
    D6_rolls = tk.IntVar()
    D6_spinbox = ttk.Spinbox(input_frame, from_=1, to=100, textvariable=D6_rolls, wrap=True)
    D6_spinbox.grid(column=2, row=2, padx=entry_padx, pady=std_pady)
    D6_result = tk.IntVar()
    D6_modifier_label = ttk.Label(input_frame, text='MODIFIER')
    D6_modifier_label.grid(column=3, row=2, padx=label_padx)
    D6_modifier_var = tk.StringVar()
    D6_modifier_entry = ttk.Entry(input_frame, textvariable=D6_modifier_var)
    D6_modifier_entry.grid(column=4, row=2, padx=entry_padx)
    D6_button = ttk.Button(input_frame, text='ROLL', command=D6_roll)
    D6_button.grid(column=10, row=2, padx=button_padx, pady=std_pady)

    # D8 INPUT AND BUTTON
    D8_label = ttk.Label(input_frame, text='D8')
    D8_label.grid(column=1, row=3, padx=label_padx, pady=std_pady)
    D8_rolls = tk.IntVar()
    D8_spinbox = ttk.Spinbox(input_frame, from_=1, to=100, textvariable=D8_rolls, wrap=True)
    D8_spinbox.grid(column=2, row=3, padx=entry_padx, pady=std_pady)
    D8_result = tk.IntVar()
    D8_modifier_label = ttk.Label(input_frame, text='MODIFIER')
    D8_modifier_label.grid(column=3, row=3, padx=label_padx)
    D8_modifier_var = tk.StringVar()
    D8_modifier_entry = ttk.Entry(input_frame, textvariable=D8_modifier_var)
    D8_modifier_entry.grid(column=4, row=3, padx=entry_padx)
    D8_button = ttk.Button(input_frame, text='ROLL', command=D8_roll)
    D8_button.grid(column=10, row=3, padx=button_padx, pady=std_pady)

    # D10 INPUT AND BUTTON
    D10_label = ttk.Label(input_frame, text='D10')
    D10_label.grid(column=1, row=4, padx=label_padx, pady=std_pady)
    D10_rolls = tk.IntVar()
    D10_spinbox = ttk.Spinbox(input_frame, from_=1, to=100, textvariable=D10_rolls, wrap=True)
    D10_spinbox.grid(column=2, row=4, padx=entry_padx, pady=std_pady)
    D10_result = tk.IntVar()
    D10_modifier_label = ttk.Label(input_frame, text='MODIFIER')
    D10_modifier_label.grid(column=3, row=4, padx=label_padx)
    D10_modifier_var = tk.StringVar()
    D10_modifier_entry = ttk.Entry(input_frame, textvariable=D10_modifier_var)
    D10_modifier_entry.grid(column=4, row=4, padx=entry_padx)
    D10_button = ttk.Button(input_frame, text='ROLL', command=D10_roll)
    D10_button.grid(column=10, row=4, padx=button_padx, pady=std_pady)

    # D12 INPUT AND BUTTON
    D12_label = ttk.Label(input_frame, text='D12')
    D12_label.grid(column=1, row=5, padx=label_padx, pady=std_pady)
    D12_rolls = tk.IntVar()
    D12_spinbox = ttk.Spinbox(input_frame, from_=1, to=100, textvariable=D12_rolls, wrap=True)
    D12_spinbox.grid(column=2, row=5, padx=entry_padx, pady=std_pady)
    D12_result = tk.IntVar()
    D12_modifier_label = ttk.Label(input_frame, text='MODIFIER')
    D12_modifier_label.grid(column=3, row=5, padx=label_padx)
    D12_modifier_var = tk.StringVar()
    D12_modifier_entry = ttk.Entry(input_frame, textvariable=D12_modifier_var)
    D12_modifier_entry.grid(column=4, row=5, padx=entry_padx)
    D12_button = ttk.Button(input_frame, text='ROLL', command=D12_roll)
    D12_button.grid(column=10, row=5, padx=button_padx, pady=std_pady)

    # D20 INPUT AND BUTTON
    D20_label = ttk.Label(input_frame, text='D20')
    D20_label.grid(column=1, row=6, padx=label_padx, pady=std_pady)
    D20_rolls = tk.IntVar()
    D20_spinbox = ttk.Spinbox(input_frame, from_=1, to=100, textvariable=D20_rolls, wrap=True)
    D20_spinbox.grid(column=2, row=6, padx=entry_padx, pady=std_pady)
    D20_result = tk.IntVar()
    D20_modifier_label = ttk.Label(input_frame, text='MODIFIER')
    D20_modifier_label.grid(column=3, row=6, padx=label_padx)
    D20_modifier_var = tk.StringVar()
    D20_modifier_entry = ttk.Entry(input_frame, textvariable=D20_modifier_var)
    D20_modifier_entry.grid(column=4, row=6, padx=entry_padx)
    D20_button = ttk.Button(input_frame, text='ROLL', command=D20_roll)
    D20_button.grid(column=10, row=6, padx=button_padx, pady=std_pady)

    # D100 INPUT AND BUTTON
    D100_label = ttk.Label(input_frame, text='D100')
    D100_label.grid(column=1, row=7, padx=label_padx, pady=std_pady)
    D100_rolls = tk.IntVar()
    D100_spinbox = ttk.Spinbox(input_frame, from_=1, to=100, textvariable=D100_rolls, wrap=True)
    D100_spinbox.grid(column=2, row=7, padx=entry_padx, pady=std_pady)
    D100_result = tk.IntVar()
    D100_modifier_label = ttk.Label(input_frame, text='MODIFIER')
    D100_modifier_label.grid(column=3, row=7, padx=label_padx)
    D100_modifier_var = tk.StringVar()
    D100_modifier_entry = ttk.Entry(input_frame, textvariable=D100_modifier_var)
    D100_modifier_entry.grid(column=4, row=7, padx=entry_padx)
    D100_button = ttk.Button(input_frame, text='ROLL', command=D100_roll)
    D100_button.grid(column=10, row=7, padx=button_padx, pady=std_pady)

    # DX INPuT AND BUTTON
    DX_label = ttk.Label(input_frame, text='D')
    DX_label.grid(column=0, row=8, padx=0, pady=std_pady)
    DX_sides = tk.IntVar()
    DX_sides_entry = ttk.Entry(input_frame, textvariable=DX_sides, width=5)
    DX_sides_entry.grid(column=1, row=8, pady=std_pady)
    DX_rolls = tk.IntVar()
    DX_spinbox = ttk.Spinbox(input_frame, from_=1, to=100, textvariable=DX_rolls, wrap=True)
    DX_spinbox.grid(column=2, row=8, padx=entry_padx, pady=std_pady)
    DX_result = tk.IntVar()
    DX_modifier_label = ttk.Label(input_frame, text='MODIFIER')
    DX_modifier_label.grid(column=3, row=8, padx=label_padx)
    DX_modifier_var = tk.StringVar()
    DX_modifier_entry = ttk.Entry(input_frame, textvariable=DX_modifier_var)
    DX_modifier_entry.grid(column=4, row=8, padx=entry_padx)
    DX_button = ttk.Button(input_frame, text='ROLL', command=DX_roll)
    DX_button.grid(column=10, row=8, padx=button_padx, pady=std_pady)

    # FRAME FOR OUTPUTS
    output_frame = ttk.Frame(root)
    output_frame.grid(column=0, row=3)

    # RESULTS
    result_label_1 = ttk.Label(output_frame, text=f'RESULT:')
    result_label_1.grid(column=1, row=1, padx=label_padx, pady=std_pady)
    result_label_2 = ttk.Label(output_frame, textvariable=roll_result)
    result_label_2.grid(column=2, row=1)

    root.mainloop()
