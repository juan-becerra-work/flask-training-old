import dbGADI

q = "'"

def getDataComponents_all(dbConnection):
    FieldsList = 'ComponenteId, ComponenteNombre, ComponenteDescripcion'
    SQLSentence = 'SELECT DISTINCT ' + FieldsList + ' FROM CFG_Componentes'
    dbCursor = dbConnection.cursor
    lst = dbCursor.execute(SQLSentence)
    dataset = dbCursor.fetchall()
    rows = []
    for row in dataset:
        rows.append( [ row[0], row[1], row[2] ])
    return rows


def getDataComponents_one(dbConnection, DataComponentId):
    SQLSentence = 'SELECT ComponenteId, ComponenteNombre, ComponenteDescripcion FROM CFG_Componentes WHERE ComponenteId = ' + q + DataComponentId + q
    dbCursor = dbConnection.cursor
    lst = dbCursor.execute(SQLSentence)
#    print('rowcount=' + str(dbCursor.rowcount))
    dataset = dbCursor.fetchall()
    rows = []
    for row in dataset:
        rows.append( [ row[0], row[1],  row[2] ]) 
        # ComponenteId, ComponenteNombre, # ComponenteDescripcion
    return rows



def getEntityComponents_all(dbConnection, queryScope='all'):
    if queryScope == 'all':
        FieldsList = 'EntidadID, EntidadDescripcion, EntidadComentarios, ComponenteID, ComponenteNombre, ComponenteDescripcion'
    elif queryScope == 'id':
        FieldsList = 'EntidadID'
    else:
        return ([])
    SQLSentence = 'SELECT DISTINCT ' + FieldsList + ' FROM VW_CFG_EntidadComponentes'
    dbCursor = dbConnection.cursor
    lst = dbCursor.execute(SQLSentence)
    rows = []
    if queryScope == 'all':
        rows.append( [ dbCursor.fieldnames[0],  dbCursor.fieldnames[1], dbCursor.fieldnames[3],  dbCursor.fieldnames[4],  dbCursor.fieldnames[5] ]) 
    else:
        rows.append( [ dbCursor.fieldnames[0] ] )
    return rows
