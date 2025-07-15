"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

    """
    path = "files/input/data.csv"

    # Usar defaultdict para simplificar el código
    from collections import defaultdict
    suma_letras = defaultdict(int)

    with open(path, "r", encoding="utf-8") as archivo:
        for fila in archivo:
            campos = fila.strip().split("\t")
            if len(campos) >= 2:
                letra_clave = campos[0]
                try:
                    numero = int(campos[1])
                    suma_letras[letra_clave] += numero
                except ValueError:
                    # Saltar filas con datos inválidos
                    continue

    # Retornar como lista ordenada
    return sorted(suma_letras.items())
