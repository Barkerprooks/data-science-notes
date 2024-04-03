def sum2(nums):
    if len(nums) == 0:
        return 0

    if len(nums) == 1:
        return nums[0]
    
    a = nums[0]
    b = nums[1]
    return a + b


def middle_way(a, b):
    # 1. a and b are both of length 3
    #    return a NEW array containing
    #    their middle elements
    x = a[1]
    y = b[1]

    return [x, y]

print(middle_way([1, 2, 3], [4, 5, 6]))
print(middle_way([4, 5, 2], [7, 7, 7]))
print(middle_way([9, 8, 7], [3, 2, 1]))