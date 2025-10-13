import json
cod = input("введите искомый код професси: ")
with open(r"C:\Users\KudlaIva_89\Desktop\Лабы Кудлаш\lr7\task2\dump.json", "r",encoding = "UTF-8") as json_file:#обращаемся к файлу
    a = json.load(json_file)
for i in a:
    if(i["model"]) == "data.specialty":
        if cod in (i["fields"]["code"]):
            print("================найденно================")
            print(i["fields"]["code"], ">> Cпециальность ",i["fields"]["title"],",",i["fields"]["c_type"])
            print("")
            d = 1
    

if d != 1:
    print("================не найденно================")
