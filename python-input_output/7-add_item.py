#!/usr/bin/python3
"""
   Add the item 
"""
import sys
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

filename = "add_item.json"
current_list = []

if len(sys.argv) == 1:
        save_to_json_file(current_list, filename)
else:
    try:
        current_list = load_from_json_file(filename)
    except FileNotFoundError:
        pass
    finally:
        args = sys.argv[1:]
        for i in args:
            current_list.append(i)
        save_to_json_file(current_list, filename)
