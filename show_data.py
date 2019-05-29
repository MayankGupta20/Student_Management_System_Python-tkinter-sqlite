import create_database_student_info
from create_database_student_info import *


def show_data():
    cursor = connection.execute(" SELECT * FROM " + TABLE_NAME + ";")



    for row in cursor:
        print("Student id  :", row[0] ,end="")
        print("    name  :", row[1],end="")
        print("    address  :", row[2],end="")
        print("    branch : ",row[3],end="")
        print("    phone number :",row[4])



