

def isPerfectSquare(num):
    start = 0
    end = num
    while(start+1 < end):
        mid = int((start + end) / 2)
        if mid*mid > num :
            end = mid
        if mid*mid < num:
            start = mid
        if mid*mid == num:
            return True

    if start*start == num:
        return True
    if end*end == num:
        return True
    return False


if __name__ == '__main__':
    print(isPerfectSquare(1))