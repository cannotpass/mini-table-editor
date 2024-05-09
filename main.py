import csv
import os


def load_from_path(file_path):
    data = []
    with open(file_path) as f:
        reader = csv.reader(f)
        for row in reader:
            data.append(row)
    return data


def change_data(data, col, row, new_value):
    """1,0 -> kot"""
    data[row][col] = new_value
    return data


def save_to_path(file_path, data):
    with open(file_path, "w") as f:
        writer = csv.writer(f)
        writer.writerows(data)


def pretty_display(data):
    col_max_lengths = []
    for col_idx in range(len(data[0])):
        max_len = 0
        for row in data:
            if len(row[col_idx]) > max_len:
                max_len = len(row[col_idx])
        col_max_lengths.append(max_len)

    base_format_str = "|"
    for col_idx in range(len(data[0])):
        base_format_str += " {:" + str(col_max_lengths[col_idx]) + "." + str(col_max_lengths[col_idx]) + "s} |"

    for row in data:
        row_str = base_format_str.format(*row)
        print("-" * len(row_str))
        print(row_str)
    print("-" * len(row_str))


def validate_change_input(col, row, new_value, data):
    """Zwraca True jesli dobre dane, False jesli zle."""
    max_row = len(data) - 1
    max_col = len(data[0]) - 1
    messages = []
    if col < 0:
        messages.append("Numer kolumny nie moze byc mniejszy od 1.")
    if row < 0:
        messages.append("Numer wiersza nie moze byc mniejszy od 1.")
    if col > max_col:
        messages.append(f"Maksymalna dlugosc kolumn to: {max_col + 1}.")
    if row > max_row:
        messages.append(f"Maksymalna dlugosc wierszy to: {max_row + 1}.")
    return messages


def test_csv_read_change_display():
    test_path_input = "data/iris.csv"
    test_path_output = "data/iris-edit.csv"
    data = load_from_path(test_path_input)
    data = change_data(data, 0, 1, "kot")
    # pprint(data)
    pretty_display(data)
    save_to_path(test_path_output, data)


def main():
    print("Program pozwala odczytac plik, wprowadzic zmiany i zapisac.")
    while True:
        file_name = input("Podaj sciezke pliku: ")
        if os.path.exists(file_name):
            break
        print(f"Sciezka do pliku nie istnieje: {file_name}")
    data = load_from_path(file_name)
    while True:
        action = input("Aby wyswietlic zawartosc wpisz 1, aby zmienic wpisz 2, aby zapisac wpisz 3, aby przerwac wpisz 0: ")
        if action == '0':
            break
        elif action == '1':
            pretty_display(data)
        elif action == '2':
            col_idx = int(input("Podaj numer kolumny: ")) - 1
            row_idx = int(input("Podaj numer wiersza: ")) - 1
            new_value = input("Podaj nowa wartosc: ")
            validation_messages = validate_change_input(col=col_idx, row=row_idx, new_value=new_value, data=data)
            if not validation_messages:
                data = change_data(data=data, col=col_idx, row=row_idx, new_value=new_value)
            else:
                print("Podano zle dane:")
                for msg in validation_messages:
                    print(f"-> {msg}")
        elif action == '3':
            ans = input("Czy zapisac w oryginalnej sciezce (y/n): ")
            if ans == 'n':
                save_file_name = input("Podaj sciezke do zapisu: ")
                folder, plik = os.path.split(save_file_name)
                if not os.path.exists(folder):
                    os.makedirs(folder, exist_ok=True)
            else:
                save_file_name = file_name
            save_to_path(save_file_name, data)
        else:
            print(f"[ERROR] Nieznana komenda: '{action}'")


if __name__ == "__main__":
    main()
