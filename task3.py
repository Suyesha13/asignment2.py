print("Program for positive values from list")
n=eval((input("enter numbers :")))
a=[]
for i in range (0,n):
    a.append(int(input()))
    print("The list contain ",a)
for j in a:
    if j>=0:
        print(j, end=" ")
    else:
        ("no psoitive numbers")
