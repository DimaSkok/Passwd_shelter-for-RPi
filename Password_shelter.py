import random as rand

ram_passwords = ['0', '0']


#--------------------------------------------------
def pass_gener(pass_lenth, pass_curr):

    symb_old = 0
    symb_new = 0
    passwords = []

    for i in range(pass_curr):
        j = 0
        password = ""

        lenth = pass_lenth
        # print('1:', lenth)

        while j < lenth:
            j += 1

            symb1 = rand.randint(35, 38)
            symb2 = rand.randint(48, 59)
            symb3 = rand.randint(63, 90)
            symb4 = rand.randint(95, 122)
            symbols = [symb1, symb2, symb3, symb4]
            symb_new = symbols[rand.randint(0, 3)]

            # print('2:', symb_new, symb_old)
            if symb_new == symb_old:
                lenth += 1
                continue
            # print('3:', lenth)
            symb_old = symb_new
            password += chr(symb_new)

        passwords.append(password)
    return passwords

def writer (name, password):
    with open ('Shelter', 'a') as seo:
        seo.write(name + '\n')
        seo.write(password + '\n')
        seo.close()
    return

def reader (num):
    data = []
    with open('Shelter', 'r') as seo:
        number = 0
        while (num != number):
            number += 1
            void = seo.readline()
            void = seo.readline()

        name = seo.readline()[:-1]
        password = seo.readline()[:-1]

        data.append(name)
        data.append(password)

        seo.close()
    return data

def deliter (num):
    data = []
    with open('Shelter', 'r') as seo:
        data = seo.readlines()
        seo.close()

    data[num * 2] = ''
    data[num * 2 + 1] = ''

    with open('Shelter', 'w') as seo:
        seo.writelines(data)
        seo.close()
    return
#--------------------------------------------------

data = 0

while True:
    # print(data)
    if data == 5: data = 0
    if data == -1: data = 4

    # отвечает за просмотр, перезапись паролей
    if data == 0:
        button = input('Просмотреть пароли?\n')

        if button == 'f':
            number = 0
            cheker = 0
            i = 0
            while True:
                name = reader(i)
                i += 1
                if name == ['', '']: break
                cheker += 1
            cheker += 1
            while True:

                if number == cheker + 1:
                    number = 0
                if number == -1:
                    number = cheker

                if number == cheker:
                    button = input('Выйти?\n')
                    if button == 'f':
                        break
                    elif button == 's':
                        number += 1
                        continue
                    elif button == 'w':
                        number -= 1
                        continue
                    else:
                        continue

                if number == cheker - 1:
                    button = input('Проверить ОЗУ?\n')
                    if button == 'f':
                        print(ram_passwords[0], '\n', ram_passwords[1], sep='')
                        continue
                    elif button == 's':
                        number += 1
                        continue
                    elif button == 'w':
                        number -= 1
                        continue
                    else:
                        continue

                name = reader(number)[0]
                passwd = reader(number)[1]

                button = input(name + '\n')

                if button == 'f':
                    print(passwd)
                    button = input('Хотите сменить пароль?\n')
                    if button == 'f':
                        button = input('Вы уверены?\n')
                        if button == 'f':
                            num = len(passwd)

                            while True:
                                print('Длина пароля - ' + str(num))
                                button = input()
                                if button == 'w':
                                    num += 1
                                    continue
                                elif button == 's':
                                    num -= 1
                                    continue
                                else:
                                    break
                            ram_passwords = [name, passwd]
                            writer(name, pass_gener(num, 1)[0])
                            deliter(number)
                    else:
                        continue
                    continue
                elif button == 's':
                    number += 1
                    continue
                elif button == 'w':
                    number -= 1
                    continue
                else:
                    break

            continue

        elif button == 's':
            data += 1
            continue
        elif button == 'w':
            data -= 1
            continue
        else:
            continue
    # отвечает за вбивание новых паролей, нужна клава
    if data == 1:
        button = input('Добавить пароль?\n')

        if button == 'f':
            name = input('Название приложения - ')
            lenth = int(input('Длина пароля - '))
            writer(name, pass_gener(lenth, 1)[0])
            print('Пароль к приложению/сайту добавлен')
            continue
        elif button == 's':
            data += 1
            continue
        elif button == 'w':
            data -= 1
            continue
        else:
            continue
    # отвечает за удаление паролей, нужна клава
    if data == 2:
        button = input('Удалить пароль?\n')

        if button == 'f':
            number = 0
            cheker = 0
            i = 0
            while True:
                name = reader(i)
                i += 1
                if name == ['', '']: break
                cheker += 1
            # cheker += 1
            while True:

                if number == cheker + 1:
                    number = 0
                if number == -1:
                    number = cheker

                if number == cheker:
                    button = input('Выйти?\n')
                    if button == 'f':
                        break
                    elif button == 's':
                        number += 1
                        continue
                    elif button == 'w':
                        number -= 1
                        continue
                    else:
                        continue

                name = reader(number)[0]

                button = input(name + '\n')

                if button == 'f':

                    button = input('Хотите удалить пароль?\n')
                    if button == 'f':
                        button = input('Write: <I KNOW WHAT I AM DOING>\n')
                        if button == 'I KNOW WHAT I AM DOING':
                            ram_passwords = reader(number)
                            deliter(number)
                            print('Удаление успешно')
                            break
                        else:
                            continue
                    continue
                elif button == 's':
                    number += 1
                    continue
                elif button == 'w':
                    number -= 1
                    continue
                else:
                    break

            continue
        elif button == 's':
            data += 1
            continue
        elif button == 'w':
            data -= 1
            continue
        else:
            continue
    # отвечает за ещё один просмотр условного ОЗУ
    if data == 3:
        button = input('Посмотреть ОЗУ?\n')
        if button == 'f':
            print(ram_passwords[0], '\n', ram_passwords[1], sep='')
            continue
        elif button == 's':
            data += 1
            continue
        elif button == 'w':
            data -= 1
            continue
        else:
            continue
    # отвечает за выход из малинки, нужна доработка
    if data == 4:
        button = input('Выйти?\n')
        if button == 'f':
            # print('work')
            break
        elif button == 's':
            data += 1
            continue
        elif button == 'w':
            data -= 1
            continue
        else:
            continue