'''
6. Create a list with the names of friends and colleagues. Search for the
name ‘John’ using a for a loop. Print ‘not found’ if you didn't find it.

'''

names=['Sagar','Suman','John','Jack']

for name in names:
	name=input('Search name: ')
	if name=='John':
		print('John')
	else:
		print('not found')