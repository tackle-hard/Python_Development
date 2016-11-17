import fileinput
def sumArray():
	array1=[1,2,3,4]
	for  number in array1:
		print(number)

def sumInputDec():
	array=input('Input series of decimal numbers separated by comma  :  ').split(',')
	sum=0
	for number in array:
		sum+=float(number)

	print('the sum of the numbers is ', sum)

#Testing the range and how the variable effects for loop
def testRange():
	x=4
	for j in range(x):
		print(j)
		x=2


def main():
	#sumInputDec()
	#testRange()
	sumInputDec()

main()