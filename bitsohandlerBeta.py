import json
import requests
import time
import urllib
import hmac
import hashlib
import logging

logging.basicConfig(filename='Data/Logs/bitsohandler.log',level=logging.DEBUG,
                    format='%(asctime)s:%(name)s:%(levelname)s:%(message)s')

URL = "https://api.bitso.com/v3/"

DictPayloads={"AvailableBooks":("book", "minimum_amount", "maximum_amount", "minimum_price", "maximum_price", "minimum_value", "maximum_value"),
              "Ticker":("book", "volume", "high", "last", "low", "vwap", "ask", "bid", "created_at"),
              "OrderBook":(),
              "Trades":()

}

def get_url(url):
    try:
        response = requests.get(url)
        content = response.content.decode("utf8")
        return content
    except requests.exceptions.ConnectionError as e:
        logging.error("PROBLEMAS DE CONEXIÓN.")
        logging.error(e)

def get_json_from_url(url):
    try:
        content = get_url(url)
        js = json.loads(content)
        return js
    except TypeError as e:
        logging.error("get_json_from_url")
        logging.error(e)

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
            logging.error(e)

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

    def orderbook(self,book,aggregate=None):
        try:
            url = URL + "order_book?book={}".format(book)
            lbids = []
            lasks = []
            if aggregate == None:
                orders = get_json_from_url(url)
                Fecha = orders["payload"]["updated_at"]
                bids = orders["payload"]["bids"]
                asks = orders["payload"]["asks"]
                for bids in bids:
                    lbids.append(bids["price"])
                    lbids.append(bids["amount"])
                for asks in asks:
                    lasks.append(asks["price"])
                    lasks.append(asks["amount"])
                return (lbids,lasks, Fecha)
            else:
                url = url + "&aggregate=false"
                orders = get_json_from_url(url)
        except Exception as e:
            a = orders["error"]["message"]
            return a

    def trades(self, marker=None):
        try:
            books = PublicApi.available_books(self)
            final = {}
            for book in books:
                url = URL + "trades/?book={}".format(book)
                atrades = get_json_from_url(url)
                trades = atrades["payload"]
                if marker == None:
                    final[book] = trades
            return final
        except Exception as e:
            raise
