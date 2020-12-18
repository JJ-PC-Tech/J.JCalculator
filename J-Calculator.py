def calculate():
    operation = input('''
Please Type The Math operation you would like to perform
+ for Addition
- for Subtraction
* for Multiplication
/ for Division
''')

    number_1 = float(input('Please Enter The First Number :'))
    number_2 = float(input('Please Enter The Second Number :'))

    if operation == '+':
        print('{} + {} = '. format(number_1, number_2))
        print(number_1 + number_2)

    elif operation == '-':
        print('{} - {} = '. format(number_1, number_2))
        print(number_1 - number_2)

    elif operation == '*':
        print('{} * {} = '. format(number_1, number_2))
        print(number_1 * number_2)

    elif operation == '/':
        print('{} / {} = '. format(number_1, number_2))
        print(number_1 / number_2)

    else:
        print("You Have Entered a Wrong Mathematical Operation!")
    again()

def again():
    calculation_again = input('''
Do you Want to calculate Again ?
Please Type Y for Yes and N for No
''')

    if calculation_again.upper() == 'Y':
        calculate()

    elif calculation_again.upper() == 'N':
        print("Bye Bye Thank You For Coming, Do Visit Again")

    else:
        again()


calculate()
    
