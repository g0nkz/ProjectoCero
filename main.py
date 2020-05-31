#PYTHON 3.8.2
#LGsus

import json
import requests
import time
import urllib
import dbhelper
import bitsohandler
from credentials import *
from InLinemessage_dictionary import *

bpa = bitsohandler.PublicApi()
dbu = dbhelper.DBUsers()
dbb = dbhelper.DBBitso()
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
    url = URL + "getUpdates?timeout=100"
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

#CREAR EL TECLADO
def build_keyboard(items):
    keyboard = [[item] for item in items]
    reply_markup = {"keyboard":keyboard, "one_time_keyboard":True, "resize_keyboard":True}
    return json.dumps(reply_markup)

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

def handle_bitso(updates):
    for update in updates["result"]:
        if "callback_query" in update:
            UId = update["callback_query"]["from"]["id"]
            users = dbu.get_users()
        else:
            UId = update["message"]["from"]["id"]
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
            libros = bpa.available_books()
            librob = []
            libroc = ""
            #send_message(mensajes["availablebooksr"], chat)
            for libro in libros:
                libroa = libro.replace('_',' - ')
                librob.append(libroa)
                librob.append("\n")
            send_message(libroc.join(librob), chat)
            back = [{'text':"Regresar",'callback_data':"Pública."},{'text':"Available Books",'callback_data':"/AvailableBooks"}]
            keyboard = build_inlinekeyboard(back)
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
            tick = bpa.ticker(book)
            ntick = 0
            atick = 1
            c = ""
            d = []
            for i in tick:
                b = tickerr[atick].format(tick[ntick])
                d.append(b)
                d.append("\n")
                ntick = ntick + 1
                atick = atick + 1
            send_message(c.join(d), chat)
            keyboard = build_inlinekeyboard(tickere)
            send_message(mensajes["tickere"], chat, keyboard)
        ##ORDERBOOK COMPRAS##
        elif comando == "Compras":
            try:
                bbook = ltext
                book = bbook[9:]
                if book == "":
                    raise TypeError ("Libro incorrecto")
                lbids, lasks, Fecha = bpa.orderbook(book)
                a = 0
                b = 0
                c = 1
                d = (len(lbids)/2)
                g = "Fecha: {}".format(Fecha)
                m = []
                h = ""
                send_message(g, chat)
                while a != d:
                    e = orderbookrr[0].format(lbids[b])
                    f = orderbookrr[1].format(lbids[c])
                    sa = str(a)
                    m.append(sa)
                    m.append("\n")
                    m.append(e)
                    m.append("\n")
                    m.append(f)
                    m.append("\n")
                    b = b + 2
                    c = c + 2
                    a = a + 1
                send_message(h.join(m),chat)
                keyboard = build_inlinekeyboard(orderbooke)
                send_message(mensajes["tickere"], chat, keyboard)
            except TypeError as e:
                send_message(str(e), chat)
        ##ORDERBOOK VENTAS##
        elif comando == "Ventas":
            try:
                bbook = ltext
                print(bbook)
                book = bbook[9:]
                if book == "":
                    raise TypeError ("Libro incorrecto")
                lbids, lasks, Fecha = bpa.orderbook(book)
                a = 0
                b = 0
                c = 1
                d = (len(lasks)/2)
                g = "Fecha: {}".format(Fecha)
                m = []
                h = ""
                send_message(g, chat)
                while a != d:
                    e = orderbookrr[0].format(lasks[b])
                    f = orderbookrr[1].format(lasks[c])
                    sa = str(a)
                    m.append(sa)
                    m.append("\n")
                    m.append(e)
                    m.append("\n")
                    m.append(f)
                    m.append("\n")
                    b = b + 2
                    c = c + 2
                    a = a + 1
                send_message(h.join(m),chat)
                keyboard = build_inlinekeyboard(orderbooke)
                send_message(mensajes["tickere"], chat, keyboard)
            except TypeError as e:
                send_message(str(e), chat)
        elif comando.startswith("Trades"):
            try:
                ltext = dbm.return_beforelastmessage(UId, 1)
                bbook = ltext
                book = bbook[7:]
                if book == "":
                    raise TypeError ("Libro incorrecto")
                a = bpa.trades(book)
                b = ""
                keyboard = build_inlinekeyboard(tradese)
                send_message(b.join(a),chat)
                send_message(mensajes["tradesr"],chat,keyboard)
            except TypeError as e:
                send_message(str(e),chat)
        elif comando == "Entrar":
            keyboard = build_inlinekeyboard(key0)
            send_message(mensajes["entrar1"],chat,keyboard)
        elif comando == "Key0":
            keyboard = build_inlinekeyboard(key1)
            send_message(mensajes["entrar2"],chat,keyboard)
        elif comando == "Key1":
            Bitso1 = dbm.return_beforelastmessage(UId, 2)
            Bitso0 = dbm.return_beforelastmessage(UId, 4)
            #print(Bitso0 + " BICSO0")
            #print(Bitso1 + " BICSO1")
            send_message(mensajes["entrar3"],chat)
            dbb.add_bitso(UId, Bitso0, Bitso1)
            #print(UId)
            axa = dbb.get_bitso(UId)
            #print(axa)
        #elif comando == "AccountStatus":
    elif text == "Trades":
        keyboard = build_inlinekeyboard(trades)
        send_message(mensajes["trades"], chat, keyboard)
    elif text == "Ticker":
        keyboard = build_inlinekeyboard(ticker)
        send_message(mensajes["ticker"], chat, keyboard)
    elif text == "OrderBook":
        keyboard = build_inlinekeyboard(orderbook)
        send_message(mensajes["ticker"], chat, keyboard)
    elif text.startswith("OrderBook"):
        keyboard = build_inlinekeyboard(orderbookr)
        send_message(mensajes["orderbookr"], chat, keyboard)
    elif text == "Pública.":
        keyboard = build_inlinekeyboard(apipublica)
        send_message(mensajes["apipublica"], chat, keyboard)
    elif text == "Privada.":
        keyboard = build_inlinekeyboard(apiprivada)
        send_message(mensajes["apiprivada"], chat, keyboard)
    elif text == "Entrar.":
        keyboard = build_inlinekeyboard(entrar)
        send_message(mensajes["entrar0"], chat, keyboard)
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
    url = URL + "sendMessage?text={}&chat_id={}&parse_mode=Markdown".format(text, chat_id)
    if reply_markup:
        url += "&reply_markup={}".format(reply_markup)
    get_url(url)

text, chat = get_last_chat_id_and_text(get_updates())
send_message(text, chat)

##EJECUTAR
def main():
    dbu.setup()
    dbb.setup()
    last_update_id = None
    while True:
        updates = get_updates(last_update_id)
        if len(updates["result"]) > 0:
            last_update_id = get_last_update_id(updates) + 1
            handle_updates(updates)
        time.sleep(0.5)

#CONDICION PARA EJECUTAR
if __name__ == '__main__':
    main()
