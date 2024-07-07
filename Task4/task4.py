# Напишіть консольного бота помічника, який розпізнаватиме команди, 
# що вводяться з клавіатури, та буде відповідати відповідно до введеної команди.

import re

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def is_phone_number(phone):
    phone_number = re.sub(r"[^0-9]", "", phone)
    if not re.search(r'\d{10}$', phone_number):
        return False, phone
    else:
        phone = re.search(r'\d{10}$', phone_number)[0]
        return True, phone
    
def add_contact(args, contacts) -> str:
    try:
        if len(args) != 2: return f"{len(args)} Requires 2 arguments 'name' and 'phone {args}'"
        name, phone = args
        is_phon, num_phon = is_phone_number(phone)
        if not is_phon:
            return f"Phone number {num_phon} is incorrect. Contact not added"
        if contacts.get(name, False):
            return f"There is such a name in the dictionary"
        
        contacts[name] = num_phon
        return f"Contact added '{name}' phon {contacts[name]}."

    except Exception as e:
        return f"Error: {e}"

def change_contact(args, contacts) -> str:
    try:
        if len(args) != 2: return f"Requires 2 arguments 'name' and 'phone {args}'"
        name, phone = args
        if name not in contacts:
            return "Contact does not exist"
        
        is_phon, num_phon = is_phone_number(phone)
        if not is_phon:
            return f"Phone number {num_phon} is incorrect. Contact not added"

        contacts[name] = num_phon
        return f"Contact update '{name}' phon {contacts[name]}."

    except Exception as e:
        return f"Error: {e}"
    
def phone_contact():
    pass

def main():
    print("Welcome to the assistant bot!")
    contacts = {}

    while True:
        user_input  = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(phone_contact(args, contacts))



            
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()