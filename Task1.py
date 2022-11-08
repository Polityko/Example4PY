# Задача 1. Задайте натуральное число N. 
# Напишите программу, которая составит список простых множителей числа N.

def mn(n):
    if n == 1: return [1]
    lst = []
    i = 2
    while n != 1:
        if n % i == 0:
            n = n // i
            lst.append(i)
            continue
        i+=1
    return lst
print(mn(60))