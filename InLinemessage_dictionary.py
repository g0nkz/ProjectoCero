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

tickerr = [
'Alto: {}',
'Ultimo: {}',
'Fecha: {}',
'Libro: {}',
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

orderbookrr = ['Libro: {}','Precio: {}', 'Cantidad: {}', 'Lado: {}', 'Actualizado al: {}', 'Secuencia: {}']

orderbooke = [
{'text':'Regresar a OrderBook','callback_data':'OrderBook'},
{'text':'API Pública','callback_data':'Pública.'}
]

tradese = [
{'text':'Regresar a Trades','callback_data':'Trades'},
{'text':'API Pública','callback_data':'Pública.'}
]
