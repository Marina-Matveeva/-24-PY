import doctest

# TODO Написать 3 класса с документацией и аннотацией типов

class Person:
    def __init__(self, name: str, age: int):
        """
        Создание и подготовка к работе объекта "Человек"

        :param name: Имя человека (никнейм)
        :param age: Возраст человека

        Примеры:
        >>> person = Person("Миша", 15)  # инициализация экземпляра класса
        """
        if not isinstance(name, str):
            raise TypeError("Имя человека должно быть типа str.")
        self.name = name

        if not isinstance(age, int):
            raise TypeError("Возраст (число полных лет) должен быть типа int.")
        if age < 0 or age > 100:
            raise ValueError("Возраст - число неотрицательное и не больше 100.")
        self.age = age

    def say_hello(self) -> None:
        """
        Функция для представления человека (печатает подобное: Привет! Меня зовут name, мне age.)

        Примеры:
        >>> person = Person("Миша", 15)
        >>> person.say_hello()
        """
        ...

    def is_young_people(self) -> bool:
        """
        Функция проверяет, является ли человек молодежью (возраст 14-35 лет)

        :return: Является ли молодежью

        Примеры:
        >>> person = Person("Миша", 15)
        >>> person.is_young_people()
        """
        ...

class Dishwasher:
    def __init__(self, capacity: int, current_plates: int, current_spoons: int):
        """
        Создание и подготовка к работе объекта "Посудомойка"

        :param capacity: Вместимость посудомойки
        :param current_plates: Число загруженных тарелок
        :param current_spoons: Число загруженных ложек

        Примеры:
        >>> dishwasher = Dishwasher(100, 10, 14)
        """
        if not isinstance(capacity, int):
            raise TypeError("Вместимость посудомойки должна быть типа int.")
        if capacity <= 0:
            raise ValueError("Вместимость должна быть положительной.")
        self.capacity = capacity

        if not isinstance(current_plates, int):
            raise TypeError("Число загруженных тарелок должно быть типа int.")
        if current_plates < 0:
            raise ValueError("Число загруженных тарелок должно быть неотрицательным.")
        self.current_plates = 0

        if not isinstance(current_spoons, int):
            raise TypeError("Число загруженных ложек должно быть типа int.")
        if current_spoons < 0:
            raise ValueError("Число загруженных ложек должно быть неотрицательным.")
        self.current_spoons = 0
        self.load_dishwasher(current_plates, current_spoons)

    def load_dishwasher(self, plates: int, spoons: int) -> None:
        """
        Функция добавления предметов в посудомойку

        :param plates: Число загружаемых тарелок
        :param spoons: Число загружаемых ложек

        :raise ValueError: Если количество добавляемых предметов превышает свободное место в посудомойке, то вызываем ошибку

        Примеры:
        >>> dishwasher = Dishwasher(100, 10, 20)
        >>> dishwasher.load_dishwasher(30, 12)
        """
        if self.current_plates + self.current_spoons > self.capacity:
            raise ValueError("Число загружаемых предметов превышает вместимость.")
        self.current_plates += plates
        self.current_spoons += spoons

    def is_empty_dishwasher(self) -> bool:
        """
        Функция, которая проверяет, является ли посудомойка пустой

        :return: Является ли посудомойка пустой

        Примеры:
        >>> dishwasher = Dishwasher(100, 0, 0)
        >>> dishwasher.is_empty_dishwasher()
        """
        ...

    def unload_dishwasher(self, removable_plates: int, removable_spoons: int) -> None:
        """
        Извлечение посуды из посудомойки.

        :param removable_plates: Число извлекаемых тарелок
        :param removable_spoons: Число извлекаемых ложек

        :raise ValueError: Если количество извлекаемых предметов превышает количество их в посудомойке,
        то возвращается ошибка.

        Примеры:
        >>> dishwasher = Dishwasher(100, 10, 20)
        >>> dishwasher.unload_dishwasher(3, 2)
        """
        ...

class Table:
    def __init__(self, table_legs: int, cost: int | float):
        """
        Создание и подготовка к работе объекта "Стол"

        :param table_legs: Число ножек стола
        :param cost: Стоимость стола

        Примеры:
        >>> table = Table(4, 1400.8)
        """
        if not isinstance(table_legs, int):
            raise TypeError("Число ножек должно быть типа int.")
        if table_legs <= 0:
            raise ValueError("Число ножек должно быть больше 0.")
        self.table_legs = table_legs

        if not isinstance(cost, int | float):
            raise TypeError("Стоимость должна быть типа int или float.")
        self.cost = cost

    def buy_the_table(self, my_money: int | float) -> bool:
        """
        Функция проверки, можно ли человеку купить стол

        :param my_money: Бюджет человека

        :raise TypeError: Если тип my_money не int или float, то вызывается ошибка.

        :return: Хватает ли денег на покупку стола

        Примеры:
        >>> table = Table(4, 1400.8)
        >>> table.buy_the_table(204.13)
        """
        ...

    def cost_change(self, size_of_the_change: int | float) -> None:
        """
        Функция изменения стоимости стола

        :param size_of_the_change: Размер изменения

        :raise TypeError: Если тип size_of_the_change не int или float, то вызывается ошибка.
        :raise ValueError: Если стоимость стола стала <= 0, то вызывается ошибка.

        Примеры:
        >>> table = Table(4, 1400.8)
        >>> table.cost_change(204.13)
        >>> table.cost_change(-1300)
        """
        ...

if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()  # тестирование примеров, которые находятся в документации