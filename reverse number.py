n=int(input('enter number: '))
sum=0
temp=n
while n!=0:
    r=n%10
    sum = sum*10+r
    n=n//10
print('reverse of given number is %d'        %(sum))
'''enter number: 5852
reverse of given number is 2585

Your output :
	enter number: 5852
reverse of given number is 2585

[Program finished]'''
