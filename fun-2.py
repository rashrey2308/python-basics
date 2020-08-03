'''Input a number x. Find whether the number is a special number or not.
A special number is a number composed of only prime digits. Print “True” if x is a special
number and “False” otherwise.'''

x=int(input("Enter a no."))
def special(n):
    while(n!=0):
        d=n%10
        if d==1 or d==4 or d==6 or d==8 or d==9 or d==0:
            return False
        n//=10
    return True
print(special(x))
