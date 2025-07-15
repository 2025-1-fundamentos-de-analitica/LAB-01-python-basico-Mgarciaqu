"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla
    contiene  el valor de la segunda columna; la segunda parte de la tupla
    es una lista con las letras (ordenadas y sin repetir letra) de la
    primera  columna que aparecen asociadas a dicho valor de la segunda
    columna.

    Rta/
    [(0, ['C']),
     (1, ['B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E']),
     (4, ['B', 'E']),
     (5, ['B', 'C', 'D', 'E']),
     (6, ['A', 'B', 'C', 'E']),
     (7, ['A', 'C', 'D', 'E']),
     (8, ['A', 'B', 'D', 'E']),
     (9, ['A', 'B', 'C', 'E'])]

    """
    # Definir ruta del archivo
    file_path = "files/input/data.csv"
    
    # Usar sets para evitar duplicados automáticamente
    letters_by_value = {}
    
    # Abrir archivo y procesar
    with open(file_path, "r", encoding="utf-8") as input_file:
        for row in input_file:
            columns = row.strip().split("\t")
            
            # Verificar que hay suficientes columnas
            if len(columns) >= 2:
                char = columns[0]
                
                try:
                    num = int(columns[1])
                    
                    # Usar set para mantener letras únicas
                    if num not in letters_by_value:
                        letters_by_value[num] = set()
                    
                    letters_by_value[num].add(char)
                    
                except ValueError:
                    # Continuar si no se puede convertir a int
                    pass
    
    # Construir resultado final
    final_output = []
    for number in sorted(letters_by_value.keys()):
        unique_letters = letters_by_value[number]
        # Convertir set a lista ordenada
        sorted_letters = sorted(list(unique_letters))
        final_output.append((number, sorted_letters))
    
    return final_output
