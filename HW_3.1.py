# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def division(*args):
    try:
        num1 = int(input("Введите числитель: "))
        num2 = int(input("Введите знаменатель: "))
        result = num1 / num2
        return round(result, 2)
    except ZeroDivisionError:
        return "На ноль делить нельзя"
    except ValueError:
        return "Вы забыли ввести число/числа"

print(f"Результат деления:  {division()}")
