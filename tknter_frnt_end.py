import tkinter as tk
from tkinter import messagebox

import insert_data
from insert_data import *
import show_data
from  show_data import *

mainWindow = tk.Tk()
mainWindow.title(' Student_Info')

Name_label = tk.Label(mainWindow,text =' Name ',padx='20',pady='20')
Name_label.grid(row=0,column=0)

name = tk.Entry(mainWindow)
name.grid(row=0,column=1,padx=20,pady=20)

Address_label = tk.Label(mainWindow,text = ' Address ' ,padx='20',pady ='20')
Address_label.grid(row=1,column=0)

address = tk.Entry(mainWindow)
address.grid(row=1,column=1,padx=20,pady=20)

Branch_label = tk.Label(mainWindow,text = ' Branch ' ,padx='20',pady ='20')
Branch_label.grid(row=2,column=0)

branch = tk.Entry(mainWindow)
branch.grid(row=2,column=1,padx=20,pady=20)

Phone_label = tk.Label(mainWindow,text = ' Phone Number ' ,padx='20',pady ='20')
Phone_label.grid(row=3,column=0)

phone = tk.Entry(mainWindow)
phone.grid(row=3,column=1,padx=20,pady=20)

def get_value():
    s_name = name.get()
    s_address = address.get()
    s_branch = branch.get()
    s_phone = phone.get()
    insert_data(s_name, s_address, s_branch, s_phone)




button_insert =tk.Button(mainWindow,text='INSERT',bg = 'seashell2',command =lambda: get_value() )
button_insert.grid(row=4,column=0,padx=10,pady=10)

button_show = tk.Button(mainWindow,text='SHOW',bg = 'seashell2',command =lambda :show_data())
button_show.grid(row=4,column=1,padx=10,pady=10)


mainWindow.mainloop()