import interf
import logic
from datetime import datetime


interface = interf.InterfRU()
notepadArray = []

"""
добавление заметки
"""
# notepadArray.append(logic.addNotes(len(notepadArray), interface))

"""
печать заметки
"""
# print(notepadArray)

"""
сохранение в файл заметки
"""
# logic.saveNotesToFile(notepadArray)

"""
чтение из файла
"""
# notepadArray, flagLoadFile = logic.loadNotesFromFile()

"""
печать всего
"""
# logic.printAllNotes(notepadArray)

"""
печать с и по какой то даты
"""
# logic.printNotes(notepadArray, datetime.strptime(("2023-07-21 22:07:54")[:19], '%Y-%m-%d %H:%M:%S'), datetime.strptime(("2023-07-21 22:07:54")[:19], '%Y-%m-%d %H:%M:%S'))

"""
редактирование заметки
"""
# notepadArray = logic.editNotes(notepadArray, interface)

"""
Удаление заметки
"""
# logic.deletNotes(notepadArray, interface)

notepadArray, flagLoadFile = logic.loadNotesFromFile(notepadArray)


flagStop = False
while not flagStop:
    interface.choice()
    try:
        number = int(input())
    except Exception:
        interface.noInputInt
        continue
    if number == 1:
        logic.saveNotesToFile(notepadArray)
        continue
    elif number == 2:
        logic.printAllNotes(notepadArray)
        continue
    elif number == 3:
        notepadArray.append(logic.addNotes(notepadArray, interface))
        continue
    elif number == 4:
        notepadArray = logic.editNotes(notepadArray, interface)
        continue
    elif number == 5:
        notepadArray = logic.deletNotes(notepadArray, interface)
        continue
    elif number == 6:
        interface.inputDate()
        a = input()
        interface.inputDate()
        b = input()
        logic.printNotes(notepadArray, a, b)
        continue
    elif number == 7:
        flagStop = True
        break