import csv
import bitsohandlerBeta
import time

bpa = bitsohandlerBeta.PublicApi()

options =  ("AvailableBooks",
            "Ticker",
            "Trades")

def askfor(object = None, book = None, marker = None, sort = None, limit = None, aggregate = None):
    if object  ==  None:
        print ("No object request")
    elif object == "AvailableBooks":
        try:
            books = bpa.available_books()
            writecsv(object,books)
        except Exception as e:
            print(e)
            raise
    elif object == "Ticker":
        try:
            ticker = bpa.ticker()
            writecsv(object,ticker)
        except Exception as e:
            print(e)
            raise
    elif object == "Trades":
        try:
            trades = bpa.trades()
            writecsv(object, trades)
        except Exception as e:
            raise

def writecsv(Endpoint = None, Data = None):
    try:
        path = "Data/Csvs/"
        sufix = ".csv"
        if Endpoint == None:
            raise AttributeError("No se especificó un formato de Endpoint.")
        if Endpoint == "AvailableBooks":
            csvname = path + Endpoint + '_' + sufix
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
                raise
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
                print(e)
                raise
    except Exception as e:
        raise

def main():
    while True:
        for i in options:
            askfor(i)
        time.sleep(60)

if __name__ == '__main__':
    main()
