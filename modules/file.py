import csv


def load_from_path(file_path):
    data = []
    with open(file_path) as f:
        reader = csv.reader(f)
        for row in reader:
            data.append(row)
    return data


def save_to_path(file_path, data):
    with open(file_path, "w") as f:
        writer = csv.writer(f)
        writer.writerows(data)
