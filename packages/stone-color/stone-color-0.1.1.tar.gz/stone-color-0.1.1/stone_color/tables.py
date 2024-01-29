def ascii_table(headers: list[str], data: list[list[str]], spaces=4, lspace=2):
    div = " "*spaces
    ldiv = " "*lspace

    col_widths = [max(len(str(cell)) for cell in col) for col in zip(headers, *data)]

    header_row = div.join(f"{header: <{width}}" for header, width in zip(headers, col_widths))
    print("\n" + ldiv + header_row)

    separator_row = div.join("-" * width for width in col_widths)
    print(ldiv + separator_row)

    for row in data:
        row_str = div.join(f"{cell: <{width}}" for cell, width in zip(row, col_widths))
        print(ldiv + row_str)

    print()
