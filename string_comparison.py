def message_comparison(message_1, message_2):
    """Функция сравнивает два параметра, и в зависимости от результата выводит сообщение."""
    if type(message_1) is not str or type(message_2) is not str:
        number = 0
    elif message_1 == message_2:
        number = 1
    elif len(message_1) > len(message_2):
        number = 2
    elif message_1 != message_2 and message_2 == 'learn':
        number = 3
    return number


print(message_comparison('tiger', 1))
print(message_comparison('roger', 'roger'))
print(message_comparison('elephant', 'cat'))
print(message_comparison('bee', 'learn'))