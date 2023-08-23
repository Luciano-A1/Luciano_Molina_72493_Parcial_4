"""
Una empresa de venta de videojuegos mantiene información sobre los distintos juegos que tiene a la venta.
 Por cada juego se registran los datos siguientes: número de identificación (un entero),
  nombre del juego (una cadena), cantidad en stock (puede ser cero), precio de venta,
   pais de origen del juego (un valor entre 0 y 29 incluidos, por ejemplo: 0: Argentina, 1: USA, etc.)
    y tipo de juego (un número entero entre 0 y 14 incluidos, para indicar
     (por ejemplo): 0: de acción, 1: de deportes, etc.).
     Se pide definir un tipo registro Juego con los campos que se indicaron,
      y un programa completo con menú de opciones para hacer lo siguiente:
"""


class Empresa:
    def __init__(self, identificacion, nombre, cantidad_de_stock, precio_de_venta, pais, tipo):
        self.identificacion = identificacion
        self.nombre = nombre
        self.cantidad_de_stock = cantidad_de_stock
        self.precio_de_venta = precio_de_venta
        self.pais = pais
        self.tipo = tipo

    def __str__(self):
        cad = '{:<16}{:^10}{:^20}{:^25}{:>10}{:>14}'
        return cad.format(self.identificacion, self.nombre, self.cantidad_de_stock, self.precio_de_venta, self.pais, self.tipo)


def mostrar_titulo():
    cad = '{:<16}{:^10}{:^20}{:^25}{:>10}{:>14}'
    return cad.format('Identificacion', 'Nombre', 'Cantidad de stock', 'Precio de venta', 'pais', 'tipo')
