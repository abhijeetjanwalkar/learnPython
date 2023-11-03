# 013 Ask the user to enter a number that is under 20. If they enter a number that is 20 or more, display the message “Too high”, otherwise display “Thank you”. 
x = int(input('Enter your number under 20: '))
if x >= 20:
    print('Too High') 
else:
    print('Thanks you')