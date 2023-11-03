# 014 Ask the user to enter a number between 10 and 20 (inclusive). If they enter a number within this range, display the message “Thank you”, otherwise display the message “Incorrect answer”. 

x = int(input('Enter number between 0 to 20: '))
if (x<=20 and x>=0):
    print('Thank you')
else:
    print('Incorrect answer')