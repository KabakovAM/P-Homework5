# 2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

from os import path

def encode(text):
    temp = text[0]
    result = ''
    count = 1
    for i in range(1, len(text)):
        if temp == text[i]:
            count += 1
        else:
            result += str(count)+str(text[i-1])
            temp = text[i]
            count = 1
    result += str(count)+str(text[i-1])
    return result

def decode(text):
    result = ''
    count = ''
    for i in range(len(text)):
        if text[i].isdigit():
            count += text[i]
        else:
            result += text[i] * int(count)
            count = ''
    return result

def encode_decode():
    n = int(input('Введите "0" для кодирования или "1" для декодирования: '))
    if n == 0:
        file = input('Введите путь к файлу для кодирования: ')
        if path.exists(file):
            with open(file, 'r', encoding='utf-8') as output, \
                    open('Homework5\decode_result.txt', 'a', encoding='utf-8') as input_file:
                input_file.write(encode(str(output.readlines())[2:-2]))
        else:
            print('Введён неверный путь к файлу.')
    elif n == 1:
        file = input('Введите путь к файлу для декодирования: ')
        if path.exists(file):
            with open(file, 'r', encoding='utf-8') as output, \
                    open('Homework5\encode_result.txt', 'a', encoding='utf-8') as input_file:
                input_file.write(decode(str(output.readlines())[2:-2]))
        else:
            print('Введён неверный путь к файлу.')
    else:
        print('Введён неверный метод')

encode_decode()
