import dbGADI

q = "'"

def getDataComponents_all(dbConnection):
    SQLSentence = 'SELECT ComponenteId, ComponenteNombre, ComponenteDescripcion FROM CFG_Componentes'
    dbCursor = dbConnection.cursor
    lst = dbCursor.execute(SQLSentence)
#    print('rowcount=' + str(dbCursor.rowcount))
    dataset = dbCursor.fetchall()
    rows = []
    for row in dataset:
        rows.append( [ row[0], row[1],  row[2] ]) 
        # ComponenteId, ComponenteNombre, # ComponenteDescripcion
    return rows


def getDataComponents_one(dbConnection, DataComponentId):
    SQLSentence = 'SELECT ComponenteId, ComponenteNombre, ComponenteDescripcion FROM CFG_Componentes WHERE ComponenteId = ' + q + DataComponentId + q
    print (SQLSentence)
    dbCursor = dbConnection.cursor
    lst = dbCursor.execute(SQLSentence)
#    print('rowcount=' + str(dbCursor.rowcount))
    dataset = dbCursor.fetchall()
    rows = []
    for row in dataset:
        rows.append( [ row[0], row[1],  row[2] ]) 
        # ComponenteId, ComponenteNombre, # ComponenteDescripcion
    return rows



def getEntityComponents_all(dbConnection, scope='all'):
    if scope == 'all':
        FieldsList = 'EntidadID, EntidadDescripcion, EntidadComentarios, ComponenteID, ComponenteNombre, ComponenteDescripcion'
    elif scope == 'id':
        FieldsList = 'EntidadID'
    else:
        return ([])
    SQLSentence = 'SELECT DISTINCT ' + FieldsList + ' FROM VW_CFG_EntidadComponentes'
    dbCursor = dbConnection.cursor
    lst = dbCursor.execute(SQLSentence)
    dataset = dbCursor.fetchall()
    rows = []
    for row in dataset:
        if scope == 'all':
            rows.append( [ row[0], row[1], row[2], row[3], row[4], row[5] ]) 
        else:
            rows.append( [ row[0] ] )
    return rows


    