"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla
    contiene un valor posible de la columna 2 y una lista con todas las letras
    asociadas (columna 1) a dicho valor de la columna 2.

    Rta/
    [(0, ['C']),
     (1, ['E', 'B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E', 'E', 'D']),
     (4, ['E', 'B']),
     (5, ['B', 'C', 'D', 'D', 'E', 'E', 'E']),
     (6, ['C', 'E', 'A', 'B']),
     (7, ['A', 'C', 'E', 'D']),
     (8, ['E', 'D', 'E', 'A', 'B']),
     (9, ['A', 'B', 'E', 'A', 'A', 'C'])]

    """
    # Archivo de entrada
    input_file = "files/input/data.csv"
    
    # Diccionario para mapear valores a listas de letras
    value_to_letters = {}
    
    # Leer y procesar datos
    f = open(input_file, "r", encoding="utf-8")
    content = f.read().strip().split("\n")
    f.close()
    
    for record in content:
        fields = record.split("\t")
        
        # Validar que tenemos al menos 2 campos
        if len(fields) >= 2:
            letter_field = fields[0]
            
            try:
                numeric_value = int(fields[1])
                
                # Agregar letra a la lista del valor
                if numeric_value not in value_to_letters:
                    value_to_letters[numeric_value] = []
                
                value_to_letters[numeric_value].append(letter_field)
                
            except ValueError:
                # Saltar registros con valores no numéricos
                continue
    
    # Crear lista final ordenada por valor
    result_list = []
    for val in sorted(value_to_letters.keys()):
        letters_list = value_to_letters[val]
        result_list.append((val, letters_list))
    
    return result_list
