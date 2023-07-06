"""
1. Countdown - Create a function that accepts a number as an input. Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element).
Example: countdown(5) should return [5,4,3,2,1,0]
"""
num = 100 # can be any number
def countdown(num):
	new_list = []
	if num < 0:
		return None
	for i in range(num, -1, -1):
		new_list.append(i)
	return new_list
print(countdown(num))

"""
2. Print and Return - Create a function that will receive a list with two numbers. Print the first value and return the second.
Example: print_and_return([1,2]) should print 1 and return 2
"""
a = 5
b = 2
x = [a, b]
def print_and_return(x):
	print(a)
	return b
print(print_and_return(x))

"""
3. First Plus Length - Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.
"""
def first_plus_length(list):
	return list[0] + len(list)
list1 = [5, 6, 1, 2, 3, 7]
print(first_plus_length(list1))

"""
4. Values Greater than Second - Write a function that accepts a list and creates a new list containing only the values from the original list that are greater than its 2nd value. Print how many values this is and then return the new list. If the list has less than 2 elements, have the function return False
Example: values_greater_than_second([5,2,3,2,1,4]) should print 3 and return [5,3,4]
Example: values_greater_than_second([3]) should return False
"""
def values_greater_than_second(list):
	new_list = []
	count = 0
	if len(list) < 2:
		return False
	i = 0
	while i < len(list):
		if list[i] > list[1]:
			new_list.append(list[i])
			count += 1
		i += 1
	print(count)
	return new_list

list2 = [4, 5, 6, 6]
list3 = [6, 5, 3, 1, 7]
print(values_greater_than_second(list2))
print(values_greater_than_second(list3))

"""
5. This Length, That Value - Write a function that accepts two integers as parameters: size and value. The function should create and return a list whose length is equal to the given size, and whose values are all the given value.
Example: length_and_value(4,7) should return [7,7,7,7]
Example: length_and_value(6,2) should return [2,2,2,2,2,2]
"""
def length_and_value(size, value):
	new_list = []
	i = 1
	while i <= size:
		new_list.append(value)
		i += 1
	return new_list
print(length_and_value(6, 12))