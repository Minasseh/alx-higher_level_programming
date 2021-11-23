#!usr/bin/python3
def no_c(my_string):
    """Remove all characters c and C from a string."""
    for x in my_string:
    if x != 'c' and x != 'C':
        del x
    return my_string 
