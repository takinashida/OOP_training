# Приложение для тренировки ООП
Специально для SkyPro
---

---

## Модуль classes.py

1. `class Category`
   Класс, описывающий категории товаров.
   Атрибуты: `name`, `description`, `product_count`, `products`
   Методы:

   * `__str__()` — строковое представление категории
   * `__len__()` — количество продуктов в категории
   * `add_product(product: Product)` — добавляет продукт, если он является экземпляром класса `Product` или его наследников
   * `products` — список всех товаров
   * `str_products` — список товаров в виде оформленных строк

---

2. `class Product`
   Базовый класс товаров.
   Атрибуты: `name`, `description`, `price`, `quantity`
   Методы:

   * `__str__()` — строковое представление товара
   * `__add__()` — позволяет складывать два объекта одного и того же класса (возвращает общую стоимость)
   * `total_value()` — возвращает общую стоимость (цена × количество)
   * `price` — property-доступ к цене, с валидацией при изменении
   * `new_product(product_dict: dict, products: list)` — добавляет товар или обновляет существующий

---

3. `class Iteration`
   Класс-итератор для обхода товаров внутри категории.
   Используется для поддержки `for _ in category`.
   Реализует методы `__iter__()` и `__next__()`

---

4. `class Smartphone(Product)`
   Наследник `Product`, представляющий смартфон.
   Дополнительные атрибуты: `efficiency`, `model`, `memory`, `color`

---

5. `class LawnGrass(Product)`
   Наследник `Product`, представляющий газонную траву.
   Дополнительные атрибуты: `country`, `germination_period`, `color`

---

---

---

## Модуль utils.py

1. ```json_load(path_to_data: str) -> list```
    
    Открывает json файлы

    path_to_data: путь до файла

    return: список словарей
---
2. ```get_classes(categ_list: list, Product: classmethod=Product, Category: classmethod=Category) -> tuple```
    
    Распределяет данные из списка словарей по классам

    categ_list: Список словарей

    Product: Класс Product

    Category: Класс Category

    return: Кортеж из списков объектов класса
---

---

## Модуль main.py
Здесь находится финальная сборка всех функций для окончательной работы приложения

# Весь код был протестирован при помощи pytest