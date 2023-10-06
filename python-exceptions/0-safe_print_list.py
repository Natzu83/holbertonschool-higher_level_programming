#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    a = 0
    while True:
        try:
            while a != x:
                print("{}".format(my_list[a]), end="")
                a += 1
        except Exception as e:
            pass
        finally:
            print()
            return a
