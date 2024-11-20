
import tkinter as tk
from tkinter import messagebox
import random as r
root=tk.Tk()

def info():
    number=r.randint(0,1000)
    content.set(number)
    messagebox.showinfo('info',en1.get())

content=tk.StringVar()
en1=tk.Entry(root,textvariable=content)
en1.pack()

but1=tk.Button(root,text='Press me',command=info)
but1.pack()


root.mainloop()