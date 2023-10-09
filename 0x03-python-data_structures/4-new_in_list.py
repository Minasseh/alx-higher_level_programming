#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """Print new in the list"""

    copy = my_list.copy()
    if idx < 0 or idx > len(my_list) - 1:
        return my_list.copy()
    else:
        copy[idx] = element
        return copy
