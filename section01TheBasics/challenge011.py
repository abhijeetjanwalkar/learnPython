# 011 Task the user to enter a number over 100 and then enter a number under 10 and tell them how many times the smaller number goes into the larger number in a user-friendly format. 
over100 = int(input('Enter number over 100: '))
under10 = int(input('Enter number under 10: '))
goesInto = over100 // under10
print('The number', under10, 'goes', goesInto, 'times in', over100 )