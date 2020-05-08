names = []
for count in range(10):
    name = input("Enter name: ")
    names.append(name)
print(names)

def lenName(names):
    bigName=0
    smallName=0
    for name in names:
        if len(name)>5:
            bigName+=1
        else:
            smallName+=1
    print(f"Total Bigname is: {bigName} and Small Name is : {smallName}") #Formatted Print
    print("Total Bigname is: {} and Small Name is : {}".format(bigName,smallName)) #String function
lenName(names)
