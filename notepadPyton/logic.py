from datetime import datetime
import json
import os.path
from tkinter.tix import NoteBook

"""
обрезка милисекунд
return datetime
"""
def curenttime():
    curentDay = datetime.today()
    curentDay = datetime.strptime(str(curentDay)[:19], '%Y-%m-%d %H:%M:%S')
    return curentDay

def saveNotesToFile(notepadArray):
    with open('data.json', 'w') as f:
        json.dump(notepadArray, f, indent='\t')


def loadNotesFromFile(notepadArray):
    try:
        with open('data.json') as f:
            allNotes = json.load(f)
        if os.path.getsize("data.json") == 0:
            return "", False
        return allNotes, True
    except Exception:
        return notepadArray, False

def printNotes(notepadArray, fromtime, beforTime):
    try:
        fromtime = datetime.strptime(fromtime[:19], "%Y-%m-%d %H:%M:%S")
        beforTime = datetime.strptime(beforTime[:19], "%Y-%m-%d %H:%M:%S")
        for i in notepadArray: 
            if fromtime <= datetime.strptime((i["editTime"])[:19], '%Y-%m-%d %H:%M:%S') <= beforTime:
                for j in i:
                    print(j + " : " + str(i[j]))
                print("")
    except Exception:
        print("((")



def printAllNotes(notepadArray):
    count  = 1
    for i in notepadArray:
        print("Number  notes : " + str(count))
        for j in i:
            print(j + " : " + str(i[j]))
        count += 1
        print("")


def addNotes(numberNotes, interface):
    numberNotes  =  len(numberNotes)  + 1
    
    cyrentTime  = editTime  = str(curenttime())
    
    interface.inputTitleForNotes()
    tempTitl = input()

    interface.inputContentForNotes()
    content = input()

    note = {"title": tempTitl, "cyrentTime" : cyrentTime, "editTime": editTime, "content": content}
    return note

def editNotes(arrayNotes, interface):
    interface.inputNumberForEdit()
    try:
        numberNotes = int(input())
    except Exception:
        interface.noInputInt()
        return arrayNotes

    if 0 < numberNotes <= len(arrayNotes):
        interface.inputTitleForNotes()
        interface.noForNoEdit()
        interface.outDateVersion()
        print(arrayNotes[numberNotes - 1]["title"])
        title = input()
        if (title != "no"):
            arrayNotes[numberNotes - 1]["title"] = title

        interface.inputContentForNotes()
        interface.noForNoEdit()
        interface.outDateVersion()
        print(arrayNotes[numberNotes - 1]["content"])
        content = input()
        if content  != "no":
            arrayNotes[numberNotes - 1]["content"]  = content

        arrayNotes[numberNotes - 1]["editTime"] =  str(curenttime())
        interface.AllOk()
    else:
        interface.noEdit()
    return arrayNotes



def deletNotes(arrayNotes, interface):
    interface.inputNumberForDelete()
    try:
        numberNotes = int(input())
    except Exception:
        interface.noInputInt()
        return arrayNotes

    if 0 < numberNotes <= len(arrayNotes):
        arrayNotes.pop(numberNotes - 1)
        interface.AllOk()
        return arrayNotes
    else:
        interface.noForNoDelete()
        return arrayNotes