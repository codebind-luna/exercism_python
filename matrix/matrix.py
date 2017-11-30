class Matrix(object):
    def __init__(self, matrix_string):
        self.rows    = [map(int, line.split()) for line in matrix_string.split("\n")]

    @property
    def columns(self):
        columns = [[] for _ in self.rows[0]]
        for row in self.rows:
            for idx, item in enumerate(row):
                columns[idx].append(item)
        return columns
