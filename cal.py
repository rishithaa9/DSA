def addition(x,y):
    return x+y

def sub(x,y):
    return x-y
def mul(x,y):
    return x*y

def div(x,y):
    if x| y==0:
        return "error"
    else:
        return x/y
    
print('1')
print('2')
print('3')
print('4')
choice=input("1/2/3/4: ")
num1=float(input("Enter number 1: "))
num2=float(input("Enter number 2: "))

if choice == "1":
    print(addition(num1,num2))
elif choice=="2":
    print(sub(num1,num2))
elif choice =="3":
    print(mul(num1,num2))
elif choice =="4":
    print(div(num1,num2))

