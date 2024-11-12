def sum_digits(text: str):
    """return the sum of the digits in the text"""
    total = 0

    for char in text:
        if char in '0123456789':
            total += int(char)

    return total
