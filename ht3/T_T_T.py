table = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
victory = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7],
           [2, 5, 8], [0, 4, 8], [2, 4, 6]]
available_steps = ['1', '2', '3', '4', '5', '6', '7', '8', '9']


def print_table():
    print(table[0], end=" ")
    print(table[1], end=" ")
    print(table[2])

    print(table[3], end=" ")
    print(table[4], end=" ")
    print(table[5])

    print(table[6], end=" ")
    print(table[7], end=" ")
    print(table[8])


def turn(num, x_or_y, list_of_available):
    table[table.index(num)] = x_or_y
    list_of_available.remove(num)


def get_result(list_of_available):
    winner = ""
    if len(list_of_available) == 0:
        return "undefined"
    for i in victory:
        if "X" == table[i[0]] and table[i[1]] == "X" and table[i[2]] == "X":
            winner = "X"
        if table[i[0]] == "O" and table[i[1]] == "O" and table[i[2]] == "O":
            winner = "O"

    return winner


game_over = False
winner_is = ""
X = True
step = 0
while not game_over:
    print_table()
    if X:
        symbol = "X"
        while step not in available_steps:
            step = input("X! Your turn!: ")

    else:
        symbol = "O"
        while step not in available_steps:
            step = input("Y! Your turn!: ")

    turn(step, symbol, available_steps)
    winner_is = get_result(available_steps)
    if winner_is != "":
        game_over = True
    else:
        game_over = False

    X = not X

print_table()
print("Winner is:", winner_is)

'''
Для выполнения этого задания использовались парадигмы:
-структурная, т.к. питон не поддерживает гоуту
-императивная, т.к. для решения задания требуется пошаговое динамическое выполнение действий
-сразу была отметена ооп, ввиду отсутствия свободного времени
-процедурная(частично), т.к. удобно выполнять повторяющиеся действия, частично сократило время написания кода
'''