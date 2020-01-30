from tkinter import *
from tkinter import ttk
from tkinter import messagebox
root = Tk()

player = 1


def button_Pressed(buttonnumber):
    global player

    if buttonnumber == 1 and player == 1:
        button1.config(text='X')
        player = 2
    elif buttonnumber == 1 and player == 2:
        button1.config(text='O')
        player = 1

    elif buttonnumber == 2 and player == 1:
        button2.config(text='X')
        player = 2
    elif buttonnumber == 2 and player == 2:
        button2.config(text='O')
        player = 1

    elif buttonnumber == 3 and player == 1:
        button3.config(text='X')
        player = 2
    elif buttonnumber == 3 and player == 2:
        button3.config(text='O')
        player = 1

    elif buttonnumber == 4 and player == 1:
        button4.config(text='X')
        player = 2
    elif buttonnumber == 4 and player == 2:
        button4.config(text='O')
        player = 1

    elif buttonnumber == 5 and player == 1:
        button5.config(text='X')
        player = 2
    elif buttonnumber == 5 and player == 2:
        button5.config(text='O')
        player = 1

    elif buttonnumber == 6 and player == 1:
        button6.config(text='X')
        player = 2
    elif buttonnumber == 6 and player == 2:
        button6(text='O')
        player = 1
    elif buttonnumber == 7 and player == 1:
        button7.config(text='X')
        player = 2
    elif buttonnumber == 7 and player == 2:
        button7.config(text='O')
        player = 1

    elif buttonnumber == 8 and player == 1:
        button8.config(text='X')
        player = 2
    elif buttonnumber == 8 and player == 2:
        button8.config(text='O')
        player = 1

    elif buttonnumber == 9 and player == 1:
        button9.config(text='X')
        player = 2
    elif buttonnumber == 9 and player == 2:
        button9.config(text='O')
        player = 1



#define size of display
root.geometry('650x496')

# define a lot of the buttons according to project
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

button9 = ttk.Button(root, text=" ", command=lambda: button_Pressed(9))
button9.grid(row=2, column=2, ipadx=70, ipady=70)
root.mainloop()