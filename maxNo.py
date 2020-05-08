numbers=[2,34,5,355,66,100,4,33,32,44,55,434]
max=numbers[0]
for large_no in numbers:
    if large_no>max:
        second_max=max
        max=large_no
print(f"Max number is {max}")
print(f"Secon Max number is {second_max}")

#######Sorting##########
print('')
numbers.sort()
print(f"Max number is {numbers[-1]}")
print(f"Secon Max number is {numbers[-2]}")
