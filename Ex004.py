# 4. ** Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

import random


def game():
    candies = 120
    move, step = draw()
    while candies != 0:
        if move == 1:
            print("\n")
            if step == 1:
                candies = move_player(candies, move)
            else:
                candies = move_bot(candies, move)
            move *= -1
        else:
            print("\n")
            if step == 1:
                candies = move_player(candies, move)
            else:
                candies = move_bot(candies, move)
            move *= -1
    print("\n")
    if move == 1 and step == 1:
        print('Победил игрок №2!')
    if move == 1 and step == -1:
        print('Победил бот!')
    else:
        print('Победил игрок №1!')


def move_player(candies, move):
    if move == 1:
        player_1 = input(f'Игрок №1:\nНа столе лежит {candies} конфет(а).\n\
Вы можете взять не более 28 конфет.\nСколько конфет вы хотите взять: ')
        if player_1.isdigit():
            player_1 = int(player_1)
            if 0 < player_1 <= 28 and 0 < player_1 <= candies:
                candies -= player_1
                return candies
        print("\n")
        print('Ошибка! Введено неверное значение.')
        return move_player(candies, move)
    if move == -1:
        player_2 = input(f'Игрок №2:\nНа столе лежит {candies} конфет(а).\n\
Вы можете взять не более 28 конфет.\nСколько конфет вы хотите взять: ')
        if player_2.isdigit():
            player_2 = int(player_2)
            if 0 < player_2 <= 28 and 0 < player_2 <= candies:
                candies -= player_2
                return candies
        print("\n")
        print('Ошибка! Введено неверное значение.')
        return move_player(candies, move)


def draw():
    print("\n")
    start = input(
        'Введите слово "игрок", чтобы играть против другого игрока\n\
или введите слово "бот", чтобы играть против бота: ')
    if start == 'игрок':
        draw_number = random.choice([1, -1])
        method_start = 1
        return draw_number, method_start
    if start == 'бот':
        draw_number = random.choice([1, -1])
        method_start = -1
        return draw_number, method_start
    print("\n")
    print('Ошибка! Введено неверное значение.')
    return draw()


def move_bot(candies, move):
    if move == 1:
        player = input(f'Игрок №1:\nНа столе лежит {candies} конфет(а).\n\
Вы можете взять не более 28 конфет.\nСколько конфет вы хотите взять: ')
        if player.isdigit():
            player = int(player)
            if 0 < player <= 28 and 0 < player <= candies:
                candies -= player
                return candies
        print("\n")
        print('Ошибка! Введено неверное значение.')
        return move_player(candies, move)
    if move == -1:
        if candies <= 28:
            bot = candies
        if 30 <= candies <= 57:
            bot = candies-29
        if candies > 57 or candies == 29:
            bot = random.randrange(1, 28)
        print(f'Бот:\nНа столе лежит {candies} конфет(а).\n\
Бот взял {bot} конфет(а).')
        candies -= bot
        return candies


game()
