'''
Модуль оброботки контактов
'''
import re
from colorama import Fore, Style

def is_phone_number(phone) -> tuple[bool, str]:
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
            return Fore.RED + f"Phone number '{num_phon}' is incorrect. Contact not added" + Fore.RESET
        if contacts.get(name, False):
            return Fore.RED + f"The name '{name}' is in the dictionary" + Fore.RESET
        
        contacts[name] = num_phon
        return Fore.GREEN + f"Contact added '{name}' phon {contacts[name]}." +  Fore.RESET

    except Exception as e:
        return f"Error: {e}"


def change_contact(args: list, contacts: dict) -> str:
    try:
        if len(args) != 2: return f"Requires 2 arguments 'name' and 'phone'"
        name, phone = args
        if name not in contacts:
            return Fore.RED + "Contact does not exist" + Fore.RESET
        
        is_phon, num_phon = is_phone_number(phone)
        if not is_phon:
            return Fore.RED + f"Phone number {num_phon} is incorrect. Contact not update" + Fore.RESET

        contacts[name] = num_phon
        return Fore.GREEN + f"Contact update '{name}' phon {contacts[name]}." + Fore.RESET

    except Exception as e:
        return f"Error: {e}"


def get_contact(args: list, contacts: dict) -> str:
    try:
        if len(args) != 1: return f"Requires 1 arguments 'name'"
        name = args[0]
        if name not in contacts: return Fore.RED + f"Contact '{name}' does not exist" + Fore.RESET
        return Fore.YELLOW + f"'{name}' phon number {contacts[name]}" + Fore.RESET
    except Exception as e:
        return f"Error: {e}"


def all_contact(contacts: dict) -> str:
    if len(contacts) == 0: return  Fore.RED + f"Container is empty" +  Fore.RESET
    return [f"{name}: {phone}" for name, phone in contacts.items()] 