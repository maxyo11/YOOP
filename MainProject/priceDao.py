from MainProject.DBops import DBops

'''
This Database Access Object establishes a connection with our DB using the DBops class. It then uses this connection
to update the database tables with the prices of the cryptocurrencies.
'''

class priceDao:

    def __init__(self):
        self.DBops = DBops

    def connect(self):
        DBops().getDB()

    def updatePrice(self, name, price, readable_time):
        priceDao().connect()

        try:
            DBops.cnx.cursor().execute(
                f"INSERT INTO {name}Data ({name}_data,readable_{name}_time) VALUES (%s,%s)",
                (price, readable_time))

        finally:
            DBops.cnx.commit()




