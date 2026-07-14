def add(p,q):
    return p+q
def sub(p,q):
    return p-q
def multi(p,q):
    return p*q
def div (p,q):
    return p/q
print("select a opreation")
print("a.addition")
print("b.subtraction")
print("c.multiplication")
print("d.division")
choice=input("please enter a choice a/b/c/d:")
num1=int(input("enter your first number:"))
num2=int(input("enter your second number:"))
if choice=="a":
    print(num1,"+",num2,"=",add(num1,num2))
elif choice=="b":
    print(num1,"-",num2,"=",sub(num1,num2))
elif choice =="c":
    print(num1,"*",num2,"=",multi(num1,num2))
elif choice=="d":
    print(num1,"/",num2,"=",div(num1,num2))
else:
    print("invalid input")

