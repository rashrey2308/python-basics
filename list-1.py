'''Input a list of integers containing both positive and negative numbers.
You have to print a list in which all the negative integers of this list are replaced by their
squares and all the positive numbers are left as it is.'''

l=[int(x) for x in input("Enter a few numbers ").split()]
print(l)
l=[y*y if y<0 else y for y in l]
print(l)
