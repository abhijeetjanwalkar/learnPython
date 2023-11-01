# 009 Write a program that will ask for a number of days and then will show how many hours, minutes and seconds are in that number of days.
numberOfDays = int(input('Enter number of days: '))
numberOfHours = numberOfDays * 24
numberOfMinutes =  numberOfHours * 60
numberOfSeconds = numberOfMinutes * 60
print('You provided', numberOfDays, 'that is: ', numberOfHours, 'hours or', numberOfMinutes, 'minutes or', numberOfSeconds, 'seconds')