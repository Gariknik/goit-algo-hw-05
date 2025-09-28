from colorama import Fore, init
# Ініціалізуємо colorama
init(autoreset=True)

colors = [Fore.BLUE, Fore.GREEN, Fore.RED, Fore.YELLOW]

def show_logs(data: tuple[dict[str: int],dict[str: list[str]]], log: str='') -> None:     
    print("Рівень логування | Кількість")
    print("-----------------|----------")
    for color, row in zip(colors, data[0].items()): 
        print(f"{color}{row[0]:<17}", end='')
        print(f"| {row[1]:<9}")
    if log:
        print(f"Деталі логів для рівня '{log}':")
        for message in data[1][log]:
            print(message)


def log_error(message):
    print(f"{Fore.RED} {message}")