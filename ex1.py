from tkinter import *
from tkinter import ttk
from tkinter import messagebox
root = Tk()


def button_Pressed(buttonnumber):
    temp = buttonnumber

# define size of display
root.geometry('650x496')

# define a lot of the buttons acoriding to project
button1 = ttk.Button(root, text=" ", command=lambda: button_Pressed(1))
button1.grid(row=0, column=0, ipadx=70, ipady=70)

button2 = ttk.Button(root, text=" ", command=lambda: button_Pressed(2))
button2.grid(row=0, column=1, ipadx=70, ipady=70)

button3 = ttk.Button(root, text=" ", command=lambda: button_Pressed(3))
button3.grid(row=0, column=2, ipadx=70, ipady=70)

button4 = ttk.Button(root, text=" ", command=lambda: button_Pressed(4))
button4.grid(row=1, column=0, ipadx=70, ipady=70)

button5 = ttk.Button(root, text=" ", command=lambda: button_Pressed(5))
button5.grid(row=1, column=1, ipadx=70, ipady=70)

button6 = ttk.Button(root, text=" ", command=lambda: button_Pressed(6))
button6.grid(row=1, column=2, ipadx=70, ipady=70)

button7 = ttk.Button(root, text=" ", command=lambda: button_Pressed(7))
button7.grid(row=2, column=0, ipadx=70, ipady=70)

button8 = ttk.Button(root, text=" ", command=lambda: button_Pressed(8))
button8.grid(row=2, column=1, ipadx=70, ipady=70)

button9 = ttk.Button(root, text=" ", command=lambda: button_Pressed(1))
button9.grid(row=2, column=2, ipadx=70, ipady=70)
root.mainloop()