#!/usr/bin/python3
"""
Write a script that adds all arguments to a
    Python list, and then save them to a file:
"""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


try:
        existing_data = load_from_json_file('add_item.json')
except:
    existing_data = []

new_items = sys.argv[1:]
updated_data = existing_data + new_items

# for i in range(1, len(sys.argv)):
#     existing_data.append(sys.argv[i])

save_to_json_file(updated_data, 'add_item.json')
# save_to_json_file(existing_data, 'add_item.json')
