from numpy import *

vals1 = array([1,2,4,3,5,7,6])
vals2 = array([16,9,20,12,13,16,14])
vals3 = empty(7)

for i in range(len(vals1)):
    vals3[i]=vals1[i]+vals2[i]


print(vals3)
#print("The sorted array:", sorted(vals3))
#print("The max number is:", vals3[-1])

max = vals3[0]
for m in vals3:
    if (max<m):
        max=m

print("The max number is:", max)