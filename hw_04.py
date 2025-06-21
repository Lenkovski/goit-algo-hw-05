def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Enter user name."
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Enter command arguments."
    return inner


@input_error
def add_contact(args, contacts):
    name, phone = args.split()
    contacts[name] = phone
    return "Contact added."


@input_error
def change_contact(args, contacts):
    name, phone = args.split()
    if name not in contacts:
        raise KeyError
    contacts[name] = phone
    return "Contact changed."


@input_error
def phone(args, contacts):
    name = args.strip()
    return f"{name}: {contacts[name]}"


@input_error
def show_all(contacts):
    if not contacts:
        return "No contacts found."
    result = ""
    for name, phone in contacts.items():
        result += f"{name}: {phone}\n"
    return result


def main():
    contacts = {}
    commands = {
        "add": add_contact,
        "change": change_contact,
        "phone": phone,
        "all": lambda args, contacts=contacts: show_all(contacts),
        "exit": None,
        "close": None,
        "goodbye": None,
        "hello": lambda args=None, contacts=None: "How can I help you?"
    }

    while True:
        command_line = input("Enter a command: ").strip()
        if not command_line:
            print("Enter command arguments.")
            continue
        command_parts = command_line.split(' ', 1)
        command = command_parts[0].lower()

        if command in ("exit", "close", "goodbye"):
            print("Goodbye!")
            break
        elif command in commands:
            handler = commands[command]
            args = command_parts[1] if len(command_parts) > 1 else ""
            if handler:
                if command == "all":
                    # all command takes no args
                    print(handler(args))
                else:
                    print(handler(args, contacts))
            else:
                print("Command not implemented.")
        else:
            print("Unknown command.")


if __name__ == "__main__":
    main()