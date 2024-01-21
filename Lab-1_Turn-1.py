# TODO Написать 3 класса с документацией и аннотацией типов

class Telephone:
    """
    Документация на класс.
    Класс описывает модель телефона.
    Класс имеет атрибуты: version - версия телефона
                            memori_volume - объем памяти телефона
    """
    def __init__(self, version: int, memori_volume: (int, float)):
        """Инициализация экземпляра класса. """
        if isinstance(version, (int)): #Проверяем, чтобы версия была типа int
            raise TypeError("Версия должна быть типа int") #Вызываем ошибку

        if version < 0: #Проверяем, чтобы версия не была отрицательной
            raise ValueError("Версия не была отрицательной") #Вызываем ошибку
        #И только после всех проверок определяем экземпляр
        self.version = version

        if isinstance(memori_volume, (int, float)): #Проверяем, чтобы объем памяти был типа int или float
            raise TypeError("Объем памяти должен быть типа int") #Вызываем ошибку

        if memori_volume < 0: #Проверяем, чтобы объем памяти не был отрицательным
            raise ValueError("Объем памяти должен быть не отрицательным") #Вызываем ошибку
        self.memori_volume = memori_volume

    def update(self):
        """
        Метод обновляет модель.
        """
        ...
    def repair(self):
        """
        Метод чинит телефон.
        """
        ...
    def switch_on(self):
        """
        Метод включает телефон.
        """
        ...

class Laptop:
    """
    Документация на класс.
    Класс описывает модель ноутбука.
    Класс имеет атрибуты: SSD_memori - объем SSD памяти телефона
                            matrix_type - тип матрицы ноутбука
    """
    def __init__(self, SSD_memori: (int, float), matrix_type: str):
        """Инициализация экземпляра класса. """
        if isinstance(SSD_memori, (int, float)): #Проверяем, чтобы объем SSD памяти был типа int или float
            raise TypeError("Объем SSD памяти должен быть типа int или float") #Вызываем ошибку

        if SSD_memori < 0: #Проверяем, чтобы объем SSD памяти не был отрицательным
            raise ValueError("Объем SSD памяти должен быть не отрицательным") #Вызываем ошибку
        self.SSD_memori = SSD_memori

        if isinstance(matrix_type, (str)):#Проверяем, чтобы тип матрицы был типа str
            raise TypeError("Тип матрицы должен быть типа str") #Вызываем ошибку
        self.matrix_type = matrix_type

    def update(self):
        """
        Метод обновляет ноутбук.
        """
        ...

    def repair(self):
        """
        Метод чинит ноутбук.
        """
        ...

    def switch_on(self):
        """
        Метод включает ноутбук.
        """
        ...


class Table:
    """
    Документация на класс.
    Класс описывает тип стола.
    Класс имеет атрибуты: size - размеры стола
                            weight - вес стола
    """
    def __init__(self, size: (int, float), weight: (int, float)):
        """Инициализация экземпляра класса. """
        if isinstance(size, (int, float)): #Проверяем, чтобы размер стола был типа int или float
            raise TypeError("Размер стола должен быть типа int или float") #Вызываем ошибку

        if size < 0: #Проверяем, чтобы размер стола был не отрицательным
            raise ValueError("Размер стола должен быть не отрицательным") #Вызываем ошибку
        self.size = size

        if isinstance(weight, (int, float)):#Проверяем, чтобы вес стола был типа int или float
            raise TypeError("Размер стола должен быть типа int или float") #Вызываем ошибку

        if weight < 0: #Проверяем, чтобы размер стола был не отрицательным
            raise ValueError("Размер стола должен быть не отрицательным") #Вызываем ошибку
        self.weight = weight

    def break_(self):
        """
        Метод ломает стол.
        """
        ...

    def move(self):
        """
        Метод передвигает стол.
        """
        ...

    def set(self):
        """
        Метод собирает стол.
        """
        ...


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
