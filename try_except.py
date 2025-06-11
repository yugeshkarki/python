#// try except format
#  try: 
#     a=int(input("enter the number"))
#     print(a)
# except Exception as e:
#     print(e)

# print("THANK YOU")

#// raisisng EXCEPTION

a= int(input("enter the number :"))
b= int(input("enter the number :"))
if(b==0):
    raise ZeroDivisionError("program is not for divide a number by zero")
else:
    print(f"the division a/b is : {a/b}")