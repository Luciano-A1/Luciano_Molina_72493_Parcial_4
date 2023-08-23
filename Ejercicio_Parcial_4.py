print('<>' * 40)
print('Ejercicio tipo Pesadilla Parcial 4')
print('<>' * 40)

from utilidades import *
from Registro import *
import random
import pickle
import os


def menu_generico_x():
    cadena = "Menu de Opciones\n" \
             "================================\n" \
             "_1)---> Generar Vector de juegos.\n" \
             "_2)---> Mostrar juego de pais de origen.\n" \
             "_3)---> Matriz (pais * tipo)\n" \
             "_4)---> Generar Archivo.\n" \
             "_5)---> Mostrar Archivo.\n" \
             "_0) Salir\n" \
             "---> Ingrese su opcion :"
    return cadena


def add_in_order(v, reg):
    izq, der = 0, len(v) - 1
    pos = 0
    while izq <= der:
        med = (izq + der) // 2
        if v[med].nombre == reg.nombre:
            pos = med
            break

        if v[med].nombre > reg.nombre:
            der = med - 1
        else:
            izq = med + 1

    if izq > der:
        pos = izq
    v[pos:pos] = [reg]


def cargar_vector(vec, n):
    nombres = 'Juego', 'Arcade', 'Demo'
    for i in range(n):
        identificacion = random.randint(0, 10000)
        nombre = random.choice(nombres) + str(i)
        cantidad_de_stock = random.randint(0, 5000)
        precio_de_venta = random.randint(500, 10000)
        pais = random.randint(0, 29)
        tipo = random.randint(0, 14)
        reg = Empresa(identificacion, nombre, cantidad_de_stock, precio_de_venta, pais, tipo)
        add_in_order(vec, reg)
    print('---> Datos Cargados ...')


def mostrar_vector(vec, p):
    todo_bien = False
    print('-' * 120)
    print(mostrar_titulo())
    print('-' * 120)
    for i in range(len(vec)):
        if vec[i].pais == p:
            todo_bien = True
            print(vec[i])
    print('-' * 120)

    if not todo_bien:
        print('---> No se ha encontrado ningun juego con ese pais :', p)
        print('-' * 120)


def generar_matriz(vec):
    mat = [[0] * 30 for filas in range(15)]

    for reg in vec:
        filas = reg.tipo
        columnas = reg.pais - 1
        mat[filas][columnas] += reg.cantidad_de_stock

    return mat


def mostrar_matriz(mat, x):
    bandera_2 = False
    for f in range(len(mat)):
        for c in range(len(mat[f])):
            if 0 < mat[f][c] < x:
                bandera_2 = True
                print('---> tipo:', f, '_Pais de origen :', c + 1, '_stock :', mat[f][c], 'Juegos')

    if not bandera_2:
        print('---> No se ha encontrado ningun contador con ese valor del', 0, 'al', x)


def generar_archivo(fd, vec):
    m = open(fd, 'wb')
    for reg in vec:
        if reg.cantidad_de_stock > 0 and reg.pais != 0 and reg.pais != 1:
            pickle.dump(reg, m)
    m.close()
    print('-' * 80)
    print('---> Archivo :', fd, 'Generado ...')
    print('-' * 80)


def generar_promedio(monto, cant):
    promedio = 0
    if cant != 0:
        promedio = monto / cant

    return promedio


def mostrar_archivo_juegos(fd):
    if os.path.exists(fd):
        suma = 0
        total_juegos_mostrados = 0
        m = open(fd, 'rb')
        tam = os.path.getsize(fd)
        while m.tell() < tam:
            reg = pickle.load(m)
            suma += reg.precio_de_venta
            total_juegos_mostrados += 1
            print('-' * 120)
            print(mostrar_titulo())
            print(reg)
        m.close()
        promedio = generar_promedio(suma, total_juegos_mostrados)
        print('-' * 120)
        print('El promedio del precio es de :', '$', round(promedio, 2))
        print('-' * 120)
    else:
        print('---> El archivo', fd, 'no existe ...')


def principal():
    vector_x = []
    bandera = False
    opcion = -1
    while opcion != 0:
        opcion = validar_entre(0, 5, menu_generico_x())
        if opcion == 1:
            n = validar_mayor_que(0, 'Ingrese la cantidad de juegos :')
            cargar_vector(vector_x, n)
        elif opcion == 0:
            print('*** Hasta Luego ***')
        else:
            if len(vector_x) == 0:
                print('---> El vector no está cargado. Use la Opcion 1 ...')
            else:
                if opcion == 2:
                    p = validar_entre(0, 29, 'Ingrese el pais de origen :')
                    mostrar_vector(vector_x, p)
                if opcion == 3:
                    matriz = generar_matriz(vector_x)
                    x = validar_mayor_que(0, 'Ingrese un valor :')
                    mostrar_matriz(matriz, x)
                if opcion == 4:
                    bandera = True
                    fd = 'juegos.dat'
                    generar_archivo(fd, vector_x)
                if opcion == 5:
                    if bandera:
                        mostrar_archivo_juegos(fd)
                    else:
                        print('---> Primero Genere un archivo ...')


if __name__ == '__main__':
    principal()
