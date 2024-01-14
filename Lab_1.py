# TODO Написать 3 класса с документацией и аннотацией типов

class Telephone:
    def __init__(self, model: str, memori_volume: (int, float)):
        if isinstance(model, (str)):
            raise TypeError
        self.model = model
        if isinstance(model, (int, float)):
            raise TypeError
        if memori_volume < 0:
            raise ValueError
        self.memori_volume = memori_volume

    def update(self):
        ...
    def repair(self):
        ...
    def sale(self):
        ...

class Laptop:
    def __init__(self, SSD_memori: (int, float), matrix_type: str):
        if isinstance(SSD_memori, (int, float)):
            raise TypeError
        if SSD_memori < 0:
            raise ValueError
        self.SSD_memori = SSD_memori

        if isinstance(matrix_type, (str)):
            raise TypeError
        self.matrix_type = matrix_type

    def update(self):
        ...
    def repair(self):
        ...
    def sale(self):
        ...


class Table:
    def __init__(self, sise: (int, float), weight: (int, float)):
        if isinstance(sise, (int, float)):
            raise TypeError
        if sise < 0:
            raise ValueError
        self.sise = sise

        if isinstance(weight, (int, float)):
            raise TypeError
        if weight < 0:
            raise ValueError
        self.weight = weight

    def construct(self):
        ...
    def move(self):
        ...
    def set(self):
        ...


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
