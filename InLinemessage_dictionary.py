#Lista de textos

mensajes = {
    'start':'Esta es una aplicación de pruebas por lo que al hacer uso de la misma usted esta de acuerdo con lo siguiente:\n\
-Usted es el único responsable por su uso.\n\
-Usted hace uso de esta aplicación bajo su propio riesgo.\n\
-No se garantiza el correcto funcionamiento de la misma.\n\
También acepta que los siguientes datos serán guardados \n\
para mejorar el servicio:\n\
-Identificador de usuario.\n\
-Es bot.\n\
-Nombre.\n\
-Apellido.\n\
-Código de lenguaje.\n\
Para más información por favor visite:\n\
https://core.telegram.org/bots/api#use',
    'acepto':'Muy bien, ahora puede acceder a alguna de las siguientes opciones:\n\
Libros disponibles: Muestra una lista de los libros disponibles.\n\
Ticker: Muestra la información del libro seleccionado\n\
Libro de ordenes: Muestra la lista de las ordenes del libro seleccionado.\n\
Intercambios: Muestra una lista con los intercambios recientes de libro seleccionado.\n ',
    'noacepto':'Si cambia de opinión presione el siguiente botón.',
    'availablebooksr':'¿Qué desea hacer ahora?¿Ver otra vez los codigos o regresar?',
    'ticker':'Por favor eliga alguno de los libros disponibles.',
    'tickere':'¿Qué desea hacer ahora?\n¿Ver otro libro o regresar a la API Pública?',
    'orderbookr':'¿Qué parte del libro desea ver?\n¿Las compras o las ventas?',
    'trades':'Por favor eliga algun de los libros disponibles.',
    'tradesr':'¿Que desea hacer ahora?\n¿Regresar a Trades o regresar a la API Pública'
}

#Lista de 'botones'.

acuerdo = [
{'text':'Acepto.','callback_data':'/Acepto.'},
{'text':'No acepto.','callback_data':'/No acepto.'}
]

acuerdopositivo = [
{'text': 'AvailableBooks', 'callback_data': '/AvailableBooks'},
{'text': 'Ticker', 'callback_data': 'Ticker'},
{'text': 'OrderBook', 'callback_data': 'OrderBook'},
{'text': 'Trades', 'callback_data': 'Trades'}
]

acuerdonegativo = [
{'text':'Cambié de opinión.','callback_data':'/Acepto.'}
]

AvailableBooks = [
{'text':"Available Books",'callback_data':"/AvailableBooks"},
{'text':"Regresar",'callback_data':"Pública."}
]

ticker = [
{'text':'btc - mxn','callback_data':'/Tickerbtc_mxn'},
{'text':'eth - btc','callback_data':'/Tickereth_btc'},
{'text':'eth - mxn','callback_data':'/Tickereth_mxn'},
{'text':'xrp - btc','callback_data':'/Tickerxrp_btc'},
{'text':'xrp - mxn','callback_data':'/Tickerxrp_mxn'},
{'text':'ltc - btc','callback_data':'/Tickerltc_btc'},
{'text':'ltc - mxn','callback_data':'/Tickerltc_mxn'},
{'text':'bch - btc','callback_data':'/Tickerbch_btc'},
{'text':'bch - mxn','callback_data':'/Tickerbch_mxn'},
{'text':'tusd - btc','callback_data':'/Tickertusd_btc'},
{'text':'tusd - mxn','callback_data':'/Tickertusd_mxn'},
{'text':'mana - btc','callback_data':'/Tickermana_btc'},
{'text':'mana - mxn','callback_data':'/Tickermana_mxn'},
{'text':'gnt - btc','callback_data':'/Tickergnt_btc'},
{'text':'gnt - mxn','callback_data':'/Tickergnt_mxn'},
{'text':'bat - btc','callback_data':'/Tickerbat_btc'},
{'text':'bat - mxn','callback_data':'/Tickerbat_mxn'},
{'text': 'Regresar', 'callback_data': 'Pública.'}
]

tickerr = [
'Usted eligió el libro: {}',
'Alto: {}',
'Ultimo: {}',
'Fecha: {}',
'Volumen: {}',
'PMP: {}',
'Bajo: {}',
'Venta: {}',
'Compra: {}',
'Cambio en 24 hrs.: {}'
]

tickere = [
{'text':'Ticker','callback_data':'Ticker'},
{'text':'API Publica','callback_data':'Pública.'}
]

orderbook = [
{'text':'btc - mxn','callback_data':'OrderBookbtc_mxn'},
{'text':'eth - btc','callback_data':'OrderBooketh_btc'},
{'text':'eth - mxn','callback_data':'OrderBooketh_mxn'},
{'text':'xrp - btc','callback_data':'OrderBookxrp_btc'},
{'text':'xrp - mxn','callback_data':'OrderBookxrp_mxn'},
{'text':'ltc - btc','callback_data':'OrderBookltc_btc'},
{'text':'ltc - mxn','callback_data':'OrderBookltc_mxn'},
{'text':'bch - btc','callback_data':'OrderBookbch_btc'},
{'text':'bch - mxn','callback_data':'OrderBookbch_mxn'},
{'text':'tusd - btc','callback_data':'OrderBooktusd_btc'},
{'text':'tusd - mxn','callback_data':'OrderBooktusd_mxn'},
{'text':'mana - btc','callback_data':'OrderBookmana_btc'},
{'text':'mana - mxn','callback_data':'OrderBookmana_mxn'},
{'text':'gnt - btc','callback_data':'OrderBookgnt_btc'},
{'text':'gnt - mxn','callback_data':'OrderBookgnt_mxn'},
{'text':'bat - btc','callback_data':'OrderBookbat_btc'},
{'text':'bat - mxn','callback_data':'OrderBookbat_mxn'},
{'text': 'Regresar', 'callback_data': 'Pública.'}
]

orderbookr = [
{'text':'Compras','callback_data':'/Compras'},
{'text':'Ventas','callback_data':'/Ventas'}
]

orderbookrr = ['Precio: {}', 'Cantidad: {}']

orderbooke = [
{'text':'Regresar a OrderBook','callback_data':'OrderBook'},
{'text':'API Pública','callback_data':'Pública.'}
]

trades = [
{'text':'btc - mxn','callback_data':'/Tradesbtc_mxn'},
{'text':'eth - btc','callback_data':'/Tradeseth_btc'},
{'text':'eth - mxn','callback_data':'/Tradeseth_mxn'},
{'text':'xrp - btc','callback_data':'/Tradesxrp_btc'},
{'text':'xrp - mxn','callback_data':'/Tradesxrp_mxn'},
{'text':'ltc - btc','callback_data':'/Tradesltc_btc'},
{'text':'ltc - mxn','callback_data':'/Tradesltc_mxn'},
{'text':'bch - btc','callback_data':'/Tradesbch_btc'},
{'text':'bch - mxn','callback_data':'/Tradesbch_mxn'},
{'text':'tusd - btc','callback_data':'/Tradestusd_btc'},
{'text':'tusd - mxn','callback_data':'/Tradestusd_mxn'},
{'text':'mana - btc','callback_data':'/Tradesmana_btc'},
{'text':'mana - mxn','callback_data':'/Tradesmana_mxn'},
{'text':'gnt - btc','callback_data':'/Tradesgnt_btc'},
{'text':'gnt - mxn','callback_data':'/Tradesgnt_mxn'},
{'text':'bat - btc','callback_data':'/Tradesbat_btc'},
{'text':'bat - mxn','callback_data':'/Tradesbat_mxn'},
{'text': 'Regresar', 'callback_data': 'Pública.'}
]

tradese = [
{'text':'Regresar a Trades','callback_data':'Trades'},
{'text':'API Pública','callback_data':'Pública.'}
]
