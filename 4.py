'''

Create a list. Append the names of your colleagues and friends to it.
Has the id of the list changed? Sort the list. What is the first item on
the list? What is the second item on the list?

'''

alist=['bibash','yogesh','saadheet']

# id before appending list
print(id(alist))

alist.append('sagar')

# id after append on list
print(id(alist))

# sorted list
print(sorted(alist))

# first item
print(alist[0])

# second item
print(alist[1])