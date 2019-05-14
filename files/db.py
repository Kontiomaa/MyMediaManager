import os
import sqlite3

db_file = 'mediadb.db'

def initdb():
    db_is_new = not os.path.exists(db_file)

    if db_is_new:
        connection = sqlite3.connect(db_file)
        cursor = connection.cursor()

        print ('Creating db from schema')
        schema_filename = 'files/schema.sql'
        with open(schema_filename, 'rt') as sch:
            cursor.executescript(sch.read())

        cursor.close()
        connection.close()
    else:
        print ('Database exists')

def requestList(listToPrint):
    #print('db params:')
    #print(listToPrint)

    connection = sqlite3.connect(db_file)
    cursor = connection.cursor()
    cursor.execute('SELECT {} FROM {}'.format(listToPrint[0],listToPrint[1]))

    result = cursor.fetchall()
    for res in result:
        print(res)
    cursor.close()
    connection.close()
