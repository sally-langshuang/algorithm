def insertion_sort(list_, key=lambda x: x, reverse=False):
    n = len(list_)
    value = lambda index: key(list_[index])
    for i in range(1, n):
        for j in range(i)[::-1]:
            if (value(j) < value(j + 1)) is reverse:
                list_[j], list_[j + 1] = list_[j + 1], list_[j]
            else:
                break
    return list_
