
file_1 = 'data_second_variant.csv'
file_2 = 'data_copy_variant.csv'

def input_user_data():
    name = input("Введите имя: ")
    surname = input("Введите фамилия: ")
    phone = input("Введите телефон: ")
    adress = input("Введите адрес: ")
    return name, surname, phone, adress
    

def input_data(file_1):
    name, surname, phone, adress = input_user_data ()
    with open(file_1, 'a', encoding='utf-8') as file:
        file.write(f'{name};{surname};{phone};{adress}\n')
            
def read_file(file_1):
    contacts = []
    with open(file_1, 'r', encoding='utf-8') as file:
        for line in file:
            contact_data = line.strip().split(',')
            contacts.append(tuple(contact_data))
    return contacts   
        
def print_data(file_1,file_2):
    print('файл:')
    with open(file_1, 'r', encoding='utf-8') as file_1:
        data = file_1.readlines()
        print(''.join(data))
        
    print('скопированные файлы')
    with open(file_2, 'r', encoding='utf-8') as file_2:
        data_2 = file_2.readlines()
        print(''.join(data_2))
        
def copy_data(file_1, file_2):
    with open(file_1, 'r', encoding='utf-8') as file_1:
        lines = file_1.readlines()
        print(lines)
        y = int(input(f"Выберите номер строки c 1 по {len(lines)}: "))
        contact_data = lines[y - 1]
        print(contact_data)
        with open(file_2, 'a') as file_2:
            file_2.write(contact_data + '\n')


def interface():
    print('Добрый день! Это бот-помощник. \n'
          'Что вы хотите сделать? \n'
          '1 - Записать данные \n'
          '2 - Скопировать данные \n'
          '3 - Вывести даные')
    command = int(input('Ваш выбор: '))

    while command < 1 or command > 3:
        command = int(input('Ошибка! Ваш выбор: '))

    if command == 1:
        input_data(file_1)
    elif command == 2:
        copy_data(file_1, file_2)
    elif command == 3:
        print_data(file_1,file_2)
        

interface()