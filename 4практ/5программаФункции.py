import random
import string
def rand() -> None:

    """
    Функция rand принимает 0 значений. С помощью библиотек string и random генерируем рандомное 4-х значное число и рандомную строку из 3 символов.
    Реализуем вывод полученного номерного знака.
    :return:
    """

    num = random.randint(1000, 9999)
    letters = string.ascii_uppercase
    str = ''.join(random.choice(letters) for i in range(3))
    print(f"Ваш новый номер для машины: {num}{str} ")

rand()
