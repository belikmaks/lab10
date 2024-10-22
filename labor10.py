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
#Чернявська Анна КН-32/2
#Відкриття файлу
file_name_a = openFile("Python.txt", "a")
#Запис у файл
if file_name_a is not None:
     file_name_a.write("\nЧернявська Анна КН-32/2\n")
     file_name_a.write("Відповідь: Списки в Python — це змінні, впорядковані колекції елементів, які можуть містити дані різних типів. Вони підтримують індексацію, вкладеність, зміну елементів, мають динамічний розмір та дозволяють використовувати різні методи для маніпуляції, такі як додавання, видалення й сортування елементів.\n")
     file_name_a.write("Запитання наступному: Як у Python визначити кількість ключів у словнику?\n")
     file_name_a.close()
     print(f"Файл {file_name} закрито.")
#Куцевол Аліса КН-32\1
#Відкриття файлу
file_name_a = openFile("Python.txt", "a")
#Запис у файл
if file_name_a is not None:
     file_name_a.write("\nКуцевол Аліса КН-32\n")
     file_name_a.write("Відповідь: Для того, щоб на мові Python визначити кількість ключів у словнику зазвичай використовують функцію len(), яка повертає кількість ключів словника, назву якого буде записано в дужках\n")
     file_name_a.write("Питання: Що означає динамічна типізація в Python?\n")
     file_name_a.close()
     print(f"Файл {file_name} закрито.")