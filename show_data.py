import create_database_student_info
from create_database_student_info import *
import tkinter as tk
from tkinter import *
from tkinter import ttk


# def show_data():
#     cursor = connection.execute(" SELECT * FROM " + TABLE_NAME + ";")
#
#
#
#     for row in cursor:
#         print("Student id  :", row[0] ,end="")
#         print("    name  :", row[1],end="")
#         print("    address  :", row[2],end="")
#         print("    branch : ",row[3],end="")
#         print("    phone number :",row[4])




def show_data():

    secondWindow = tk.Tk()

    secondWindow.title("Display results")

    appLabel = tk.Label(secondWindow, text="Student Management System",
                        fg="#06a099", width=40)
    appLabel.config(font=("Sylfaen", 30))
    appLabel.pack()

    tree = ttk.Treeview(secondWindow)
    tree["columns"] = ("one", "two", "three", "four")

    tree.heading("one", text="Student Name")
    tree.heading("two", text="Address")
    tree.heading("three", text="Branch")
    tree.heading("four", text="Phone Number")

    cursor = connection.execute("SELECT * FROM " + TABLE_NAME + " ;")
    i = 0

    for row in cursor:
        tree.insert('', i, text="Student " + str(row[0]),
                    values=(row[1], row[2],
                            row[3], row[4]))
        i = i + 1

    tree.pack()
    secondWindow.mainloop()






