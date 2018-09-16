def search(nums, target):
    if not nums: return False
    left = 0
    right = len(nums)-1
    for i in range(0,len(nums)-1):
        if nums[i]>nums[i+1]:
            if nums[left] <= target and nums[i] >= target:
                right = i
                break
            if nums[i+1] <= target and nums[right] >= target:
                left = i+1
                break
    while right >= left:
        mid = int((left+(right-left)/2))
        if nums[mid] > target:
            right = mid-1
        if nums[mid] < target:
            left = mid+1
        if nums[mid] == target:
            return True
    return False




if __name__ == '__main__':
    print(search([3,3],3))