from MainProject.DBops import DBops


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




