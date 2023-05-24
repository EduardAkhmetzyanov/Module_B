print("Игра 'Крестики - Нолики'")
print("Ход осуществляется по очереди")
print("Чтобы сходить, нужно ввести 2 цифры через пробел")
print("Хорошей игры!")

game = [[" "] * 3 for i in range(3)]


def game_map():
    print("   0 1 2")
    for i in range(3):
        print(f" {i} {game[i][0]} {game[i][1]} {game[i][2]}")


def func():
    while True:
        enter = input("Введите координаты x, y через пробел: ").split()
        if len(enter) != 2:
            print("Неправильный ввод! Повторите попытку!")
            continue
        x, y = enter
        x, y = int(x), int(y)
        if 0 <= x <= 2 and 0 <= y <= 2:
            if game[x][y] == " ":
                return x, y
            else:
                print("Клетка занята! Повторите попытку!")
        else:
            print("Вы ввели неверные координаты! Повторите попытку!")


def win_():
    win_comb = [ ((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)),
                 ((0, 0), (1, 0), (2, 0)), ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)),
                 ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2))]
    for item in win_comb:
        a = item[0]
        b = item[1]
        c = item[2]
        if game[a[0]][a[1]] == game[b[0]][b[1]] == game[c[0]][c[1]] != " ":
            print(f" Победил {game[a[0]][a[1]]}!")
            return True
    return False


count = 0
while True:
    count += 1
    game_map()
    if count % 2 == 1:
        print("Ходит крестик!")
    else:
        print("Ходит нолик!")

    x, y = func()
    if count % 2 == 1:
        game[x][y] = "X"
    else:
        game[x][y] = "O"

    if win_():
        break

    if count > 8:
        print("Ничья!")
        break
