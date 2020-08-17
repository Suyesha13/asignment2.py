n=int(input("enter the numbers?"))
a=0
b = 1
count=0
if n<=0:
    print("the psotive number")
elif n==1:
    print("fibonacci sequence",n,":")
    print(a)
else:
    print("series:")
    while count<n:
        print(a)
        c=a+b
        a=b
        c=n
        count += 1
