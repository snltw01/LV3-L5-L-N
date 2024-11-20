
import tkinter as tk
from tkinter import messagebox


class calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('500x500+100+50')
        self.title('Calculator')
        self.result=''
        self.content=tk.StringVar()
        self.Creat()

    def press(self,number):
        self.result=self.result+str(number)
        self.content.set(self.result)

    def get_result(self):
        print(eval(self.result))
        self.content.set(eval(self.result))


    def Creat(self):
        frame1=tk.Frame(self,bg='white')
        frame1.pack()

       

        en1=tk.Entry(frame1,textvariable=self.content,state='readonly')
        en1.grid(row=0,column=0,columnspan=5,padx=10)

        butC=tk.Button(frame1,text='C')
        butC.grid(row=4,column=0)

        but0=tk.Button(frame1,text='0',command=lambda: self.press(0))
        but0.grid(row=4,column=1)

        but1=tk.Button(frame1,text='1',command=lambda: self.press(1))
        but1.grid(row=3,column=0)

        but2=tk.Button(frame1,text='2',command=lambda: self.press(2))
        but2.grid(row=3,column=1)


        but3=tk.Button(frame1,text='3',command=lambda: self.press(3))
        but3.grid(row=3,column=2)


        but4=tk.Button(frame1,text='4',command=lambda: self.press(4))
        but4.grid(row=2,column=0)


        but5=tk.Button(frame1,text='5',command=lambda: self.press(5))
        but5.grid(row=2,column=1)


        but6=tk.Button(frame1,text='6',command=lambda: self.press(6))
        but6.grid(row=2,column=2)


        but7=tk.Button(frame1,text='7',command=lambda: self.press(7))
        but7.grid(row=1,column=0)


        but8=tk.Button(frame1,text='8',command=lambda: self.press(8))
        but8.grid(row=1,column=1)


        but9=tk.Button(frame1,text='9',command=lambda: self.press(9))
        but9.grid(row=1,column=2)

        but_plus=tk.Button(frame1,text="+",command=lambda: self.press('+'))
        but_plus.grid(row=4,column=4)

        but_minus=tk.Button(frame1,text="-",command=lambda: self.press('-'))
        but_minus.grid(row=3,column=4)

        but_divide=tk.Button(frame1,text="/",command=lambda: self.press('/'))
        but_divide.grid(row=2,column=4)

        but_multiplied=tk.Button(frame1,text="*",command=lambda: self.press('*'))
        but_multiplied.grid(row=1,column=4)

        but_count=tk.Button(frame1,text="=",command=self.get_result)
        but_count.grid(row=4,column=2)

cal1=calculator()
cal1.mainloop()