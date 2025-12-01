a=int(input("Enter a number1: "))
b=int(input("Enter a number2: "))
c=int(input("Enter a number3: "))
d=int(input("Enter a number4: "))

sum = "a" if (a>b and a>c and a>d) else "b" if(b>c and c>d) else "c" if (c>d) else "d"

print(f"largest number is {sum}")
