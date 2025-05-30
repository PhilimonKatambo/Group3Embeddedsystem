import sqlite3

class DataBase:
    def __init__(self):
        self.conn = sqlite3.connect("Rooms.db")
        self.cursor = self.conn.cursor()

    def GetIntoDB(self,cardID,name,roomNumber):
            try:
                self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    cardID TEXT PRIMARY KEY,
                    name TEXT,
                    roomNumber TEXT
                )""")

                success = self.cursor.execute("INSERT INTO users VALUES (?,?,?)",
                                         (cardID, name, roomNumber))

                if success:
                    self.conn.commit()
                    self.conn.close()
                    return ("Successfully inserted user")

            except Exception as e:
                if (str(e) == "UNIQUE constraint failed: users.cardID"):
                    self.conn.close()
                    return ("User already exists\n")


    def RetriveDB(self):
        try:
            retrive= self.cursor.execute("SELECT * FROM users").fetchall()
            self.conn.close()
            return retrive
        except Exception as e:
            self.conn.close()
            return ("Failed to retrieve users")

    def Entrance(self,cardID,roomNumber):
        try:
            retrive = self.cursor.execute("SELECT roomNumber FROM users WHERE cardID = ?",(cardID,)).fetchall()
            if retrive[0][0] ==str(roomNumber):
                return True
            else:
                return False
        except Exception as e:
            return False