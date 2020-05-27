import logging
import json
import requests
import time
import urllib
import csv

logging.basicConfig(filename='test.log',level=logging.DEBUG,
                    format='%(asctime)s:%(name)s:%(levelname)s:%(message)s')

URL = "https://api.bitso.com/v3/"

tickerr = [
            'high',
            'last',
            'created_at',
            'book',
            'volume',
            'vwap',
            'low',
            'ask',
            'bid',
            'change_24'
]

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
        logging.error("GET_JSON_FROM_URL")
        logging.error(e)

def ticker():
    try:
        tick = []
        url = URL + "ticker/"
        ticker = get_json_from_url(url)
        for i in ticker["payload"]:
            tick.append(i)
        return tick
    except Exception as e:
        logging.error("TICKER")
        logging.error(e)

def log():
    try:
        Tick = ticker()
        book = 0
        while book < len(Tick):
            writecsv(Tick[book])
            book = book + 1
    except Exception as e:
        logging.error("LOG")
        logging.error(e)

def writecsv(booklist):
    try:
        book = booklist['book']
        path = 'Ticker/'
        sufix = '.csv'
        csvname = path + book + sufix
        with open(csvname,'a',newline='') as csv_file:
            cabecera = ['high','last','created_at','book','volume','vwap','low','ask','bid','change_24']
            csv_writer = csv.DictWriter(csv_file, fieldnames=cabecera)
            csv_writer.writerow(booklist)
    except Exception as e:
        logging.error("WRITE CSV")
        logging.error(e)

while True:
    try:
        ToLog = log()
        exito = "Se ha hecho el registro sin problemas. Proximo registro en 60 s"
        logging.debug(exito)
        time.sleep(60)
    except TypeError as e:
        logging.error("ERROR EN EL OBJETO JSON.")
        logging.error(e)
    except json.decoder.JSONDecodeError as e:
        logging.error("LA PÁGINA NO ES LA ESPERADA, POR ENDE NO SE PUDO PROCESAR.")
        logging.error(e)

