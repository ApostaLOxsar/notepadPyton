import interf
import logic
from datetime import datetime


interface = interf.InterfRU()

tempTitl = "temptitle"
note1 = {"numberNotes": 1, "title": tempTitl, "cyrentTime" : str(logic.curenttime()), "editTime": str(logic.curenttime()), "content": "1234124"}
note2 = {"numberNotes": 2, "title": tempTitl, "cyrentTime" : str(logic.curenttime()), "editTime": str(logic.curenttime()), "content": "dfghdfg"}

notepadArray = []
notepadArray.append(note1)
notepadArray.append(note2)


logic.saveNotesToFile(notepadArray)
notepadArray, flagLoadFile = logic.loadNotesFromFile()

#logic.printAllNotes(notepadArray)

#logic.printNotes(notepadArray, datetime.strptime(("2023-07-21 22:07:54")[:19], '%Y-%m-%d %H:%M:%S'), datetime.strptime(("2023-07-21 22:07:54")[:19], '%Y-%m-%d %H:%M:%S'))
