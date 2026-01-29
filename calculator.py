print("simple calculator")
a=int(input("enter first number:")
b=int(input("enter second number:")
print ("1. add")
print("2. subtract")
print("3. multipy")
print("4. divide")
choice= input("enter choice (1/2/3/4):")
if choice =='1':
print("result:",a+b)
elif chocie =='2':
print("result:",a-b)
elif choice =='3':
print("result:",a*b)
elif choice =='4':
if b!=0:
print ("result:",a/b)
else:
print("cannot divide by zero ")
else:
print("invaild choice")
