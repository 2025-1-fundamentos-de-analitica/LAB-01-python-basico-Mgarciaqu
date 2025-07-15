"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """

    ruta = "files/input/data.csv"

    total = 0
    try:
        with open(ruta, "r", encoding="utf-8") as file:
            content = file.readlines()
            for row in content:
                fields = row.strip().split("\t")
                if len(fields) > 1:
                    total += int(fields[1])
    except (ValueError, IndexError):
        pass
    
    return total
