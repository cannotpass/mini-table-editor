import os
from modules.printers import pretty_display
from modules.data import change_data
from modules.data import validate_change_input
from modules.file import load_from_path
from modules.file import save_to_path


def main():
    print("Program pozwala odczytac plik, wprowadzic zmiany i zapisac.")
    # Load file name as long as it does not exist
    while True:
        file_name = input("Podaj sciezke pliku: ")
        if os.path.exists(file_name):
            break
        print(f"Sciezka do pliku nie istnieje: {file_name}")
    # Load data from file
    data = load_from_path(file_name)
    while True:
        action = input("Aby wyswietlic zawartosc wpisz 1, aby zmienic wpisz 2, aby zapisac wpisz 3, aby przerwac wpisz 0: ")
        if action == '0':
            # Exit
            break
        elif action == '1':
            # Display table
            pretty_display(data)
        elif action == '2':
            # Load change data
            col_idx = int(input("Podaj numer kolumny: ")) - 1
            row_idx = int(input("Podaj numer wiersza: ")) - 1
            new_value = input("Podaj nowa wartosc: ")
            # Check if change data is ok
            validation_messages = validate_change_input(col=col_idx, row=row_idx, new_value=new_value, data=data)
            if not validation_messages:
                # If yes, do change
                data = change_data(data=data, col=col_idx, row=row_idx, new_value=new_value)
            else:
                # If no, print validation error messages
                print("Podano zle dane:")
                for msg in validation_messages:
                    print(f"-> {msg}")
        elif action == '3':
            # Save in chosen file
            ans = input("Czy zapisac w oryginalnej sciezce (y/n): ")
            if ans == 'n':
                save_file_name = input("Podaj sciezke do zapisu: ")
                folder, plik = os.path.split(save_file_name)
                # If target folder does not exist, create it
                if not os.path.exists(folder):
                    os.makedirs(folder, exist_ok=True)
            else:
                save_file_name = file_name
            save_to_path(save_file_name, data)
        else:
            print(f"[ERROR] Nieznana komenda: '{action}'")


if __name__ == "__main__":
    main()
