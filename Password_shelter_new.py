import random as rand
import RPi.GPIO as gp
import time

ram_passwords = ['0', '0']
gp.setmode(gp.BCM)
gp.setwarnings(False)

data = 0
info = ['Check passwords', 'Add passwords', 'Delete passwords', 'Check "RAM"', 'Exit']
keyboard_d = [False, False, False]
exiter = False

gp.setup(20, gp.OUT)
gp.output(20, 1)
gp.setup(5, gp.IN)
gp.setup(6, gp.IN)
gp.setup(26, gp.IN)

# stop time before new button tap
timer = 0.2

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

def keyboard ():
    global data
    if gp.input(5):
        keyboard_d[0] = True
        data -= 1
        return False
    elif gp.input(26):
        keyboard_d[2] = True
        data += 1
        return False
    elif gp.input(6):
        keyboard_d[1] = True
        return False
    else:
        for i in range(3):
            keyboard_d[i] = False
    return True

def starter (num):
    if num == 0: program_check()
    if num == 1: program_add()
    if num == 2: program_delete()
    if num == 3: program_RAM()
    if num == 4: program_Exit()

def program_check ():
    # отвечает за просмотр, перезапись паролей
    global ram_passwords, data, timer
    data_dump = data
    print('Check passwords?')
    data = 0
    time.sleep(timer)
    while True:
        if keyboard(): continue
        if data == 2: data = 0
        if data == -1: data = 1

        time.sleep(timer)

        if data == 0:
            print('Check passwords?')
            if keyboard_d[1]:
                data_dump_l = data
                data = 0
                cheker = 0
                i = 0
                while True:
                    name = reader(i)
                    i += 1
                    if name == ['', '']: break
                    cheker += 1
                name = reader(data)[0]
                print(name)
                time.sleep(timer)
                while True:
                    if keyboard(): continue

                    time.sleep(timer)

                    if data == cheker + 2:
                        data = 0
                    if data == -1:
                        data = cheker + 1

                    if data == cheker + 1:
                        print('Exit?')
                        if keyboard_d[1]:
                            data = data_dump_l
                            time.sleep(timer)
                            print('Check passwords?')
                            break
                    if data == cheker:
                        print('Check "RAM"?')
                        if keyboard_d[1]:
                            print(ram_passwords[0], '\n', ram_passwords[1], sep='')
                            continue

                    if data != (cheker + 2) and data != (cheker + 1):
                        name = reader(data)[0]
                        passwd = reader(data)[1]
                        print(name)

                        if keyboard_d[1]:
                            print(passwd)
                            time.sleep(timer)
                            while True:
                                flag = False
                                if keyboard(): continue
                                if keyboard_d[1]:
                                    print('You really want change password?')
                                    time.sleep(timer)
                                    while True:
                                        if keyboard(): continue
                                        if keyboard_d[1]:
                                            num = len(passwd)
                                            data_dump_ll = data
                                            data = 0
                                            print('Length of password - ' + str(num))
                                            time.sleep(timer)
                                            while True:
                                                if keyboard(): continue

                                                time.sleep(timer)
                                                if keyboard_d[2]:
                                                    num += 1
                                                    print('Length of password - ' + str(num))
                                                    continue
                                                elif keyboard_d[0]:
                                                    num -= 1
                                                    print('Length of password - ' + str(num))
                                                    continue

                                                if keyboard_d[1]:
                                                    data = data_dump_ll
                                                    flag = True
                                                    break
                                            ram_passwords = [name, passwd]
                                            writer(name, pass_gener(num, 1)[0])
                                            deliter(data)
                                            flag = True

                                        if keyboard_d[0] or keyboard_d[2] or flag:
                                            flag = True
                                            break
                                if keyboard_d[0] or keyboard_d[2] or flag:
                                    break

        if data == 1:
            print('Exit?')
            if keyboard_d[1]:
                data = data_dump
                break
 
def program_add():
    # отвечает за вбивание новых паролей, нужна клава
    global data, timer
    data_dump = data
    print('Generate password')
    data = 1
    time.sleep(timer)
    while True:
        if keyboard(): continue
        if data == 4: data = 1
        if data == 0: data = 3

        time.sleep(timer)

        if data == 1:
            print('Generate password')
            if keyboard_d[1]:
                name = input('Name of app - ')
                lenth = int(input('Lenth of password - '))
                writer(name, pass_gener(lenth, 1)[0])
                print('Password into app/site added')
                data = data_dump
                break
        if data == 2:
            print('Add password')
            if keyboard_d[1]:
                name = input('Name of app - ')
                passw = input('Password - ')
                writer(name, passw)
                print('Password into app/site added')
                data = data_dump
                break
        if data == 3:
            print('Exit?')
            if keyboard_d[1]:
                data = data_dump
                break

def program_delete():
    # отвечает за удаление паролей, нужна клава
    global ram_passwords, data, timer
    data_dump = data
    print('Delete passwords?')
    data = 2
    time.sleep(timer)
    while True:
        if keyboard(): continue
        if data == 4: data = 2
        if data == 1: data = 3

        time.sleep(timer)

        if data == 2:
            print('Delete passwords?')
            if keyboard_d[1]:
                data_dump_l = data
                data = 0
                cheker = 0
                i = 0
                while True:
                    name = reader(i)
                    i += 1
                    if name == ['', '']: break
                    cheker += 1
                name = reader(data)[0]
                print(name)
                time.sleep(timer)
                while True:
                    if keyboard(): continue

                    time.sleep(timer)

                    if data == cheker + 1:
                        data = 0
                    if data == -1:
                        data = cheker

                    if data == cheker:
                        print('Exit?')
                        if keyboard_d[1]:
                            print('Delete passwords?')
                            time.sleep(timer)
                            break

                    if data != cheker:
                        name = reader(data)[0]
                        print(name)

                        if keyboard_d[1]:
                            button = input('Write: <I KNOW WHAT I AM DOING>\n')
                            if button == 'I KNOW WHAT I AM DOING':
                                ram_passwords = reader(data)
                                deliter(data)
                                print('Deleted success')
                                data = data_dump_l
                                print('Delete passwords?')
                                time.sleep(timer)
                                break
                            else:
                                print(name)
                                time.sleep(timer)
                                continue


        if data == 3:
            print('Exit?')
            if keyboard_d[1]:
                data = data_dump
                break

def program_RAM():
    # отвечает за просмотр условного ОЗУ
    global ram_passwords
    print(ram_passwords[0], '\n', ram_passwords[1], sep='')

def program_Exit():
    # отвечает за выход из малинки, нужна доработка
    global exiter
    exiter = True
#--------------------------------------------------


print(info[data])
while True:
    if keyboard():
        continue

    else:
        if exiter:
            break

        # print(data)
        if data == 5: data = 0
        if data == -1: data = 4

        if keyboard_d[1]:
            starter(data)

        time.sleep(timer)
        print(info[data])


