import csv
import bitsohandler
import time
import logging
import dbhelper

dbb = dbhelper.DBBitso()
bpa = bitsohandler.PublicApi()
Flogger = logging.getLogger(__name__)
Flogger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s')
file_handler = logging.FileHandler('Data/Logs/Logger.log')
file_handler.setFormatter(formatter)
Flogger.addHandler(file_handler)

def AskFor(object = None, book = None, marker = None, sort = None, limit = None, aggregate = None):
    if object  ==  None:
        Flogger.error("No EndPoint selected")
    elif object == "AvailableBooks":
        try:
            RawData = bpa.available_books()
            Data = []
            id = 0
            while id < (len(RawData)):
                TemporalDict = []
                count = 0
                while count < 1:
                    TemporalDict.append(id)
                    TemporalDict.append(RawData[id])
                    count += 1
                Data.append(TemporalDict)
                id += 1
            return Data
        except Exception as e:
            Flogger.error(e)
    elif object == "OrderBook":
        try:
            orders = bpa.orderbook()
            return orders
        except Exception as e:
            Flogger.error(e)
        pass
    elif object == "Ticker":
        try:
            ticker = bpa.ticker()
            return ticker
        except Exception as e:
            Flogger.error(e)
    elif object == "Trades":
        try:
            trades = bpa.trades()
            return trades
        except Exception as e:
            Flogger.error(e)

def WriteToDB(EndPoint, Data):
    if EndPoint == "AvailableBooks":
        try:
            previusData = dbb.GetData(EndPoint)
            TempList = []
            for tupla in previusData:
                SmallList = []
                for i in tupla:
                    SmallList.append(i)
                TempList.append(SmallList)
            if Data != TempList:
                for i in Data:
                    dbb.AddData(EndPoint, BId = i[0], Book = i[1])
        except Exception as e:
            Flogger.error(e)
    elif EndPoint == "OrderBook":
        try:
            Counter = 0
            for Book in Data:
                for BookEntry in Data[Counter]:
                    dbb.AddData(EndPoint = EndPoint, Book = BookEntry[0], Price = float(BookEntry[1]), Amount = float(BookEntry[2]), Side = BookEntry[3], Updated_At = BookEntry[4], Sequence = int(BookEntry[5]))
                Counter += 1
        except Exception as e:
            Flogger.error(e)
    elif EndPoint == "Ticker":
        try:
            for Book in Data:
                dbb.AddData(EndPoint = EndPoint, High = float(Book[0]), Last = float(Book[1]), Created_At = Book[2], Book = Book[3], Volume = float(Book[4]), VWAP = float(Book[5]), Low = float(Book[6]), Ask = float(Book[7]), Bid = float(Book[8]), Change_24 = float(Book[9]))
        except Exception as e:
            Flogger.error(e)
    elif EndPoint == "Trades":
        try:
            RawBooks = AskFor("AvailableBooks")
            Books = []
            for i in RawBooks:
                Books.append(i[1])
            for i in Books:
                for Entry in Data[i]:
                    dbb.AddData(EndPoint = EndPoint, Book = Entry['book'], Price = float(Entry['price']), Amount = float(Entry['amount']), Maker_Side = Entry['maker_side'], Created_At = Entry['created_at'], TId = int(Entry['tid']))
        except Exception as e:
            Flogger.error(e)

def main():
    #dbb.BitsoSetup()
    while True:
        Data = AskFor("AvailableBooks")
        WriteToDB("AvailableBooks", Data)
        Data = AskFor("OrderBook")
        WriteToDB("OrderBook", Data)
        Data = AskFor("Ticker")
        WriteToDB("Ticker", Data)
        Data = AskFor("Trades")
        WriteToDB("Trades", Data)
        time.sleep(60)

if __name__ == '__main__':
    main()
