from typing import List

def productExceptSelf(nums):
    n = len(nums)
    result = [1] * n

    left = 1
    for i in range(n):
        result[i] = left
        left *= nums[i]

    right = 1
    for i in range(n - 1, -1, -1):
        result[i] *= right
        right *= nums[i]

    return result


if __name__ == '__main__':
    arr = list(map(int, input().split()))
    print(productExceptSelf(arr))