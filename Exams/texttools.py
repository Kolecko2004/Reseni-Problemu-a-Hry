def count_rows_and_words(filename):
    file = open(filename, mode='r', encoding='UTF-8')
    
    whole_file = file.read()
    
    pocet_radku = 0
    pocet_slov = 0
    
    for i in whole_file:
        if i == '\n':
            pocet_radku += 1
            
    
    pocet_slov = len(whole_file.split())
    
    return (pocet_radku, pocet_slov)

def compute_word_frequencies(filename):
    file = open(filename, mode='r', encoding='UTF-8')
    words_count = {}
    
    whole_file = file.read()
    
    pocet_slov = len(whole_file.split())
    
    for i in whole_file.split():
        if i in words_count:
            words_count.update({i, words_count[i] + 1})
        else:
            words_count[i] = 1
            
    print(words_count)
    return words_count
    
if __name__ == "__main__":
    print(count_rows_and_words('hello.txt'))
    compute_word_frequencies('hello.txt')