import csv
import bitsohandler
import time
import logging

Flogger = logging.getLogger(__name__)
Flogger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s')
file_handler = logging.FileHandler('Data/Logs/Logger.log')
file_handler.setFormatter(formatter)
Flogger.addHandler(file_handler)

bpa = bitsohandler.PublicApi()

def askfor(object = None, book = None, marker = None, sort = None, limit = None, aggregate = None):
    if object  ==  None:
        Flogger.error("No EndPoint selected")
    elif object == "AvailableBooks":
        try:
            books = bpa.available_books()
            writecsv(object,books)
        except Exception as e:
            Flogger.error(e)
    elif object == "OrderBook":
        try:
            orders = bpa.orderbook()
            writecsv(object,orders)
        except Exception as e:
            Flogger.error(e)
        pass
    elif object == "Ticker":
        try:
            ticker = bpa.ticker()
            writecsv(object,ticker)
        except Exception as e:
            Flogger.error(e)
    elif object == "Trades":
        try:
            trades = bpa.trades()
            writecsv(object, trades)
        except Exception as e:
            Flogger.error(e)

def writecsv(Endpoint = None, Data = None):
    try:
        path = "Data/Csvs/"
        sufix = ".csv"
        if Endpoint == "AvailableBooks":
            csvname = path + Endpoint + sufix
            ABdict = []
            id = 0
            while id < (len(Data)):
                jaxa = []
                count = 0
                while count < 1:
                    jaxa.append(id)
                    jaxa.append(Data[id])
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
        elif Endpoint == "OrderBook":
            try:
                for book in Data:
                        libro = book[0][0]
                        csvname = path + Endpoint + '_' + libro + sufix
                        with open(csvname, 'w', newline='') as csv_file:
                            for order in book:
                                writer = csv.writer(csv_file)
                                writer.writerow(order)
            except Exception as e:
                Flogger.error(e)
        elif Endpoint == "Ticker":
            try:
                for i in Data:
                    book = i[3]
                    csvname = path + Endpoint + '_' + book + sufix
                    with open(csvname,'a', newline='') as csv_file:
                        csv_writer = csv.writer(csv_file)
                        header = ['high','last','created_at','book','volume','vwap','low','ask','bid','change_24']
                        tickdict = dict(zip(header,i))
                        csv_writer = csv.DictWriter(csv_file, fieldnames = header)
                        csv_writer.writerow(tickdict)
            except AttributeError as e:
                Flogger.error(e)
        elif Endpoint == "Trades":
            try:
                keys = []
                for i in Data:
                    keys.append(i)
                for key in keys:
                    for trade in Data[key]:
                        csvname = path + Endpoint + '_' + key + sufix
                        with open(csvname,'a', newline='') as csv_file:
                            header = ['book','created_at','amount','maker_side','price','tid']
                            writer = csv.DictWriter(csv_file, fieldnames = header)
                            writer.writerow(trade)
            except Exception as e:
                Flogger.error(e)
        elif Endpoint == None:
            Flogger.error(e)
    except Exception as e:
        Flogger.error(e)

def main():
    while True:
        askfor("AvailableBooks")
        askfor("OrderBook")
        askfor("Ticker")
        askfor("Trades")
        time.sleep(60)

if __name__ == '__main__':
    main()
