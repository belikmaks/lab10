#Бєлік Максим КН-32
#Функція відкриття файлу
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
     file_name_w.write("Чи є мова Python інтерпретованою?\n")
     file_name_w.close()
     print(f"Файл {file_name} закрито.")

#Баранова Софія КН-31
#Відкриття файлу
file_name_a = openFile("Python.txt", "a")

#Запис у файл
if file_name_a is not None:
     file_name_a.write("Баранова Софія КН-31\n")
     file_name_a.write("Python - інтерпретована мова. Інтерпретатор Python читає вихідний код і перетворює його в байт-код, який потім рядок за рядком виконується віртуальною машиною Python.\n")
     file_name_a.write("Які основні характеристики списків у мові Python?\n")
     file_name_a.close()
     print(f"Файл {file_name} закрито.")
