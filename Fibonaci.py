#Fibonaci is 0 1 1 2 3 5 8...

def fibonaci(count):
    firstNum = 0
    secondNum = 1
    if(count<=0):
        print("Invalid Count")
    elif(count==1):
        print(firstNum)
    elif(count==2):
        print(firstNum)
        print(secondNum)
    else:
        print(firstNum)
        print(secondNum)
        for no in range(2,count):
            nextNum=firstNum+secondNum
            print(nextNum)
            firstNum,secondNum=secondNum,nextNum

fibonaci(int(input("Enter the count of Fibonacci: ")))