import mysql.connector
import mysql.connector.errorcode
import config

'''
This Class allows us to connect to the Database. The necessary information user, password and so on is stored in the
config.py file. We have added a testConnection method. This allows us to do troubleshooting if we ever fail to connect
to the database.
'''

class DBops:
    def __init__(self, db_name=config.database, user=config.User, password=config.password, cnx=None):
        self.db_name = db_name
        self.user = user
        self.password = password
        DBops.DB_Flag = False
        DBops.cnx = cnx

    def getConnection(self):
        if not DBops.DB_Flag:
            DBops.cnx = self.connectDB()
        return DBops.cnx

    def connectDB(self):
        if not DBops.DB_Flag:
            DBops.cnx = mysql.connector.connect(user=config.User, password=config.password,
                                          host=config.host,
                                          database=config.database,
                                          charset=config.charset)
            DBops.DB_Flag = True
        return DBops.cnx

    def disconnectDB(self):
        if DBops.DB_Flag:
            DBops.cnx.cursor.close()
            DBops.cnx.close()
            DBops.DB_Flag = False

    # Why do i need this?
    def getDB(self):
        if DBops.DB_Flag:
            return self
        else:
            self.getConnection()
            return self

    def testConnection(self):
        try:
            DBops().getDB()

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)

        else:
            DBops.cnx.close()




