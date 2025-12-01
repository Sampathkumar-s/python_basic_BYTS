a=int(input("Enter a number1: "))
b=int(input("Enter a number2: "))
c=int(input("Enter a number3: "))
d=int(input("Enter a number4: "))
e=int(input("Enter a number5: "))

tot = (a+b+c+d+e)/5

print("Your total is:",tot)

if tot>=50 and tot<=60:
    print("Your grade is D")
elif tot>=60 and tot<=70:
    print("Your grade is C")
elif tot>=70 and tot<=80:
    print("Your grade is B")
elif tot>=80 and tot<=90:
    print("Your grade is A")
elif tot>=90 and tot<=100:
    print("Your grade is O")
else:
    print("Your grade is U")
