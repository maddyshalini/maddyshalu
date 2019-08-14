x,y,z=input("enter number:").split()
if(x>y)and(x>z):
    print(x,"is greatest number")
elif(y>z)and(y>x):
    print(y,"is greatest number")
else:
    print(z,"is the greatest number")
