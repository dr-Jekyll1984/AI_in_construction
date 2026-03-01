import doctest

class Furniture:
    """Класс для описания мебели."""

    def __init__(self, material: str, weight_kg: float, color: str):
        """
        Инициализирует объект мебели.

        Args:
            material: Материал изготовления
            weight_kg: Вес в килограммах (должен быть положительным)
            color: Цвет мебели

        Raises:
            ValueError: Если вес не положительный или материал пустой
        """
        if not material or not material.strip():
            raise ValueError("Материал не может быть пустым")
        if weight_kg <= 0:
            raise ValueError("Вес должен быть положительным числом")

        self.material = material.strip()
        self.weight_kg = weight_kg
        self.color = color

    def get_volume(self) -> float:
        """
        Рассчитывает объем мебели.

        Returns:
            Объем в кубических метрах
        """
        pass

    def can_hold_weight(self, weight_to_hold: float) -> bool:
        """
        Проверяет, может ли мебель выдержать определенный вес.

        Args:
            weight_to_hold: Вес для проверки в кг

        Returns:
            True если может выдержать, иначе False
        """
        pass

    def change_color(self, new_color: str) -> None:
        """
        Изменяет цвет мебели.

        Args:
            new_color: Новый цвет
        """
        pass


class Plant:
    """Абстрактный класс для описания растений."""

    def __init__(self, species: str, height_meters: float, age_years: int):
        """
        Инициализирует объект растения.

        Args:
            species: Вид растения
            height_meters: Высота в метрах (0.01-150)
            age_years: Возраст в годах (0-5000)

        Raises:
            ValueError: Если параметры вне допустимых диапазонов
        """
        if not species or not species.strip():
            raise ValueError("Вид растения не может быть пустым")
        if height_meters < 0.01 or height_meters > 150:
            raise ValueError("Высота должна быть в диапазоне 0.01-150 метров")
        if age_years < 0 or age_years > 5000:
            raise ValueError("Возраст должен быть в диапазоне 0-5000 лет")

        self.species = species.strip()
        self.height_meters = height_meters
        self.age_years = age_years

    def grow(self, years: int) -> float:
        """
        Симулирует рост растения за определенное количество лет.

        Args:
            years: Количество лет для роста (должно быть положительным)

        Returns:
            Новая высота растения в метрах

        Raises:
            ValueError: Если years не положительное число
        """
        pass

    def get_annual_growth(self) -> float:
        """
        Рассчитывает среднегодовой прирост растения.

        Returns:
            Среднегодовой прирост в метрах
        """
        pass

    def is_deciduous(self) -> bool:
        """
        Проверяет, является ли растение листопадным.

        Returns:
            True если листопадное, False если вечнозеленое
        """
        pass


class CelestialBody:
    """Абстрактный класс для описания небесных тел."""

    def __init__(self, name: str, mass_kg: float, diameter_km: float):
        """
        Инициализирует объект небесного тела.

        Args:
            name: Название небесного тела
            mass_kg: Масса в килограммах (должна быть положительной)
            diameter_km: Диаметр в километрах (должен быть положительным)

        Raises:
            ValueError: Если масса или диаметр не положительные
        """
        if not name or not name.strip():
            raise ValueError("Название не может быть пустым")
        if mass_kg <= 0:
            raise ValueError("Масса должна быть положительным числом")
        if diameter_km <= 0:
            raise ValueError("Диаметр должен быть положительным числом")

        self.name = name.strip()
        self.mass_kg = mass_kg
        self.diameter_km = diameter_km

    def calculate_gravity(self, distance_from_surface_km: float = 0) -> float:
        """
        Рассчитывает силу притяжения на поверхности или на расстоянии.

        Args:
            distance_from_surface_km: Расстояние от поверхности в км

        Returns:
            Ускорение свободного падения в м/с²

        Raises:
            ValueError: Если расстояние отрицательное
        """
        pass

    def get_volume(self) -> float:
        """
        Рассчитывает объем небесного тела.

        Returns:
            Объем в кубических километрах
        """
        pass

    def compare_size(self, other_body: 'CelestialBody') -> str:
        """
        Сравнивает размер текущего небесного тела с другим.

        Args:
            other_body: Другое небесное тело для сравнения

        Returns:
            Строка с результатом сравнения
        """
        pass


# Конкретные реализации для тестирования
class ConcreteTable(Furniture):
    """Конкретная реализация стола.

    Примеры:
    >>> table = ConcreteTable("Дуб", 25.0, "коричневый")
    >>> table.get_volume()
    0.05
    >>> table.can_hold_weight(70)
    True
    >>> table.can_hold_weight(80)
    False
    >>> table.change_color("белый")
    >>> table.color
    'белый'
    >>> # Проверка исключений
    >>> table.can_hold_weight(-10)
    Traceback (most recent call last):
    ...
    ValueError: Вес не может быть отрицательным
    >>> ConcreteTable("", 10, "red")
    Traceback (most recent call last):
    ...
    ValueError: Материал не может быть пустым
    """

    def get_volume(self) -> float:
        return self.weight_kg / 500  # Упрощенный расчет

    def can_hold_weight(self, weight_to_hold: float) -> bool:
        if weight_to_hold < 0:
            raise ValueError("Вес не может быть отрицательным")
        return weight_to_hold <= self.weight_kg * 3

    def change_color(self, new_color: str) -> None:
        if not new_color or not new_color.strip():
            raise ValueError("Цвет не может быть пустым")
        self.color = new_color.strip()


class ConcreteTree(Plant):
    """Конкретная реализация дерева.

    Примеры:
    >>> tree = ConcreteTree("Oak", 5.0, 10)
    >>> tree.grow(5)
    7.5
    >>> tree.get_annual_growth()
    0.5
    >>> tree.is_deciduous()
    True
    >>> tree = ConcreteTree("Pine", 3.0, 5)
    >>> tree.is_deciduous()
    False
    >>> tree.grow(-1)
    Traceback (most recent call last):
    ...
    ValueError: Количество лет должно быть положительным
    >>> ConcreteTree("", 1, 1)
    Traceback (most recent call last):
    ...
    ValueError: Вид растения не может быть пустым
    """

    def grow(self, years: int) -> float:
        if years <= 0:
            raise ValueError("Количество лет должно быть положительным")
        annual_growth = 0.5 if self.age_years < 50 else 0.1
        self.age_years += years
        self.height_meters += annual_growth * years
        return self.height_meters

    def get_annual_growth(self) -> float:
        if self.age_years == 0:
            return 0
        return self.height_meters / self.age_years

    def is_deciduous(self) -> bool:
        deciduous_species = ["Oak", "Maple", "Birch", "Beech"]
        return self.species in deciduous_species


class ConcretePlanet(CelestialBody):
    """Конкретная реализация планеты.

    Примеры:
    >>> earth = ConcretePlanet("Earth", 5.97e24, 12742)
    >>> round(earth.calculate_gravity(), 2)
    9.8
    >>> round(earth.get_volume(), 2)
    1.08e12
    >>> mars = ConcretePlanet("Mars", 6.39e23, 6779)
    >>> earth.compare_size(mars)
    'Earth больше, чем Mars'
    >>> earth.compare_size(earth)
    'Earth равен по размеру Earth'
    >>> earth.calculate_gravity(-10)
    Traceback (most recent call last):
    ...
    ValueError: Расстояние не может быть отрицательным
    >>> ConcretePlanet("", 1, 1)
    Traceback (most recent call last):
    ...
    ValueError: Название не может быть пустым
    """

    G = 6.67430e-11  # Гравитационная постоянная

    def calculate_gravity(self, distance_from_surface_km: float = 0) -> float:
        if distance_from_surface_km < 0:
            raise ValueError("Расстояние не может быть отрицательным")
        radius_m = (self.diameter_km / 2) * 1000
        distance_m = distance_from_surface_km * 1000
        r = radius_m + distance_m
        return (self.G * self.mass_kg) / (r ** 2)

    def get_volume(self) -> float:
        radius_km = self.diameter_km / 2
        return (4 / 3) * 3.14159 * (radius_km ** 3)

    def compare_size(self, other_body: CelestialBody) -> str:
        if self.diameter_km > other_body.diameter_km:
            return f"{self.name} больше, чем {other_body.name}"
        elif self.diameter_km < other_body.diameter_km:
            return f"{self.name} меньше, чем {other_body.name}"
        else:
            return f"{self.name} равен по размеру {other_body.name}"


if __name__ == "__main__":
    # Запуск doctest
    doctest.testmod(verbose=True)

    # Демонстрация работы (необязательно)
    print("\nДемонстрация работы:\n")
    try:
        table = ConcreteTable("Дуб", 25.0, "коричневый")
        print(f"Стол: материал={table.material}, вес={table.weight_kg}кг, цвет={table.color}")
        print(f"Объем стола: {table.get_volume():.2f} м³")
        print(f"Может выдержать 50кг: {table.can_hold_weight(50)}")
        table.change_color("белый")
        print(f"Новый цвет стола: {table.color}")
    except ValueError as e:
        print(f"Ошибка создания стола: {e}")

    print("\n" + "=" * 50 + "\n")
