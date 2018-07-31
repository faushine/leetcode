def nextGreatestLetter(letters, target):
    start = 0
    end = len(letters)-1
    if target >= letters[end] or target < letters[start]:
        return letters[start]

    while(start + 1 < end):
        mid = int((start+end)/2)
        if letters[mid] >= target:
            end = mid
        if letters[mid] <= target:
            start = mid

    while(letters[start] == target):
        start = start+1

    if letters[start-1] == target:
        return letters[start]

    return letters[end]

if __name__ == '__main__':
    print(nextGreatestLetter(["c", "f", "j"],"d"))