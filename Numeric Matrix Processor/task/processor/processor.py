class NumericMatrix:
    def __init__(self, name, size, items_type):
        self.name = name
        self.items_type = items_type
        self.size = [int(s) for s in size]
        self.row_count = self.size[0]
        self.column_count = self.size[1]
        self.items = []
        if self.items_type != '':
            self.initialize_items()

    def print(self):
        for row in range(0, self.row_count):
            print(' '.join(str(r) for r in self.items[row]))

    def set_type(self, text):
        _number = None

        for number in text:
            try:
                int(number)
                self.items_type = 'int'
            except ValueError:
                try:
                    float(number)
                    self.items_type = 'float'
                    break
                except ValueError:
                    print("The operation cannot be performed.")

        self.initialize_items()

    def initialize_items(self):
        if self.items_type == 'int':
            self.items = [[int(0)*i*j for i in range(self.column_count)]
                          for j in range(self.row_count)]
        elif self.items_type == 'float':
            self.items = [[float(0)*i*j for i in range(self.column_count)]
                          for j in range(self.row_count)]

    def read_items(self):
        print(f'Enter {self.name}matrix:')
        for row in range(0, self.row_count):
            text = input().split(' ')
            if self.items_type == '':
                self.set_type(text)
            for column in range(0, self.column_count):
                if self.items_type == 'int':
                    self.items[row][column] = int(text[column])
                elif self.items_type == 'float':
                    self.items[row][column] = float(text[column])

    def set_items(self, items):
        self.items = items


class MatrixProcessor:
    @staticmethod
    def print_menu():
        print("1. Add matrices")
        print("2. Multiply matrix by a constant")
        print("3. Multiply matrices")
        print("4. Transpose matrix")
        print("5. Calculate a determinant")
        print("0. Exit")
        selection = input("Your choice:")
        return selection

    @staticmethod
    def transpose_menu():
        print("1. Main diagonal")
        print("2. Side diagonal")
        print("3. Vertical line")
        print("4. Horizontal line")
        selection = input("Your choice:")
        return selection

    @staticmethod
    def create_matrix(name):
        size = input(f'Enter size of {name}matrix:').split(' ')
        matrix = NumericMatrix(name, size, '')
        matrix.read_items()
        return matrix

    @staticmethod
    def create_matrix2(items_type=''):
        size = input(f'Enter matrix size:').split(' ')
        matrix = NumericMatrix('', size, items_type)
        matrix.read_items()
        return matrix

    @staticmethod
    def can_sum(a: NumericMatrix, b: NumericMatrix):
        return a.size == b.size

    @staticmethod
    def can_multiply(a: NumericMatrix, b: NumericMatrix):
        return a.column_count == b.row_count

    @staticmethod
    def can_calculate_determinant(a: NumericMatrix):
        return a.row_count == a.column_count

    @staticmethod
    def sum(a: NumericMatrix, b: NumericMatrix) -> NumericMatrix:
        print('The result is:')
        result = NumericMatrix('', a.size, a.items_type)
        for row in range(0, a.row_count):
            for column in range(0, a.column_count):
                result.items[row][column] = a.items[row][column] + b.items[row][column]

        return result

    @staticmethod
    def multiply_constant(a: NumericMatrix, number) -> NumericMatrix:
        print('The result is:')
        result = NumericMatrix('', a.size, a.items_type)
        for row in range(0, a.row_count):
            for column in range(0, a.column_count):
                result.items[row][column] = number * a.items[row][column]

        return result

    @staticmethod
    def multiply(a: NumericMatrix, b: NumericMatrix) -> NumericMatrix:
        print('The result is:')
        size = [a.row_count, b.column_count]
        result = NumericMatrix('', size, a.items_type)
        for row in range(0, result.row_count):
            for column in range(0, result.column_count):
                partial = [a.items[row][index] * b.items[index][column] for index in range(0, a.column_count)]
                result.items[row][column] = sum(partial)

        return result

    @staticmethod
    def transpose_diagonal(a: NumericMatrix) -> NumericMatrix:
        print('The result is:')
        result = NumericMatrix('', a.size, a.items_type)
        for row in range(0, a.row_count):
            for column in range(0, a.column_count):
                result.items[column][row] = a.items[row][column]

        return result

    @staticmethod
    def transpose_side_diagonal(a: NumericMatrix) -> NumericMatrix:
        print('The result is:')
        result = NumericMatrix('', a.size, a.items_type)
        for row in range(0, a.row_count):
            for column in range(0, a.column_count):
                result.items[-(column + 1)][-(row + 1)] = a.items[row][column]

        return result

    @staticmethod
    def transpose_vertical(a: NumericMatrix) -> NumericMatrix:
        print('The result is:')
        result = NumericMatrix('', a.size, a.items_type)
        for row in range(0, a.row_count):
            for column in range(0, a.column_count):
                result.items[row][-(column + 1)] = a.items[row][column]

        return result

    @staticmethod
    def transpose_horizontal(a: NumericMatrix) -> NumericMatrix:
        print('The result is:')
        result = NumericMatrix('', a.size, a.items_type)
        for row in range(0, a.row_count):
            for column in range(0, a.column_count):
                result.items[-(row + 1)][column] = a.items[row][column]

        return result

    @staticmethod
    def read_number():
        _number = None
        text = input("Enter constant:")
        try:
            _number = int(text)
        except ValueError:
            try:
                _number = float(text)
            except ValueError:
                print("The operation cannot be performed.")

        return _number

    @staticmethod
    def minor(a: NumericMatrix, exclude_row, exclude_column) -> NumericMatrix:
        size = [a.row_count - 1, a.column_count - 1]
        result = NumericMatrix('', size, a.items_type)
        result_row = 0
        for row in range(0, a.row_count):
            result_column = 0
            if row != exclude_row:
                for column in range(0, a.column_count):
                    if column != exclude_column:
                        result.items[result_row][result_column] = a.items[row][column]
                        result_column += 1
                result_row += 1
        return result

    def determinant(self, a: NumericMatrix):
        if a.size == [1, 1]:
            return int(a.items[0][0]) if a.items_type == "int" else a.items[0][0]
        elif a.size == [2, 2]:
            main = a.items[0][0] * a.items[1][1]
            side = a.items[1][0] * a.items[0][1]
            result = main - side
            return int(result) if a.items_type == "int" else result
        else:
            row_to_remove = 0
            determinant = 0
            for column in range(0, a.column_count):
                m = a.items[row_to_remove][column]
                sign = (-1) ** (row_to_remove + column)
                cofactor = sign * self.determinant(self.minor(a, row_to_remove, column))
                determinant += m * cofactor
            return int(determinant) if a.items_type == "int" else determinant

    def add_matrices(self):
        a = self.create_matrix('first ')
        b = self.create_matrix('second ')

        if self.can_sum(a, b):
            summed = self.sum(a, b)
            summed.print()
        else:
            print("The operation cannot be performed.")

    def multiply_by_constant(self):
        a = self.create_matrix('')
        number = self.read_number()
        if number:
            multiplied = self.multiply_constant(a, number)
            multiplied.print()

    def multiply_matrices(self):
        a = self.create_matrix('first ')
        b = self.create_matrix('second ')

        if self.can_multiply(a, b):
            multiplied = self.multiply(a, b)
            multiplied.print()
        else:
            print("The operation cannot be performed.")

    def calculate_determinant(self):
        a = self.create_matrix2()

        if self.can_calculate_determinant(a):
            determinant = self.determinant(a)
            print('The result is:')
            print(determinant)
            print()
        else:
            print("The operation cannot be performed.")

    def run_transpose(self):
        selection = self.transpose_menu()
        matrix = self.create_matrix2('float')
        if selection == '1':
            transpose = self.transpose_diagonal(matrix)
            transpose.print()
        elif selection == '2':
            transpose = self.transpose_side_diagonal(matrix)
            transpose.print()
        elif selection == '3':
            transpose = self.transpose_vertical(matrix)
            transpose.print()
        elif selection == '4':
            transpose = self.transpose_horizontal(matrix)
            transpose.print()

    def run(self):
        while True:
            selection = self.print_menu()

            if selection == '0':
                break
            elif selection == '1':
                self.add_matrices()
            elif selection == '2':
                self.multiply_by_constant()
            elif selection == '3':
                self.multiply_matrices()
            elif selection == '4':
                self.run_transpose()
            elif selection == '5':
                self.calculate_determinant()


proc = MatrixProcessor()
proc.run()
