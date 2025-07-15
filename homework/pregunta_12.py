"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
    # Archivo de entrada
    input_path = "files/input/data.csv"
    
    # Diccionario para acumular sumas por letra
    totals_by_letter = {}
    
    # Abrir y leer archivo
    file_reader = open(input_path, "r", encoding="utf-8")
    all_data = file_reader.readlines()
    file_reader.close()
    
    # Procesar cada registro
    for record in all_data:
        columns = record.strip().split("\t")
        
        # Validar que tiene todas las columnas
        if len(columns) >= 5:
            main_letter = columns[0]
            values_column = columns[4]
            
            # Calcular suma total de valores en columna 5
            total_for_row = 0
            key_value_pairs = values_column.split(",")
            
            for kv_pair in key_value_pairs:
                if ":" in kv_pair:
                    # Dividir en clave y valor
                    parts = kv_pair.split(":", 1)
                    if len(parts) == 2:
                        value_part = parts[1]
                        
                        try:
                            # Convertir a número y sumar
                            num_value = int(value_part)
                            total_for_row += num_value
                        except ValueError:
                            # Saltar valores no numéricos
                            pass
            
            # Acumular al total de la letra
            if main_letter in totals_by_letter:
                totals_by_letter[main_letter] += total_for_row
            else:
                totals_by_letter[main_letter] = total_for_row
    
    # Generar resultado ordenado
    final_dict = {}
    for letter in sorted(totals_by_letter.keys()):
        final_dict[letter] = totals_by_letter[letter]
    
    return final_dict
