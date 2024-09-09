import api
import ui

def main():
    while True:
        ui.print_header()
        option = ui.get_option()

        if option == '0':
            break
        elif option == '1':
            ui.print_get_departament()
            departament = ui.get_departament()
            ui.separator()

        try:
            data = api.get_data(25, departament)
            data_frame = api.process_data(data)
            ui.print_data_table(data_frame)
        
        except Exception as message:
            ui.print_error(message)
    
    print("\n FIN DEL PROGRAMA")

if __name__ == "__main__":
    main()
