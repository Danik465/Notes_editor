
import functions
import re


print("Здравствуйте, вас приветствует редактор заметок\nВведите необходимое действие: \n"
      "Для просмотра доступных функций введите команду 'help' ")

notes_table = []
command = input()
while True:
    if command == 'add':
        data = functions.add()
        notes_table.append(data)
        data = str(data).strip("[").strip("]")
        save = input('Сохранить заметку в файл? y/n\n ')
        if save == 'y':
            functions.save(data)
            ques = input('Хотите продолжить? y/n\n')
            if ques == 'y':
                command = input("Введите следующее действие:\n")
            else:
                break
        elif save == 'n':
            ques = input('Хотите продолжить? y/n\n')
            if ques == 'y':
                command = input("Введите следующее действие:\n")
            else: break
    elif command == 'help':
        functions.help()
    elif command == 'read':
        data = int(input("Какую заметку вы хотите прочитать? Введите номер заметки:\n"))
        functions.read(data)
        ques = input('Хотите продолжить? y/n\n')
        if ques == 'y':
            command = input("Введите следующее действие:\n")
        else:
            break
    elif command == 'del':
        number = input("Какую заметку вы ходите удалить? Напишите номер:")
        functions.delete(number)
        ques = input('Хотите продолжить? y/n\n')
        if ques == 'y':
            command = input("Введите следующее действие:\n")
        else:
            break

    elif command == 'red':
        number = int(input("Какую заметку вы ходите отредактировать? Напишите номер:"))
        functions.redact(number)
        ques = input('Хотите продолжить? y/n\n')
        if ques == 'y':
            command = input("Введите следующее действие:\n")
        else:
            break

