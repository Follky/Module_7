class Birthday(Field):
    def __init__(self, value):
        try:
            # Перевіряємо коректність формату дати та перетворюємо рядок на об'єкт datetime
            self.value = datetime.strptime(value, '%d.%m.%Y')
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_birthday(self, birthday):
        # Додаємо день народження до контакту
        self.birthday = Birthday(birthday)

@input_error
def add_birthday(args, book):
    # Перевіряємо правильність введення аргументів
    if len(args) != 2:
        return "Invalid command format. Please provide name and birthday in format DD.MM.YYYY"
    
    name, birthday = args
    # Шукаємо контакт у книзі за іменем
    contact = book.get_contact(name)
    if contact:
        # Додаємо день народження до знайденого контакту
        contact.add_birthday(birthday)
        return f"Birthday added for {name}"
    else:
        return f"Contact with name '{name}' not found"


@input_error
def show_birthday(args, book):
    # Перевіряємо правильність введення аргументів
    if len(args) != 1:
        return "Invalid command format. Please provide name"
    
    name = args[0]
    # Шукаємо контакт у книзі за іменем
    contact = book.find(name)
    if contact and contact.birthday:
        return f"Birthday of {name}: {contact.birthday.value.strftime('%d.%m.%Y')}"
    elif contact:
        return f"{name} does not have a birthday set"
    else:
        return f"Contact with name '{name}' not found"

@input_error
def add_contact_birthday(args, book):
    # Перевіряємо правильність введення аргументів
    if len(args) != 2:
        return "Invalid command format. Please provide name and birthday in format DD.MM.YYYY"
    
    name, birthday = args
    # Шукаємо контакт у книзі за іменем
    contact = book.get_contact(name)
    if contact:
        # Перевіряємо чи вже є день народження для знайденого контакту
        if contact.birthday:
            return f"Birthday already exists for {name}"
        # Перевіряємо правильність формату дати народження
        try:
            # Пробуємо перетворити введену дату на об'єкт datetime
            birthday_date = datetime.strptime(birthday, "%d.%m.%Y")
        except ValueError:
            return "Invalid date format. Use DD.MM.YYYY"
        
        # Перевіряємо чи є метод add_birthday у класі Contact
        if not hasattr(contact, "add_birthday"):
            # Якщо такого методу немає, додаємо його
            def add_birthday(self, birthday_date):
                self.birthday = birthday_date

            setattr(contact.__class__, "add_birthday", add_birthday)

        # Додаємо день народження до знайденого контакту
        contact.add_birthday(birthday_date)
        return f"Birthday added for {name}"
    else:
        return f"Contact with name '{name}' not found"

def parse_input(user_input):
    # Розділяємо введений рядок на слова за пробілами і повертаємо список слів
    return user_input.split()

def main():
    book = AddressBook()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            # реалізація

        elif command == "change":
            # реалізація

        elif command == "phone":
            # реалізація

        elif command == "all":
            # реалізація

        elif command == "add-birthday":
            print(add_birthday(args, book))

        elif command == "show-birthday":
            print(show_birthday(args, book))

        elif command == "birthdays":
            print(birthdays(args, book))

        else:
            print("Invalid command.")
