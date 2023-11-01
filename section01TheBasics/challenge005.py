# 005 Ask the user to enter three numbers. Add together the first two numbers and then multiply this total by the third. Display the answer as The answer is [answer]. 
x = int(input('Enter first  number: '))
y = int(input('Enter second number: '))
z = int(input('Enter third  number: '))
ans = ( x + y )*z
print('The answer is', ans)