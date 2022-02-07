import random
from termcolor import colored


def show_matrix_board(matrix):
    """ Вывод игровой доски на экран """
    print()
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(str(matrix[i][j]).ljust(3), end='')
        print()
    print()


def definition_computer_sign(sign):
    """ Определение знака символа у компьютера """
    if sign.lower() == colored('x', 'green'):
        return colored('0', 'red')
    else:
        return colored('X', 'red')


def input_by_human_cell(sign):
    """ Ввод номера ячейки для записи в нее символа """
    while True:
        digit = input(f'Введите номер ячейки, в которую хотите записать "{sign}": ')
        if digit not in game_digits and digit.isdigit() and 1 <= int(digit) <= 100:
            break
        elif digit in game_digits and digit.isdigit() and 1 <= int(digit) <= 100:
            print('Эта ячейка уже занята, попробуйте выбрать другую')
        elif digit not in game_digits and not digit.isdigit():
            print('Вы вводите не число, а набор символов, попробуйте еще раз.')
        elif digit not in game_digits and digit.isdigit() and (int(digit) > 100 or int(digit) < 1):
            print('Введенное число не попадает под диапазон числовых значений ячеек, от 1 до 100, включительно.\nПопробуйте еще раз.')
    game_digits.append(digit)
    return digit


def record_human_sign(sign, digit, matrix):
    """ Запись символа в ячейку игровой доски, выбранную пользователем """
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if digit == matrix[i][j]:
                matrix[i][j] = sign + '  '
                break
    return matrix


def record_computer_sign(sign, matrix):
    """ Запись символа в ячейку игровой доски, выбранную компьютером """
    while True:
        random_digit = str(random.randint(1, 100))
        if random_digit not in game_digits:
            break
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if random_digit == matrix[i][j]:
                matrix[i][j] = sign + '  '
                break
    game_digits.append(random_digit)
    print(f'Компьютер записывает свой знак в ячейку под номером "{random_digit}"')
    return matrix


def examination(matrix, hum_sign, comp_sign):
    """ Проверка ряда из 5 одинаковых символов по горизонтали, вертикали и диагоналям """
    green_x = colored('X', 'green')
    red_x = colored('X', 'red')
    green_0 = colored('0', 'green')
    red_0 = colored('0', 'red')
    green_five_x = (green_x + '  ') * 5
    green_five_0 = (green_0 + '  ') * 5
    red_five_x = (red_x + '  ') * 5
    red_five_0 = (red_0 + '  ') * 5
    for line in matrix:
        joined_line = ''.join(line)
        if (green_five_x in joined_line and hum_sign == green_x) or (green_five_0 in joined_line and hum_sign == green_0):
            return 'Вы проиграли!!!'
        elif (red_five_x in joined_line and comp_sign == red_x) or (red_five_0 in joined_line and comp_sign == red_0):
            return 'Вы победили!!!'
    for column in zip(*matrix):
        joined_column = ''.join(column)
        if (green_five_x in joined_column and hum_sign == green_x) or (green_five_0 in joined_column and hum_sign == green_0):
            return 'Вы проиграли!!!'
        elif (red_five_x in joined_column and comp_sign == red_x) or (red_five_0 in joined_column and comp_sign == red_0):
            return 'Вы победили!!!'
    diagonals_1 = []
    diagonals_2 = []
    for p in range(2 * 9):
        diagonals_1.append([matrix[p - q][q] for q in range(max(0, p - len(matrix[i]) + 1), min(p, len(matrix[i]) - 1) + 1)])
        diagonals_2.append([matrix[len(matrix[i]) - p + q - 1][q] for q in range(max(0, p - len(matrix[i]) + 1), min(p, len(matrix[i]) - 1) + 1)])
    for el in diagonals_1:
        joined_el = ''.join(el)
        if (green_five_x in joined_el and hum_sign == green_x) or (green_five_0 in joined_el and hum_sign == green_0):
            return 'Вы проиграли!!!'
        elif (red_five_x in joined_el and comp_sign == red_x) or (red_five_0 in joined_el and comp_sign == red_0):
            return 'Вы победили!!!'
    for el in diagonals_2:
        joined_el = ''.join(el)
        if (green_five_x in joined_el and hum_sign == green_x) or (green_five_0 in joined_el and hum_sign == green_0):
            return 'Вы проиграли!!!'
        elif (red_five_x in joined_el and comp_sign == red_x) or (red_five_0 in joined_el and comp_sign == red_0):
            return 'Вы победили!!!'


def draw_examination():
    """ Проверка на ничью """
    if len(game_digits) < 100:
        return True
    else:
        print('Свободных ячеек больше не осталось, ничья!!!')
        return False


flag = True
while flag:
    game_digits = []
    matrix_board = [['*' for j in range(10)] for i in range(10)]
    count = 1
    for i in range(len(matrix_board)):
        for j in range(len(matrix_board[i])):
            matrix_board[i][j] = str(count)
            count += 1
    print('Добро пожаловать в игру "Обратные крестики-нолики!!!"')
    show_matrix_board(matrix_board)
    print('Перед вами поле 10 х 10 с ячейками, в которые необходимо записывать значения "Х" или "0".\nЦвет, выбранного вами знака, будет "зеленым", а компьютера - "красным".')
    print()
    while True:
        human_sign = input('Введите знак, которым хотите играть, "Х" или "0": ').upper()
        human_sign = colored(human_sign, 'green')
        if human_sign in (colored('0', 'green'), colored('X', 'green')):
            break
    computer_sign = definition_computer_sign(human_sign)
    if human_sign == colored('X', 'green'):
        print('Вы выбрали знак "Х", вы начинаете первым.')
    else:
        print('Вы выбрали знак "0", вы начинаете вторым.')
    while True:
        if human_sign == colored('X', 'green'):
            human_digit = input_by_human_cell(human_sign)
            matrix_board = record_human_sign(human_sign, human_digit, matrix_board)
            show_matrix_board(matrix_board)
            if examination(matrix_board, human_sign, computer_sign):
                print(examination(matrix_board, human_sign, computer_sign))
                break
            print(f'Компьютер вводит номер ячейки, в которую хочет записать "{computer_sign}".')
            matrix_board = record_computer_sign(computer_sign, matrix_board)
            show_matrix_board(matrix_board)
            if examination(matrix_board, human_sign, computer_sign):
                print(examination(matrix_board, human_sign, computer_sign))
                break
            if not draw_examination:
                break
        else:
            print()
            print(f'Компьютер вводит номер ячейки, в которую хочет записать "{computer_sign}".')
            matrix_board = record_computer_sign(computer_sign, matrix_board)
            show_matrix_board(matrix_board)
            if examination(matrix_board, human_sign, computer_sign):
                print(examination(matrix_board, human_sign, computer_sign))
                break
            human_digit = input_by_human_cell(human_sign)
            matrix_board = record_human_sign(human_sign, human_digit, matrix_board)
            show_matrix_board(matrix_board)
            if examination(matrix_board, human_sign, computer_sign):
                print(examination(matrix_board, human_sign, computer_sign))
                break
            if not draw_examination:
                break
    while True:
        answer = input('Хотите сыграть еще раз? Нажмите "y" или "n": ').lower()
        if answer == 'y':
            break
        elif answer == 'n':
            flag = False
            break






