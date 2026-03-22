if __name__ == "__main__":

    from typing import Union
    class Vehicle:
        """ Базовый класс для всех транспортных средств.
        Атрибуты:
            make (str): Марка автомобиля.
            model (str): Модель автомобиля.
            year (int): Год выпуска.
            color (str): Цвет кузова.
            _fuel_type (str): Тип топлива (защищённый, доступен в дочерних классах).
            __vin (str): Уникальный идентификатор VIN (приватный, для внутреннего использования)."""

        def __init__(self, make: str, model: str, year: int, color: str,
                     fuel_type: str, vin: str) -> None:
            """ Инициализация базового транспортного средства.
            :param make: Марка
            :param model: Модель
            :param year: Год выпуска
            :param color: Цвет
            :param fuel_type: Тип топлива
            :param vin: VIN-номер"""
            self.make = make
            self.model = model
            self.year = year
            self.color = color
            self._fuel_type = fuel_type  # защищённый атрибут
            self.__vin = vin  # приватный атрибут

        def __str__(self) -> str:
            """Человеко-читаемое представление: марка, модель, год."""
            return f"{self.make} {self.model} ({self.year})"

        def __repr__(self) -> str:
            """Официальное представление для воссоздания объекта."""
            return (f"Vehicle(make='{self.make}', model='{self.model}', "
                    f"year={self.year}, color='{self.color}', "
                    f"fuel_type='{self._fuel_type}', vin='{self.__vin}')")

        def get_info(self) -> str:
            """ Возвращает полную информацию об автомобиле. """
            return (f"{self.make} {self.model}, {self.year} год, цвет {self.color}, "
                    f"топливо: {self._fuel_type}, VIN: {self.__vin}")

        def start_engine(self) -> str:
            """ Запуск двигателя. Базовое поведение. """
            return "Двигатель запущен."

        def calculate_range(self, fuel_volume: float, fuel_efficiency: float) -> float:
            """Рассчитывает возможный пробег на имеющемся топливе
            :param fuel_volume: Объём топлива (л)
            :param fuel_efficiency: Расход топлива (км/л)
            :return: Максимальный пробег (км)"""
            return fuel_volume * fuel_efficiency


    class Car(Vehicle):
        """ Класс легкового автомобиля. Наследует Vehicle. Дополнительный атрибут:
            num_doors (int): Количество дверей."""

        def __init__(self, make: str, model: str, year: int, color: str,
                     fuel_type: str, vin: str, num_doors: int) -> None:
            """ Расширяет конструктор базового класса, добавляя количество дверей. """
            super().__init__(make, model, year, color, fuel_type, vin)
            self.num_doors = num_doors
        def calculate_range(self, fuel_volume: float, fuel_efficiency: float) -> float:

            return super().calculate_range(fuel_volume, fuel_efficiency)

    class Truck(Vehicle):
        """Класс грузового автомобиля. Наследует Vehicle.Дополнительный атрибут:
            capacity (float): Грузоподъёмность (тонн). """

        def __init__(self, make: str, model: str, year: int, color: str,
                     fuel_type: str, vin: str, capacity: float) -> None:
            """Расширяет конструктор базового класса, добавляя грузоподъёмность. """
            super().__init__(make, model, year, color, fuel_type, vin)
            self.capacity = capacity

        def __str__(self) -> str:
            """ Перегруженное строковое представление: добавляет грузоподъёмность. """
            return f"{super().__str__()} (грузоподъёмность {self.capacity} т)"

        def __repr__(self) -> str:
            """ Перегруженное официальное представление с учётом грузоподъёмности."""
            return (f"Truck(make='{self.make}', model='{self.model}', "
                    f"year={self.year}, color='{self.color}', "
                    f"fuel_type='{self._fuel_type}', vin='{self._Vehicle__vin}', "
                    f"capacity={self.capacity})")

        def calculate_range(self, fuel_volume: float, fuel_efficiency: float) -> float:
            """Перегруженный метод расчёта пробега.Причина перегрузки: пробег грузовика зависит от загрузки.
            Здесь добавлен понижающий коэффициент при полной загрузке. """

            if fuel_volume > 0:
                # Упрощённая модель: эффективность падает на 0.2 * (загрузка / макс. грузоподъёмность)
                # Для демонстрации считаем, что если загрузка > 0, то коэффициент = 0.8
                load_factor = 0.8
                effective_efficiency = fuel_efficiency * load_factor
                return fuel_volume * effective_efficiency
            return 0.0


    if __name__ == "__main__":
        # Демонстрация работы классов
        car = Car(make="Toyota", model="Camry", year=2020, color="серебристый",
                  fuel_type="бензин", vin="JTDBE32K123456789", num_doors=4)

        truck = Truck(make="Volvo", model="FH", year=2019, color="синий",
                      fuel_type="дизель", vin="YV2JN22A8VA123456", capacity=20.0)

        print("=== Легковой автомобиль ===")
        print(f"str: {car}")
        print(f"repr: {repr(car)}")
        print(f"get_info: {car.get_info()}")
        print(f"start_engine: {car.start_engine()}")
        print(f"Пробег на 50 л (эфф. 12 км/л): {car.calculate_range(50, 12):.1f} км")
        print(f"Количество дверей: {car.num_doors}")

        print("\n=== Грузовой автомобиль ===")
        print(f"str: {truck}")
        print(f"repr: {repr(truck)}")
        print(f"get_info: {truck.get_info()}")
        print(f"start_engine: {truck.start_engine()}")
        print(f"Пробег на 200 л (эфф. 5 км/л): {truck.calculate_range(200, 5):.1f} км")
        print(f"Грузоподъёмность: {truck.capacity} т")

        # Проверка инкапсуляции
        print("\n=== Инкапсуляция ===")
        # _fuel_type доступен (но защищён)
        print(f"Тип топлива (защищённый): {car._fuel_type}")
        # __vin напрямую не доступен (приватный)
        try:
            print(car.__vin)
        except AttributeError as e:
            print(f"Ошибка доступа к __vin: {e}")
        # Доступ через name mangling возможен, но не рекомендуется
        print(f"VIN через name mangling: {car._Vehicle__vin}")
    pass
