'''Write a program using sys. Argv  that would depict the -name of the script -the number of the arguments and lastly the-list of the arguments used'''

import sys

lst=sys.argv
print("Name: ",lst[0])
print("Number of arguments: ",len(lst))
print("List of arguments: ")
for i in lst: print(i)
