# 006 Ask how many slices of pizza the user started with and ask how many slices they have eaten. Work out how many slices they have left and display the answer in a user-friendly format. 
slicesOrdered = int(input('Please tell me how many slices did you ordered? '))
slicesAte = int(input('Please tell me how many slices you alredy ate? '))
slicesRemaining = slicesOrdered - slicesAte
print('Slices still remaining in the plate are:', slicesRemaining )