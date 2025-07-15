"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """
    # Ubicación del archivo de datos
    source_file = "files/input/data.csv"
    
    # Contador para cada clave
    key_counter = {}
    
    # Leer archivo completo
    with open(source_file, "r", encoding="utf-8") as data:
        all_lines = data.readlines()
        
        for line in all_lines:
            parts = line.strip().split("\t")
            
            # Solo procesar si tiene 5 columnas
            if len(parts) >= 5:
                # Obtener columna con pares key:value
                key_value_column = parts[4]
                
                # Dividir en pares individuales
                individual_pairs = key_value_column.split(",")
                
                for pair in individual_pairs:
                    if ":" in pair:
                        # Extraer solo la clave (antes del :)
                        key_part = pair.split(":")[0]
                        
                        # Incrementar contador
                        if key_part in key_counter:
                            key_counter[key_part] += 1
                        else:
                            key_counter[key_part] = 1
    
    # Ordenar alfabéticamente y retornar
    sorted_keys = sorted(key_counter.keys())
    ordered_result = {}
    for k in sorted_keys:
        ordered_result[k] = key_counter[k]
    
    return ordered_result
