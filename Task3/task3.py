#  - не обов'язкове
# Розробіть скрипт, який приймає шлях до директорії в якості аргументу 
# командного рядка і візуалізує структуру цієї директорії, виводячи імена 
# всіх піддиректорій та файлів. Для кращого візуального сприйняття, 
# імена директорій та файлів мають відрізнятися за кольором.

import sys
from pathlib import Path
from colorama import Fore, Style

def print_dir_content(current_dir = Path('.'), shift = 0):
    path = Path(current_dir)

    if not path.exists() or not path.is_dir():
        print(Fore.RED + f"Error: {current_dir} the path is incorrect" + Style.RESET_ALL)
        return

    if shift == 0:
        print(" " * shift + Fore.BLUE + f"{path.name}")

    for ipath in path.iterdir():
        if ipath.is_dir():
            print(' ' * shift + '|-' + Fore.YELLOW + f'{ipath.name}' + Fore.BLUE)
            print_dir_content(ipath, shift + 2)
            continue
        elif ipath.is_file():
            print(' ' * shift + f'|-' + Fore.GREEN + f'{ipath.name}' + Fore.BLUE)
    
    if shift == 0:
         print(' ' + Style.RESET_ALL)



if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(Fore.RED + "The path to the directory must be specified." + Style.RESET_ALL)
        sys.exit(1)

    directory_path = sys.argv[1]
    print_dir_content(directory_path)


    # "d:\\!Tosh\\!GoIT\\GoITPython\\PythonCore2\\PythonLessons\\goit-algo-hw-04\\Task3\\picture\\



