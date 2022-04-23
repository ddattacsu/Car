a= input('What is your name? ')
a= str(a)
print(f"Hi {a}")
#print(a)
print('''Welcome to the 
1st Professional 
Bathurst
''')
print('The house is only $1M')
b = input('Please input your weekly income ')
b=int(b)

if b>1000:
    print('Congratulation!, You need only 10% down payment')
    print('Enjoy your new house')

elif b<500:
    print('Sorry! You are not suitable to buy a house, better to stay at rent')
    print('Enjoy your rent house')

else:
    print('Congratulation!, You need only 20% down payment')
    print('Enjoy your new house')

print('Thanks for considering 1st professional Bathurst')