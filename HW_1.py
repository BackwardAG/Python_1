# Задача 2: Найдите сумму цифр трехзначного числа.

# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |


number = int(input("Enter a three-digit number: "))
a = number // 100
b = (number % 100) // 10
c = number % 10
result = a + b + c
print(result)