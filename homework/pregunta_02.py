"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

    """
    archivo_datos = "files/input/data.csv"

    # Crear diccionario vacío para llevar cuenta
    conteo = {}

    # Abrir y leer archivo
    with open(archivo_datos, "r", encoding="utf-8") as f:
        lineas = f.readlines()
        for registro in lineas:
            datos = registro.strip().split("\t")
            if datos:
                primera_letra = datos[0]
                conteo[primera_letra] = conteo.get(primera_letra, 0) + 1

    # Convertir a lista y ordenar
    lista_resultado = [(k, v) for k, v in conteo.items()]
    lista_resultado.sort()

    return lista_resultado
