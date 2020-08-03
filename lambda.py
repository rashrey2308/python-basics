'''Given a number n, generate a list of the first n fibonacci numbers,  being the first number. Then, apply the map function and a lambda expression to square each fibonacci number and print the list.'''

n=int(input("Enter a number between 0 to 20:"))
assert(n>=0 or n<=20),"number should be between 0 and 20"
l=[]
l.append(0)
l.append(1)
for i in range(2,n):
    f=l[i-1]+l[i-2]
    l.append(f)
print(l)
l=list(map(lambda x:x**2,l))
print(l)
