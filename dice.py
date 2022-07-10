import random
while True:
    print('''1. Roll the dice 2.To exit ''')
    user = int(input("What you want to do \n"))
    if user==1:
        number = random.randint(1,6)
        print("The rolled dice number = ", number)
    else:
        break
