def select_sort(list_, key=lambda x: x, reverse=False):
    value = lambda x : key(list_[x])
    n = len(list_)
    for i in range(n - 1):
       for j in range(i + 1, n):
           if (value(i) > value(j)) ^ reverse:
               list_[i], list_[j] = list_[j], list_[i]
    return list_
