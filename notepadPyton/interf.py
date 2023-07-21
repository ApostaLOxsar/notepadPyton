class InterfRU:
    def __init__(self):
        print("Выбран русский язык")
    
    def saveNoteToFile(self):
        print("Вы выбрали сохранить заметку")
    
    def readNoteToFile(self):
        print("Вы выбрали прочитать из файла")
    
    def addNote(self):
        print("Вы выбрали добавить заметку")
    
    def editNote(self):
        print("Вы выбрали редактировать заметку")
    
    def deletNote(self):
        print("Вы выбрали удалить заметку")
    
    def exitNotepade(self):
        print("Вы уходите(( Мы ждем вас снова")
    
    def errorReadFile(self):
        print("При чтении файла произошла, вероятно он не существует")
    

class InterfEN:
    def __init__(self):
        print("Selected language: English")
    
    def saveNoteToFile(self):
        print("You chose to save the note.")
    
    def readNoteToFile(self):
        print("You chose to read from the file.")
    
    def addNote(self):
        print("You chose to add a note.")
    
    def editNote(self):
        print("You chose to edit a note.")
    
    def deleteNote(self):
        print("You chose to delete a note.")
    
    def exitNotepad(self):
        print("You are leaving. We hope to see you again.")
    
    def errorReadFile(self):
        print("An error occurred while reading the file. It probably does not exist.")
