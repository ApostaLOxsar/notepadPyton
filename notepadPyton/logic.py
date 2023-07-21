from datetime import datetime
import json
import os.path

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


def loadNotesFromFile():
    try:
        with open('data.json') as f:
            allNotes = json.load(f)
        if os.path.getsize("data.json") == 0:
            return "", False
        return allNotes, True
    except FileNotFoundError:
        return "", False

def printNotes(notepadArray, fromtime, beforTime):
    for i in notepadArray:
        if fromtime <= datetime.strptime((i["editTime"])[:19], '%Y-%m-%d %H:%M:%S') <= beforTime:
            for j in i:
                print(j + " : " + str(i[j]))
            print("")



def printAllNotes(notepadArray):
    for i in notepadArray:
        for j in i:
            print(j + " : " + str(i[j]))
        print("")