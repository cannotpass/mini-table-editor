def change_data(data, col, row, new_value):
    """1,0 -> kot"""
    data[row][col] = new_value
    return data


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