"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
    data_path = "files/input/data.csv"
    
    # Diccionario para agrupar valores por letra
    data_by_letter = {}
    
    # Leer datos del archivo
    file = open(data_path, "r", encoding="utf-8")
    for row in file:
        cols = row.strip().split("\t")
        
        # Verificar formato correcto
        if len(cols) >= 2:
            letter = cols[0]
            try:
                value = int(cols[1])
                
                # Inicializar lista si no existe
                if letter not in data_by_letter:
                    data_by_letter[letter] = []
                
                # Agregar valor a la lista
                data_by_letter[letter].append(value)
                
            except ValueError:
                # Omitir valores no numéricos
                pass
    
    file.close()
    
    # Calcular min/max para cada letra
    output = []
    for letra in sorted(data_by_letter.keys()):
        valores_letra = data_by_letter[letra]
        valor_max = max(valores_letra)
        valor_min = min(valores_letra)
        
        # Crear tupla con formato requerido
        output.append((letra, valor_max, valor_min))
    
    return output
