'''
Напишіть консольного бота помічника, який розпізнаватиме команди, 
що вводяться з клавіатури, та буде відповідати відповідно до введеної команди.

'''
from Task3.fun_contact import add_contact, change_contact, get_contact, all_contact


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


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
            print(get_contact(args, contacts))
        elif command == "all":
            print( all_contact(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()