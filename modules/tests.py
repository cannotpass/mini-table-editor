from modules.data import change_data
from modules.file import load_from_path
from modules.file import save_to_path
from modules.printers import pretty_display


def test_csv_read_change_display():
    test_path_input = "data/iris.csv"
    test_path_output = "data/iris-edit.csv"
    data = load_from_path(test_path_input)
    data = change_data(data, 0, 1, "kot")
    # pprint(data)
    pretty_display(data)
    save_to_path(test_path_output, data)
