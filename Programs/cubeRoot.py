import fileinput

# Read a integer

number=int(input('Enter an integer  : ')

anumber=abs(number)

ans=0

while (ans**3 < anumber):
	ans+=1

if number<0 :
	ans=-(ans)
if (ans**3 == number):
	print('The cube root of ',number, '  is ' , ans)

else:
	print('The number isnt a perfect cube')