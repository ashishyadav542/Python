pos = -1

def search(nums,n):
    lowerBound=0
    upperBound=len(nums)-1

    while lowerBound<=upperBound:
        mid=(lowerBound+upperBound)// 2

        if nums[mid]==n:
            globals() ['pos'] =mid
            return True
        else:
            if nums[mid]<n:
                lowerBound=mid+1
            else:
                upperBound=mid-1
    return False

nums = [10,21,32,43,50,65,76,88,94]
numbertoSearch=44
if search(nums,numbertoSearch):
    print("Found at position",pos)
else:
    print("Not Found")