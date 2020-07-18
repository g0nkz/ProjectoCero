#PYTHON 3.8.2
#LGsus

import csv
import time
import json
import urllib
import requests
import dbhelper
import bitsohandler
from credentials import *
from InLinemessage_dictionary import *

dbu = dbhelper.DBUsers()
ltext = []

#DECLARAR ID DEL BOT Y URL DE TELEGRAM
URL = "https://api.telegram.org/bot{}/".format(telegram_token)

#CONSULTAR ESTADO
def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content

#CAMBIAR DE JSON A PYTHON (PARSE)
def get_json_from_url(url):
    content = get_url(url)
    js = json.loads(content)
    return js

#SOLICITAR LISTA DE MENSAJES
def get_updates(offset=None):
    url = URL + "getUpdates?timeout=50"
    if offset:
        url += "&offset={}".format(offset)
    js = get_json_from_url(url)
    return js

#DETERMINAR MENSAJES NO LEÍDOS
def get_last_update_id(updates):
    update_ids = []
    for update in updates["result"]:
        update_ids.append(int(update["update_id"]))
    return max(update_ids)

#CREAR TECLADO EN LINEA
def build_inlinekeyboard(items):
    nitems = []
    b = 0
    d = 2
    e = 0
    if len(items) > 2:
        a = int((len(items))/2)
        c = (len(items))%2
        f = a + c
        while len(nitems) != f:
            aitems = []
            while b < d:
                aitems.append(items[b])
                b = b + 1
            nitems.append(aitems)
            e = e + 1
            if e < a:
                d = d + 2
            else:
                d = d + 1
        keyboard = nitems
    else:
        keyboard = [items]
    reply_markup = {'inline_keyboard':keyboard}
    return json.dumps(reply_markup)

#MANEJAR A LOS USUARIOS
def handle_users(updates):
    #AÑADIR NUEVOS USUARIOS
    for update in updates["result"]:
        if "callback_query" in update:
            UId = update["callback_query"]["from"]["id"]
            IsBot = update["callback_query"]["from"]["is_bot"]
            FirstName = update["callback_query"]["from"]["first_name"]
            LastName = update["callback_query"]["from"]["last_name"]
            LanguageCode = update["callback_query"]["from"]["language_code"]
            users = dbu.get_users()
        else:
            UId = update["message"]["from"]["id"]
            IsBot = update["message"]["from"]["is_bot"]
            FirstName = update["message"]["from"]["first_name"]
            LastName = update["message"]["from"]["last_name"]
            LanguageCode = update["message"]["from"]["language_code"]
            users = dbu.get_users()
        if UId not in users:
            dbu.add_user(UId, IsBot, FirstName, LastName, LanguageCode)

#RESPONDER A TODOS LOS NO LEIDOS
def handle_updates(updates):
    #EJECUTA EL MANEJO DE USUARIOS
    handle_users(updates)
    #DE LA RESPUESTA DEL SERVIDOR(JSON) DE TELEGRAM ASIGNA LOS VALORES A LAS VARIABLES.
    for update in updates["result"]:
        if "callback_query" in update:
            text = update["callback_query"]["data"]
            chat = update["callback_query"]["message"]["chat"]["id"]
            UId = update["callback_query"]["from"]["id"]
            Date = update["callback_query"]["message"]["date"]
        else:
            text = update["message"]["text"]
            chat = update["message"]["chat"]["id"]
            UId = update["message"]["from"]["id"]
            Date = update["message"]["date"]
        #BUSCA QUÉ HACER CON EL TEXTO QUE LLEGA..
        search_text(text, chat, UId)

#BUSCA LA INFORMACION SOLICITADA
def retrieve_data(EndPoint, Book = None):
    path = 'Data/Csvs/'
    sufix = '.csv'
    if EndPoint == 'AvailableBooks':
        Returner = []
        csvname = path + EndPoint + sufix
        with open(csvname,'r') as csv_file:
            reader = csv.reader(csv_file)
            next(reader)
            for i in reader:
                Returner.append(i[1])
        return Returner
    if EndPoint == 'Ticker':
        csvname = path + EndPoint + '_' + Book + sufix
        with open(csvname,'r') as csv_file:
            reader = csv.reader(csv_file)
            lista = list(reader)
            Returner = lista[-1]
        return Returner
    if EndPoint == 'OrderBook':
        Returner = []
        csvname = path + EndPoint + '_' + Book + sufix
        with open(csvname, 'r') as csv_file:
            reader = csv.reader(csv_file)
            for i in reader:
                Returner.append(i)
        return Returner
    if EndPoint == 'Trades':
        Returner = []
        csvname = path + EndPoint + '_' + Book + sufix
        with open(csvname, 'r') as csv_file:
            reader = csv.reader(csv_file)
            for i in reader:
                Returner.append(i)
        return Returner

def CreateDictForKeyboar(list,EndPoint=None):
    Returner = []
    for i in list:
        Format = {'text':'','callback_data':''}
        Format['text'] = i
        CallBackData = '/' + EndPoint + i
        Format['callback_data'] = CallBackData
        Returner.append(Format)
    Regresar = {'text': 'Regresar', 'callback_data': 'Pública.'}
    Returner.append(Regresar)
    return Returner

def OrderBookDictCreator(Book):
    Returner = [
    {'text':'Compras','callback_data':''},
    {'text':'Ventas','callback_data':''}
    ]
    CallBackDataCompras = '/Compras' + Book
    CallBackDataVentas = '/Ventas' + Book
    Returner[0]['callback_data'] = CallBackDataCompras
    Returner[1]['callback_data'] = CallBackDataVentas
    return Returner

#DETERMINAR QUE HACER A PARTIR DEL TEXTO RECIVIDO
def search_text(text, chat, UId):
    print(text)
    ltext = text
    if text.startswith("/"):
        comando = text[1:]
        ##START##
        if comando == "start":
            keyboard = build_inlinekeyboard(acuerdo)
            send_message(mensajes["start"], chat, keyboard)
        ##LIBROS DISPONIBLES##
        elif comando == "AvailableBooks":
            libros = retrieve_data(comando)
            librob = []
            libroc = ""
            for libro in libros:
                libroa = libro.replace('_',' - ')
                librob.append(libroa)
                librob.append("\n")
            send_message(libroc.join(librob), chat)
            keyboard = build_inlinekeyboard(AvailableBooks)
            send_message(mensajes["availablebooksr"], chat, keyboard)
        ##ACEPTO##
        elif comando == "Acepto.":
            keyboard = build_inlinekeyboard(acuerdopositivo)
            send_message(mensajes["acepto"], chat, keyboard)
        ##NO ACEPTO##
        elif comando == "No acepto.":
            keyboard = build_inlinekeyboard(acuerdonegativo)
            send_message(mensajes["noacepto"], chat, keyboard)
        ##TICKER##
        elif comando.startswith("Ticker"):
            book = comando[6:]
            EndPoint = comando[:6]
            tick = retrieve_data(EndPoint, book)
            ntick = 0
            atick = 0
            a = ""
            d = []
            for i in tick:
                b = tickerr[atick].format(tick[ntick])
                d.append(b)
                d.append("\n")
                ntick = ntick + 1
                atick = atick + 1
            c = a.join(d)
            send_message(c, chat)
            keyboard = build_inlinekeyboard(tickere)
            send_message(mensajes["tickere"], chat, keyboard)
        ##ORDERBOOK##
        elif comando.startswith("OrderBook"):
            book = comando[9:]
            response = OrderBookDictCreator(book)
            keyboard = build_inlinekeyboard(response)
            send_message(mensajes["orderbookr"], chat, keyboard)
        ##ORDERBOOK COMPRAS##
        elif comando.startswith("Compras"):
            try:
                bbook = ltext
                book = bbook[8:]
                RawCompras = retrieve_data('OrderBook', book)
                Compras = []
                for i in RawCompras:
                    if i[3] == 'bids':
                        Compras.append(i)
                Texto = ""
                for Compra in Compras:
                    Lista = []
                    Contador = 0
                    for i in Compra:
                        dos = orderbookrr[Contador].format(i)
                        Lista.append(dos)
                        Lista.append('\n')
                        Contador += 1
                    Mensaje = Texto.join(Lista)
                    send_message(Mensaje, chat)
                keyboard = build_inlinekeyboard(orderbooke)
                send_message(mensajes["tickere"], chat, keyboard)
            except TypeError as e:
                print(e)
        ##ORDERBOOK VENTAS##
        elif comando.startswith("Ventas"):
            try:
                bbook = ltext
                book = bbook[7:]
                RawVentas = retrieve_data('OrderBook', book)
                Ventas = []
                for i in RawVentas:
                    if i[3] == 'asks':
                        Ventas.append(i)
                Texto = ""
                for Venta in Ventas:
                    Lista = []
                    Contador = 0
                    for i in Venta:
                        dos = orderbookrr[Contador].format(i)
                        Lista.append(dos)
                        Lista.append('\n')
                        Contador += 1
                    Mensaje = Texto.join(Lista)
                    send_message(Mensaje, chat)
                keyboard = build_inlinekeyboard(orderbooke)
                send_message(mensajes["tickere"], chat, keyboard)
            except TypeError as e:
                send_message(str(e),chat)
        elif comando.startswith("Trades"):
            try:
                bbook = ltext
                book = bbook[7:]
                Trades = retrieve_data('Trades',book)
                Texto = ""
                for Trade in Trades:
                    Lista = []
                    Contador = 0
                    for i in Trade:
                        Dos = tradesrr[Contador].format(i)
                        Lista.append(Dos)
                        Lista.append('\n')
                        Contador += 1
                    Mensaje = Texto.join(Lista)
                    send_message(Mensaje,chat)
                keyboard = build_inlinekeyboard(tradese)
                send_message(mensajes["tradesr"],chat,keyboard)
            except TypeError as e:
                send_message(str(e),chat)
    elif text == "Trades":
        trades = retrieve_data('AvailableBooks')
        TradesToSend = CreateDictForKeyboar(trades, text)
        keyboard = build_inlinekeyboard(TradesToSend)
        send_message(mensajes["trades"], chat, keyboard)
    elif text == "Ticker":
        libros = retrieve_data('AvailableBooks')
        tickexxxx = CreateDictForKeyboar(libros, text)
        keyboard = build_inlinekeyboard(tickexxxx)
        send_message(mensajes["ticker"], chat, keyboard)
    elif text == "OrderBook":
        orders = retrieve_data('AvailableBooks')
        OrdersToSend = CreateDictForKeyboar(orders, text)
        keyboard = build_inlinekeyboard(OrdersToSend)
        send_message(mensajes["ticker"], chat, keyboard)
    elif text == "Pública.":
        keyboard = build_inlinekeyboard(acuerdopositivo)
        send_message(mensajes["acepto"], chat, keyboard)
    else:
        send_message("Entrada invalida. Intente de nuevo.", chat)

#SOLICITAR ULTIMO MENSAJE Y ID DEL CHAT
def get_last_chat_id_and_text(updates):
    #print(updates)
    num_updates = len(updates["result"])
    lista = updates["result"]
    data = json.dumps(lista)
    last_update = num_updates - 1
    full_last = updates["result"][last_update]
    if "callback_query" in full_last:
        text = full_last["callback_query"]["data"]
        chat_id = full_last["callback_query"]["message"]["chat"]["id"]
    else:
        text = "text" in full_last["message"]
        if text == True:
            text = updates["result"][last_update]["message"]["text"]
        else:
            text = "Entrada invalida"
        chat_id = updates["result"][last_update]["message"]["chat"]["id"]
    return (text, chat_id)

#ENVIAR MENSAJE
def send_message(text, chat_id, reply_markup=None):
    text = text.encode(encoding='utf-8')
    text = urllib.parse.quote_plus(text)
    url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
    if reply_markup:
        url += "&reply_markup={}".format(reply_markup)
    get_url(url)

text, chat = get_last_chat_id_and_text(get_updates())
send_message(text, chat)

##EJECUTAR
def main():
    try:
        dbu.setup()
        last_update_id = None
        while True:
            updates = get_updates(last_update_id)
            if len(updates["result"]) > 0:
                last_update_id = get_last_update_id(updates) + 1
                handle_updates(updates)
            time.sleep(0.5)
    except Exception as e:
        raise e

#CONDICION PARA EJECUTAR
if __name__ == '__main__':
    main()
