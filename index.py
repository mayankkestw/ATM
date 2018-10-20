from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import sqlite3

Courier = ('Courier',17,'bold')
class Atm:
    def __init__(self,main):
        self.conn = sqlite3.connect('atm.db',timeout=100)
        self.login = False
        self.main = main
        self.top = Label(self.main,text='MGA-BANK',bg='#1f1c2c',fg='white',font=('Courier',30,'bold'))
        self.top.pack(fill=X)
        self.frame = Frame(self.main,bg='#2193b0',width=600,height=500)

        self.account = Label(self.frame,text='Account Number',bg="#728B8E",fg="white",font=Courier)
        self.accountEntry = Entry(self.frame,bg='#FFFFFF',highlightcolor="#50A8B0", highlightthickness=2, highlightbackground="white")
        self.pin = Label(self.frame,text='Pin',bg="#728B8E",fg="white",font=Courier)
        self.pinEntry = Entry(self.frame,bg='#FFFFFF',highlightcolor="#50A8B0", highlightthickness=2, highlightbackground="white")
        self.button = Button(self.frame,text='Login',bg='#1f1c2c',fg='white',font=('Courier',20,'bold'))
        self.quit = Button(self.frame,text='Quit',bg='#1f1c2c',fg='white',font=('Courier',20,'bold'),command=self.main.destroy)

        self.account.place(x=45,y=100,width=220,height=20)
        self.accountEntry.place(x=325,y=97,width=200,height=25)
        self.pin.place(x=45,y=180,width=220,height=20)
        self.pinEntry.place(x=325,y=180,width=200,height=25)
        self.button.place(x=240,y=260,width=100,height=30)
        self.quit.place(x=400,y=420,width=100,height=30)
        self.frame.pack()
main = Tk()
main.title('MGA-Bank')
main.geometry('700x600')
main.resizable(width=False, height=False)
icon = PhotoImage(file='bank.png')
main.tk.call('wm','iconphoto',main._w,icon)
interface = Atm(main)
main.mainloop()
