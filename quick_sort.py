def quick_sort(list_, key=lambda x: x, reverse=False):
    value = lambda index: key(list_[index])
    def binary_sort(start, end):
        if start >= end:
            return
        head, tail = start, end
        no_change = lambda : (value(head) <= value(tail)) ^ reverse
        while head < tail:
            while head < tail and no_change():
                tail -= 1
            list_[head], list_[tail] = list_[tail], list_[head]
            while head < tail and no_change():
                head += 1
            list_[head], list_[tail] = list_[tail], list_[head]
        # 无需再拍head/tail项
        binary_sort(start, head - 1)
        binary_sort(head + 1, end)
    binary_sort(0, len(list_) - 1)
    return list_
        

