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
dbb = dbhelper.DBBitso()
ltext = []

#DECLARAR ID DEL BOT Y URL DE TELEGRAM
URL = "https://api.telegram.org/bot{}/".format(telegram_token)

#CONSULTAR ESTADO
def GetURL(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content

#CAMBIAR DE JSON A PYTHON (PARSE)
def GetJSONFromURL(url):
    content = GetURL(url)
    js = json.loads(content)
    return js

#SOLICITAR LISTA DE MENSAJES
def GetUpdates(offset=None):
    url = URL + "getUpdates?timeout=50"
    if offset:
        url += "&offset={}".format(offset)
    js = GetJSONFromURL(url)
    return js

#DETERMINAR MENSAJES NO LEÍDOS
def GetLasUpdateID(updates):
    update_ids = []
    for update in updates["result"]:
        update_ids.append(int(update["update_id"]))
    return max(update_ids)

#CREAR TECLADO EN LINEA
def BuildInlineKeyboard(items):
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

def GetUserData(update):
    if "callback_query" in update:
        UID = update["callback_query"]["from"]["id"]
        IsBot = update["callback_query"]["from"]["is_bot"]
        FirstName = update["callback_query"]["from"]["first_name"]
        LastName = update["callback_query"]["from"]["last_name"]
        LanguageCode = update["callback_query"]["from"]["language_code"]
    else:
        UID = update["message"]["from"]["id"]
        IsBot = update["message"]["from"]["is_bot"]
        FirstName = update["message"]["from"]["first_name"]
        LastName = update["message"]["from"]["last_name"]
        LanguageCode = update["message"]["from"]["language_code"]
    return UID, IsBot, FirstName, LastName, LanguageCode

#MANEJAR A LOS USUARIOS
def HandleUsers(method = None, updates = None, TimerParam = None, UID = None):
    #AÑADIR NUEVOS USUARIOS
    if method == "general":
        for update in updates["result"]:
            if "callback_query" in update:
                UID, IsBot, FirstName, LastName, LanguageCode = GetUserData(update)
                users = dbu.get_users()
            else:
                UID, IsBot, FirstName, LastName, LanguageCode = GetUserData(update)
                users = dbu.get_users()
            if UID not in users:
                Timer = 0
                Time = 0
                dbu.add_user(UID, IsBot, FirstName, LastName, LanguageCode, Timer, Time)
    if method == "SetTimer":
        for update in updates["result"]:
            UID, IsBot, FirstName, LastName, LanguageCode = GetUserData(update)
            Time = time.time()
            dbu.SetTimer(TimerParam, UID, Time)

#RESPONDER A TODOS LOS NO LEIDOS
def HandleUpdates(updates):
    #EJECUTA EL MANEJO DE USUARIOS
    HandleUsers("general",updates)
    #DE LA RESPUESTA DEL SERVIDOR(JSON) DE TELEGRAM ASIGNA LOS VALORES A LAS VARIABLES.

    for update in updates["result"]:
        if "callback_query" in update:
            text = update["callback_query"]["data"]
            chat = update["callback_query"]["message"]["chat"]["id"]
            UID = update["callback_query"]["from"]["id"]
            Date = update["callback_query"]["message"]["date"]
        else:
            text = update["message"]["text"]
            chat = update["message"]["chat"]["id"]
            UID = update["message"]["from"]["id"]
            Date = update["message"]["date"]
        #BUSCA QUÉ HACER CON EL TEXTO QUE LLEGA..
        Timer = dbu.CheckTime(UID)
        SearchText(text, chat, UID, updates)

#BUSCA LA INFORMACION SOLICITADA
def RetrieveData(EndPoint, Book = None):
    path = 'Data/CSVs/'
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
    Regresar = {'text': 'Regresar', 'callback_data': 'MenuBitso'}
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
def SearchText(text, chat, UID, updates):
    ltext = text
    if text.startswith("/"):
        comando = text[1:]
        ##START##
        if comando == "start":
            keyboard = BuildInlineKeyboard(acuerdo)
            SendMessage(mensajes["start"], chat, keyboard)
        ##LIBROS DISPONIBLES##
        elif comando == "AvailableBooks":
            libros = RetrieveData(comando)
            librob = []
            libroc = ""
            for libro in libros:
                libroa = libro.replace('_',' - ')
                librob.append(libroa)
                librob.append("\n")
            SendMessage(libroc.join(librob), chat)
            keyboard = BuildInlineKeyboard(AvailableBooks)
            SendMessage(mensajes["availablebooksr"], chat, keyboard)
        ##TICKER##
        elif comando.startswith("Ticker"):
            book = comando[6:]
            EndPoint = comando[:6]
            tick = RetrieveData(EndPoint, book)
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
            SendMessage(c, chat)
            keyboard = BuildInlineKeyboard(tickere)
            SendMessage(mensajes["tickere"], chat, keyboard)
        ##ORDERBOOK##
        elif comando.startswith("OrderBook"):
            book = comando[9:]
            response = OrderBookDictCreator(book)
            keyboard = BuildInlineKeyboard(response)
            SendMessage(mensajes["orderbookr"], chat, keyboard)
        ##ORDERBOOK COMPRAS##
        elif comando.startswith("Compras"):
            try:
                bbook = ltext
                book = bbook[8:]
                RawCompras = RetrieveData('OrderBook', book)
                count = 0
                Compras = []
                for i in RawCompras:
                    if i[3] == 'bids':
                        count += 1
                        Compras.append(i)
                if count != 0:
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
                        SendMessage(Mensaje, chat)
                    keyboard = BuildInlineKeyboard(orderbooke)
                    SendMessage(mensajes["tickere"], chat, keyboard)
                else:
                    keyboard = BuildInlineKeyboard(orderbooke)
                    SendMessage(mensajes["EmptyList"],chat,keyboard)
            except TypeError as e:
                pass
        ##ORDERBOOK VENTAS##
        elif comando.startswith("Ventas"):
            try:
                bbook = ltext
                book = bbook[7:]
                RawVentas = RetrieveData('OrderBook', book)
                count = 0
                Ventas = []
                for i in RawVentas:
                    if i[3] == 'asks':
                        count += 1
                        Ventas.append(i)
                if count != 0:
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
                        SendMessage(Mensaje, chat)
                    keyboard = BuildInlineKeyboard(orderbooke)
                    SendMessage(mensajes["tickere"], chat, keyboard)
                else:
                    keyboard = BuildInlineKeyboard(orderbooke)
                    SendMessage(mensajes["EmptyList"],chat,keyboard)
            except TypeError as e:
                SendMessage(str(e),chat)
        elif comando.startswith("Trades"):
            try:
                bbook = ltext
                book = bbook[7:]
                TradesRaw = RetrieveData('Trades',book)
                Trades = TradesRaw[:50]
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
                    SendMessage(Mensaje,chat)
                keyboard = BuildInlineKeyboard(tradese)
                SendMessage(mensajes["tradesr"],chat,keyboard)
            except TypeError as e:
                SendMessage(str(e),chat)
        elif comando.startswith("Timer"):
            TimerParam = comando[5:]
            HandleUsers("SetTimer", updates, TimerParam, UID)
            keyboard = BuildInlineKeyboard(InLineKeyBoardTimer)
            SendMessage(mensajes["Timerr"], chat, keyboard)
    elif text == "Acepto":
        keyboard = BuildInlineKeyboard(acuerdopositivo)
        SendMessage(mensajes["acepto"], chat, keyboard)
    elif text == "No acepto":
        keyboard = BuildInlineKeyboard(acuerdonegativo)
        SendMessage(mensajes["noacepto"], chat, keyboard)
    elif text == "Trades":
        trades = RetrieveData('AvailableBooks')
        TradesToSend = CreateDictForKeyboar(trades, text)
        keyboard = BuildInlineKeyboard(TradesToSend)
        SendMessage(mensajes["trades"], chat, keyboard)
    elif text == "Ticker":
        libros = RetrieveData('AvailableBooks')
        tickexxxx = CreateDictForKeyboar(libros, text)
        keyboard = BuildInlineKeyboard(tickexxxx)
        SendMessage(mensajes["ticker"], chat, keyboard)
    elif text == "OrderBook":
        orders = RetrieveData('AvailableBooks')
        OrdersToSend = CreateDictForKeyboar(orders, text)
        keyboard = BuildInlineKeyboard(OrdersToSend)
        SendMessage(mensajes["ticker"], chat, keyboard)
    elif text == "MenuBitso":
        keyboard = BuildInlineKeyboard(MenuBitso)
        SendMessage(mensajes["MenuBitso"], chat, keyboard)
    elif text == "Configuration":
        keyboard = BuildInlineKeyboard(Configuration)
        SendMessage(mensajes["Configuracion"], chat, keyboard)
    elif text == "Timer":
        keyboard = BuildInlineKeyboard(InLineKeyBoardTimer)
        SendMessage(mensajes["Timer"], chat, keyboard)
    else:
        SendMessage("Entrada invalida. Intente de nuevo.", chat)

#SOLICITAR ULTIMO MENSAJE Y ID DEL CHAT
def GetLastChatIDAndText(updates):
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
def SendMessage(text, chat_id, reply_markup=None):
    text = text.encode(encoding='utf-8')
    text = urllib.parse.quote_plus(text)
    url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
    if reply_markup:
        url += "&reply_markup={}".format(reply_markup)
    GetURL(url)

text, chat = GetLastChatIDAndText(GetUpdates())
SendMessage(text, chat)

##EJECUTAR
def Main():
    try:
        dbu.setup()
        last_update_id = None
        while True:
            updates = GetUpdates(last_update_id)
            if len(updates["result"]) > 0:
                last_update_id = GetLasUpdateID(updates) + 1
                HandleUpdates(updates)
            time.sleep(0.5)
    except Exception as e:
        raise e

#CONDICION PARA EJECUTAR
if __name__ == '__main__':
    Main()
