import datetime
count = 1
def add():
    global count
    now ="{:%Y-%m-%d %H:%M:%S}".format(datetime.datetime.now())
    head = input("Введите заголовок заметки:")
    body = input("Введите тело заметки:")
    note = [count, head, body, now ]
    count+=1

    return note


def save(data):
    with open("note.csv", "a", encoding='utf-8') as f:
        f.write(data +'\n')
    return 0


def read(data):
    with open("note.csv", "r", encoding='utf-8') as f:
        lines = f.readlines()
        print(lines[data])

    return 0
def help():
    print('add - добавить заметку\n'
          'delete - удалить заметку\n'
          'read - читать необходимую заметку\n'
          'edite - редактировать заметку')
def delete(number):
    with open("note.csv", "r") as f:
        lines = f.readlines()
    with open("note.csv", "w") as f:
        for line in lines:
            if line.strip("\n") != number:
                f.write(line)


def redact(number):
    with open("note.csv", "r") as f:
        lines = f.readlines()
    with open("note.csv", "a") as f:
        now = "{:%Y-%m-%d %H:%M:%S}".format(datetime.datetime.now())
        head = input("Введите заголовок заметки:")
        body = input("Введите тело заметки:")
        note =   head+ " "  + body+ " "  + now
        lines.insert(number, note)
        f.writelines(lines)
    return 0