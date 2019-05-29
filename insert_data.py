import create_database_student_info
from create_database_student_info import *


def insert_data(name,address,branch,phone):
    connection.execute("INSERT INTO " + TABLE_NAME + "(" + STUDENT_NAME + " , " + STUDENT_ADDRESS + " , " + STUDENT_BRANCH + " , "
                       + STUDENT_PHONE + ") VALUES ('"+name+"','"+address+"','"+branch+"','"+phone+"');")

    connection.commit()


