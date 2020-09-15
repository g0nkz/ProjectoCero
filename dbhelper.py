import sqlite3
import time

#ESTA CLASE ESTA DESTINADA AL CONTROL DE USUARIOS.
class DBUsers:
    def __init__(self, dbname='Data/Db/dbusers.sqlite'):
        self.dbname = dbname
        self.conn = sqlite3.connect(dbname, uri= True)

    def setup(self):
        tblstmt = "CREATE TABLE IF NOT EXISTS users (UID int, IsBot text, FirstName text, LastName text, LanguageCode text, Timer int, Time int)"
        UIDidx = "CREATE INDEX IF NOT EXISTS UIDIndex ON users (UID ASC)"
        IsBotidx = "CREATE INDEX IF NOT EXISTS IsBotIndex ON users (IsBot ASC)"
        FirstNameidx = "CREATE INDEX IF NOT EXISTS FirstNameIndex ON users (FirstName ASC)"
        LastNameidx = "CREATE INDEX IF NOT EXISTS LastNameIndex ON users (LastName ASC)"
        LanguageCodeidx = "CREATE INDEX IF NOT EXISTS LanguageCodeIndex ON users (LanguageCode ASC)"
        Timeridx = "CREATE INDEX IF NOT EXISTS TimerIndex ON users (Timer ASC)"
        Timeidx = "CREATE INDEX IF NOT EXISTS TimeIndex ON users (Time ASC)"
        self.conn.execute(tblstmt)
        self.conn.execute(UIDidx)
        self.conn.execute(IsBotidx)
        self.conn.execute(FirstNameidx)
        self.conn.execute(LastNameidx)
        self.conn.execute(LanguageCodeidx)
        self.conn.execute(Timeridx)
        self.conn.execute(Timeidx)
        self.conn.commit()

    def add_user(self, UID, IsBot, FirstName, LastName, LanguageCode, Timer, Time):
        stmt = "INSERT INTO users (UID, IsBot, FirstName, LastName, LanguageCode, Timer, Time) values(?, ?, ?, ?, ?, ?, ?)"
        args = (UID, IsBot, FirstName, LastName, LanguageCode, Timer, Time)
        self.conn.execute(stmt, args)
        self.conn.commit()

    def get_users(self):
        stmt = "SELECT UID FROM users"
        return [x[0] for x in self.conn.execute(stmt)]

    def SetTimer(self, TimerParam, UID, Time):
        stmt = "UPDATE users SET Timer = (?), Time = (?) WHERE UID = (?)"
        args = (TimerParam, Time, UID)
        self.conn.execute(stmt, args)
        self.conn.commit()

    def CheckTime(self, UID):
        cur = self.conn.cursor()
        stmt = "SELECT Timer FROM users WHERE UID = (?)"
        args = (UID,)
        return [x[0] for x in self.conn.execute(stmt, args)]
