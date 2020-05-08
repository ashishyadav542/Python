# def factorial(number):
#     f=0   ###0!=1
#     if number==0:
#         pass
#     else:
#         for i in range(1,number+1):
#             f=f*i
#     return f
#
# print(factorial(int(input("Enter the Factorial: "))))

###############Recursion###################

def factorial(number):
    if number==0:
        return 1
    return number*factorial(number-1)

print(factorial(int(input("Enter the Factorial: "))))