# У вас є текстовий файл, який містить інформацію про місячні заробітні плати 
# розробників у вашій компанії. Кожен рядок у файлі містить прізвище розробника 
# та його заробітну плату, які розділені комою без пробілів.

# Ваше завдання - розробити функцію total_salary(path), яка аналізує цей файл 
# і повертає загальну та середню суму заробітної плати всіх розробників.
import os

def total_salary(path):
    if not os.path.exists(path): return f"File '{path}' does not exist"
    try:
        with open(path, "r") as file:
            list = []
            while True:
                text = file.readline()
                if not text: break
                list.append(int(text.split(",")[1]))

            total = sum(list)
            average = total//len(list)
            return f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}"

    except Exception as e:
        return f"Error opening: {e}"

print(total_salary(r"Task1\developers.txt"))