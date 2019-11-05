def merge_sort(list_, key=None, reverse=None):

    def merge(head, tail):
        if head >= tail:
            return
        mid = (head + tail) // 2
        merge(head, mid)
        merge(mid + 1, tail)

        temp = []
        left = list_[head: mid + 1][:]
        right = list_[mid + 1: tail + 1][:]
        
        while left and right:
            obj = 'left' if left[0] <= right[0] else 'right'
            temp.append(eval(obj).pop(0))
        temp += left + right

        list_[head: tail + 1] = temp
    merge(0, len(list_) + 1)
    return list_


if __name__ == '__main__':
    l1 = [1,5,9,10,11]
    l2 = [0,2,4,7]
    l = []
    i, j = 0,0
    while l1 and l2:
        obj = 'l1' if l1[0] <= l2[0] else 'l2'
        l.append(eval(obj).pop(0))
    l += (l1 + l2)
    print(l)
