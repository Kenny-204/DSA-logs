nums = [20, 100, 10, 12, 5, 13]


def increasing_triplet_subsequence(nums):
    first = float('inf')
    second = float('inf')

    for i in range(len(nums)):
        
        if nums[i] <= first:
            first = nums[i]
        elif nums[i] <= second:
            second = nums[i]
        
        elif  nums[i] > second:
            return True
    return False
        

    # while right < len(nums):
    #     if nums[left] < nums[middle] < nums[right]:
    #         return True
    #     else:
    #         left += 1
    #         middle += 1
    #         right += 1
    # return False


print(increasing_triplet_subsequence(nums))
