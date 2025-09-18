#1 
# Реалізуйте функцію caching_fibonacci, 
# яка створює та використовує кеш для зберігання і повторного використання вже обчислених значень чисел Фібоначчі.
from typing import Callable


def caching_fibonacci() -> Callable:
    """
    Функція caching_fibonacci() повертає внутрішню функцію fibonacci(n).
    """
    cache = {} # словник в якості кешу
    def fibonacci(n: int) -> int:
        """
        fibonacci(n) обчислює n-те число Фібоначчі. Якщо число вже знаходиться у кеші, функція має повертати значення з кешу.
        Якщо число не знаходиться у кеші, функція має обчислити його, зберегти у кеш та повернути результат.
        Використання рекурсії для обчислення чисел Фібоначчі.
        """
        #гранічні умови для рекурсивної функції
        if n == 0: return 0 
        if n == 1: return 1 
        if n in cache: return cache[n]
        #рекурсивне виконання 
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]
    return fibonacci


# Отримуємо функцію fibonacci
fib = caching_fibonacci()

# Використовуємо функцію fibonacci для обчислення чисел Фібоначчі. Тестові дані
try:
    assert fib(2) == 1, "Test 1: 1"
    assert fib(5) == 5, "Test 2: 5"
    assert fib(10) == 55, "Test 3: 55"
    assert fib(135) == 7308805952221443105020355490, "Test 4: 7308805952221443105020355490"
    assert fib(0) == 0, "Test 5: 0"
except AssertionError as e:
    print(e)

