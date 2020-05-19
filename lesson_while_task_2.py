people = ['Вася', 'Маша', 'Петя', 'Валера', 'Саша', 'Даша']


def find_person(names, man):
    if man in names:
        i = 0
        while True:
            i += 1
            name = names.pop(0)
            if name == man:
                print(f'{man} нашелся!, он {i} в списке.')
                break
            else:
                print(f'{name.title()} - не Валера, ищем дальше.')
    else:
        print(f"Вангую, человека по имени {man.title()} нет в списке.")


find_person(people, 'Валера')