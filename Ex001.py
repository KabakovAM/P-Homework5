# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв".
# В тексте используется разделитель пробел.

from random import choices

def create_list_str():
    n = int(input('Введите размер списка: '))
    while n <= 0:
        print('Введён неверный размер списка')
        n = int(input('Введите размер списка: '))
    result = ''
    for i in range(n-1):
        result+=(f'{"".join(choices("абв", k = 3))} ')
    result+=(f'{"".join(choices("абв", k = 3))}')
    return result

def check(word):
    if word != 'абв':
        return True
    else:
        return False

res = create_list_str()
print(res)
lis_result = filter(check, res.split(' '))
print(" ".join(lis_result))
