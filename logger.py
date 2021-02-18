import csv
import bitsohandler
import time
import logging
import dbhelper
import os

dbb = dbhelper.DBBitso()
bpa = bitsohandler.PublicApi()
Flogger = logging.getLogger(__name__)
Flogger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s')
file_handler = logging.FileHandler('Data/Logs/TestLogger.log')
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
            Flogger.error(f"Error at AskFor: {object}")
    elif object == "OrderBook":
        try:
            orders = bpa.orderbook()
            return orders
        except Exception as e:
            Flogger.error(e)
            Flogger.error(f"Error at AskFor: {object}")
        pass
    elif object == "Ticker":
        try:
            ticker = bpa.ticker()
            return ticker
        except Exception as e:
            Flogger.error(e)
            Flogger.error(f"Error at AskFor: {object}")
    elif object == "Trades":
        try:
            trades = bpa.trades()
            return trades
        except Exception as e:
            Flogger.error(e)
            Flogger.error(f"Error at AskFor: {object}")

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
            Flogger.error(f"Error at WriteToDB: {EndPoint}")
    elif EndPoint == "OrderBook":
        try:
            Counter = 0
            for Book in Data:
                for BookEntry in Data[Counter]:
                    dbb.AddData(EndPoint = EndPoint, Book = BookEntry[0], Price = float(BookEntry[1]), Amount = float(BookEntry[2]), Side = BookEntry[3], Updated_At = BookEntry[4], Sequence = int(BookEntry[5]))
                Counter += 1
        except Exception as e:
            Flogger.error(e)
            Flogger.error(f"Error at WriteToDB: {EndPoint}")
    elif EndPoint == "Ticker":
        try:
            for Book in Data:
                dbb.AddData(EndPoint = EndPoint, High = float(Book[0]), Last = float(Book[1]), Created_At = Book[2], Book = Book[3], Volume = float(Book[4]), VWAP = float(Book[5]), Low = float(Book[6]), Ask = float(Book[7]), Bid = float(Book[8]), Change_24 = float(Book[9]))
        except Exception as e:
            Flogger.error(e)
            Flogger.error(f"Error at WriteToDB: {EndPoint}")
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
            Flogger.error(f"Error at WriteToDB: {EndPoint}")

def WriteToCSV(EndPoint, Data):
    try:
        path = "Data/CSVs/"
        sufix = ".csv"
        if EndPoint == "AvailableBooks":
            csvname = path + EndPoint + sufix
            ABdict = []
            id = 0
            while id < (len(Data)):
                jaxa = []
                count = 0
                while count < 1:
                    jaxa.append(id)
                    jaxa.append(Data[id][1])
                    count += 1
                ABdict.append(jaxa)
                id += 1
            comparator = []
            try:
                with open(csvname,'r') as csv_file:
                    csv_reader = csv.reader(csv_file)
                    next(csv_reader)
                    for i in csv_reader:
                        i[0] = int(i[0])
                        comparator.append(i)
                if comparator == ABdict:
                    pass
                else:
                    with open(csvname,'w') as csv_file:
                        csv_writer = csv.writer(csv_file)
                        csv_writer.writerow(["id","book"])
                        for i in ABdict:
                            csv_writer.writerow(i)
            except:
                with open(csvname,'w') as csv_file:
                    csv_writer = csv.writer(csv_file)
                    csv_writer.writerow(["id","book"])
                    for i in ABdict:
                        csv_writer.writerow(i)
        elif EndPoint == "OrderBook":
            try:
                for book in Data:
                        libro = book[0][0]
                        csvname = path + EndPoint + '_' + libro + sufix
                        with open(csvname, 'w', newline='') as csv_file:
                            for order in book:
                                writer = csv.writer(csv_file)
                                writer.writerow(order)
            except Exception as e:
                Flogger.error(e)
        elif EndPoint == "Ticker":
            try:
                for i in Data:
                    book = i[3]
                    csvname = path + EndPoint + '_' + book + sufix
                    with open(csvname,'a', newline='') as csv_file:
                        csv_writer = csv.writer(csv_file)
                        header = ['high','last','created_at','book','volume','vwap','low','ask','bid','change_24']
                        tickdict = dict(zip(header,i))
                        csv_writer = csv.DictWriter(csv_file, fieldnames = header)
                        csv_writer.writerow(tickdict)
            except AttributeError as e:
                Flogger.error(e)
        elif EndPoint == "Trades":
            try:
                keys = []
                for i in Data:
                    keys.append(i)
                for key in keys:
                    for trade in Data[key]:
                        csvname = path + EndPoint + '_' + key + sufix
                        with open(csvname,'a', newline='') as csv_file:
                            header = ['book','created_at','amount','maker_side','price','tid']
                            writer = csv.DictWriter(csv_file, fieldnames = header)
                            writer.writerow(trade)
            except Exception as e:
                Flogger.error(e)
        elif EndPoint == None:
            Flogger.error(e)
    except Exception as e:
        Flogger.error(e)

def main():
    EndPoints = ["AvailableBooks","OrderBook","Ticker","Trades"]
    while True:
        Inicio = time.time()
        for i in EndPoints:
            data = AskFor(i)
            WriteToDB(i, data)
        Fin = time.time()
        print(Fin - Inicio)
        exit()
if __name__ == '__main__':
    main()
