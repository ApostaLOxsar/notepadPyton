import interf
import logic
from datetime import datetime


interface = interf.InterfRU()
notepadArray = []



"""
добавление заметки
"""
#notepadArray.append(logic.addNotes(len(notepadArray), interface))

"""
печать заметки
"""
#print(notepadArray)

"""
сохранение в файл заметки
"""
#logic.saveNotesToFile(notepadArray)

"""
чтение из файла
"""
#notepadArray, flagLoadFile = logic.loadNotesFromFile()

"""
печать всего
"""
#logic.printAllNotes(notepadArray)

"""
печать с и по какой то даты
"""
#logic.printNotes(notepadArray, datetime.strptime(("2023-07-21 22:07:54")[:19], '%Y-%m-%d %H:%M:%S'), datetime.strptime(("2023-07-21 22:07:54")[:19], '%Y-%m-%d %H:%M:%S'))

"""
редактирование заметки
"""
#notepadArray = logic.editNotes(notepadArray, interface)

"""
Удаление заметки
"""
#logic.deletNotes(notepadArray, interface)
