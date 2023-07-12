#!/usr/bin/python3
"""
Script that adds all arguments to a Python list, and then saves them to a file
"""
import os.path
import sys


save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

arguments = sys.argv[1:]
list = []
filename = "add_item.json"

if os.path.exists(filename):
    list = load_from_json_file(filename)

save_to_json_file(list + arguments, filename)
