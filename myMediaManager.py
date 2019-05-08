import os
import sqlite3

db_file = 'mediadb.db'

db_is_new = not os.path.exists(db_file)

connection = sqlite3.connect(db_file)
cursor = connection.cursor()

if db_is_new:
    print ('Creating schema')
    schema_filename = 'schema.sql'
    with open(schema_filename, 'rt') as sch:
        cursor.executescript(sch.read())
else:
    print ('Database exists')
    #cursor.execute("insert into test values ('testing this out')")
    #connection.commit()

    #cursor.execute("select * from test")
    #print(cursor.fetchone())

cursor.close()
connection.close()

print('What do you want to do?')
print('1. List')
print('2. Search')
print('3. Insert')
print('4. Delete')

while True:
    try:
        userinput = int(input())
        break
    except ValueError:
        print('Enter a number (1-4)')

#if userinput()
