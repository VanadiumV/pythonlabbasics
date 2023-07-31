def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y

print("enter choice")
print("a.add")
print("b.subtract")
print("c.mul")
print("d.div")

choice=input("Please enter choice(a/b/c/d):")

n1=int(input("enter 1st number"))
n2=int(input("enter 2nd number"))

if choice=='a':
    print(n1,"+",n2,"=",add(n1,n2))
elif choice=='b':
     print(n1,"-",n2,"=",subtract(n1,n2))
     elif choice=='c':
     print(n1,"*",n2,"=",mul(n1,n2))
     elif choice=='d':
     print(n1,"/",n2,"=",div(n1,n2))

     
