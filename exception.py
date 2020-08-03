pass1=input("enter your password ")

s=len(pass1)
try:
    assert(s>=8), "Must be greater than 7"
except AssertionError as obj:
    print(obj)
else:
    print("Saved!")
