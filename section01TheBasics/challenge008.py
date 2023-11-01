# 008 Ask for the total price of the bill, then ask how many diners there are. Divide the total bill by the number of diners and show how much each person must pay.
bill = int(input('What is the bill amount?'))
guests = int(input('How many guests were there?'))
perGuestBill = bill / guests
print('Per person bill is: ', perGuestBill)