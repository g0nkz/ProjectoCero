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

#ESTA CLASE ESTA DESTINADA AL CONTROL DE LOS MENSAJES.
# class DBMessages:
#     def __init__(self, dbname="Data/Db/dbmessage.sqlite"):
#         self.dbname = dbname
#         self.conn = sqlite3.connect(dbname)
#
#     def setup(self):
#         tblstmt = "CREATE TABLE IF NOT EXISTS mensajes (UId int, Message text, Date int)"
#         UIdidx = "CREATE INDEX IF NOT EXISTS UIdIndex ON mensajes (UId ASC)"
#         Messagedidx = "CREATE INDEX IF NOT EXISTS MessageIndex ON mensajes (Message ASC)"
#         Dateidx = "CREATE INDEX IF NOT EXISTS DateIndex ON mensajes (Date ASC)"
#         self.conn.execute(tblstmt)
#         self.conn.execute(UIdidx)
#         self.conn.execute(Messagedidx)
#         self.conn.execute(Dateidx)
#         self.conn.commit()
#
#     def add_message(self, UId, Message, Date):
#         stmt = "Insert into mensajes (UId, Message, Date) values(?, ?, ?)"
#         args = (UId, Message, Date)
#         self.conn.execute(stmt, args)
#         self.conn.commit()
#
#     def delete_messageP(self):
#         stmt = "SELECT Date FROM mensajes"
#         for x in self.conn.execute(stmt):
#             Date = x[0]
#             ct = int(time.time())
#             a = ct - Date
#             if a > 86400:
#                 stmt = "DELETE FROM mensajes WHERE Date = (?)"
#                 args = (Date, )
#                 self.conn.execute(stmt, args)
#                 self.conn.commit()
#
#     def return_beforelastmessage(self, UId, desf):
#         stmt = "Select message from mensajes where UId = (?)"
#         args = (UId, )
#         alast = [x[0] for x in self.conn.execute(stmt, args)]
#         last = alast[-desf]
#         return last


# class DBBitso:
#     def __init__(self, dbname="Data/Db/dbbitso.sqlite"):
#         self.dbname = dbname
#         self.conn = sqlite3.connect(dbname)
#
#     def setup(self):
#         tblstmt = "CREATE TABLE IF NOT EXISTS bitso (UId int, Bitso0 text, Bitso1 text)"
#         UIdidx = "CREATE INDEX IF NOT EXISTS UIdIndex ON bitso (UId ASC)"
#         Bitso0idx = "CREATE INDEX IF NOT EXISTS Bitso0Index ON bitso (Bitso0 ASC)"
#         Bitso1idx = "CREATE INDEX IF NOT EXISTS Bitso1Index ON bitso (Bitso1 ASC)"
#         self.conn.execute(tblstmt)
#         self.conn.execute(UIdidx)
#         self.conn.execute(Bitso0idx)
#         self.conn.execute(Bitso1idx)
#         self.conn.commit()
#
#     def add_bitso(self, UId, Bitso0, Bitso1):
#         stmt = "Insert into bitso (UId, Bitso0, Bitso1) values(?, ?, ?)"
#         args = (UId, Bitso0, Bitso1)
#         self.conn.execute(stmt, args)
#         self.conn.commit()
#
#     def get_bitso(self, UId):
#         stmt = "SELECT * FROM bitso WHERE UId = (?)"
#         args = (UId, )
#         self.conn.execute(stmt, args)
#         self.conn.commit()
#
#     def delete_bitso(self, UId):
#         stmt = "DELETE FROM bitso WHERE UId = (?)"
#         args = (UId, )
#         self.conn.execute(stmt, args)
#         self.conn.commit()
