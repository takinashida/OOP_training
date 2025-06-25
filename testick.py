# ✅ ЗАДАНИЕ 1: Абстрактный класс + метод
# Создай абстрактный класс Transport, который задаёт обязательные методы:
# start_engine()
# stop_engine()
# info() — возвращает строку с названием транспорта
# Создай два класса-наследника:
# Car (с полями model, fuel)
# Bike (с полями brand, speed)
# 🔹 Обязательно переопредели все @abstractmethod
# 🔹 Попробуй создать Transport() — убедись, что выбрасывается ошибка
#
# ---
#
# ## ✅ ЗАДАНИЕ 2: Миксин
# Создай миксин `LoggerMixin`, который добавляет метод:
# * `log_action(action: str)` — печатает в консоль: `"Лог: {действие}"`
# Добавь этот миксин в `Car`, чтобы при запуске двигателя автоматически логировалось `"Двигатель запущен"`.
#
# ---
#
# ## ✅ ЗАДАНИЕ 3: `__slots__`
# Добавь `__slots__` в класс `Bike`, чтобы он содержал только: `brand`, `speed`, `engine_on`.
# 🔹 Попробуй создать поле `bike.color = "Red"` — убедись, что Python не даст это сделать.
#
# ---
#
# ## ✅ ЗАДАНИЕ 4: Проверка через `isinstance` и `issubclass`
#
# 1. Проверь: является ли `bike` экземпляром `Transport`
# 2. Проверь: является ли `Car` наследником `Transport`
# 3. Убедись, что `LoggerMixin` — это не подтип `Transport`
#
# ---
#
# ## ✅ ЗАДАНИЕ 5: Полиморфизм
#
# Напиши функцию `launch(t: Transport)`, которая:
# * вызывает `start_engine()` и `info()`
# * работает одинаково с `Car`, `Bike` и любым другим `Transport`
#
# ---

from abc import ABC, abstractmethod


class Transport(ABC):
    __slots__ = ()

    @abstractmethod
    def info(self):
        pass

    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass


class LoggerMixin:

    def __init__(self, *args, **kwargs):
        #   super().__init__(*args, **kwargs)
        clas = self.__class__.__name__
        print(f"Объект класса {clas} с аргументами:{args, kwargs}")

    def start_engine(self):
        print("Двигатель запущен")

    def stop_engine(self):
        print("Двигатель остановлен")


class Car(LoggerMixin, Transport):

    __slots__ = ("model", "fuel")

    def __init__(self, model, fuel):
        super().__init__(model, fuel)
        self.model = model
        self.fuel = fuel

    def info(self):
        print(f"Model: {self.model}, Consumed fuel: {self.fuel}")


class Bike(LoggerMixin, Transport):

    __slots__ = ("brand", "speed", "engine_on")

    def __init__(self, brand, speed, engine_on):
        self.brand = brand
        self.speed = speed
        self.engine_on = engine_on

    def info(self):
        print(f"Brand: {self.brand}, Top speed: {self.speed}")


def launch(t: Transport):
    t.info()
    t.start_engine()
    return


# # Пример Car с логированием
# print("▶ Создание автомобиля:")
# mashina = Car("Toyota Camry", "бензин")
# mashina.start_engine()
# mashina.stop_engine()
#
# print("\n▶ Попытка задать неразрешённый атрибут:")
# try:
#     mashina.color = "серый"  # Допустимо, если __slots__ отсутствует в родителе
# except AttributeError as e:
#     print("Ошибка:", e)
#
# # Пример Bike с __slots__
# print("\n▶ Создание велосипеда:")
# bike = Bike("Yamaha", 25, False)
# bike.start_engine()
# bike.stop_engine()
#
# print("\n▶ Попытка задать color у Bike:")
# try:
#     bike.color = "красный"
# except IndentationError as e:
#     print("Ошибка:", e)
#
# # Проверка isinstance / issubclass
# print("\n▶ Проверки isinstance и issubclass:")
# print("bike является Transport?", isinstance(bike, Bike))  # True
# print("Car является подклассом Transport?", issubclass(Car, Bike))  # False
#
# car = Car("Toyota", "бензин")
# bike = Bike("Yamaha", 30, True)
#
# # Универсальный запуск транспорта — полиморфизм!
# launch(car)
# launch(bike)
#
# # Проверка isinstance
# print("✅ car - Transport:", isinstance(car, Car))
# print("✅ bike - Transport:", isinstance(bike, Bike))
#
#
# print(type(car).__name__)

car = Car("Toyota", "бензин")

print(car)
