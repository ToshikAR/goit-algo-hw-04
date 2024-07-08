'''
Модуль оброботки контактов
'''
import re

def is_phone_number(phone):
    phone_number = re.sub(r"[^0-9]", "", phone)
    if not re.search(r'\d{10}$', phone_number):
        return False, phone
    else:
        phone = re.search(r'\d{10}$', phone_number)[0]
        return True, phone
    

def add_contact(args: list, contacts: dict) -> str:
    try:
        if len(args) != 2: return f"{len(args)} Requires 2 arguments 'name' and 'phone'"
        name, phone = args
        is_phon, num_phon = is_phone_number(phone)
        if not is_phon:
            return f"Phone number {num_phon} is incorrect. Contact not added"
        if contacts.get(name, False):
            return f"The name '{name}' is in the dictionary"
        
        contacts[name] = num_phon
        return f"Contact added '{name}' phon {contacts[name]}."

    except Exception as e:
        return f"Error: {e}"


def change_contact(args: list, contacts: dict) -> str:
    try:
        if len(args) != 2: return f"Requires 2 arguments 'name' and 'phone'"
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


def get_contact(args: list, contacts: dict) -> str:
    try:
        if len(args) != 1: return f"Requires 1 arguments 'name'"
        name = args[0]
        if name not in contacts: return f"Contact '{name}' does not exist"
        return f"'{name}' phon number {contacts[name]}"
    except Exception as e:
        return f"Error: {e}"


def all_contact(contacts: dict) -> str:
    if len(contacts) == 0: return f"Container is empty"
    return [f"{name}: {phone}" for name, phone in contacts.items()]