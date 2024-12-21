def answer():
    """Answer for the question.

    :return set:
    """
    return set(6)


def longest_word(inputed_string):
    """Find the longest word in the given string, and its length.

    A 'word' is a sequence of characters other than spaces, which has non-zero length.

    If the given string contains no words, (0, '') should be returned.

    If multiple words are of the longest length, return the one that occurs first in the string.

    :param string: The string to find longest word in.
    :type string: str
    :return: A tuple (length of the longest word, the longest word).
    :rtype: tuple
    """
    word = ""
    best_word = ""
    best_length = 0

    for char in inputed_string:
        if char == " ":
            word = char
            # if best_length == 0:
            #     best_length = 1
            #     best_word = word
        else:
            if char != " ":
                word += char
                if len(word) > best_length:
                    best_length = len(word)
                    best_word = word
            else:
                word = ""                
        
        if word == " ":
            word = ""
        
    if best_word == " ":
        best_word = ""
        best_length = 0

    return best_length, best_word

if __name__ == "__main__":
    print(longest_word(' a '))
