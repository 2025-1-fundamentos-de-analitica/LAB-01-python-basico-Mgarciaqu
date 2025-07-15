"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la
    cantidad de registros por cada mes, tal como se muestra a continuación.

    Rta/
    [('01', 3),
     ('02', 4),
     ('03', 2),
     ('04', 4),
     ('05', 3),
     ('06', 3),
     ('07', 5),
     ('08', 6),
     ('09', 3),
     ('10', 2),
     ('11', 2),
     ('12', 3)]

    """
    # Definir la ruta del archivo
    data_file = "files/input/data.csv"
    
    # Lista para almacenar todos los meses
    meses_encontrados = []
    
    # Procesar archivo línea por línea
    with open(data_file, "r", encoding="utf-8") as f:
        for line in f:
            # Dividir en campos
            fields = line.strip().split("\t")
            
            # Validar que existe la columna de fecha
            if len(fields) > 2:
                # Obtener la fecha y extraer el mes
                fecha_completa = fields[2]
                try:
                    # Dividir fecha por guiones y tomar mes
                    _, mes, _ = fecha_completa.split("-")
                    meses_encontrados.append(mes)
                except ValueError:
                    # Ignorar fechas malformadas
                    pass
    
    # Contar ocurrencias de cada mes
    conteo_meses = {}
    for mes in meses_encontrados:
        conteo_meses[mes] = conteo_meses.get(mes, 0) + 1
    
    # Crear lista de tuplas ordenada
    return sorted(list(conteo_meses.items()))
