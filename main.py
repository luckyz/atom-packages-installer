import json
from os import system

#system("sudo -s")
archivo = open("output.txt", "w")
with open(r"C:\Users\lzurverra\Desktop\packages.txt", "r") as json_file:
    data = json.load(json_file)
    for p in data:
        package = p["name"]
        archivo.write(package + "\n")

archivo.close()
