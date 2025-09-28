import re

def parse_input(path: str, flag: bool=False)->tuple[dict[str: int],dict[str: list[str]]]:
    """Parsering filed. Return data dict"""
    
    types_logs_count = {'INFO': 0, 'DEBUG': 0, 'ERROR': 0, 'WARNING': 0} #словник для підрахунку логів
    types_logs_messages = {'INFO': [], 'DEBUG': [], 'ERROR': [], 'WARNING': []} #словник для сповіщень
    pattern = r'(?!\s)[A-Z]{2,}(?<!\s)' #паттерн для пошуку логу
    
    
    with open(path, 'r', encoding='utf-8') as file:

        for row in file.readlines():
            row = row.strip()
            log = re.search(pattern, row)[0]  
            types_logs_count[log] += 1
            if flag: # якщо флаг True, виконується форматування рядків сповіщень і додавання іх в лист до відповідного логу
                message = re.sub(pattern, '-', row)
                types_logs_messages[log].append(message)
    return types_logs_count, types_logs_messages