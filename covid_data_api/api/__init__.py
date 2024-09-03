import pandas as pd
from sodapy import Socrata

def get_data(record_limit, department_name):
    """
    Obtiene datos desde la API de datos abiertos de Colombia.

    Parámetros:
        record_limit (int): Límite de registros a obtener.
        
        department_name (str): Nombre del departamento para filtrar los datos.

    Retorna:
        data (list): Lista de diccionarios que contienen los datos de COVID-19.
    """
    # Crear el cliente para la API de datos abiertos de Colombia
    client = Socrata("www.datos.gov.co", None)

    # Obtener los datos desde la API
    data = client.get("gt2j-8ykr", limit=record_limit, departamento_nom=department_name)
    
    return data

def process_data(data):
    """
    Convierte los resultados de la API en un DataFrame de pandas.
    
    Parámetros:
        data (list): Lista de resultados de la API.
        
    Retorna:
        data_frame: DataFrame de pandas que contiene los datos de COVID-19.
    """
    # Convertir los resultados en un DataFrame
    data_frame = pd.DataFrame.from_records(data)

    return data_frame
