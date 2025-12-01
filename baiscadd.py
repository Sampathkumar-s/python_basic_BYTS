print(''' 
      1. addition
      2. subraction
      3.multiplication
      4.division
      5. modulus
      6.floor division
      7. exponent''')

1
c=input("Enter a chouice(1-7): ")
a=int(input("Enter the number: "))
b=int(input("Enter the number: "))

if c=="1":
    print("addition: ",a+b)
elif c=="2":
    print("subration: ",a-b)
elif c=="3":
    print("multiplication: ",a*b)
elif c=="4":
    print("division: ",a/b)
elif c=="5":
    print("modulus: ",a%b)
elif c=="6":
    print("floor division: ",a//b)
else:
    print("exponent: ",a**b)