import json
import requests
import time
import urllib
import hmac
import hashlib
import logging

Blogger = logging.getLogger(__name__)
Blogger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s')
file_handler = logging.FileHandler('Data/Logs/BitsoHandler.log')
file_handler.setFormatter(formatter)
Blogger.addHandler(file_handler)

URL = "https://api.bitso.com/v3/"

DictPayloads={"AvailableBooks":("book", "minimum_amount", "maximum_amount", "minimum_price", "maximum_price", "minimum_value", "maximum_value"),
              "Ticker":("book", "volume", "high", "last", "low", "vwap", "ask", "bid", "created_at"),
              "OrderBook":(),
              "Trades":()
}

def get_url(url):
    try:
        response = requests.get(url, timeout = 1)
        content = response.content.decode("utf8")
        return content
    except requests.exceptions.ConnectionError as e:
        Blogger.error("PROBLEMAS DE CONEXIÓN.")
        Blogger.error(e)

def get_json_from_url(url):
    try:
        content = get_url(url)
        js = json.loads(content)
        return js
    except TypeError as e:
        Blogger.error("get_json_from_url")
        Blogger.error(e)

class PublicApi:
    def available_books(self):
        try:
            books = []
            url = URL + "available_books/"
            booksr = get_json_from_url(url)
            for booksr in booksr["payload"]:
                books.append(booksr["book"])
            return books
        except TypeError as e:
            Blogger.error(e)

    def ticker(self):
        tick = []
        url = URL + "ticker/"
        dict = get_json_from_url(url)
        for i in dict["payload"]:
            list = []
            Alto = i["high"]
            Ultimo = i["last"]
            Fecha = i["created_at"]
            Libro = i["book"]
            Volumen = i["volume"]
            VWAP = i["vwap"]
            Bajo = i["low"]
            Venta = i["ask"]
            Compra = i["bid"]
            Cambio = i["change_24"]
            list.append(Alto)
            list.append(Ultimo)
            list.append(Fecha)
            list.append(Libro)
            list.append(Volumen)
            list.append(VWAP)
            list.append(Bajo)
            list.append(Venta)
            list.append(Compra)
            list.append(Cambio)
            tick.append(list)
        return tick

    def orderbook(self,aggregate=None):
        try:
            books = PublicApi.available_books(self)
            orderbooks = []
            keysside = ['book', 'price', 'amount']
            keysbook = ['bids','asks']
            for book in books:
                listbook = []
                url = URL + "order_book?book={}".format(book)
                lbids = []
                lasks = []
                if aggregate == None:
                    orders = get_json_from_url(url)
                    for keyb in keysbook:
                        length = len(orders['payload'][keyb])
                        count = 0
                        while count < length:
                            tlist = []
                            for keys in keysside:
                                tlist.append(orders['payload'][keyb][count][keys])
                            tlist.append(keyb)
                            tlist.append(orders['payload']['updated_at'])
                            tlist.append(orders['payload']['sequence'])
                            listbook.append(tlist)
                            count += 1
                else:
                    url = url + "&aggregate=false"
                    orders = get_json_from_url(url)
                orderbooks.append(listbook)
            return orderbooks
        except Exception as e:
            raise e

    def trades(self, marker=None):
        try:
            books = PublicApi.available_books(self)
            final = {}
            for book in books:
                url = URL + "trades/?book={}&limit=20".format(book)
                atrades = get_json_from_url(url)
                trades = atrades["payload"]
                if marker == None:
                    final[book] = trades
            return final
        except Exception as e:
            raise
