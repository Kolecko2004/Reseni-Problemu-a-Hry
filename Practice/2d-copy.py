def line_size(row, column, data):
    main_value = data[row][column]
    vertical_size = 1
    horizontal_size = 1
    max_rows = len(data)
    max_col = len(data[0])
    i = 1
    vl = True
    vr = True

    while vl or vr:
        vl = False
        vr = False
        if column + i < max_rows and data[row][column + i] == main_value:
            print('+')
            vertical_size += 1
            vr = True
        if column - i >= 0 and data[row][column - i] == main_value:
            print(f'- and row{row} and column{column - i}')
            vertical_size += 1
            vl = True
        i += 1

    '''i = 1

    while (row + i < 8 and data[row + i][column] == main_value) or (row - i >= 0 and data[row - i][column] == main_value) :
        if data[row + i][column] == main_value:
            horizontal_size += 1
        if data[row - i][column] == main_value:
            horizontal_size += 1
        i += 1'''

    print(f"{vertical_size}x - [{main_value}] on the vertical line")
    # print(f"{horizontal_size}x - [{main_value}] on the horizontal line")


if __name__ == '__main__':
    a = 7
    b = 5
    c = [
        [0, 1, 1, 1, 1, 0, 0, 0],
        [1, 1, 0, 1, 0, 1, 1, 1],
        [0, 1, 1, 0, 0, 1, 0, 1],
        [1, 1, 1, 0, 1, 1, 0, 1],
        [0, 1, 0, 0, 0, 0, 1, 1],
        [1, 0, 1, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 1, 1, 1],
        [1, 1, 0, 1, 0, 1, 1, 1]]

    line_size(a, b, c)
