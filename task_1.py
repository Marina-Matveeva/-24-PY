import doctest


class Animal:
    """
    Базовый класс Животные.
    """
    def __init__(self, species: str, name: str, age: int) -> None:
        """
        Конструктор класса Animal.

        :param species: Вид животного. Непубличный атрибут, так как вид не может меняться (имя и возраст может).
        :param name: Имя животного.
        :param age: Возраст животного.

        Пример:
        >>> animal = Animal("Собака", "Шарик", 3)
        """
        self._species = species
        self.name = name
        self.age = age

    @property
    def species(self) -> str:
        """
        Возвращает вид животного.

        :return: Вид животного.
        """
        return self._species

    @staticmethod
    def basic_skills() -> str:
        """
        Возвращает базовые навыки животного.
        Статический, так как не меняется, принадлежит классу (одинаков для всех животных).

        :return: Строка с базовыми навыками.

        Пример:
        >>> animal = Animal("Собака", "Шарик", 3)
        >>> animal.basic_skills()
        'Могу спать, есть, дышать и размножаться.'
        """
        return "Могу спать, есть, дышать и размножаться."

    def fly(self) -> str:
        """
        Метод возвращает, может ли животное летать.
        По Животному нет информации об умении летать.

        :return: Сообщение о способности летать.

        Пример:
        >>> animal = Animal("Собака", "Шарик", 3)
        >>> animal.fly()
        'Не знаю, могу ли я летать...'
        """
        return "Не знаю, могу ли я летать..."

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта.

        :return: Строка с информацией о животном.

        Пример:
        >>> animal = Animal("Собака", "Шарик", 3)
        >>> print(animal)
        Я Собака. Меня зовут Шарик и мне 3.
        """
        return f"Я {self.species}. Меня зовут {self.name} и мне {self.age}."

    def __repr__(self) -> str:
        """
        Возвращает формальное строковое представление объекта.

        :return: Строка с названием класса и атрибутами.

        Пример:
        >>> animal = Animal("Собака", "Шарик", 3)
        >>> print(repr(animal))
        Animal(species='Собака', name='Шарик', age=3)
        """
        return f"{self.__class__.__name__}(species={self.species!r}, name={self.name!r}, age={self.age!r})"


class Mammal(Animal):
    """
    Класс Млекопитающие (наследуется от класса Животные).
    """
    def __init__(self, species: str, name: str, age: int, coat_color: str) -> None:
        """
        Конструктор класса Mammal.

        :param species: Вид млекопитающего.
        :param name: Имя млекопитающего.
        :param age: Возраст млекопитающего.
        :param coat_color: Цвет щерсти млекопитающего.

        Пример:
        >>> mammal = Mammal("Лев", "Лёвушка", 10, "песочный")
        >>> mammal.basic_skills() #наследуется от класса Animal
        'Могу спать, есть, дышать и размножаться.'
        """
        super().__init__(species, name, age)
        self.coat_color = coat_color

    def fly(self) -> str:
        """
        Метод возвращает, может ли млекопитающее летать.
        Метод переопределен, так как они не летают.

        :return: Сообщение о том, что не умеет летать.

        Пример:
        >>> mammal = Mammal("Лев", "Лёвушка", 10, "песочный")
        >>> mammal.fly()
        'Я Лев и не умею летать.'
        """
        return f"Я {self.species} и не умею летать."

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта.

        :return: Строка с информацией о млекопитающем.

        Пример:
        >>> mammal = Mammal("Лев", "Лёвушка", 10, "песочный")
        >>> print(mammal)
        Я Лев. Меня зовут Лёвушка и мне 10. А, цвет моей шерсти: песочный.
        """
        return f"{super().__str__()} А, цвет моей шерсти: {self.coat_color}."

    def __repr__(self) -> str:
        """
        Возвращает формальное строковое представление объекта.

        :return: Строка с названием класса и атрибутами.

        Пример:
        >>> mammal = Mammal("Лев", "Лёвушка", 10, "песочный")
        >>> print(repr(mammal))
        Mammal(species='Лев', name='Лёвушка', age=10, coat_color='песочный')
        """
        return f"{self.__class__.__name__}(species={self.species!r}, name={self.name!r}, age={self.age!r}, coat_color={self.coat_color!r})"


class Bird(Animal):
    """
    Класс Птицы (наследуется от класса Животные).
    """
    def __init__(self, species: str, name: str, age: int, wingspan: float) -> None:
        """
        Конструктор класса Bird.

        :param species: Вид птицы.
        :param name: Имя птицы.
        :param age: Возраст птицы.
        :param wingspan: Размах крыльев птицы.

        Пример:
        >>> bird = Bird("Орел", "Веня", 5, 1.5)
        >>> bird.basic_skills() #наследуется от класса Animal
        'Могу спать, есть, дышать и размножаться.'
        """
        super().__init__(species, name, age)
        self.wingspan = wingspan

    def fly(self) -> str:
        """
        Метод возвращает, может ли птица летать.
        Метод переопределен, так как птицы летают (в большинстве своем).

        :return: Сообщение о том, что умеет летать.

        Пример:
        >>> bird = Bird("Орел", "Веня", 5, 1.5)
        >>> bird.fly()
        'Я Орел и умею летать!'
        """
        return f"Я {self.species} и умею летать!"

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта.

        :return: Строка с информацией о птице.

        Пример:
        >>> bird = Bird("Орел", "Веня", 5, 1.5)
        >>> print(bird)
        Я Орел. Меня зовут Веня и мне 5. Размах моих крыльев = 1.5м.
        """
        return f"{super().__str__()} Размах моих крыльев = {self.wingspan}м."

    def __repr__(self) -> str:
        """
        Возвращает формальное строковое представление объекта.

        :return: Строка с названием класса и атрибутами.

        Пример:
        >>> bird = Bird("Орел", "Веня", 5, 1.5)
        >>> print(repr(bird))
        Bird(species='Орел', name='Веня', age=5, wingspan=1.5)
        """
        return f"{self.__class__.__name__}(species={self.species!r}, name={self.name!r}, age={self.age!r}, wingspan={self.wingspan!r})"


if __name__ == "__main__":
    doctest.testmod()

    print("Животное:")
    animal = Animal("Кот", "Рыжик", 12)
    print(animal)
    print(animal.basic_skills())
    print(animal.fly())
    print(repr(animal))
    print("\n")

    print("Млекопитающее:")
    mammal = Mammal("Жираф", "Жорик", 15, "песочно-желтый")
    print(mammal)
    print(mammal.basic_skills())
    print(mammal.fly())
    print(repr(mammal))
    print("\n")

    print("Птица:")
    bird = Bird("Воробей", "Петя", 1, 0.02)
    print(bird)
    print(bird.basic_skills())
    print(bird.fly())
    print(repr(bird))