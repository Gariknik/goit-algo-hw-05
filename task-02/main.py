from typing import Callable, Generator
import re
#2
# Необхідно створити функцію generator_numbers, яка буде аналізувати текст, 
# ідентифікувати всі дійсні числа, що вважаються частинами доходів, і повертати їх як генератор. 
# Дійсні числа у тексті записані без помилок, 
# чітко відокремлені пробілами з обох боків. Також потрібно реалізувати функцію sum_profit, 
# яка буде використовувати generator_numbers для підсумовування цих чисел і обчислення загального прибутку.
def generator_numbers(text: str) -> Generator:
    """
    Функція generator_numbers(text: str) повинна приймати рядок як аргумент і повертати генератор, 
    що ітерує по всіх дійсних числах у тексті. 
    Дійсні числа у тексті вважаються записаними без помилок і чітко відокремлені пробілами з обох боків.
    """
    pattern = r'\d+\.\d+' #складаємо паттерн для отримання дійсних чисел з тексту
    iterator = map(float, re.findall(pattern, text))
    yield from iterator

        
def sum_profit(text: str, func: Callable) -> float:
    """
    Функція sum_profit(text: str, func: Callable) має використовувати генератор generator_numbers 
    для обчислення загальної суми чисел у вхідному рядку та приймати його як аргумент при виклику.
    Функція вертає дійсне число суму чисел згенерованих generator_numbers
    """
    return sum(func(text))


text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(total_income)
try:
    assert f"Загальний дохід: {total_income}" == "Загальний дохід: 1351.46", "Test 1. 1351.46"
except AssertionError as e:
    print(f"Не виконан: {e}")