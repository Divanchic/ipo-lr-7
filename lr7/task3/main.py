#Кудлаш Иван
import json
x=1#вводим переменную с помощью которой будет проходить цикл
while x!=0:
     # Меню
print(">>  Вывод записей << - 1")
print(">>  Вывод записи по полю << - 2")
print(">>  Добавить запись << - 3")
print(">>  Удалить запись по полю << - 4")
print(">>  Выход их программы << - 5")
print(" ")

   
comand = int(input("Выберите пункт(например:1): ")) # Запрашиваем число для вывода пункта меню
if(comand == 0 or comand <= 0 or comand > 5): # Проверяем правльное ли число
    print("Неверное число")
    print(" ")
else:
    match comand: # Исполнение выбранной команды
        case 1:# Считываем файл и выводим его 
            with open("C:\Users\KudlaIva_89\Desktop\Лабы Кудлаш\lr7\task3\dump.json", "r", encoding = "utf-8") as file:
                first = json.load(file) # Запрашиваем данные из файла
                print(json.dumps(first))

        case 2:# Вывести записи по id
            id_for_search = input("Введите id: ") # Запрашиваем id
            with open("C:\Users\KudlaIva_89\Desktop\Лабы Кудлаш\lr7\task3\dump.json", "r", encoding="utf-8") as file:
                second = json.load(file) # Запрашиваем данные из файла
                have_id = False # Вводим переменную для проверки существования id
                for i, j in enumerate(second): # Перебираем данные из файла
                    if str(j.get("id")) == id_for_search:
                        print(json.dumps(j))
                        have_id = True
                        break
                if have_id == False: # Проверяем существует ли файл
                    print("id не найдено")

        case 3: # Добавляем записи
            with open("C:\Users\KudlaIva_89\Desktop\Лабы Кудлаш\lr7\task3\dump.json", "r", encoding="utf-8") as file:
                    third = json.load(file)  # Запрашиваем данные из файла

               
            new_id = int(input("Введите id: ")) # Запрашиваем данные у пользователя
            name = input("Введите общее название звезды: ")
            constellation = input("Введите название созвездия: ")
            is_visible = input("Можно ли увидеть звезду без телескопа?(да/нет): ")
            if is_visible == "да":
                is_vis = True
            else:
                is_vis = False
            radius = float(input("Cолнечный радиус звезды: "))

                
            stars = {# Создаем словарь данных
                "id": new_id,
                "name": name,
                "constellation": constellation,
                "is_visible": is_visible,
                "radius": radius
            }

            if third is None:#Если файл пустой то создаем словарь
                    third = []

            third.append(stars)  # Добавляем словарь в список

            # Сохраняем данные в файл
            with open("C:\Users\KudlaIva_89\Desktop\Лабы Кудлаш\lr7\task3\dump.json", "w", encoding="utf-8") as file:
                json.dump(third)

        case 4:# Удаляем выбранную запись
            id_for_del = input("Введите id для удаления: ") # Запрашиваем id для удаления
            with open("C:\Users\KudlaIva_89\Desktop\Лабы Кудлаш\lr7\task3\dump.json", "r", encoding="utf-8") as file:
                fourth = json.load(file)

                lens = len(fourth)# Считываем длину файла для будущей прверки
                fourth = [star for star in fourth if str(star.get("id")) != id_for_del] # Перебираем список, но без элемента с выбранным id

                if len(fourth) < lens: # Проверяем удалился ли элемент
                    with open("C:\Users\KudlaIva_89\Desktop\Лабы Кудлаш\lr7\task3\dump.json", "w", encoding="utf-8") as file:
                        json.dump(fourth) # Сохраняем изменения
                    print("Запись удалена.")
                else:
                    print("Запись с таким id не найдена.")

        case 5:
            x=0 # Завершаем цикл
