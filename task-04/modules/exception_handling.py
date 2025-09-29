from functools import wraps
from typing import Callable
# Всі помилки введення користувача повинні оброблятися за допомогою декоратора input_error. 
# Цей декоратор відповідає за повернення користувачеві повідомлень типу "Enter user name", "Give me name and phone please" тощо.
# Декоратор input_error повинен обробляти винятки, що виникають у функціях — handler — і це винятки KeyError, ValueError, IndexError. 
# Коли відбувається виняток декоратор повинен повертати відповідь користувачеві. 
# Виконання програми при цьому не припиняється.

def input_error(func: Callable)-> str | list[str]:
    @wraps(func)
    def inner(*args, **kwargs) -> str | list[str]:
        try:
            return func(*args, **kwargs)
        except ValueError:
            return 'Please enter contact name and phone number. Format command [username] [phone]'
        except KeyError:
            return 'Failed operations. There is no such contact in your contacts.'
        except IndexError:
            return 'Please enter contact name. Format command [username]' 

    return inner