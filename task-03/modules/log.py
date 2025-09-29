from colorama import Fore, init
# Ініціалізуємо colorama
init(autoreset=True)

colors = [Fore.BLUE, Fore.GREEN, Fore.RED, Fore.YELLOW]

# def show_logs(data: tuple[dict[str: int],dict[str: list[str]]], log: str='') -> None:     
#     print("Рівень логування | Кількість")
#     print("-----------------|----------")
#     for color, row in zip(colors, data[0].items()): 
#         print(f"{color}{row[0]:<17}", end='')
#         print(f"| {row[1]:<9}")
#     if log:
#         print(f"Деталі логів для рівня '{log}':")
#         for message in data[1][log]:
#             print(message)


def log_error(message):
    print(f"{Fore.RED} {message}")
    
def load_logs(file_path: str) -> list:
    """Loading file logs. Return list lines"""
    with open(file_path, 'r', encoding='utf-8') as file:
        return [row.strip() for row in file.readlines()]

def filter_logs_by_level(logs: list, level: str) -> list:
    """Filter logs by level"""
    level = level.upper()
    return list(map(lambda y: y[level], filter(lambda x: list(x.keys())[0] == level, logs)))

def count_logs_by_level(logs: list) -> dict:
    """Get count logs dict"""
    types_logs_count = {'INFO': 0, 'DEBUG': 0, 'ERROR': 0, 'WARNING': 0} #словник для підрахунку логів
    for log in logs:
        key = list(log.keys())[0]
        types_logs_count[key] += 1
    return types_logs_count

def display_log_counts(counts: dict):
    """Show logs counts"""
    print("Рівень логування | Кількість")
    print("-----------------|----------")
    for color, row in zip(colors, counts.items()): 
        print(f"{color}{row[0]:<17}", end='')
        print(f"| {row[1]:<9}")