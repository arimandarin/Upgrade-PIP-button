import os
from tkinter import *

root = Tk()

root.title("Upgrade PIP")


canvas1 = Canvas(root, width=300, height=350,
                    bg='pink', relief='raised')
canvas1.pack()

label1 =Label(root, text='Upgrade PIP', bg='pink')
label1.config(font=('Times New Roman', 20))
canvas1.create_window(150, 80, window=label1)


def upgradePIP():
    os.system('start cmd /k python.exe -m pip install --upgrade pip')


button1 = Button(text='      Upgrade PIP     ', command=upgradePIP,
                    bg='red', fg='white', font=('Times New Roman', 12, 'bold'))
canvas1.create_window(150, 180, window=button1)

root.mainloop()
