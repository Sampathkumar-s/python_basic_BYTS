print(''' 
      1. addition
      2. subraction
      3.multiplication
      4.division
      5. modulus
      6.floor division
      7. exponent''')


c=input("Enter a chouice(1-7): ")
a=int(input("Enter the number: "))
b=int(input("Enter the number: "))

match (c):
    case "1": print("addition: ",a+b)
    case "2": print("subraction: ",a-b)
    case "3": print("multiplicaiton: ",a*b)
    case "4": print("division: ",a/b)
    case "5": print("modulus: ",a%b)
    case "6": print("floor division: ",a//b)
    case "7": print("exponent: ",a**b)
    case _:   print("Entered the Wrong number")
    
    #a if (a > b and a > c) else b if (b > c and b > a) else c
    #a if (a > b and a > c) else b if (b > c) else c

