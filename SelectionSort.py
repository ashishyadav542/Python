def sort(nums):

    for i in range(len(nums)):
        minpos = i
        for j in range(i,len(nums)):
            if nums[j] < nums[minpos]:
                minpos = j


        nums[i],nums[minpos]=nums[minpos],nums[i]
        #temp = nums[i]
        #nums[i] = nums[minpos]
        #nums[minpos] = temp


nums = [6, 4, 5, 7, 3, 2]
sort(nums)

print(nums)