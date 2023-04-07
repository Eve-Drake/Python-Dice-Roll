import tkinter as tk
from tkinter import *
from dice_roll import getNumberDice
from dice_roll import diceRoll

root = tk.Tk()
root.title('Roll Dice')
root.geometry('600x400+50+50')

button = tk.Button(root, text='Roll Dice', command=diceRoll(2))
button.pack()

root.mainloop()