x=int(input("Enter a first number: "))
y=int(input("Enter a second number: "))
try:
    z=x/y
    print("Division result",z)
except Exception as e:
    print(e)
finally:
    print("finally")