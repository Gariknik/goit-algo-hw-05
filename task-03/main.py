import sys
from pathlib import Path
from modules import log_error, show_logs, parse_input


# Основна частина програми
def main():
    # Перевіряємо, чи передано аргумент
    if len(sys.argv) < 2:
        log_error("Помилка: потрібно вказати шлях до директорії!")
        return
    
    # Отримуємо шлях до директорії з аргументів
    file_path = sys.argv[1]
    
    path = Path(file_path)
    
    # Перевірка, чи існує вказаний шлях і чи це директорія
    if not path.exists() or not path.is_file():
        log_error(f"Помилка: вказаний шлях не існує!")
        return
    # Перевірка, чи є 2 необовьязковий аргумент, якщо є передається флаг True до парсера та найменування лога до функції видображання
    if len(sys.argv) == 3:
        data = parse_input(str(path), True)
        #Перевірка, чи коректний 2 необовьязковий аргумент
        if sys.argv[2].upper() not in ['INFO', 'DEBUG', 'ERROR', 'WARNING']:
            log_error("Помилка: такого логу не існує")
            return
        show_logs(data, sys.argv[2].upper())
    else:
        data = parse_input(str(path))
        show_logs(data)




if __name__ == "__main__":
    main()