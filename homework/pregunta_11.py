"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """
    # Ruta del dataset
    dataset_file = "files/input/data.csv"
    
    # Acumuladores por letra
    letter_sums = {}
    
    # Leer datos
    with open(dataset_file, "r", encoding="utf-8") as f:
        for line in f:
            fields = line.strip().split("\t")
            
            # Validar que tiene suficientes columnas
            if len(fields) >= 4:
                try:
                    # Obtener valor numérico de columna 2
                    numeric_val = int(fields[1])
                    
                    # Obtener letras de columna 4
                    letters_string = fields[3]
                    
                    # Separar letras individuales
                    individual_letters = letters_string.split(",")
                    
                    # Distribuir el valor entre todas las letras
                    for single_letter in individual_letters:
                        clean_letter = single_letter.strip()
                        
                        # Sumar al acumulador
                        if clean_letter in letter_sums:
                            letter_sums[clean_letter] += numeric_val
                        else:
                            letter_sums[clean_letter] = numeric_val
                            
                except ValueError:
                    # Omitir si no se puede convertir a número
                    continue
    
    # Crear diccionario ordenado alfabéticamente
    sorted_result = {}
    for letter in sorted(letter_sums.keys()):
        sorted_result[letter] = letter_sums[letter]
    
    return sorted_result
