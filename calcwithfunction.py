def add(a,b):
    print(a+b)
def sub(a,b):
    print(a-b)
def mul(a,b):
    print(a*b)
def div(a,b):
    print(a/b)
def mod(a,b):
    print(a%b)
def fdiv(a,b):
    print(a//b)

print(''' 
      1. addition
      2. subraction
      3.multiplication
      4.division
      5. modulus
      6.floor division
      7. exponent''')

a = int(input("Enter a number: "))
b = int(input("ENter a number: "))
c = input("Enter a number(1-7): ")

if c=="1":
    add(a,b)
elif c=="2":
   sub(a,b)
elif c=="3":
    mul(a,b)
elif c=="4":
    div(a,b)
elif c=="5":
    mod(a,b)
else:
    fdiv(a,b)