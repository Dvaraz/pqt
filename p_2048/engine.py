import random


# def pretty_mas(mas):
#     print("-" * 10)
#     for row in mas:
#         print(*row)
#     print("-" * 10)
#
#
# def get_number_from_index(i, j):
#     return i*4+j+1
#
#
# def get_index_from_number(num):
#     num -= 1
#     x, y = num // 4, num % 4
#     return x, y
#
#
# def insert_2_or_4(mas, x, y):
#     if random.random() <= 0.75:
#         mas[x][y] = 2
#     else:
#         mas[x][y] = 4
#     return mas
#
#
# def get_empty_list(mas):
#     empty = []
#     for i in range(4):
#         for j in range(4):
#             if mas[i][j] == 0:
#                 num = get_number_from_index(i, j)
#                 empty.append(num)
#
#     return empty
#
#
# def is_zero_in_mas(mas):
#     for row in mas:
#         if 0 in row:
#             return True
#     return False


# def move_left(mas):
#     delta = 0
#     for row in mas:
#         while 0 in row:
#             row.remove(0)
#         while len(row) != 4:
#             row.append(0)
#     for i in range(4):
#         for j in range(3):
#             if mas[i][j] == mas[i][j + 1] and mas[i][j] != 0:
#                 mas[i][j] *= 2
#                 delta += mas[i][j]
#                 mas[i].pop(j + 1)
#                 mas[i].append(0)
#     return mas, delta
#
#
# def move_right(mas):
#     delta = 0
#     for row in mas:
#         while 0 in row:
#             row.remove(0)
#         while len(row) != 4:
#             row.insert(0, 0)
#     for i in range(4):
#         for j in range(3, 0, -1):
#             if mas[i][j] == mas[i][j - 1] and mas[i][j] != 0:
#                 mas[i][j] *= 2
#                 delta += mas[i][j]
#                 mas[i].pop(j - 1)
#                 mas[i].insert(0, 0)
#     return mas, delta
#
#
# def move_up(mas):
#     delta = 0
#     column = []
#     for num, row in enumerate(mas):
#         column.append([row[num] for row in mas])
#     for rows in column:
#         while 0 in rows:
#             rows.remove(0)
#         while len(rows) != 4:
#             rows.append(0)
#     for i in range(4):
#         for j in range(3):
#             if column[i][j] == column[i][j + 1] and column[i][j] != 0:
#                 column[i][j] *= 2
#                 delta += column[i][j]
#                 column[i].pop(j + 1)
#                 column[i].append(0)
#     mas = []
#     for num, row in enumerate(column):
#         mas.append([row[num] for row in column])
#     return mas, delta
#
#
# def move_down(mas):
#     delta = 0
#     column = []
#     for num, row in enumerate(mas):
#         column.append([row[num] for row in mas])
#     for rows in column:
#         while 0 in rows:
#             rows.remove(0)
#         while len(rows) != 4:
#             rows.insert(0, 0)
#     for i in range(4):
#         for j in range(3, 0, -1):
#             if column[i][j] == column[i][j - 1] and column[i][j] != 0:
#                 column[i][j] *= 2
#                 delta += column[i][j]
#                 column[i].pop(j - 1)
#                 column[i].insert(0, 0)
#     mas = []
#     for num, row in enumerate(column):
#         mas.append([row[num] for row in column])
#     return mas, delta

class Move:
    def __init__(self, mas):
        self.mas = mas

    def pretty_mas(self):
        print("-" * 10)
        for row in self.mas:
            print(*row)
        print("-" * 10)

    @staticmethod
    def get_number_from_index(i, j):
        return i * 4 + j + 1

    @staticmethod
    def get_index_from_number(num):
        num -= 1
        x, y = num // 4, num % 4
        return x, y

    def insert_2_or_4(self, x, y):
        if random.random() <= 0.75:
            self.mas[x][y] = 2
        else:
            self.mas[x][y] = 4
        return self.mas

    def get_empty_list(self):
        empty = []
        for i in range(4):
            for j in range(4):
                if self.mas[i][j] == 0:
                    num = self.get_number_from_index(i, j)
                    empty.append(num)

        return empty

    def is_zero_in_mas(self):
        for row in self.mas:
            if 0 in row:
                return True
        return False

    def move_left(self):
        delta = 0
        for row in self.mas:
            while 0 in row:
                row.remove(0)
            while len(row) != 4:
                row.append(0)
        for i in range(4):
            for j in range(3):
                if self.mas[i][j] == self.mas[i][j + 1] and self.mas[i][j] != 0:
                    self.mas[i][j] *= 2
                    delta += self.mas[i][j]
                    self.mas[i].pop(j + 1)
                    self.mas[i].append(0)
        return self.mas, delta

    def move_right(self):
        delta = 0
        for row in self.mas:
            while 0 in row:
                row.remove(0)
            while len(row) != 4:
                row.insert(0, 0)
        for i in range(4):
            for j in range(3, 0, -1):
                if self.mas[i][j] == self.mas[i][j - 1] and self.mas[i][j] != 0:
                    self.mas[i][j] *= 2
                    delta += self.mas[i][j]
                    self.mas[i].pop(j - 1)
                    self.mas[i].insert(0, 0)
        return self.mas, delta

    def move_up(self):
        delta = 0
        column = []
        for num, row in enumerate(self.mas):
            column.append([row[num] for row in self.mas])
        for rows in column:
            while 0 in rows:
                rows.remove(0)
            while len(rows) != 4:
                rows.append(0)
        for i in range(4):
            for j in range(3):
                if column[i][j] == column[i][j + 1] and column[i][j] != 0:
                    column[i][j] *= 2
                    delta += column[i][j]
                    column[i].pop(j + 1)
                    column[i].append(0)
        self.mas = []
        for num, row in enumerate(column):
            self.mas.append([row[num] for row in column])
        return self.mas, delta

    def move_down(self):
        delta = 0
        column = []
        for num, row in enumerate(self.mas):
            column.append([row[num] for row in self.mas])
        for rows in column:
            while 0 in rows:
                rows.remove(0)
            while len(rows) != 4:
                rows.insert(0, 0)
        for i in range(4):
            for j in range(3, 0, -1):
                if column[i][j] == column[i][j - 1] and column[i][j] != 0:
                    column[i][j] *= 2
                    delta += column[i][j]
                    column[i].pop(j - 1)
                    column[i].insert(0, 0)
        self.mas = []
        for num, row in enumerate(column):
            self.mas.append([row[num] for row in column])
        return self.mas, delta


def game_start():
    mas = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
    ]
    grid = Move(mas)
    while True:
        a = grid.get_index_from_number(random.choice(grid.get_empty_list()))
        grid.insert_2_or_4(a[0], a[1])
        grid.pretty_mas()
        input_ = input("please select from a, d, s, w")
        if input_ == "a":
            grid.move_left()
        elif input_ == "d":
            grid.move_right()
        elif input_ == "w":
            grid.move_up()
        elif input_ == "s":
            grid.move_down()




