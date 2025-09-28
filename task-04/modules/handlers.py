from .exception_handling import input_error


@input_error
def add_contact(args: list[str], contacts: dict[str]) -> str:
    """
    функція-хендлер, яка викликається за "add". Функція перевіряє наявність контакта в словнику.  
    Якщо контакт є у словнику запитає чи хоче користувач замінити існуючий контакт.
    Якщо так викликає change_contact. Якщо ні завершує своє виконання
    Функція вертає строку повідомлення.
    В якості параметрів передаються: список з імьям та словник.
    """    
    name, phone = args
    if name in contacts: raise KeyError
    contacts[name] = phone
    return "Contact added."


@input_error
def change_contact(args: list[str], contacts: dict[str]) -> str:
    """
    функція-хендлер, яка викликається за "change". Функція заміняє контакт, якщо він є у словнику та вертає строку повідомлення 
    В якості параметрів передаються: список з імьям та словник.
    """
    name, phone = args
    contacts[name] = phone
    return "Changed contacts."
    

@input_error
def show_phone(args: list[str], contacts: dict[str]) -> str:
    """
    функція-хендлер, яка викликається за "phone username" та вертає номер телефону для зазначеного контакту username
    В якості параметрів передаються: список з імьям та словник.
    """
    name = args[0]
    return contacts[name]


    
@input_error    
def show_all_contact(contacts: dict[str]) -> list[str]:
    """
    функція-хендлер, яка викликається за "all" та вертає список усіх контактів
    В якості параметрів передаються: словник.
    """
    return [f'{name} - {phone}' for name, phone in contacts.items()]