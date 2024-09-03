from api import get_data, process_data
from ui import create_covid_data_ui_cli

def main():
    """
    Función principal que obtiene datos de COVID-19 desde la API,
    los convierte en un DataFrame y luego los muestra en una interfaz gráfica.
    """
    # Solicitar al usuario el nombre del departamento
    departament = input("Ingrese el nombre del departamento: ").upper()

    try:
        # Obtener datos de la API
        data = get_data(100, departament)
        
        # Procesar los datos con pandas
        data_frame = process_data(data)

        # Crear la interfaz gráfica con los datos
        create_covid_data_ui_cli(data_frame)
    
    except Exception as e:
        print(f"Ocurrió un error al obtener o procesar los datos: {e}")

# Llamar a la función principal
if __name__ == "__main__":
    main()
