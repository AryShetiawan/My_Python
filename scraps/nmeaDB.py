#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Jon
#
# Created:     16/02/2013
# Copyright:   (c) Jon 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import pypyodbc

def getDescription(cursor):
    for line in cursor.description:
        print line

def getInfo(cursor):
##    get tables
    tables = cursor.tables()
    for table in tables:
        print table[2:4]
##        break
    try:
        print(cursor.statistics(table[2]))
    except pypyodbc.Error, err:
        pass
    print '-'*200
##  get columns
    for col in cursor.columns():
        print col[2:4]
        break
##  get statistics
##    print(cursor.statistics)

def getConnect(path_to_db):
##    Then you can continue to use pypyodbc to connect to those mdb files and manipulate them with ODBC interface
    db = pypyodbc.connect(u'''Driver={Microsoft Access Driver (*.mdb)};DBQ='''+path_to_db,
    unicode_results = True, readonly = True)
    return db

def getCursor(db):
    cursor = db.cursor()
    return cursor

def prinRows(rows):
    for row in rows:
        print row
##        break

def exmpleQuery(cursor, query = 'SELECT * FROM Type_Tbl;'):
    rows = cursor.execute(query).fetchall()
    prinRows(rows)

def getCount(cursor):
    cursor.execute("SELECT count(*) AS id_count FROM IDRef_Tbl")# WHERE user_id < 100")
    row = cursor.fetchone()
    print row#, cursor.__dict__

def runQuery(cursor, query):
    '''cursor is now iterable?'''
    cursor.execute(query)
    return cursor


def db_exit(cursor, db):
    cursor.close()
##    db.commit() #not writing
    db.close()


##    Finally, To compact an existing Access mdb file
##    pypyodbc.win_compact_mdb("D:\\The path to the original to be compacted mdb file",
##    "D:\\The path to put the compacted new mdb file")
joinQuery = '''
select * from [DF#_Tbl] inner join [DD#_Tbl] on (DF#_Tbl.[df #] = DD#_Tbl.[df #])
'''

def main():
    db = getConnect('nmea.mdb')
    cursor = getCursor(db)
##    getInfo(cursor)
##    getCount(cursor)
##    getDescription(cursor)
##    exmpleQuery(cursor)
##    print(runQuery(cursor,"SELECT * FROM IDRef_Tbl ").fetchall())
##    print(runQuery(cursor,'select * from Type_Tbl').fetchone())
    rows = runQuery(cursor,joinQuery)#.fetchone()
    prinRows(rows)
##    print(runQuery(cursor,'select * from DD#_Tbl').fetchone())
##    print(runQuery(cursor,'select * from IDRef_Tbl').fetchone())
##    print(runQuery(cursor,'select * from IDRef_Detail_Tbl').fetchone())


    db_exit(cursor, db)
if __name__ == '__main__':
    main()
