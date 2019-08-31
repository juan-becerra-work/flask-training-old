
import adodbapi

import win32com.client
import pythoncom

from xml.dom import minidom
pythoncom.CoInitialize()



# ----------------------------------------------
# Connect to a SQLServer database
# ----------------------------------------------
def db_connect_MSSQLSERVER( \
    # Database service provider (ej. SQLOLEDB)
    dbProvider, \
    # Server name or IP address
    dbServer, \
    # Database user name
    dbUser, \
    # Database user password
    dbPassword, \
    # Database name, without brackets
    dbName) :

    conn_string = \
        'Provider=%s;\
        Data Source=%s;\
        Initial Catalog=%s;\
        User ID=%s;\
        Password=%s;\
        autocommit=True;' % \
        ( \
            dbProvider, \
            dbServer, \
            dbName, \
            dbUser, \
            dbPassword  \
        )

    conn = adodbapi.connect(conn_string)

    return (conn)
# ----------------------------------------------


# ----------------------------------------------
# Detele existing records by AttributeId
# ----------------------------------------------
def DeleteAttribute(dbConnection, dbTable, EntityId, AttributeId):

    cursor = dbConnection.cursor()

    sql = "DELETE FROM dbo.[" + dbTable + "] \
           WHERE EntidadID = '" + EntityId + \
          "' AND AtributoId = '" + \
          AttributeId + "';"
    cursor.execute(sql)
    dbConnection.commit()
# ----------------------------------------------


# ----------------------------------------------
# Detele all attributes
# ----------------------------------------------
def EmptyAttributes(dbConnection):

    cursor = dbConnection.cursor()

    sql = "DELETE FROM dbo.[CFG_Atributos] WHERE 1 = 1;"
    cursor.execute(sql)
    dbConnection.commit()
# ----------------------------------------------


# ----------------------------------------------
# Detele all entities
# ----------------------------------------------
def EmptyEntities(dbConnection):

    cursor = dbConnection.cursor()

    sql = "DELETE FROM dbo.[CFG_Entidades] WHERE 1 = 1;"
    cursor.execute(sql)
    dbConnection.commit()
# ----------------------------------------------


# ----------------------------------------------
# Detele all dependent entities
# ----------------------------------------------
def EmptyDependentEntities(dbConnection):

    cursor = dbConnection.cursor()

    sql = "DELETE FROM dbo.[CFG_EntidadesDependencias] WHERE 1 = 1;"
    cursor.execute(sql)
    dbConnection.commit()
# ----------------------------------------------


# ----------------------------------------------
# Detele existing records by EntityId
# ----------------------------------------------
def DeleteEntity(dbConnection, dbTable, EntityId):

    cursor = dbConnection.cursor()

    sql = "DELETE FROM dbo.[" + dbTable + "] \
        WHERE EntidadID = '" + EntityId + "';"
    cursor.execute(sql)
    dbConnection.commit()
# ----------------------------------------------


# ----------------------------------------------
# Insert new entity record
# ----------------------------------------------
def InsertEntityRecord(
      dbConnection,
      dbTable,
      EntityId,
      EntityName,
      EntityComments):

    cursor = dbConnection.cursor()

    with dbConnection:
        sql = "INSERT INTO dbo.[" + dbTable + "] (\
               EntidadID,           \
               EntidadDescripcion,  \
               EntidadComentarios   \
            ) VALUES ('" +         \
               EntityId + "', '" +    \
               EntityName + "', '" +  \
               EntityComments +       \
              "')"
        cursor.execute(sql)  # write the first row of data
        dbConnection.commit()
# ----------------------------------------------


# ----------------------------------------------
# Insert new attribute record
# ----------------------------------------------
def InsertAttributeRecord(
      dbConnection,
      dbTable,
      EntityId,
      AttributeId,
      AttributeDataType,
      AttributeDescription):

    cursor = dbConnection.cursor()

    with dbConnection:
        sql = "INSERT INTO dbo.[" + dbTable + "] (\
               EntidadID,               \
               AtributoID,              \
               AtributoTipoDatoId,      \
               AtributoDescripcion      \
            ) VALUES ('" +              \
               EntityId + "','" +          \
               AttributeId + "','" +       \
               AttributeDataType.strip() + "','" + \
               AttributeDescription +      \
              "')"
        cursor.execute(sql)  # write the first row of data
        dbConnection.commit()
# ----------------------------------------------


# ----------------------------------------------
# Insert new dependent entity record
# ----------------------------------------------
def InsertDependentEntityRecord(
      dbConnection,
      dbTable,
      EntityId,
      DependentEntityID):

    cursor = dbConnection.cursor()

    with dbConnection:
        sql = "INSERT INTO dbo.[" + dbTable + "] (\
               EntidadID,                         \
               EntidadDependienteID              \
            ) VALUES ('" +                        \
               EntityId + "','" +                 \
               DependentEntityID +                \
              "')"
        cursor.execute(sql)  # write the first row of data
        dbConnection.commit()
# ----------------------------------------------


# ----------------------------------------------
# Insert new task record
# ----------------------------------------------
def InsertTaskRecord( dbConnection, dbTableTasks, ProcessName, TaskId, TaskName ):

    cursor = dbConnection.cursor()

    with dbConnection:
        sql = "INSERT INTO dbo.[" + dbTableTasks + "] (ProcessName, TaskId, TaskName) values ('" + ProcessName + "', '" + TaskId + "', '" + TaskName + "')"
        cursor.execute(sql)  # write the first row of data
        dbConnection.commit()
# ----------------------------------------------


