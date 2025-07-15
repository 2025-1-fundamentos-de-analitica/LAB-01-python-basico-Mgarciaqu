"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]


    """
    # Archivo fuente
    data_source = "files/input/data.csv"
    
    # Lista para el resultado final
    output_list = []
    
    # Procesar archivo
    file_handle = open(data_source, "r", encoding="utf-8")
    file_content = file_handle.read()
    file_handle.close()
    
    # Dividir en líneas y procesar cada una
    rows = file_content.strip().split("\n")
    for row in rows:
        cols = row.split("\t")
        
        # Verificar que tiene todas las columnas necesarias
        if len(cols) >= 5:
            letter = cols[0]
            col4_data = cols[3]  # Columna 4
            col5_data = cols[4]  # Columna 5
            
            # Contar elementos separados por coma en cada columna
            count_col4 = len(col4_data.split(","))
            count_col5 = len(col5_data.split(","))
            
            # Agregar tupla al resultado
            output_list.append((letter, count_col4, count_col5))
    
    return output_list
