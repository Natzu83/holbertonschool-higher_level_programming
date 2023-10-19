#!/usr/bin/python3
class MyList(list):
    def print_sorted(self):
        sorted_list = sorted(self)  # Create a sorted copy of the list
        print(sorted_list)

# Example usage:
my_list = MyList([5, 1, 3, 2, 4])
my_list.print_sorted()
