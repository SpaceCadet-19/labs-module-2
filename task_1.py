class Vehicle:
    """
    Базовый класс для транспортных средств.
    """

    def __init__(self, brand: str, model: str):
        self._brand = brand  # Инкапсулированный атрибут, так как бренд менять не предполагается
        self._model = model  # Инкапсулированный атрибут, так как модель менять не предполагается

    def get_brand(self) -> str:
        return self._brand

    def get_model(self) -> str:
        return self._model

    def start_engine(self) -> str:
        return "Двигатель запущен."

    def __str__(self) -> str:
        return f"{self.get_brand()} {self.get_model()}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(бренд='{self.get_brand()}', модель='{self.get_model()}')"


class Car(Vehicle):
    """
    Дочерний класс для легковых автомобилей.
    """

    def __init__(self, brand: str, model: str, passenger_capacity: int):
        super().__init__(brand, model)
        self.set_passenger_capacity(passenger_capacity)

    def get_passenger_capacity(self) -> int:
        return self._passenger_capacity

    def set_passenger_capacity(self, value: int):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Вместимость пассажиров должна быть положительным целым числом")
        self._passenger_capacity = value

    def start_engine(self) -> str:
        """
        Перегружаем метод, так как у легковых автомобилей может быть дополнительная проверка перед запуском.
        """
        return "Двигатель автомобиля запущен. Пристегните ремни безопасности."

    def __str__(self) -> str:
        return f"{self.get_brand()} {self.get_model()}, вместимость {self.get_passenger_capacity()} человек"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(бренд='{self.get_brand()}', модель='{self.get_model()}', вместимость={self.get_passenger_capacity()})"