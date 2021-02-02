import sqlite3
import time

#ESTA CLASE ESTA DESTINADA AL CONTROL DE USUARIOS.
class DBUsers:
    def __init__(self, dbname='Data/Db/users.sqlite'):
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
        stmt = "INSERT INTO users (UID, IsBot, FirstName, LastName, LanguageCode, Timer, Time) VALUES(?, ?, ?, ?, ?, ?, ?)"
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

class DBBitso:
    def __init__(self, dbname='Data/Db/bitso.sqlite'):
        self.dbname = dbname
        self.conn = sqlite3.connect(dbname, uri= True)

    def BitsoSetup(self):
        ABtblstmt = "CREATE TABLE IF NOT EXISTS AvailableBooks (BId int, Book text)"
        TItblstmt = "CREATE TABLE IF NOT EXISTS Ticker (High float, Last float, Created_At text, Book text, Volume float, VWAP float, Low float, Ask float, Bid float, Change_24 float)"
        OBtblstmt = "CREATE TABLE IF NOT EXISTS OrderBook (Updated_At text, Sequence int, Side text, Book text, Price float, Amount float)"
        TRtblstmt = "CREATE TABLE IF NOT EXISTS Trades (Book text, Created_At text, Amount float, Maker_Side text, Price float, TId int)"
        BIdIdx = "CREATE INDEX IF NOT EXISTS BIDIndex ON AvailableBooks (BID ASC)"
        Bookidx = "CREATE INDEX IF NOT EXISTS IsBotIndex ON AvailableBooks (Book ASC)"
        HighIdx = "CREATE INDEX IF NOT EXISTS HighIndex ON Ticker (High ASC)"
        LastIdx = "CREATE INDEX IF NOT EXISTS LastIndex ON Ticker (Last ASC)"
        CreatedAtIdx = "CREATE INDEX IF NOT EXISTS Created_AtIndex ON Ticker (Created_At ASC)"
        TickerBookIdx = "CREATE INDEX IF NOT EXISTS BookIndex ON Ticker (Book ASC)"
        VolumeIdx = "CREATE INDEX IF NOT EXISTS VolumeIndex ON Ticker (Volume ASC)"
        VWAPIdx= "CREATE INDEX IF NOT EXISTS VWAPIndex ON Ticker (VWAP ASC)"
        LowIdx = "CREATE INDEX IF NOT EXISTS LowIndex ON Ticker (Low ASC)"
        AskIdx = "CREATE INDEX IF NOT EXISTS AskIndex ON Ticker (Ask ASC)"
        BidIdx = "CREATE INDEX IF NOT EXISTS BidIndex ON Ticker (Bid ASC)"
        Change_24Idx = "CREATE INDEX IF NOT EXISTS Change_24Index ON Ticker (Change_24 ASC)"
        Updated_AtIdx = "CREATE INDEX IF NOT EXISTS Updated_AtIndex ON OrderBook (Updated_At ASC)"
        SequenceIdx = "CREATE INDEX IF NOT EXISTS SequenceIndex ON OrderBook (Sequence ASC)"
        SideIdx = "CREATE INDEX IF NOT EXISTS SideIndex ON OrderBook (Side ASC)"
        OrderBookIdx = "CREATE INDEX IF NOT EXISTS BookIndex ON OrderBook (Book ASC)"
        OrderbookPriceIdx = "CREATE INDEX IF NOT EXISTS OrderbookPriceIndex ON OrderBook (Price ASC)"
        AmountIdx = "CREATE INDEX IF NOT EXISTS AmountIndex ON OrderBook (Amount ASC)"
        TradesBookIdx = "CREATE INDEX IF NOT EXISTS BookIndex ON Trades (Amount ASC)"
        TradesCreatedAtIdx = "CREATE INDEX IF NOT EXISTS Created_AtIndex ON Trades (Created_At ASC)"
        TradesAmountIdx = "CREATE INDEX IF NOT EXISTS AmountIndex ON Trades (Amount ASC)"
        Maker_SideIdx = "CREATE INDEX IF NOT EXISTS Maker_SideIndex ON Trades (Amount ASC)"
        TradesPrice = "CREATE INDEX IF NOT EXISTS TradesPriceIndex ON Trades (Amount ASC)"
        TIdIdx = "CREATE INDEX IF NOT EXISTS TIdIndex ON Trades (Amount ASC)"
        self.conn.execute(ABtblstmt)
        self.conn.execute(TItblstmt)
        self.conn.execute(OBtblstmt)
        self.conn.execute(TRtblstmt)
        self.conn.execute(BIdIdx)
        self.conn.execute(Bookidx)
        self.conn.execute(HighIdx)
        self.conn.execute(LastIdx)
        self.conn.execute(CreatedAtIdx)
        self.conn.execute(TickerBookIdx)
        self.conn.execute(VolumeIdx)
        self.conn.execute(VWAPIdx)
        self.conn.execute(LowIdx)
        self.conn.execute(AskIdx)
        self.conn.execute(BidIdx)
        self.conn.execute(Change_24Idx)
        self.conn.execute(Updated_AtIdx)
        self.conn.execute(SequenceIdx)
        self.conn.execute(SideIdx)
        self.conn.execute(OrderBookIdx)
        self.conn.execute(OrderbookPriceIdx)
        self.conn.execute(AmountIdx)
        self.conn.execute(TradesBookIdx)
        self.conn.execute(TradesCreatedAtIdx)
        self.conn.execute(TradesAmountIdx)
        self.conn.execute(Maker_SideIdx)
        self.conn.execute(TradesPrice)
        self.conn.execute(TIdIdx)
        self.conn.commit()

    def AddData(self, EndPoint, BId=None, Book=None, Updated_At=None, Sequence=None, Side=None, Price=None, Amount=None, High=None, Last=None, Created_At=None, Volume=None, VWAP=None, Low=None, Ask=None, Bid=None, Change_24=None, Maker_Side=None, TId=None):
        if EndPoint == "AvailableBooks":
            stmt = "INSERT INTO AvailableBooks (BId, Book) VALUES(?, ?)"
            args = (BId, Book)
            self.conn.execute(stmt, args)
            self.conn.commit()

        elif EndPoint == "Ticker":
            stmt = "INSERT INTO Ticker (High, Last, Created_At, Book, Volume, VWAP, Low, Ask, Bid, Change_24) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
            args = (High, Last, Created_At, Book, Volume, VWAP, Low, Ask, Bid, Change_24)
            self.conn.execute(stmt, args)
            self.conn.commit()

        elif EndPoint == "OrderBook":
            stmt = "INSERT INTO OrderBook (Updated_At, Sequence, Side, Book, Price, Amount) VALUES(?, ?, ?, ?, ?, ?)"
            args = (Updated_At, Sequence, Side, Book, Price, Amount)
            self.conn.execute(stmt, args)
            self.conn.commit()

        elif EndPoint == "Trades":
            stmt = "INSERT INTO Trades (Book, Created_At, Amount, Maker_Side, Price, TId) VALUES(?, ?, ?, ?, ?, ?)"
            args = (Book, Created_At, Amount, Maker_Side, Price, TId)
            self.conn.execute(stmt, args)
            self.conn.commit()

    def GetData(self, EndPoint):
        if EndPoint == "AvailableBooks":
            stmt = "SELECT * FROM AvailableBooks"
            a = self.conn.execute(stmt)
            return [x for x in self.conn.execute(stmt)]
