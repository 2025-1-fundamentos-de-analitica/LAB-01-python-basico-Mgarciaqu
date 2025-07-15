"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """
    # Ruta del dataset
    dataset_path = "files/input/data.csv"
    
    # Estructura para guardar todos los valores por clave
    key_values = {}
    
    # Procesar archivo
    with open(dataset_path, "r", encoding="utf-8") as data_file:
        lines = data_file.readlines()
        
        for line in lines:
            parts = line.strip().split("\t")
            
            # Solo procesar si tiene la columna 5
            if len(parts) >= 5:
                # Obtener la última columna
                last_column = parts[4]
                
                # Procesar cada par key:value
                pairs = last_column.split(",")
                for pair in pairs:
                    if ":" in pair:
                        key, val_str = pair.split(":", 1)
                        
                        # Intentar convertir a número
                        try:
                            val_num = int(val_str)
                            
                            # Almacenar valor
                            if key not in key_values:
                                key_values[key] = []
                            key_values[key].append(val_num)
                            
                        except ValueError:
                            # Ignorar valores no convertibles
                            continue
    
    # Generar resultado final
    final_result = []
    for key in sorted(key_values.keys()):
        values_list = key_values[key]
        min_val = min(values_list)
        max_val = max(values_list)
        
        final_result.append((key, min_val, max_val))
    
    return final_result
