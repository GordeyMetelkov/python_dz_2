# Напишите программу, которая принимает две строки вида “a/b”
# - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей.
# Для проверки своего кода используйте модуль fractions.

from fractions import Fraction

s_1 = input("Введите первую дробь вида “a/b”: ")
s_2 = input("Введите вторую дробь вида “a/b”: ")

numerator_1 = int(s_1.split("/")[0])
denominator_1 = int(s_1.split("/")[1])

numerator_2 = int(s_2.split("/")[0])
denominator_2 = int(s_2.split("/")[1])

if (denominator_1 > denominator_2):
    if not denominator_1 % denominator_2:
        numerator_2 *= denominator_1 // denominator_2
    else:
        numerator_2 *= denominator_1
        numerator_1 *= denominator_2
        denominator_1 = denominator_2 = denominator_1 * denominator_2
elif (denominator_2 > denominator_1):
    if not denominator_2 % denominator_1:
        numerator_1 *= denominator_2 // denominator_1
    else:
        numerator_2 *= denominator_1
        numerator_1 *= denominator_2
        denominator_1 = denominator_2 = denominator_1 * denominator_2

sum_numerator = numerator_1 + numerator_2
sum_denominator = denominator_2

product_numerator = numerator_1 * numerator_2
product_denominator = denominator_2 * denominator_1

for i in range(sum_numerator, 1, -1):
    if sum_numerator % i == 0 and sum_denominator % i == 0:
        sum_numerator //= i
        sum_denominator //= i

for i in range(product_numerator, 1, -1):
    if product_numerator % i == 0 and product_denominator % i == 0:
        product_numerator //= i
        product_denominator //= i

print(sum_numerator, "/", sum_denominator, sep='')
print(Fraction(numerator_1, denominator_1) + Fraction(numerator_2, denominator_2))
print(product_numerator, "/", product_denominator,sep='')
print(Fraction(numerator_1, denominator_1) * Fraction(numerator_2, denominator_2))
