class NumericMatrix:
    def __init__(self, name, size):
        self.name = name
        self.size = [int(s) for s in size]
        self.row_count = self.size[0]
        self.column_count = self.size[1]
        self.items = [[0 for i in range(self.column_count)]
                      for j in range(self.row_count)]

    def print(self):
        for row in range(0, self.row_count):
            print(' '.join(str(r) for r in self.items[row]))

    def read_items(self):
        for row in range(0, self.row_count):
            text = input().split(' ')
            for column in range(0, self.column_count):
                self.items[row][column] = int(text[column])

    def set_items(self, items):
        self.items = items


class MatrixProcessor:
    @staticmethod
    def create_matrix(name):
        size = input().split(' ')
        matrix = NumericMatrix(name, size)
        matrix.read_items()
        return matrix

    @staticmethod
    def can_sum(a: NumericMatrix, b: NumericMatrix):
        return a.size == b.size

    @staticmethod
    def sum(a: NumericMatrix, b: NumericMatrix) -> NumericMatrix:
        result = NumericMatrix("C", a.size)
        for row in range(0, a.row_count):
            for column in range(0, a.column_count):
                result.items[row][column] = a.items[row][column] + b.items[row][column]

        return result

    @staticmethod
    def mutiply(a: NumericMatrix, number: int) -> NumericMatrix:
        result = NumericMatrix("C", a.size)
        for row in range(0, a.row_count):
            for column in range(0, a.column_count):
                result.items[row][column] = number * a.items[row][column]

        return result

    @staticmethod
    def read_number():
        return int(input())

    def start_stage_1(self):
        a = self.create_matrix("A")
        b = self.create_matrix("B")

        if self.can_sum(a, b):
            summed = self.sum(a, b)
            summed.print()
        else:
            print("ERROR")

    def start_stage_2(self):
        a = self.create_matrix("A")
        number = self.read_number()
        multiplied = self.mutiply(a, number)
        multiplied.print()


proc = MatrixProcessor()
proc.start_stage_2()
