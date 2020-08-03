#take a string as input and return a string with vowels removed.
'''s=input("enter a string ")
v='aeiouAEIOU'
lst=[x for x in s if x not in v]
s=''
for ele in lst:
    s += ele
print(s)'''

#Find common numbers from two lists using list comprehension
'''a=[int(x) for x in input("enter numbers:").split()]
b=[int(x) for x in input("enter numbers:").split()]
l=[x for x in a if x in b]
print(l)'''

#Compute the performance of list comprehension vs. for loop. So, you’ll be writing two functions and use the Python time module to measure their execution time
'''import time, decimal
t1=decimal.Decimal(time.time())
a=[x for x in range(11) if x%2==0]
t2=decimal.Decimal(time.time())
b=[]
t3=decimal.Decimal(time.time())
for x in range(11):
    if x%2==0:
        b.append(x)
t4=decimal.Decimal(time.time())
print(a)
print(b)
print("List: ", (t2-t1)*1000)
print("Loop: ", (t4-t3)*1000)'''


# Make a single list comprehension to return two lists, one for even and another for odd numbers
list_of_ints = range(1, 21)
oddNums = []
evenNums = []
def ListComp():
   # let's prepare the list comprehension
   return [x for x in list_of_ints if x%2 == 0 or oddNums.append(x)]
evenNums = ListComp()
# print list of even numbers and its size
print("Found {} even numbers: {}".format(len(evenNums), evenNums))
# print list of odd numbers and its size
print("Found {} odd numbers: {}".format(len(oddNums), oddNums))


#find even numbers from a list of lists of integers.
'''l=[[1,2,3],[4,5,6],[7,8,9]]
eve=[[i for i in x if i%2==0 ] for x in l]
print(eve)'''

#You have to print a list of all possible coordinatesgiven by i, j, k on a 3D grid where the sum of (i+j+k)  is not equal to N.
'''p,q,r,n=[int(x) for x in input("enter numbers:").split()]
l=[[i,j,k]for i in range (p+1) for j in range(q+1) for k in range(r+1) if i+j+k !=n]
print(l)'''
