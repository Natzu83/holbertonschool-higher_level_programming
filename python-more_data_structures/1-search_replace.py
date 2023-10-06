#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    for l in range(len(my_list)):
        if my_list[l] == search:
            new_list[l] = replace
    return new_list
