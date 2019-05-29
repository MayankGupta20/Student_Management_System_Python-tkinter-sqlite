import sqlite3

connection = sqlite3.connect('Student_Informaion')

TABLE_NAME ='student_info'
STUDENT_ID ='student_id'
STUDENT_NAME ='student_name'
STUDENT_ADDRESS ='student_address'
STUDENT_BRANCH ='student_branch'
STUDENT_PHONE = 'student_phone'

connection.execute('CREATE TABLE IF NOT EXISTS '+TABLE_NAME+' ( ' +STUDENT_ID+ ' INTEGER PRIMARY KEY AUTOINCREMENT ,'+
                   STUDENT_NAME+' TEXT, '+ STUDENT_ADDRESS +' TEXT, '+ STUDENT_BRANCH + ' TEXT,'+STUDENT_PHONE + ' TEXT);')


