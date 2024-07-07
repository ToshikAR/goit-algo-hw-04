#У вас є текстовий файл, який містить інформацію про котів. 
# Кожен рядок файлу містить унікальний ідентифікатор кота, 
# його ім'я та вік, розділені комою.

import os

def total_salary(path):
    if not os.path.exists(path): return f"File '{path}' does not exist"
    try:
        with open(path, "r") as file:
            list = []
            while True:
                text = file.readline()
                if not text: break
                id, name, age = text.strip().split(",")
                idict = {'id': id, 'name': name, 'age': age}
                list.append(idict)

            return list

    except Exception as e:
        return f"Error opening: {e}"

print(total_salary(r"Task2\cat.txt"))