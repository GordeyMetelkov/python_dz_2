# Напишите программу, которая получает целое число и возвращает
# его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата
NUM_SYSTEM = 16
NEXT_ORDER = 10
count = 1
num = int(input("Введите число: "))
hex_num = 0
num_2 = num
while(num_2 > 16):
    hex_num += num_2 % NUM_SYSTEM * count
    count *= NEXT_ORDER
    num_2 //= NUM_SYSTEM
hex_num += num_2 % NUM_SYSTEM * count
print(hex_num)
print(hex(num))