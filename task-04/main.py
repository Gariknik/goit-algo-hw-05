from modules import add_contact, change_contact, show_phone, parse_input, show_all_contact

def main():
    """
    Програма повинна мати функцію main(), яка управляє основним циклом обробки команд.
    
    Реалізуйте функцію parse_input(), яка розбиратиме введений користувачем рядок на команду та її аргументи. 
    Команди та аргументи мають бути розпізнані незалежно від регістру введення.
    
    Ваша програма повинна очікувати на введення команд користувачем та обробляти їх за допомогою відповідних функцій. 
    В разі введення команди "exit" або "close", програма повинна завершувати виконання.
    
    Напишіть функції-обробники для різних команд, наприклад add_contact(), change_contact(), show_phone() тощо.
    
    Використовуйте словник Python для зберігання імен і номерів телефонів. Ім'я буде ключем, а номер телефону – значенням.
    Ваша програма має вміти ідентифікувати та повідомляти про неправильно введені команди.

    """
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)
        
        match command:
            case "close" | "exit":
                print("Good bye!")
                break
            case "hello": print("How can I help you?")
            case "add": print(add_contact(args, contacts))
            case "change": print(change_contact(args, contacts))
            case "phone": print(show_phone(args, contacts))
            case "all": print(*show_all_contact(contacts), sep='\n')
            case _: print("Invalid command.")


if __name__ == "__main__":
    main()