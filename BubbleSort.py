def sort(nums):
    for i in range(len(nums)-1,0,-1):
        for j in range(i):
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1]=nums[j+1],nums[j]
                #temp=nums[j]
                #nums[j]=nums[j+1]
                #nums[j+1]=temp

nums=[60,50,40,30,20,10,0]
sort(nums)

print(nums)
