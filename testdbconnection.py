import mysql.connector
from mysql.connector import errorcode
import time
import config
def testconnection():
    try:
        cnx = mysql.connector.connect(user=config.User, password=config.password,
                                      host=config.host,
                                      database=config.database,
                                      charset=config.charset)
    except mysql.connector.Error as err:
      if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
      elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
      else:
        print(err)
    else:
      cnx.close()

testconnection()