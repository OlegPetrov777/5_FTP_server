import shutil
import os

class System:

    def __init__(self, way):
        self.way = way


    def main(self, command):

        if command == "help":
            return """
                "ls": "Вывод содержимого текущей папки на экран",
                "mkdir": "Создание папки",
                "rmdir": "Удаление папки",
                "remove": "Удаление файла",
                "rename": "Переименовать файл/папку",
                "exit": "Отключение от сервера",
                "stop": "Выключение сервера"
        """

        elif command == 'ls':
            try:
                directs = os.listdir(self.way)
                return str(directs)[1:-1]
            except FileNotFoundError:
                return "File not found"
            except NotADirectoryError:
                return "Directory not found"

        elif command[:5] == 'mkdir':
            try:
                os.mkdir(self.way + '\\' + command[6:])
                return "Ok"
            except OSError:
                return "Error"

        elif command[:5] == 'rmdir':
            try:
                shutil.rmtree(self.way + '\\' + command[6:], ignore_errors=False)
                return "Ok"
            except FileNotFoundError:
                return "Error"
            except OSError:
                return "Error"

        elif command[:6] == 'remove':
            try:
                os.remove(self.way + '\\' + command[7:])
                return "Ok"
            except FileNotFoundError:
                return "Error"
            except OSError:
                return "Error"

        elif command[:6] == 'rename':
            rename_objects = command.split(' ')
            try:
                os.rename(self.way + '\\' + rename_objects[1], self.way + '\\' + rename_objects[2])
                return "Ok"
            except FileNotFoundError:
                return "Error"
            except IndexError:
                return "Error"
            except OSError:
                return "Error"

        else:
            return "None"



    def setWay(self, way):
        # кривой способ проверить существование директории
        # но рабочий)
        try:
            os.listdir(way)
            check = True
        except FileNotFoundError:
            check = False
        except NotADirectoryError:
            check = False
        except OSError:
            check = False

        if check:
            self.way = way
            return f"Home directory saved: {self.way}"
        else:
            return f"Not found directory: {way} \nTry again!"
