#!/usr/bin/python3

def element_at(my_list, idx):
    """Prints elements at index idx"""
    if idx < 0:
        return None
    if idx > (len(my_list) - 1):
        return None
    else:
        return my_list[idx]
