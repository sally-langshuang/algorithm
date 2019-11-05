def merge_sort(list_, key=None, reverse=None):
    '''
    # 方法1
    if len(list_) <= 1:
        return list_
    def merge(left,right):
        r, l=0, 0
        result=[]
        while l<len(left) and r<len(right):
            if left[l] <= right[r]:
                result.append(left[l])
                l += 1
            else:
                result.append(right[r])
                r += 1
        result += list(left[l:])
        result += list(right[r:])
        return result
    num = int( len(list_) / 2 )
    left = merge_sort(list_[:num])
    right = merge_sort(list_[num:])
    return merge(left, right)
    '''
    # 方法2
    def merge(head, tail):
        if head >= tail:
            return
        mid = (head + tail) // 2
        merge(head, mid)
        merge(mid + 1, tail)

        temp = []
        left = list_[head: mid + 1]
        right = list_[mid + 1: tail + 1]
        
        # eval 效率不高
        # while left and right:
            #obj = 'left' if left[0] <= right[0] else 'right'
            #temp.append(eval(obj).pop(0))
            
        while left and right:
            if left[0] <= right[0]:
                temp.append(left.pop(0))
            else:
                temp.append(right.pop(0))
        temp += left + right

        list_[head: tail + 1] = temp
    merge(0, len(list_) + 1)
    return list_


if __name__ == '__main__':
    pass
