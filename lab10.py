#Функція відкриття файлов
def openFile(file_name, mode):
    try:
        file = open(file_name, mode)
    except:
        print("Файл", file_name, "не відкрився")
        return None;
    else:
        print("Файл", file_name, "відкрився")
        return file

file_name = "Python.txt"

#Відкриття файлу
file_name_w = openFile("Python.txt", "w")

#Запис у файл
if file_name_w is not None:
     file_name_w.write("Бєлік Максим КН-32\n")
     file_name_w.write("Чи є мова Python інтерпретованою?")
     file_name_w.close()
     print(f"Файл {file_name} закрито.")