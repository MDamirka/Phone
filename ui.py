from delete_data import delete_row
from change_data import change_row
from add_data import add_row
from print_data import print_file


def check_number(n):
    while n < 1 or n > 5:
        n = int(input("Ошибка, такого номера команды не "
                      "существует! Введите цифру от 1 до 5\n"
                      "Выберите функцию:\n"
                      "1. Добавить в справочник\n"
                      "2. Удалить из справочника\n"
                      "3. Изменить запись в справочнике\n"
                      "4. Вывод справочника\n"
                      "5. Выход\n"
                      "Введите номер команды: "))
    return n


def start_menu():
    command = None
    while command != 5:
        command = int(input("Доброго времени суток!\n"
                            "Выберите функцию:\n"
                            "1. Добавить в справочник\n"
                            "2. Удалить из справочника\n"
                            "3. Изменить запись в справочнике\n"
                            "4. Вывод справочника\n"
                            "5. Выход\n"
                            "Введите номер команды: "))
        command = check_number(command)
        if command == 1:
            add_row()
        elif command == 2:
            delete_row()
        elif command == 3:
            change_row()
        elif command == 4:
            print_file()
    print("Спасибо, что воспользовались нашим справочником!\n"
          "Всего хорошего! Заходите к нам еще :)")