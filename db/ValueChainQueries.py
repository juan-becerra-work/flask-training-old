import dbGADI

def getDataComponents(dbConnection):
    dbCursor = dbConnection.cursor
    lst = dbCursor.execute('SELECT * from dbo.CFG_Componentes')
    print("list of columns:")
    print(dbCursor.fieldnames)
    print('rowcount=' + str(dbCursor.rowcount))
    rows = dbCursor.fetchall()
    rows = dbCursor.fieldnames
    for x in rows:
        print(x)
        rows.append(x)
    
    return rows
