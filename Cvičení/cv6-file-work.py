import os
'''
Zapisovat a cist ze souboru
Textove soubory
na strankach je odkaz na soubor prace se soubory
balik import os nam pomaha s praci se soubory
otevrit a zavrit abychom mohli pracovat se soubory formou cteni nebo zapisu
file = open
file.close()

Kodovani - pouzivejme UTF-8 co nejcasteji
obecne v python je kodovanui UTF-8
a to se prida k funkci open, ze to ma byt v kodovani UTF-8

pro praci musime soubor otevrit a take je potreba ho zavirat
da se cist po znacich a po radcich
cteni radku ve for cyklu

Zapis do souboru
f.write
pokud chci psat tak musim soubor otevrit se znakem 'w'
'''
class MyMatrix:
    def __init__(self, matrix = None):
        self.matrix = matrix
    
    def save(self, filename):
        self.file = open(filename, mode='w', encoding='UTF-8')
        
        for i in range(len(self.matrix)):
            for j in self.matrix[i]:
                self.file.write(f'{j} ')
                
            self.file.write('\n')
        self.file.close()
        
    def load(self, filename):
        self.file = open(filename, encoding='UTF-8')
        
        for line in self.file:
            each = line.strip()
            for i in each:
                if i != ' ':
                    print(f'{i}\n')
        
        self.file.close()

def count_chars_in_string(s):
    dictionary = {}
        
    for char in s:
        dictionary[char] = dictionary.get(char, 0) + 1
            
    return dictionary

def count_chars_in_file(filename):
    file = open(filename, encoding='UTF-8')
    whole_txt = file.read()
    char_num = 0
    for i in whole_txt:
        if i == '\n' or i == ' ':
            char_num += 1
    file.close()
    return char_num

if __name__ == "__main__":
    a = MyMatrix([[1, 2, 3], [2, 3, 4]])
    a.save("matrix.txt")
    b = MyMatrix()
    b.load('matrix.txt')
    s = 'Ahoj jak se mas?'
    
    print(count_chars_in_string(s))
    print(count_chars_in_file("kk.txt"))