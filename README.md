# Приложение для тренировки ООП
Специально для SkyPro
---

---

## Модуль classes.py
Здесь находятся все классы проекта

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