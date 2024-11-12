def value_count(data, value):
    count = 0
    for i in range(len(data)):
        for s in data[i]:
            if s == value:
                count += 1
    return count


def value_positions(data, value):
    array = []
    k = 0
    for i in range(len(data)):
        k = 0
        for s in data[i]:
            k += 1
            if s == value:
                array.append((i, k - 1))

    return array


if __name__ == "__main__":
    value = 0
    data = [(0, -1, 1), (-1, 0, -1), (1, 0, 0)]
    final = value_count(data, value)
    print(final)
    positions = value_positions(data, value)
    print(positions)
