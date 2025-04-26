def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact not found."
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Enter user name."
    return wrapper

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return f"Contact '{name}' added."

@input_error
def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return f"Contact '{name}' updated."
    else:
        raise KeyError

@input_error
def show_phone(args, contacts):
    name = args[0]
    return contacts[name]

@input_error
def show_all(contacts):
    if not contacts:
        return 'No contacts found.'
    return '\n'.join(f'{name}: {phone}' for name, phone in contacts.items())

def print_help():
    return (
        "Available commands:\n"
        "  hello                 - Greet the bot\n"
        "  add <name> <phone>    - Add a new contact\n"
        "  change <name> <phone> - Change an existing contact\n"
        "  phone <name>          - Show contact's phone number\n"
        "  all                   - Show all contacts\n"
        "  help                  - Show help\n"
        "  exit / close          - Exit the assistant"
    )

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ").strip()
        if not user_input:
            print('Please enter a command.')
            continue
        
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif not args and command in ["add", "change", "phone"]:
            print("Enter the argument for the command")
            continue
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        elif command == "help":
            print(print_help())
        else:
            print("Invalid command. Type 'help' to see available commands.")

if __name__ == "__main__":
    main()
