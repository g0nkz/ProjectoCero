import sqlite3
import time

#ESTA CLASE ESTA DESTINADA AL CONTROL DE USUARIOS.
class DBUsers:
    def __init__(self, dbname='Data/Db/dbusers.sqlite'):
        self.dbname = dbname
        self.conn = sqlite3.connect(dbname, uri= True)

    def setup(self):
        tblstmt = "CREATE TABLE IF NOT EXISTS users (UId int, IsBot text, FirstName text, LastName text, LanguageCode text)"
        UIdidx = "CREATE INDEX IF NOT EXISTS UIdIndex ON users (UId ASC)"
        IsBotidx = "CREATE INDEX IF NOT EXISTS IsBotIndex ON users (IsBot ASC)"
        FirstNameidx = "CREATE INDEX IF NOT EXISTS FirstNameIndex ON users (FirstName ASC)"
        LastNameidx = "CREATE INDEX IF NOT EXISTS LastNameIndex ON users (LastName ASC)"
        LanguageCodeidx = "CREATE INDEX IF NOT EXISTS LanguageCodeIndex ON users (LanguageCode ASC)"
        self.conn.execute(tblstmt)
        self.conn.execute(UIdidx)
        self.conn.execute(IsBotidx)
        self.conn.execute(FirstNameidx)
        self.conn.execute(LastNameidx)
        self.conn.execute(LanguageCodeidx)
        self.conn.commit()

    def add_user(self, UId, IsBot, FirstName, LastName, LanguageCode):
        stmt = "Insert into users (UId, IsBot, FirstName, LastName, LanguageCode) values(?, ?, ?, ?, ?)"
        args = (UId, IsBot, FirstName, LastName, LanguageCode)
        self.conn.execute(stmt, args)
        self.conn.commit()

    def get_users(self):
        stmt = "Select UId from users"
        return [x[0] for x in self.conn.execute(stmt)]
