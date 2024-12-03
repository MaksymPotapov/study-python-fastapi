import calculator


print('---------------------------------\n\tWelcome to the calculator\n---------------------------------')
first_number = int(input('Please, type the first number: '))
second_number = int(input('Please, type the second number: '))
operation = int(input('Choose the operation: sum[1], subtract[2], multiply[3], divide[4]: '))

if operation == 1: result = calculator.add(first_number, second_number)
elif operation == 2: result = calculator.subtract(first_number, second_number)
elif operation == 3: result = calculator.multiply(first_number, second_number)
elif operation == 4: result = calculator.divide(first_number, second_number)

print(f'The result is: {result}') if result else 0
