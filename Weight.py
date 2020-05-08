#############Weight in KG#################
'''
weight_in_lbs = input('Enter your weight in pounds: ')
weight_in_kg = float(weight_in_lbs) * 0.454
print('Weight in Kg is: ' + str(weight_in_kg))
'''
weight=input('Enter your weight: ')
kg_lb = input('weight in lb(l) or in kg(k)')

if kg_lb.upper()=='K':
    weight_lb= int(weight)*2.2
    print("Weight in lbs is " + str(weight_lb))
elif kg_lb.upper()=='L':
    weight_kg= int(weight)*0.45
    print("Weight in kgs is " + str(weight_kg))
else:
    print("Incorrect measure entered")
