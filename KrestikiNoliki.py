def introduction(): # Вступление
    print(' ' * space,"<--------------->   ")
    print(' ' * space," Добро пожаловать   ")
    print(' ' * space,"       в           ")
    print(' ' * space,"      игру         ")
    print(' ' * space," крестики-нолики!   ")
    print(' ' * space,"<--------------->   ")
    print(' ' * space,"Ввод координат: X Y ")
    print(' ' * space,"X - номер строки   ")
    print(' ' * space,"Y - номер столбца  ")
    print(' ' * space,"<--------------->   ")
#-----------------------------------------------------------
space = 40 # Space - позиционирует расположение поля игры на экране
empty_cell = "-" # символ заполнения пустых ячеек
introduction()
cells = [[empty_cell]*3 for i in range(3)]
#-----------------------------------------------------------
def game_field (): # Функция отображения игрового поля
    print("")
    print(' ' * space, "   | 0 | 1 | 2 |")
    for i, row in enumerate(cells):
        print(' ' * space, "<--------------->")
        row_and_str = f" {i} | {' | '.join(row)} |"
        print(' ' * space, row_and_str)
#-----------------------------------------------------------
game_field()
print(" ")
max_steps = 9 # Максимальное число шагов
steps_counter = 0 # Счётчик шагов
XO_flag = True # Переменная, указывающая на признак активности X-а или O-уля
InCorr = 1
#-----------------------------------------------------------
def check_xy(xy): # Функция проверки правильности ввода координат
    if len(xy) == 3:
        if not xy[0].isdigit():
            InCorr = "Координата X - не число!"
        elif xy[1] != " ":
            InCorr = "Между координатами не пробел!"
        elif not xy[2].isdigit():
            InCorr = "Координата Y - не число!"
        else:
            # формат ввода координат правильный!
            x, y = int(xy[0]), int(xy[2])
            # проверка диапазона X и Y
            if 0 <= x <= 2 and 0 <= y <= 2:
                InCorr = ""
            else:
                InCorr = "Неправильный диапозон координат!"
    else:
        InCorr = "Введите 2 координаты!"
    return InCorr
#-----------------------------------------------------------
def win_control(): # Функция проверки выигрышных комбинаций
    if XO_flag:
        Cntrl_Key = 'X'
    else:
        Cntrl_Key = 'O'
    # Проверка строк
    for j in range(3):
        count = 0
        for i in range(3):
            if cells[j][i] == Cntrl_Key:
                count += 1
        if count == 3:
            win_str = "Победили " + Cntrl_Key + "!"
            return win_str
    # Проверка столбцов
    for j in range(3):
        count = 0
        for i in range(3):
            if cells[i][j] == Cntrl_Key:
                count += 1
        if count == 3:
            win_str = "Победили " + Cntrl_Key + "!"
            return win_str
    # Проверка диагонали 1
    count = 0
    for i in range(3):
        if cells[i][i] == Cntrl_Key:
            count += 1
    if count == 3:
        win_str = "Победили " + Cntrl_Key + "!"
        return win_str
    # Проверка диагонали 2
    count = 0
    for i in range(3):
        if cells[i][2-i] == Cntrl_Key:
            count += 1
    if count == 3:
        win_str = "Победили " + Cntrl_Key + "!"
        return win_str
#-----------------------------------------------------------
while True: # Основной игровой цикл
    if steps_counter < max_steps:
        if XO_flag:
            OutStr = ' ' * space + "Введите координаты X: "
            xy = input(OutStr)
        else:
            OutStr = ' ' * space + "Введите координаты O: "
            xy = input(OutStr)
        InCorr = check_xy(xy)
        if InCorr:
            print(' ' * space,InCorr)
        else:
            x, y = int(xy[0]), int(xy[2])
            if cells[x][y] == '-':
                if XO_flag:
                    cells[x][y] = "X"
                else:
                    cells[x][y] = "O"
                game_field()
                result = win_control()
                if result:
                    print(' ' * space, result, "Игра окончена!")
                    break
                else:
                    steps_counter += 1
                    XO_flag = not XO_flag
            else:
                print(' ' * space, "Ячейка занята!")
    else:
        print(' ' * space, "Ничья!")
        break
#-----------------------------------------------------------
