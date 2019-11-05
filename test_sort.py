from count_time import count_time
import random
from bubble_sort import bubble_sort
from select_sort import select_sort
from insertion_sort import insertion_sort
from quick_sort import quick_sort
from key_binary_tree_sort import key_binary_tree_sort
from merge_sort import merge_sort

if __name__ == "__main__":
    l = []
    n = 2000
    for x in range(n):
        l.append(random.randint(0,99))
    def cp(l):
        cp_l = []
        for x in l:
            cp_l.append(x)
        return cp_l
    def show(rst):
        do = 1 if n <= 30 else 0 
        if do:
            print(rst)

    show(count_time(bubble_sort)(cp(l)))
    show(count_time(select_sort)(cp(l)))
    show(count_time(insertion_sort)(cp(l)))
    show(count_time(quick_sort)(cp(l)))
    show(count_time(key_binary_tree_sort)(cp(l)))
    show(count_time(merge_sort)(cp(l)))
