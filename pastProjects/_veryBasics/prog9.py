# data structures: lists in python
# a list is a ordered collection of data
# a list in python can contain elements of any data type
# basics

# indexing, slicing, indexing in indexing, etc stuff can be done with lists

# printing the whole list displays all its elements in order
nums = [1, 2, 3, 4]
print(nums)

words = ["aviral", "srivastava", 'studies', 'in', 'class 12']
print(words)

mixed = [1, 2, 3, 4, "a", "srivastava", None]
print(mixed)

# example of indexing in python lists
print(mixed[1])

# example of slicing in python lists
print(words[0: 3])

# example of nested indexing...
# here, the line below prints out the character at 0th index of the word at...
# ...3rd index in the list named 'words'
print(words[3][0])

# lists are mutable
mixed[1] = 'two'
print(mixed)

# NOTE: SEE THIS
mixed[1:] = ["Harshir", "Vashishth"]
print(mixed)

# AND ALSO THIS:

mixed[1:] = "Harshit"
print(mixed)

# Adding data to the list -
# There are three methods to add data to list:

mylist = [1, 'two', 3, 'four', 5.0]

# append() method is used to add new data item to the end of the list
mylist.append("six")

# lists can also be concatenated using the + operator
list1 = ['a', 'b', 'c', 'd']
list2 = ['e', 'f', 'g', 'h']
list3 = list1 + list2
# now the list3 = [a, b, c, d, e, f, g, h]
print(list3)

# alternative method to get result as the + operator is extend() method
list1.extend(list2)
# this method extends one list. So we don't require any third variable
# so now, list1 = [a, b, c, d, e, f, g, h]
print(list1)

# Here, we could also have used the append() method,
# but it produces a different output -
list1.append(list2)
# this adds the whole list2 as one item at the endof list1
# so this is the case of 'list inside a list'
print(list1)

# Now let's see some methods to delete data from our list
# Here also there are three methods possible -

list1 = ['a', 'b', 'c', 'd']

# pop() method deleted the last item by defalut when no argument is passed
list1.pop()
print(list1)
# when a index is passed to pop() as an arg., it deletes the data at that index
list1.pop(1)
print(list1)

# 'del' operator can also be used to do deletion
del list1[1]
print(list1)

list1 = ['a', 1, 'b', 2, 'c', 3, 'b', 'b']

# the last method to do the task of deletion is using the remove() function
print(list1)
# remove() is used when we don't know the index of element to be deleted
# the value of data item that has to be deleted is passed as an argument
# then it deletes the first occurance of the specified data, if found ...
# otherwise throws an error of item not found.list1
list1.remove('b')
print(list1)

# Other lists related functions

list1 = ['a', 1, 'b', 2, 'c', 3, 'b', 'b']

# count() function counts the number of occurances of the specified item
print(list1.count("b"))

new_list = ["avi", "loves", "to", "program", "in", "python"]

# sort() function sorts the list in increasing / alphabetical orderorder
new_list.sort()
print(new_list)

# sorted() function is used to only temporarily sort the list
# it is unlike the sort() function which permanently sorts the list
# no changed are made actually to the list.
new_list = ["avi", "loves", "to", "program", "in", "python"]
print(sorted(new_list))
print(new_list)

# clear() function is used to empty a list
new_list.clear()
print(new_list)

# to assign a duplicate of a list to another list, copy() function is used
avi_list = ["avi", "loves", "to", "program", "in", "python"]
dup_list1 = avi_list
dup_list2 = avi_list.copy()

print(avi_list)
print(dup_list1)
print(dup_list2)

# in the above code, we have created two lists that look like avi_list
# dup_list1 has been created by the '=' operator, whereas,
# dup_list2 has been created by the copy() function
# NOTE: When we assign by the '=' operator, then the list at LHS and RHS
# share the same memory location in RAM
# But by the use of copy() function, a different list is created with the same
# elements as the avi_list

# This can be proved by the following code:

# Comparison by '==' is done by comparing that do the lists contain the same
# elements in the same order or not.
# Where as, comarison by 'is' keyword is done by python by checking if the
# operands share the same memory location / plot or not.

print(dup_list1 == avi_list)    # true
print(dup_list2 == avi_list)    # true
print(dup_list1 == dup_list2)    # true

print(dup_list1 is avi_list)    # true, as assignment is done by the = operator
print(dup_list2 is avi_list)    # false
print(dup_list1 is dup_list2)    # false

# split() is used to convert a string to list
# join() method is used to convert a list to string

user_info = "Aviral 18".split()
# when no argument is passed, by default the string breaks into lists at spaces
print(user_info)

# argument specifying the breakpoint char can be passed to the split() function
user_info = "Aviral:Srivastava".split(':')
print(user_info)

# join() method does the opposite of what split() does
user_info = ["Avi", "Sri"]
# the following code joins the elements of the list seperated by a '-'
print('-'.join(user_info))
