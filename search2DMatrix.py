def search(matrix, target):
    if not matrix:
        return False
    if not matrix[0]:
        return False
    n = len(matrix)
    m = len(matrix[0])
    left = 0
    right = n * m - 1
    while right >= left:
        mid = int((left+(right-left)/2))
        x = int(mid/m)
        y = mid - x*m
        if matrix[x][y] > target:
            right = mid-1
        if matrix[x][y] < target:
            left = mid+1
        if matrix[x][y] == target:
            return True
    return False

if __name__ == '__main__':
    print(search([[1,3,5,7],[10,11,16,20],[23,30,34,50]],50))