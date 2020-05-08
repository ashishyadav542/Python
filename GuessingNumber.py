secret_no = 9
no_of_chances=0
while no_of_chances < 3:
    no_of_chances+=1
    guess_no = int(input('Guess: '))
    if guess_no==secret_no:
        print('You win')
        break
else:
    print('Max chances')
        
