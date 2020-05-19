
def get_age():
    """Функция уточняет возраст пользователя и проверяет, записанно ли оно цифрами."""
    age = input("\nPlease, enter your age: ")
    try:
        age = int(age)
    except ValueError:
        pass
    else:
        return age


def print_message():
    """В зависимости от возраста, функция выводит сообщение для пользователя."""
    age = get_age()
    if age is None:
        message = "You need enter age by numbers."
    elif age < 3:
        message = "You need go to day nursery."
    elif age < 7:
        message = "You need go to kindergarten."
    elif age < 16:
        message = "You need go to school."
    elif age < 22:
        message = "You need go to college."
    else:
        message = "You need money? Go work."
    print(f"\n{message}")


print_message()