__author__ = 'Algoritmos utiles... by 0A1'


# ---> while corta cuando sea Falsa

def validar_mayor_que(minimo, mensaje='Ingrese un numero ... :'):
    numero = -1

    while numero <= minimo:
        numero = int(input(mensaje))
        if numero <= minimo:
            print('*** Error, Ingrese un numero MAYOR a :', minimo)

    return numero


def validar_entre(minimo, maximo, mensaje='Ingrese un numero ... :'):
    numero = -1

    while numero < minimo or numero > maximo:
        numero = int(input(mensaje))
        if numero < minimo or numero > maximo:
            print('*** Error, Ingrese un numero mayor que :', minimo, 'y menor que :', maximo)

    return numero


def promedio_generico_vector(vector):
    suma = 0
    tam = len(vector)
    for i in range(tam):
        suma += vector[i]

    if len(vector) != 0:
        prom = suma / tam
    else:
        prom = 0

    return prom


def calcular_porcentaje_generico(cantidad, total):
    porcentaje = 0
    if total > 0:
        porcentaje = cantidad * 100 / total
    return porcentaje


def contadores_vector(v):
    c = [0] * 15
    n = len(v)
    for i in range(n):
        ind = v[i].tipo
        c[ind] += 1
        # c[v[i].tipo] += 1

    print('Cantidad de servicios tipo:')
    for r in range(15):
        if c[r] != 0:
            print('---> Tipo de servicio', r, 'Cantidad de apariciones:', c[r])

    # for i in range(len(c)):
    # if c[i] > 0:
    # print('Con ', str(i + 1), 'estrellas hay: ', vec_conteo[i], 'artículos.')


def buscar_x_vector_secuencial(vector, x):
    ban = False

    for numero in range(len(vector)):
        if vector[numero] == x:
            ban = True
            break

    return ban


def busqueda_binaria(vector, valor):
    izq, der = 0, len(vector)
    while izq <= der:
        med = (izq + der) // 2
        if vector[med] == valor:
            return med

        if vector[med] > valor:
            der = med - 1
        else:
            izq = med + 1

    return -1


def ordenar_vec_mayor(vec):
    n = len(vec)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if vec[i] < vec[j]:
                vec[i], vec[j] = vec[j], vec[i]


def menu_generico():
    cadena = "Menu de Opciones\n" \
             "================================\n" \
             "_1)---> Mostrar generación y carga del VECTOR.\n" \
             "_2)---> \n" \
             "_3)---> \n" \
             "_4)---> \n" \
             "_5)---> \n" \
             "_6)---> \n" \
             "_7)---> \n" \
             "_0) Salir\n" \
             "---> Ingrese su opcion :"
    return cadena
