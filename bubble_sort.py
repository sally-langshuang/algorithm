def bubble_sort(list_, key=lambda x: x, reverse=False):
    value = lambda x : key(list_[x])
    n = len(list_)
    for i in range(n - 1):
       for j in range(n - 1 - i):
           if (value(j) < value(j + 1)) is reverse:
               list_[j], list_[j + 1] = list_[j + 1], list_[j]
    return list_
