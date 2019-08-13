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
    connection = sqlite3.connect(db_file)
    cursor = connection.cursor()
    cursor.execute('SELECT {} FROM {}'.format(listToPrint[0],listToPrint[1]))

    result = cursor.fetchall()
    print("\nResult:")
    for res in result:
        print(res)
    cursor.close()
    connection.close()

def runSearch(searchFrom, searchFor):
    print('Searching: ' + str(searchFrom) + ' ' + searchFor)

    connection = sqlite3.connect(db_file)
    cursor = connection.cursor()
    cursor.execute('SELECT {} FROM {} WHERE {} LIKE "%{}%"'.format(searchFrom[0],searchFrom[1],searchFrom[2],searchFor))

    result = cursor.fetchall()
    for res in result:
        print(res)
    cursor.close()
    connection.close()

def insertToDatabase(table, name):
    #print('Adding: ' + str(name) + ' to ' + str(table))

    connection = sqlite3.connect(db_file)
    cursor = connection.cursor()
    cursor.execute('INSERT INTO {} ({}) VALUES (\'{}\')'.format(table[0],table[1],name))
    connection.commit()
    cursor.close()
    connection.close()

def dumpDatabaseContent():
    # https://stackoverflow.com/questions/4719159/python-and-sqlite3-importing-and-exporting-databases
    print('Attempting backup to file: dump.sql')
    connection = sqlite3.connect(db_file)
    with open('dump.sql', 'w') as file:
        for line in connection.iterdump():
            file.write('%s\n' % line)
