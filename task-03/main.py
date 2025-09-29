import sys
from pathlib import Path
from modules import load_logs, log_error, filter_logs_by_level, count_logs_by_level, display_log_counts, parse_log_line


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
    
    #завантаження логів з файла
    logs = load_logs(str(path))
    #парсім кожний рядок для отримання логів
    log_levels = [parse_log_line(log) for log in logs]
    #пфдраховуємо логи за рівнями
    counts = count_logs_by_level(log_levels)
    #відображення логів
    display_log_counts(counts)
    
    # Перевірка, чи є 2 необовьязковий аргумент, якщо є передається флаг True до парсера та найменування лога до функції видображання
    if len(sys.argv) == 3:
        #Перевірка, чи коректний 2 необовьязковий аргумент
        level = sys.argv[2].upper()
        if level not in ['INFO', 'DEBUG', 'ERROR', 'WARNING']:
            log_error("Помилка: такого логу не існує")
            return
        data = filter_logs_by_level(log_levels, level)
        print(*data, sep='\n')


if __name__ == "__main__":
    main()