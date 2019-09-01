import win32com.client
import GADI_lib_file
import getpass


connection = win32com.client.Dispatch(r'ADODB.Connection')


# ----------------------------------------------
# CONNECT TO DATABASE
# ----------------------------------------------
def ConnectToDatabase():
    global conn
    global dbUser
    global ACDParameters

    # GADI_lib_file.GetParametersFromFile()
    ACDParameters = GADI_lib_file.GetParametersFromFile()

    # Ask for database user password
    InputMessage = "Enter password for user " + ACDParameters.get("dbUser") + \
        " in the database " + ACDParameters.get("dbName") + "(" + \
        ACDParameters.get("dbServer") + "): "
    # ************************************************dbPassword = getpass.getpass(InputMessage)
    dbPassword = 'Arkitectura29'

    # Connect to a SQLServer database
    conn = db_connect_MSSQLSERVER(
           ACDParameters.get("dbServer"),
           ACDParameters.get("dbUser"),
           dbPassword, 
           ACDParameters.get("dbName"))

    return (conn)
    # ----------------------------------------------
# ----------------------------------------------



#Constants
adStateOpen = 1


class Connection:
    def __init__(self, servername, username='', password='', db=''):
        self.connection = connection;
        self.version = '';
        self.servername = servername;
        self.username = username;
        self.password = password;
        self.defdb = db;
        self.constr = '';
        if db == '':
            self.defdb = 'master'
        self.connected = 0

        if username == '':
            self.constr = "Provider=SQLOLEDB.1;Data Source=" + self.servername + ";Trusted_Connection=yes; database=" + self.defdb
        else:
            self.constr = "Provider=SQLOLEDB.1;Data Source=" + self.servername + ";uid=" + username + ";pwd=" + password + "; database=" + self.defdb

        #test connection:
        s = "set nocount on select name from master..syslogins where name = 'sa'"
        connection.Open(self.constr)
        if connection.State == adStateOpen:
            self.connected = 1

        try:
            c = Cursor()
            c.servername = servername
            c.username = username
            c.password = password
            c.defdb = db
            c.constr = self.constr
            self.cursor = c
        except IndexError:
            self.connected = 0
            print("Could not connect")

    def commit(self):
        "this is here for compatibility"
        pass

    def close(self):
        self = None
        return self


class Cursor:
    def __init__(self):
        self.records = []
        self.rowid = 0
        self.fieldnames = []
   
    def execute(self,sql):
        self.recordset = connection.execute(sql)
        self.records = []
        self.fieldnames = []

        for x in range(self.recordset.Fields.Count):
            self.fieldnames.append(self.recordset.Fields.Item(x).Value)

        #Need the try for not select type of sql, like updates, inserts
        values_list = []
        try:
            data = self.recordset.GetRows()
            self.rowcount = len(data[0])
            for y in range(0, self.rowcount):
                for x in data:
                    values_list.append(x[y])
                self.records.append(tuple(values_list))
                values_list = []
            self.records = tuple(self.records)
        except UnboundLocalError:
            pass
        except:
            pass

    def fetchall(self):
        lst = []
        try:
            for x in self.records:
                lst.append(x)
        except IndexError:
            pass
        return lst

    def fetchone(self):
        i = self.rowid
        j = i + 1
        self.rowid = j
        try:
            return tuple(self.records[i])
        except IndexError:
            pass


def db_connect_MSSQLSERVER( \
    # Server name or IP address
    dbServer, \
    # Database user name
    dbUser, \
    # Database user password
    dbPassword, \
    # Database name, without brackets
    dbName) :

    #conn = adodbapi.connect(conn_string)
    SQLServerConnection = Connection(dbServer, dbUser, dbPassword, db=dbName)
    if SQLServerConnection.connected == 1:
        print("Connected OK to database " + dbName + " in server " + dbServer)
        return (SQLServerConnection)
    else:
        return None

def ConnectDatabaseTest():
    c = Connection('172.17.97.18', 'svcarq', 'Arkitectura29', db='RULES')
    # print("Connection string: " + c.constr)
    if c.connected == 1:
        print("Connected OK")
    cu = c.cursor
    lst = cu.execute('select * from RUL_Rule')
    print("list of columns:")
    print(cu.fieldnames)
    print('rowcount=' + str(cu.rowcount))
    # print('select * from RUL_Rule')
    rows = cu.fetchall()
    for x in rows:
        print(x)

    print('Bringing records one by one')
    cu.rowid = 1
    rows = cu.fetchone()
    print(rows[0])
    rows = cu.fetchone()
    # print(rows)

    c.close()

if __name__ == '__main__':
    print ('Hello from test ...')