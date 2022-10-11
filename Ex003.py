# # 3. * Создайте программу для игры в "Крестики-нолики". Поле 3x3. Игрок - игрок, без бота.

def print_field_1 (field):
    print(' - - - - - - - - - ')
    print(f'|   {field[0]}   |  {field[1]}  |  {field[2]}  |')
    print(' - - - - - - - - - ')
    print(f'|  {field[3]}  |  {field[4]}  |  {field[5]}  |')
    print(' - - - - - - - - - ')
    print(f'|  {field[6]}  |  {field[7]}  |  {field[8]}  |')
    print(' - - - - - - - - - ')

def win (field):
    win_list = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 4, 8], [0, 4, 8], [2, 4, 6]]
    for i in range(8):
        if field[win_list[i][0]]==field[win_list[i][1]]==field[win_list[i][2]]:
            return 1
    return -1 

def move_player (field, a):
    if a == 1:
        n = input('Введите номер клетки, в которую хотите поставить "X": ')
        if n in field:
            field[field.index(n)] = 'X'
            return field
        else:
            print('Ошибка! Введено неверное значение.')
            return move_player (field, a)
    if a == -1:
        n = input('Введите номер клетки, в которую хотите поставить "O": ')
        if n in field:
            field[field.index(n)] = 'O'
            return field
        else:
            print('Ошибка! Введено неверное значение.')
            return move_player (field, a)

def game ():
    field_main = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    player_id = 1
    for i in range(9):
        print("\n" * 100)
        print_field_1(field_main)
        field_main = move_player (field_main, player_id)
        win_id = win(field_main)
        if win_id == 1 and player_id==1:
            print("\n" * 100)
            print_field_1(field_main)
            return print('Выиграл "X".')
        if win_id == 1 and player_id==-1:
            print("\n" * 100)
            print_field_1(field_main)
            return print('Выиграл "O".')
        player_id *=-1
    print("\n" * 100)
    print_field_1(field_main)
    return print('Ничья.')

game ()

