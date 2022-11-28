import math
def drob(chi:int,zna:int) -> None:

    """
    Функция drop принимает значения chi - числитель и zna - знаменатель, в самой функции реализуется присвоение переменной gen общий делитель
    числителя и знаменателя, далее выводится результат в виде итоговой дроби, или же в виде целого/не целого числа.
    :param chi:
    :param zna:
    :return:
    """

    gen = math.gcd(chi, zna)
    print(f"Результат равен: {chi//gen}/{zna//gen}, или же {(chi//gen)/(zna//gen)}")

chi = int(input("Введите числитель дроби: "))
zna = int(input("Введите знаменатель дроби: "))
drob(chi,zna)
