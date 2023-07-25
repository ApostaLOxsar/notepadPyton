from abc import ABC, abstractmethod

class Interf(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def saveNoteToFile(self):
        pass

    @abstractmethod
    def choice(self):
        pass

    @abstractmethod
    def readNoteToFile(self):
        pass

    @abstractmethod
    def addNote(self):
        pass

    @abstractmethod
    def editNote(self):
        pass

    @abstractmethod
    def deletNote(self):
        pass

    @abstractmethod
    def exitNotepade(self):
        pass

    @abstractmethod
    def errorReadFile(self):
        pass

    @abstractmethod
    def inputTitleForNotes(self):
        pass

    @abstractmethod
    def inputNumberForEdit(self):
        pass

    @abstractmethod
    def noForNoEdit(self):
        pass

    @abstractmethod
    def noEdit(self):
        pass

    @abstractmethod
    def noInputInt(self):
        pass
    @abstractmethod
    def outDateVersion(self):
        pass

    @abstractmethod
    def inputNumberForDelete(self):
        pass

    @abstractmethod
    def noForNoEdit(self):
        pass

    @abstractmethod
    def noForNoDelete(self):
        pass


    @abstractmethod
    def AllOk(self):
        pass


    @abstractmethod
    def inputDate(self):
        pass

class InterfRU(Interf):
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

    def inputTitleForNotes(self):
        print("Введите название заметки")

    def inputContentForNotes(self):
        print("Введите заметку")

    def inputNumberForEdit(self):
        print("Введите номер заметки для изменение")

    def noForNoEdit(self):
        print("Введите no если нет необходимости редактировать")

    def noEdit(self):
        print("Редактирование не удалось, заметка не найдена")

    def noInputInt(self):
        print("Введено не  число")

    def outDateVersion(self):
        print("Преведущая версия:")

    def inputNumberForDelete(self):
        print("Введите номер для удаление")

    def noForNoDelete(self):
        print("Вот вам замеетка \nВведите no если передумали")

    def noForNoDelete(self):
        print("Удаление не удалось, заметка не найдена")
    
    def AllOk(self):
        print("Успешно")

    def choice(self):
        print("1 - сохранить")
        print("2 - прочитать")
        print("3 - добавить")
        print("4 - редактировать")
        print("5 - удалить")
        print("6 - выборка по дате")
        print("7 - выйти")

    def inputDate(self):
        print("Введите дату формата: yyyy-mm-dd hh:mm:ss")
        






class InterfEN(Interf):
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
