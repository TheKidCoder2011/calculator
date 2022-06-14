Num1 = int(input('Enter the first number: '))
Num2 = int(input('Enter the second number: '))

print('1 = +, 2 = -, 3 = *, 4 = /')
symbol = int(input('Enter the symbol: '))

def add(x, y):
    print(x + y)

def sub(x, y):
    print(x - y)

def multiply(x, y):
    print(x * y)

def div(x, y):
    print(x / y)

if symbol == 1:
    add(Num1, Num2)

if symbol == 2:
    sub(Num1, Num2)

if symbol == 3:
    multiply(Num1, Num2)

if symbol == 4:
    div(Num1, Num2)