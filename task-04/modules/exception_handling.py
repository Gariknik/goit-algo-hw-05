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
        match func.__name__:
            case 'add_contact':
                try:
                    return func(*args, **kwargs)
                except ValueError:
                    return 'Contact added failed. Please enter contact name and phone number. Format command [username] [phone]'
                except KeyError:
                    return 'Failed added contact. To replace the contact, use change [username] [phone] or enter another name'
            case 'change_contact':
                try:
                    return func(*args, **kwargs)
                except ValueError:
                    return 'Contact changed failed. Please enter contact name and phone number. Format command [username] [phone]'
                except KeyError:
                    return 'There is no such contact in your contacts.'
             
            case 'show_phone':
                try:
                    return func(*args, **kwargs)
                except KeyError:
                    return 'There is no such contact in your contacts.' 
                except IndexError:
                    return 'Please enter contact name. Format command [username]'                
            case 'show_all_contact':
                return func(*args, **kwargs)
            case _:
                return "Sorry, I don't process that function."
    return inner