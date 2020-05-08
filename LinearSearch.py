'''
def search(nums,n):
    for i in nums:
        if i==n:
           return True
    else:
        return False

nums = [10,21,32,43,50,65,76,68,90]
numbertoSearch=90
if search(nums,numbertoSearch):
    print("Found")
else:
    print("Not Found")
'''
val = [2,1,4,7,3,8,9]

valueTosearch = 7

for i in range(len(val)):
    if val[i] == valueTosearch:
        print("Found the value at position", i+1)
        break
else:
    print("Not Found in the nums")