import fileinput
#Program reads 3 number and displays the larget odd
#If no number is odd print a message "No Odds"

#Input 3 numbers
FLAG=False
largest=0
oddFound=False
while FLAG==False:

	arr = input("Enter 3 numbers separated by Space")
	arr = arr.split(' ')
	if len(arr)==3:
		FLAG=True
		index=len(arr)-1

#Processing
while index>0:
	if int(arr[index])%2==1:
		oddFound=True
		if int(arr[index])>largest:
			largest=int(arr[index])
	index-=1

if oddFound==True:
	print('The largest Odd number is   ',largest)

else:
	print('No Odd Found')

