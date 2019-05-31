import tkinter as tk
from tkinter import messagebox

import insert_data
from insert_data import *
import show_data
from  show_data import *

mainWindow = tk.Tk()
mainWindow.configure(background = 'alice blue')
mainWindow.title(' Student_Info')


title_label = tk.Label(mainWindow,text='Student Management System ',font=("Sylfaen",30),fg ='red',padx='30',pady='30',width='40',bg='alice blue')
title_label.grid(row=0,columnspan=2)


Name_label = tk.Label(mainWindow,text =' Name ',padx='20',pady='20',bg='alice blue')
Name_label.grid(row=1,column=0)

name = tk.Entry(mainWindow)
name.grid(row=1,column=1,padx=20,pady=20)

Address_label = tk.Label(mainWindow,text = ' Address ' ,padx='20',pady ='20',bg='alice blue')
Address_label.grid(row=2,column=0)

address = tk.Entry(mainWindow)
address.grid(row=2,column=1,padx=20,pady=20)

Branch_label = tk.Label(mainWindow,text = ' Branch ' ,padx='20',pady ='20',bg='alice blue')
Branch_label.grid(row=3,column=0)

branch = tk.Entry(mainWindow)
branch.grid(row=3,column=1,padx=20,pady=20)

Phone_label = tk.Label(mainWindow,text = ' Phone Number ' ,padx='20',pady ='20',bg='alice blue')
Phone_label.grid(row=4,column=0)

phone = tk.Entry(mainWindow)
phone.grid(row=4,column=1,padx=20,pady=20)

def get_value():
    s_name = name.get()
    s_address = address.get()
    s_branch = branch.get()
    s_phone = phone.get()
    insert_data(s_name, s_address, s_branch, s_phone)
    name.delete(0,END)
    address.delete(0,END)
    branch.delete(0,END)
    phone.delete(0,END)

def show():
    mainWindow.destroy()
    show_data()




button_insert =tk.Button(mainWindow,text='INSERT',bg = 'rosy brown',command =lambda: get_value() )
button_insert.grid(row=5,column=0,padx=10,pady=15)

button_show = tk.Button(mainWindow,text='SHOW',bg = 'rosy brown',command =lambda :show())
button_show.grid(row=5,column=1,padx=10,pady=15)


mainWindow.mainloop()
