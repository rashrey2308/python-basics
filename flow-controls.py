'''Anna likes to draw right angled triangles. She recently learnt how to code in Python, and she is curious to see if it can be used to print the same. You need to help her out by writing a program which takes an input number n from the user and prints a right angled triangle of height n. Anna also wants that the triangle should display the respective line numbers if the line number is odd (1st, 3rd, 5th… line), and censor out the even numbered lines (2nd, 4th, 6th… line) using the hash (‘#’) symbol.

Note: 1 ≤ n ≤ 10'''

n=int(input("Enter a number b/w 1-10:"))
assert(n<11 and n>0),"number should be between 1-10"
for i in range(1,n+1):
    for j in range(i,n):
        print(" ", end=" ")
    for k in range(i):
        if i%2==0:
            print("#", end=" ")
        else:
            print(i, end=" ")
    print()
