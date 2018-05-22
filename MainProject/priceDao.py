from MainProject.DBops import DBops
import pandas as pd
'''
This Database Access Object establishes a connection with our DB using the DBops class. It then uses this connection
to update the database tables with the prices of the cryptocurrencies.
'''

class priceDao:

    def __init__(self):
        self.DBops = DBops

    def connect(self):
        DBops().getDB()         # Establish a connection to the DB

    def updatePrice(self, name, price, readable_time):
        priceDao().connect()

        try:
            DBops.cnx.cursor().execute(
                f"INSERT INTO {name}Data ({name}_data,readable_{name}_time) VALUES (%s,%s)",
                (price, readable_time))

        finally:
            DBops.cnx.commit()
            DBops().disconnectDB()

    def selectPrice(self, cryptoName):
        priceDao().connect()
        # retrieve crypto values
        try:
            df = pd.read_sql(f"select {cryptoName}_data,readable_{cryptoName}_time from {cryptoName}Data ORDER BY readable_{cryptoName}_time",
                         con=DBops.cnx)
            return df
        finally:
            DBops().disconnectDB()

