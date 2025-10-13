import json
a = {"key":"men"}
with open (r"C:\Users\KudlaIva_89\Desktop\Лабы Кудлаш\lr7\task3\dump.json", "w",encoding = "UTF-8") as json_file:
    json.dump(a, json_file, indent=4)
with open (r"C:\Users\KudlaIva_89\Desktop\Лабы Кудлаш\lr7\task3\dump.json", "r",encoding = "UTF-8") as jsole:
    b = json.load(jsole)
print(b["key"])