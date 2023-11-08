print('Welcome to the temperature converter')
temp = int(input('What is the temperature? '))
m = input('What would you like to convert to (Fahrenheit(F), Celsius(C)').upper()

if m == 'F':
    print(temp * 1.8 + 32)
elif m == 'C':
    print((temp - 32) * .5556)
else:
    print('Enter a valid measurement')

