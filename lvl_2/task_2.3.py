# Задача 2.3.

# Напишите функцию, которая принимает цифры от 0 до 9 и возвращает значение прописью.
# Например,
# switch_it_up(1) -> 'One'
# switch_it_up(3) -> 'Three'
# switch_it_up(10000) -> None
# Использовать условный оператор if-elif-else нельзя!


# Вариант 1. (для Python версии >= 3.10)
def switch_it_up(number):
    match number:
        case 0:
            return 'Zero'

        case 1:
            return 'One'

        case 2:
            return 'Two'

        case 3:
            return 'Three'

        case 4:
            return 'Four'

        case 5:
            return 'Five'

        case 6:
            return 'Six'

        case 7:
            return 'Seven'

        case 8:
            return 'Eight'

        case 9:
            return 'Nine'

        case _:
            return None
        

words = switch_it_up(1)
print(words)


# Вариант 2. (для Python версии < 3.10)
def switch_it_up_2(number):
    number = str(number)
    numbers_in_words = {
        '0': 'Zero',
        '1': 'One',
        '2': 'Two',
        '3': 'Three',
        '4': 'Four',
        '5': 'Five',
        '6': 'Six',
        '7': 'Seven',
        '8': 'Eight',
        '9': 'Nine'
    }

    try:
        words = numbers_in_words[number]
        return words
    except KeyError:
        return None


words = switch_it_up_2(1)
print(words)