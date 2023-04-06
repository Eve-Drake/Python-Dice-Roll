import tkinter as tk
from tkinter import *
from dice_roll import getNumberDice

root = tk.Tk()
root.title('Roll Dice')
root.geometry('600x400+50+50')

message = tk.Label(root, text="How many dice would you Like to roll?")
message.pack()

entry = Entry(root)
entry.pack()

root.mainloop()