#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    '''Print x elements ofa a list.
    Args:
        my_list(list): the list to print elements from.
        x(int): The number of elements of my_lists to print.
    Returns:
       The number of elements printed.
    '''

    ret = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            ret += 1
        except IndexError:
            break
    print("")
    return (ret)
