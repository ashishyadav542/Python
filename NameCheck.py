name=input('Enter name: ')
if len(name)<3:
    print("Name must be atleast 3 characters long")
elif len(name)>50:
    print("Name must must not be more than 50 characters long")
    print("Enter correct name")
else:
    print("Name is good")
