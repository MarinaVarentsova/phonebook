# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt.
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной
# записи(Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной
# 5.Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
# для изменения и удаления данных и поиска по фамилии.

from os.path import exists
import csv
path = "phone.csv"


def get_info():
    global phone_number
    info = []
    first_name = input("Введите имя: ")
    info.append(first_name.lower())
    surname = input("Введите отчество: ")
    info.append(surname.lower())
    last_name = input("Введите фамилию: ")
    info.append(last_name.lower())
    flag = False
    while not flag:
        try:
            phone_number = int(input('Введите номер телефона: '))
            if len(str(phone_number)) != 11:
                print('wrong number')
            else:
                flag = True
        except ValueError:
            print('not valid number')

    info.append(phone_number)
    print('\n')
    return info


def create_file():
    with open('phone.txt', 'w', encoding='utf-8') as data:
        data.write('FirstName,Surname,LastName,Phone')


def write_file(info):
    with open(path, 'a', encoding='utf-8') as data:
        data.write(f'{info[0]},{info[1]},{info[2]},{info[3]}\n')


def read_file(path):
    with open(path, 'r', encoding='utf-8') as data:
        phone_book = data.readlines()
    return phone_book


def find_file(file_name):
    x = input("введите параметр для поиска: ")
    with open(path, "r") as data:
        phone_book = data.readlines()
        index = 0
        for i in phone_book:
            if x in i:
                print(i, end='')
                index += 1
        return (print(f'найдено {index-1}'))


def record_info():
    info = get_info()
    write_file(info)


def find_for_change_file(file_name):
    global contact
    contact = input("введите параметр для поиска: ")
    with open(file_name, 'r', encoding='utf-8') as data:
        phone_book = data.readlines()
        for i, line in enumerate(phone_book):
            if contact in line.strip():
                if i == 0:
                    print(f"fieldnames: ", line.strip())
                else:
                    print(f"Contact №{i}: ", line.strip())
        flag = False
        while not flag:
            try:
                contact = int(input("выберите контакт для изменения: "))
                if contact < 0:
                    print('wrong contact')
                    flag = False
                if contact == 0:
                    contact = 0
                    flag = True
                if contact > 0:
                    contact = contact - 1
                    flag = True
                else:
                    flag = True
            except ValueError:
                print('not valid number')
        return contact


def change_file(path, contact):
    global new_phone_number
    with open(path, "r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        phone_book = []
        for row in csv_reader:
            print(row)
            phone_book.append(row)
    print('\n')
    to_update = phone_book[contact].values()
    print(f"Contact №{contact+1} будет изменен, текущие данные: ", to_update)
    new_first_name = input("Введите новое имя контакта: ")
    new_first_name = f'{new_first_name}'
    new_surname = input("Введите новое отчество контакта: ")
    new_surname = f'{new_surname}'
    new_last_name = input("Введите новую фамилию контакта: ")
    new_last_name = f'{new_last_name}'
    flag = False
    while not flag:
        try:
            new_phone_number = int(input('Введите номер телефона: '))
            if len(str(new_phone_number)) != 11:
                print('wrong number')
            else:
                flag = True
        except ValueError:
            print('not valid number')
    new_phone_number = f'{new_phone_number}'
    with open(path, 'w', newline='') as csv_file:
        fieldnames = phone_book[0].keys()
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for row in phone_book:
            if set(to_update).issubset(set(row.values())):
                row['FirstName'] = new_first_name
            if set(to_update).issubset(set(row.values())):
                row['Surname'] = new_surname
            if set(to_update).issubset(set(row.values())):
                row['LastName'] = new_last_name
            if set(to_update).issubset(set(row.values())):
                row['Phone'] = new_phone_number
            writer.writerow(row)


def delete_file(path, contact):
    global new_phone_number
    with open(path, "r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        phone_book = []
        for row in csv_reader:
            print(row)
            phone_book.append(row)
    print('\n')
    to_update = phone_book[contact].values()
    number = contact + 1
    print(f"Contact №{number} будет удален, текущие данные: ", to_update)
    valid = input("подтвердите удаление Y/N: ")
    if valid == 'Y':
        with open(path, 'w', newline='') as csv_file:
            fieldnames = phone_book[0].keys()
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            phone_book.pop(contact)
            for row in phone_book:
                writer.writerow(row)
                print(row)
    else:
        print('контакт для удаления не выбран')


def main():
    while True:
        print("q - выход\n" + "r - чтение данных\n" + "a - добавить данные\n"
              + "f - поиск данных\n"+"c - изменить данные\n"+"d - удалить данные\n")
        command = input('Введите команду: ')
        if command == 'q':
            print("Пограмма завершена")
            break
# п.1 Задачи (вывод информации)
        elif command == 'r':
            if not exists(path):
                print('Файл не создан')
                break
            print(*read_file(path))
# п.2 Задачи (добавление новых записей)
        elif command == 'a':
            if not exists(path):
                create_file()
                record_info()
            else:
                record_info()
# п.3 Задачи (поиск инфорации)
        elif command == 'f':
            if not exists(path):
                print('Файл не создан')
                break
            else:
                print(find_file(path))

# п.4 Задачи (изменение информации)
        elif command == 'c':
            if not exists(path):
                print('Файл не создан')
                break
            else:
                contact = find_for_change_file(path)
                print(change_file(path, contact))

# п.5 Задачи (удаление информации)
        elif command == 'd':
            if not exists(path):
                print('Файл не создан')
                break
            else:
                contact = find_for_change_file(path)
                print(delete_file(path, contact))


main()