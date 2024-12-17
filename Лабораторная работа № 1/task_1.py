import doctest


class Human:

    def __init__(self, age: int, weight: (int, float), height: (int, float)):
        """
                Создание и подготовка к работе объекта "Человек"

                :param age: Возраст человека
                :param weight: Вес человека
                :param height: Рост человека

                Примеры:
                >>> human = Human(20, 85, 187.5)

        """
        if not isinstance(age, int):
            raise TypeError('Age must be an integer number!')
        if age < 0:
            raise ValueError('Age must be a positive number!')
        self.age = age

        if weight < 0:
            raise ValueError('Weight must be a positive number!')
        self.weight = weight

        if height < 0:
            raise ValueError('Height must be a positive number!')
        self.height = height

    def human_sex(self, sex: str) -> None:
        """
                Функция определения пола человека.
                :param sex: Пол человека

                :raise TypeError: Если введённое значение не является строкой

                Примеры:
                >>> human = Human(20, 85, 187.5)
                >>> human.human_sex('Male')
        """
        ...

    def more_then_average_height(self, average_male_height=176, average_female_height=165) -> bool:
        """
                Функция проверяет, выше ли человек, относительно среднего значения роста (По умлочанию в России)(Male - 176, Female - 165).
                :param average_male_height:
                :param average_female_height:
                :return: является ли человек выше среднего роста

                >>> human = Human(20, 85, 187.5)
                >>> human.more_then_average_height()

        """
        ...


class School:
    def __init__(self, school_number: int, number_of_graduates: int, number_of_medalists: int):
        """
                Создание и подготовка к работе объекта "Школа"

                :param school_number: Номер школы
                :param number_of_graduates: количесвто выпускников
                :param number_of_medalists: количество медалистов

                Примеры:
                >>> school = School(12, 150, 88)
        """
        if not isinstance(school_number, int):
            raise TypeError('School number must be an integer number!')
        if school_number < 0:
            raise ValueError('School number must be a positive number')
        self.school_number = school_number

        if not isinstance(number_of_graduates, int):
            raise TypeError('The number of graduates must be an integer number!')
        if number_of_graduates < 0:
            raise ValueError('The number of graduates must be a positive number')
        self.number_of_graduates = number_of_graduates

        if not isinstance(number_of_medalists, int):
            raise TypeError('The number of medalists must be an integer number!')
        if number_of_medalists < 0:
            raise ValueError('The number of medalists must be a positive number')
        self.number_of_medalists = number_of_medalists

    def medalists_percentage(self) -> float:
        """
                Функция вычисляет долю медалистов от общего количества учеников
                :return: Процент медалистов.
                :raise ValueError: Если количество выпускников равно 0.

                >>> school_12 = School(12, 200, 45)
                >>> school_12.medalists_percentage()
        """
        ...

    def compare_medalists(self, other_school: str) -> str:
        """
                Функция сравнивает количество медалистов в 2 школах
                :param other_school: - объекст класса School
                :return: сообщение о том, в какой школе больше медалистов


        """


class SignalBase:
    def __init__(self, number_of_military: int, number_of_officers: int, type_of_base: str):
        """
                Создание и подготовка к работе объекта "База_4"

                :param number_of_military: Номер базы
                :param number_of_officers: количество военнослужащих
                :param type_of_base: тип базы

                Примеры:
                >>> base_4 = SignalBase(1000, 312, 'Полк')
        """
        if not isinstance(number_of_military, int):
            raise TypeError('The number of military must be an integer number!')
        if number_of_military < 0:
            raise ValueError('The number of military must be a positive number')
        self.number_of_military = number_of_military

        if not isinstance(number_of_officers, int):
            raise TypeError('The number of officers must be an integer number!')
        if number_of_military < 0:
            raise ValueError('The number of officers must be a positive number')
        self.number_of_officers = number_of_officers

        if not isinstance(type_of_base, str):
            raise TypeError('The type of base must be a string!')
        self.type_of_base = type_of_base

    def officers_percentage(self) -> int:
        """
                Фукнция позволяет узнать процент офицеров на базе
                :return: Процент офицеров.
                :raise ValueError: Если количество офицеров равно 0.

                >>> base_4 = SignalBase(1000, 150, 'Полк')
                >>> base_4.officers_percentage()

        """

    def total_personnel(self) -> int:
        """
                Функция подсчитывает общее количество людей на базе
                :return: Общее количество военных на базе

                >>> base_4 = SignalBase(1000, 150, 'Полк')
                >>> base_4.total_personnel()

        """


if __name__ == "__main__":
    doctest.testmod()
