import create_database_student_info
from create_database_student_info import *
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

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

def insert_data(name,address,branch,phone):
    connection.execute("INSERT INTO " + TABLE_NAME + "(" + STUDENT_NAME + " , " + STUDENT_ADDRESS + " , " + STUDENT_BRANCH + " , "
                       + STUDENT_PHONE + ") VALUES ('"+name+"','"+address+"','"+branch+"','"+phone+"');")


    connection.commit()
    messagebox.showinfo('','Inserted successfully ')



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

def delete(name):
    # cursor = connection.execute("SELECT * FROM " + TABLE_NAME + " WHERE "+ STUDENT_NAME +" = ? ",(name,) )
    # for row in cursor:
    #     print(row)

    connection.execute(" DELETE FROM " + TABLE_NAME + " WHERE "+ STUDENT_NAME +" = ? ",(name,))
    connection.commit()
    messagebox.showinfo('','Delted Successfully')



def search(name):

    srch_window = tk.Tk()
    srch_window.title(' Search Data')

    search_label = tk.Label(srch_window,text= ' Searched Data')
    search_label.pack()

    tree1 = ttk.Treeview(srch_window)
    tree1["columns"]=("one", "two", "three", "four")
    tree1.heading("one", text="Student Name")
    tree1.heading("two", text="Address")
    tree1.heading("three", text="Branch")
    tree1.heading("four", text="Phone Number")

    i=0
    cursor = connection.execute("  SELECT * FROM " + TABLE_NAME + " WHERE " + STUDENT_NAME + " = ? ;", (name,))
    # for row in cursor:
    #      print(row)

    for row in cursor:
        tree1.insert('', i, text="Student "+ str(row[0]),
                        values=(row[1],row[2],
                                row[3],row[4]))

        i = i+1

    tree1.pack()
    srch_window.mainloop()



    # works with both with and without semicolon  ???????
    # see in update and delete query





