# Задача 3.1.
# Создайте класс матрицы (или таблицы).
# Требования к классу:
#   - каждая колонка является числом от 1 до n (n любое число, которые вы поставите!)
#   - в каждой ячейке содержится либо число, либо None
#   - доступы следующие методы матрицы:
#       * принимать новые значения,
#       * заменять существующие значения,
#       * выводить число строк и колонок.

# Пример матрицы 10 на 10 из единиц:
# [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

# Примечание!
#   - новый класс не запрещено строить на базе существующих типов данных: списков, словарей и тд.
#   - отображать в таблице/матрице название колонки не обязательно!
#   - использовать готовые классы numpy.array() и pandas.DataFrame() запрещено!
#   - проявите фантазию :)


class Matrix:
    """
    Создаем матрицу заданного размера.
    Все элементы матрицы равны заданному при инициализации значению
    (по умолчанию все элементы матрицы равны "1")
    """
    def __init__(self, height: int, width: int, val_cell=1):
        self.rows = [[val_cell]*width for _ in range(height)]
        self.height = height
        self.width = width

    def set_value(self, height_index: int, width_index: int, new_val):
        """
        Устанавливаем новое значение элемента матрицы
        """
        try:
            self.rows[height_index][width_index] = new_val
        except IndexError:
            print('Индекс ячейки выходит за границы матрицы!')

    def inspect(self):
        """
        Выводим размер матрицы
        """
        return print(f'Размер матрицы: {self.height} X {self.width}')

    def __str__(self):
        return '\n'.join(map(str, self.rows))


m = Matrix(10, 10, 1)
m.set_value(2, 5, 1000)
m.set_value(20, 5, 1000)
m.inspect()
print(m)
