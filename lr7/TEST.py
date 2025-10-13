import json
b = [{"asd":"das", "ad":"das"}]
with open (r"C:\Users\KudlaIva_89\Desktop\Лабы Кудлаш\lr7\task3\dump.json", "w",encoding = "UTF-8") as json_file:
    json.dump(b, json_file, indent=4)