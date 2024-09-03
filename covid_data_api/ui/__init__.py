def create_covid_data_ui_cli(data_frame):
    """
    Crea una interfaz de línea de comandos para mostrar los datos de COVID-19 con bordes en la tabla.

    Parámetros:
        data_frame: DataFrame de pandas que contiene los datos de COVID-19.

    Retorna:
        None
    """
    # Filtrar y renombrar columnas específicas
    columns_to_show = {
        'ciudad_municipio_nom': 'Ciudad',
        'departamento_nom': 'Departamento',
        'edad': 'Edad',
        'tipo_recuperacion': 'Tipo',
        'estado': 'Estado'
    }

    # Seleccionar solo las columnas necesarias del DataFrame
    filtered_data = data_frame[list(columns_to_show.keys())]
    filtered_data.columns = list(columns_to_show.values())

    # Definir el ancho de cada columna
    col_widths = [25, 15, 5, 10, 10]

    # Definir el formato para las filas y bordes
    row_format = "│ " + " │ ".join(f"{{:<{w}}}" for w in col_widths) + " │"
    top_border = "┌" + "┬".join("─" * (w + 2) for w in col_widths) + "┐"
    mid_border = "├" + "┼".join("─" * (w + 2) for w in col_widths) + "┤"
    bottom_border = "└" + "┴".join("─" * (w + 2) for w in col_widths) + "┘"
    
    # Imprimir el borde superior
    print(top_border)
    
    # Imprimir el encabezado
    print(row_format.format(*filtered_data.columns))
    
    # Imprimir la línea entre el encabezado y los datos
    print(mid_border)
    
    # Imprimir cada fila de datos
    for row in filtered_data.itertuples(index=False):
        print(row_format.format(*row))
    
    # Imprimir el borde inferior
    print(bottom_border)
