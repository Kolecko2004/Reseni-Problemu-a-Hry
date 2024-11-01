class Myclass:
    def __init__(self, row, column, data):
        self.main_value = data[row][column]
        self.max_rows = len(data)
        self.max_col = len(data[0])
        self.row = row
        self.column = column
        self.data = data
        size = 1
        self.index = 1

        self.vertical(size, self.index)
        self.horizontal(size, self.index)
        self.diagonal(size, self.index)
        self.cycle(size, self.index, self.column + self.index < self.max_col and self.data[self.row][self.column + self.index])
        print(self.column + self.index < self.max_col and self.data[self.row][self.column + self.index])

    def cycle(self, size, index, way):
        condition = 0
        if way == 'left':
            condition == self.column + index < self.max_col and self.data[self.row][self.column + index]

        while condition == self.main_value:
            size += 1
            self.index += 1
            print(way)

    def vertical(self, size, index):

        while self.column + index < self.max_col and self.data[self.row][self.column + index] == self.main_value :
            size += 1
            index += 1
        
        index = 1
        
        while self.column - index >= 0 and self.data[self.row][self.column - index] == self.main_value :
            size += 1
            index += 1
        
        self.print_res(size, 'vertical')

    def horizontal(self, size, index):

        while self.row + index < self.max_rows and self.data[self.row + index][self.column] == self.main_value :
            size += 1
            index += 1
        
        index = 1
        
        while self.row - index >= 0 and self.data[self.row - index][self.column] == self.main_value :
            size += 1
            index += 1
        
        self.print_res(size, 'horizontal')

    def diagonal(self, size, index):

        while self.row + index < self.max_rows and self.column + index < self.max_col and self.data[self.row + index][self.column + index] == self.main_value :
            size += 1
            index += 1
        
        index = 1
        
        while self.row - index >= 0 and self.column - index >= 0 and self.data[self.row - index][self.column - index] == self.main_value :
            size += 1
            index += 1
        
        self.print_res(size, 'diagonal')

    def print_res(self, size, type):
        print(f"{size} x [{self.main_value}] on the {type} line")

if __name__ == '__main__':
    a = 0
    b = 2
    c = [
    [0, 1, 1, 1, 1, 0, 0, 0 ],
    [1, 1, 0, 1, 0, 1, 1, 1 ],
    [0, 1, 1, 0, 0, 1, 0, 1 ],
    [1, 1, 1, 0, 1, 1, 0, 1 ],
    [0, 1, 0, 0, 0, 0, 1, 1 ],
    [1, 0, 1, 1, 0, 0, 0, 0 ],
    [0, 1, 1, 1, 0, 1, 1, 1 ],
    [1, 1, 0, 1, 0, 1, 1, 1 ]]

    Myclass(a, b, c)