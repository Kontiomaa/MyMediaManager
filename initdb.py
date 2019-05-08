import os
import sqlite3

def initdb():
    db_file = 'mediadb.db'
    db_is_new = not os.path.exists(db_file)

    if db_is_new:
        connection = sqlite3.connect(db_file)
        cursor = connection.cursor()

        print ('Creating db from schema')
        schema_filename = 'schema.sql'
        with open(schema_filename, 'rt') as sch:
            cursor.executescript(sch.read())
    else:
        print ('Database exists')

    cursor.close()
    connection.close()
