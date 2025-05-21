from functools import reduce

nums = [1, 2, 3, 4]


# def productOfArrayExceptSelf(nums):
#     output = []
#     for i in range(len(nums)):
#         trim = nums[:i] + nums[i + 1 :]
#         result = reduce(lambda x, y: x * y, trim)
#         output.append(result)
#     return output


def productOfArrayExceptSelf(nums):
    output = []
    pre = 1
    post = 1
    for i in range(len(nums)):
        if i == 0:
            output.append(pre)
        else:
            pre *= nums[i - 1]
            output.append(pre)
    for i in reversed(range(len(nums))):
        if i == len(nums) - 1:
            output[i] *= 1
        else:
            post *= nums[i + 1]
            output[i] *= post
    return output


print(productOfArrayExceptSelf(nums))
