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
        self.button = Button(self.frame,text='Login',bg='#1f1c2c',fg='white',font=('Courier',20,'bold'),command=self.validate)
        self.quit = Button(self.frame,text='Quit',bg='#1f1c2c',fg='white',font=('Courier',20,'bold'),command=self.main.destroy)

        self.account.place(x=45,y=100,width=220,height=20)
        self.accountEntry.place(x=325,y=97,width=200,height=25)
        self.pin.place(x=45,y=180,width=220,height=20)
        self.pinEntry.place(x=325,y=180,width=200,height=25)
        self.button.place(x=240,y=260,width=100,height=30)
        self.quit.place(x=400,y=420,width=100,height=30)
        self.frame.pack()

    def fetch(self):
        self.list = []
        self.details = self.conn.execute('Select name, password, acc_no, type, balance from atm where acc_no = ?',(self.ac,))
        for i in self.details:
            self.list.append('Name = {}'.format(i[0]))
            self.list.append('Account no = {}'.format(i[2]))
            self.list.append('Type = {}'.format(i[3]))
            self.ac = i[2]
            self.list.append('Balance = {}'.format(i[4]))

    def validate(self):
        ac = False
        self.details = self.conn.execute('Select name, password, acc_no, type, balance from atm where acc_no = ?',(int(self.accountEntry.get()),))
        for i in self.details:
            self.ac = i[2]
            if i[2] == self.accountEntry.get():
                ac = True
            elif i[1] == self.pinEntry.get():
                ac = True
                m = '{}! Welcome to MGA-BANK'.format(i[0])
                self.fetch()
                messagebox._show("Login Info", m)
                self.frame.destroy()
                self.menu()
            else:
                ac = True
                m = " Login UnSucessFull ! Wrong Password"
                messagebox._show("Login Info!", m)

            if not ac:
                m = " Wrong Acoount Number !"
                messagebox._show("Login Info!", m)

    def menu(self):
        self.frame = Frame(self.main,bg='#2193b0',width=650 ,height=600)
        main.geometry('800x600')
        self.user_info = Button(self.frame,text='Account Info',bg='#1f1c2c',fg='white',font=('Courier',10,'bold'),command=self.account_details)
        self.balance_enquiry = Button(self.frame,text='Balance Enquiry',bg='#1f1c2c',fg='white',font=('Courier',10,'bold'),command=self.check)
        self.deposit = Button(self.frame,text='Deposit',bg='#1f1c2c',fg='white',font=('Courier',10,'bold'),command=self.deposit)
        self.withdraw = Button(self.frame,text='Withdrawal',bg='#1f1c2c',fg='white',font=('Courier',10,'bold'),command=self.withdraw)

        self.last = Button(self.frame,text='Last Transaction',bg='#1f1c2c',fg='white',font=('Courier',8,'bold'))
        self.changePin = Button(self.frame,text='Change Pin',bg='#1f1c2c',fg='white',font=('Courier',8,'bold'))

        self.quit = Button(self.frame, text='Quit', bg='#1f1c2c', fg='white', font=('Courier', 10, 'bold'),command=self.main.destroy)

        self.user_info.place(x=0,y=0,width=200,height=50)
        self.balance_enquiry.place(x=0,y=450,width=200,height=50)
        self.deposit.place(x=450,y=0,width=200,height=50)
        self.withdraw.place(x=450,y=450,width=200,height=50)
        self.last.place(x=0,y=240,width=130,height=50)
        self.changePin.place(x=530, y=240, width=130, height=50)
        self.quit.place(x=270,y=470,width=100,height=30)
        self.frame.pack()

    def account_details(self):
        self.fetch()
        display = self.list[0]+'\n'+self.list[1]+'\n'+self.list[2]
        self.label = Label(self.frame, text=display, font=('Courier',20,'bold'))
        self.label.place(x=200, y=180, width=300, height=100)

    def check(self):
        self.fetch()
        b = self.list[3]
        self.label = Label(self.frame, text=b, font=('Courier',20,'bold'))
        self.label.place(x=200, y=180, width=300, height=100)

    def deposit(self):
        self.amount = Entry(self.frame,bg='#FFFFFF',highlightcolor="#50A8B0", highlightthickness=2, highlightbackground="white")
        self.submitButton = Button(self.frame,text='Submit',bg='#1f1c2c',fg='white',font=('Courier',10,'bold'))

        self.amount.place(x=220,y=300,width=180,height=20)
        self.submitButton.place(x=420,y=300,width=100,height=20)
        self.submitButton.bind("<Button-1>",self.deposit_trans)

    def deposit_trans(self,flag):
        self.label = Label(self.frame,text='Transaction successfull!',font=('Courier',10,'bold'))
        self.label.place(x=200, y=180, width=300, height=100)
        self.conn.execute('Update atm set balance = balance+? where acc_no=?',(self.amount.get(),self.ac))
        self.conn.commit()

    def withdraw(self):
        self.amount = Entry(self.frame, bg='#FFFFFF', highlightcolor="#50A8B0", highlightthickness=2,
                            highlightbackground="white")
        self.submitButton = Button(self.frame, text='Submit', bg='#1f1c2c', fg='white', font=('Courier', 10, 'bold'))

        self.amount.place(x=220, y=300, width=180, height=20)
        self.submitButton.place(x=420, y=300, width=100, height=20)
        self.submitButton.bind("<Button-1>", self.with_trans)

    def with_trans(self,flag):
        self.label = Label(self.frame, text='Transaction successfull!', font=('Courier', 10, 'bold'))
        self.label.place(x=200, y=180, width=300, height=100)
        self.conn.execute('Update atm set balance = balance-? where acc_no=?', (self.amount.get(), self.ac))
        self.conn.commit()






main = Tk()
main.title('MGA-Bank')
main.geometry('700x600')
main.resizable(width=False, height=False)
icon = PhotoImage(file='bank.png')
main.tk.call('wm','iconphoto',main._w,icon)
interface = Atm(main)
main.mainloop()
