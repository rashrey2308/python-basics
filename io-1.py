'''Input and Output FunctionsQuestion:Write a program to input your name, and your marks in 3 subjects. Display the marks with your name, as shown in the sample output. Do not use more than 2 input statements in your program.Sample Input: Enter your name: AnitaEnter your marks: 80,70,60Sample Output: Anita, your marks are [80,70,60]'''
n=input("Enter name:")
l=[int(x) for x in input("Enter your marks:").split()]
print(n,", your marks are ",l)
