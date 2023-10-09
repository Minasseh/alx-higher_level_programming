##!/usr/bin/python3

def element_at(my_list, idx):
    """Prints elements at index idx"""

    for idx in range(len(my_list)):
        if idx < 0:
            return
        if idx > (len(my_list)):
            return
        else:
            print("Element at index {:d} is {:d}".format(idx, my_list[idx]))
