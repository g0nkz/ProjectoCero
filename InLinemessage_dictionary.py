#Lista de textos

mensajes = {
    'start':'Esta es una aplicación de pruebas por lo que al hacer\
 uso de la misma usted esta de acuerdo con lo siguiente:\n\
-Usted es el único responsable por su uso.\n\
-Usted hace uso de esta aplicación bajo su propio riesgo.\n\
-No se garantiza el correcto funcionamiento de la misma.',
    'acepto':'Muy bien. Ahora, ¿Qué API desea usar? \n\
-Usar API pública. \n\
-Usar API privada. \n\
Seleccione cualquiera para ver que opciones tiene.',
    'noacepto':'Si cambia de opinión presione el siguiente botón.',
    'apipublica':'Las opciones para la API pública son las \
siguientes:\n\
Libros disponibles: Muestra una lista de los libros disponibles.\n\
Ticker: Muestra la información del libro seleccionado\n\
Libro de ordenes: Muestra la lista de las ordenes del libro seleccionado.\n\
Intercambios: Muestra una lista con los intercambios recientes de libro seleccionado.\n\
Regresar: Regresa al menú anterior.',
    'availablebooksr':'¿Qué desea hacer ahora?¿Ver otra vez los codigos o regresar?',
    'ticker':'Por favor eliga alguno de los libros disponibles.',
    'tickere':'¿Qué desea hacer ahora?\n¿Ver otro libro o regresar a la API Pública?',
    'orderbookr':'¿Qué parte del libro desea ver?\n¿Las compras o las ventas?',
    'trades':'Por favor eliga algun de los libros disponibles.',
    'tradesr':'¿Que desea hacer ahora?\n¿Regresar a Trades o regresar a la API Pública',
    'apiprivada':'Para ver las opciones de la API privada de Bitso primero \
tiene que insertar sus llaves de Bitso.',
    'entrar0':'Solo queremos asegurarnos de que esta seguro de querer entrar \
en su cuenta de Bitso a través de este bot.',
    'entrar1':'Por favor inserte su "Clave API" y presione "Listo".',
    'entrar2':'Por favor inserte su "Secreto API" y presione "Listo".',
    'entrar3':'Espere mientras comprobamos los datos proporcionados'
}

acuerdo = [
{'text':'Acepto.','callback_data':'/Acepto.'},
{'text':'No acepto.','callback_data':'/No acepto.'}
]

acuerdopositivo = [
{'text':'Pública.','callback_data':'Pública.'},
{'text':'Privada','callback_data':'Privada.'},
{'text':'Ayuda','callback_data':'Ayuda'}
]

acuerdonegativo = [
{'text':'Cambié de opinión.','callback_data':'/Acepto.'}
]

apipublica = [
{'text': 'AvailableBooks', 'callback_data': '/AvailableBooks'},
{'text': 'Ticker', 'callback_data': 'Ticker'},
{'text': 'OrderBook', 'callback_data': 'OrderBook'},
{'text': 'Trades', 'callback_data': 'Trades'},
{'text': 'Regresar', 'callback_data': '/Acepto.'}
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

apiprivada = [
{'text':'Entrar.', 'callback_data':'Entrar.'},
{'text':'Ayuda (Bitso).', 'url':'https://bitso.com/api_info'},
{'text':'Regresar','callback_data':'Pública,'}
]

entrar = [
{'text':'Estoy seguro.','callback_data':'/Entrar'},
{'text':'No estoy seguro.','callback_data':'Privada.'},
{'text':'Ayuda','callback_data':'None'}
]

key0 = [
{'text':'Listo.','callback_data':'/Key0'},
{'text':'Regresar.','callback_data':'Privada.'},
{'text':'Cancelar.','callback_data':'/CancelarRegistro'}
]

key1 = [
{'text':'Listo.','callback_data':'/Key1'},
{'text':'Regresar','callback_data':'/Entrar'},
{'text':'Cancelar.','callback_data':'/CancelarRegistro'}
]
