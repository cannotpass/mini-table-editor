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
    if data:
        print("-" * len(row_str))
