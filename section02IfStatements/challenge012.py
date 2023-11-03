# 012 Ask for two numbers. If the first one is larger than the second, display the second number first and then the first number, otherwise show the first number first and then the second. 

x = int(input('Enter your first number: '))
y = int(input('Enter your second number: '))
if (x>y):
    print(y, x)
else:
    print(x, y)