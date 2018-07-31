def partition(list, left, right):
    pivot = list[0]
    left = left
    leftMark = left+1
    rightMark = right
    while True:
        while leftMark < right and list[leftMark]<pivot:
            leftMark += 1
        while rightMark > left and list[rightMark]>pivot:
            rightMark -= 1
        if leftMark>=rightMark:
            break
        else:
            temp = list[rightMark]
            list[rightMark] = list[leftMark]
            list[leftMark] = temp

    return rightMark

def quickSelect(list, left, right, k):
    split = partition(list,left,right)
    length = split-left+1
    if split == k:
        return k
    if k > split:
        return quickSelect(list,split+1,len(list)-1,k-length)
    else:
        return quickSelect(list,0,k,k)


def partition(list):
    pivot = list[0]
    left = 0
    leftMark = left+1
    right = len(list)-1
    rightMark = right
    while True:
        while leftMark < right and list[leftMark]<pivot:
            leftMark += 1
        while rightMark > left and list[rightMark]>pivot:
            rightMark -= 1
        if leftMark>=rightMark:
            break
        else:
            temp = list[rightMark]
            list[rightMark] = list[leftMark]
            list[leftMark] = temp

    temp = list[left]
    list[left] = list[rightMark]
    list[rightMark] = temp
    return {list[left:]}

def quickSmallest(list, k):
    listLeft = partition(list)


if __name__ == '__main__':
    print(quickSelect([5,3,6,2,4,1],0,5,3))