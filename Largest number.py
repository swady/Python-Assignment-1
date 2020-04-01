n1 = int(input("enter first number"))
n2 = int(input("enter second number"))
n3 = int(input("enter last number"))

if n1 > n2 and n1 > n3:
    print("biggest number is: ",n2)
elif n2 > n3:
    print("biggest number is: ",n2)
else:
    print("biggest number is: ",n3)
