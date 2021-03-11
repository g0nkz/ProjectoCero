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
'MenuBitso':'Muy bien, ahora puede acceder a alguna de las siguientes opciones:\n\
Libros disponibles: Muestra una lista de los mercados disponibles.\n\
Ticker: Muestra la información del libro seleccionado\n\
Libros de ordenes: Muestra la lista de las ordenes del libro seleccionado.\n\
Intercambios: Muestra una lista con los intercambios recientes de libro seleccionado.\n\
Inicio: Regresar el menú inicial.\n',
'acepto':'Muy bien, ahora puede seleccionar alguna de las siguientes opciones:\n\
Menu Bitso: Muestra el menu de acciones para bitso.\n\
Configuracion: Muestra los ajustes que puede realizar a este bot.\n ',
'noacepto':'Si cambia de opinión presione el siguiente botón.',
'availablebooksr':'¿Qué desea hacer ahora?¿Ver otra vez los codigos o regresar?',
'ticker':'Por favor eliga alguno de los libros disponibles.',
'tickere':'¿Qué desea hacer ahora?\n¿Ver otro libro o regresar a la API Pública?',
'orderbookr':'¿Qué parte del libro desea ver?\n¿Las compras o las ventas?',
'trades':'Por favor eliga algun de los libros disponibles.',
'tradesr':'¿Que desea hacer ahora?\n¿Ver otro libro de Trades o regresar al menú',
'Configuracion':'Eliga alguna de las siguientes opciones: \n\
Temporizador: Ajustar el intervalo de tiempo entre mensajes automaticos.',
'Timer':'Eliga un intervalo de tiempo o desactive los mensajes automaticos.',
'Timerr':'Su configuracion ha sido cambiada. Puede volver a cambiar la configuracion o regresar al menu anterior.',
'EmptyList':'Este libro esta vacio. Por favor intente con otro.',
'EntradaInvalida':'Entrada invalida, por favor intente de nuevo o eliga una opción.'
}

#Lista de 'botones'.

acuerdo = [
{'text':'Acepto','callback_data':'Acepto'},
{'text':'No acepto','callback_data':'No acepto'}
]

acuerdopositivo = [
{'text': 'Menu Bitso', 'callback_data': 'MenuBitso'},
{'text': 'Configuracion', 'callback_data': 'Configuration'}
]

MenuBitso = [
{'text': 'Libros disponibles', 'callback_data': '/AvailableBooks'},
{'text': 'Ticker', 'callback_data': 'Ticker'},
{'text': 'Libros de ordenes', 'callback_data': 'OrderBook'},
{'text': 'Trades', 'callback_data': 'Trades'},
{'text': 'Inicio', 'callback_data': 'Acepto'},
]

acuerdonegativo = [
{'text':'Cambié de opinión.','callback_data':'/start'}
]

AvailableBooks = [
{'text':"Libros disponibles",'callback_data':"/AvailableBooks"},
{'text':"Regresar",'callback_data':"MenuBitso"}
]

tickere = [
{'text':'Ticker','callback_data':'Ticker'},
{'text':'Regresar','callback_data':'MenuBitso'}
]

orderbooke = [
{'text':'Ver otro libro','callback_data':'OrderBook'},
{'text':'Regresar','callback_data':'MenuBitso'}
]

tradese = [
{'text':'Ver otro libro','callback_data':'Trades'},
{'text':'Regresar','callback_data':'MenuBitso.'}
]

Configuration = [
{'text':'Temporizador','callback_data':'Timer'},
{'text':'Regresar','callback_data':'Acepto'}
]

InLineKeyBoardTimer = [
{'text':'5 minutos','callback_data':'/Timer300'},
{'text':'30 minutos','callback_data':'/Timer1800'},
{'text':'1 hora','callback_data':'/Timer3600'},
{'text':'5 horas','callback_data':'/Timer18000'},
{'text':'Desactivar','callback_data':'/Timer0'},
{'text':'Regresar','callback_data':'Configuration'}
]

EntradaInvalida = [
{'text': 'Menu Bitso', 'callback_data': 'MenuBitso'},
{'text': 'Configuracion', 'callback_data': 'Configuration'}
]

#FORMATOS DE RESPUESTA

orderbookrr = [
                'Libro: {}',
                'Precio: {}',
                'Cantidad: {}',
                'Lado: {}',
                'Actualizado al: {}',
                'Secuencia: {}'
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

tradesrr = [
            'Libro: {}',
            'Fecha: {}',
            'Cantidad: {}',
            'Lado: {}',
            'Precio: {}',
            'TID: {}'
           ]
