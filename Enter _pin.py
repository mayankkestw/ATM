from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
root = Tk()
root.geometry('700x700')
root.title('MDA-ATM')
head = Label(root,text='Mayank Gaurav Adarsh - ATM',bg='gray',fg='black')
head.config(font=("Courier", 30))
head.pack(side = "top", fill = "both", expand = "yes",padx=0,pady=50)
l1 = Label(root,text='TO CONTINUE',fg='yellow',pady=50)
l1.config(font=('Garamound',20))
l2 = Label(root,text='Enter pin',bg='yellow')

l1.pack()
l2.pack()
img = ImageTk.PhotoImage(Image.open("featured-image.png"))
panel = Label(root, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")
#root.after(50000,lambda :root.destroy())
root.mainloop()