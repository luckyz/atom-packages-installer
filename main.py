#!/usr/bin/env python3
import json
from os import system, path
import os
import tkinter as tk
from tkinter import filedialog

DEFAULT_DIR = "/Users/lucas/Documents/develop/atom/atom-config/packages.json"
FILEOPENOPTIONS = (("JSON files", "*.json"), ("All files", "*.*"))

root = tk.Tk()
root.withdraw()
FILE_INPUT = filedialog.askopenfilename(initialdir=DEFAULT_DIR, title="Select file", filetypes=FILEOPENOPTIONS)

with open(FILE_INPUT, "r") as json_file:
    dir_path = os.path.dirname(json_file.name)
    source = json.load(json_file)
    packages = []
    for index in range(len(source)):
        package_name = source[index]["name"]
        packages.append(package_name)
json_file.close()

system("apm install {}".format(" ".join(packages)))
