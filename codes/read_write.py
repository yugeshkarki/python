#  to write a file
str=input("enter the text")

f=open("myfile.txt","w")
f.write(str)

f.close()

# to read file
f=open("myfile.txt","r")
data=f.read()
print(data)
f.close()

#  to Append a file
str=input("enter the text")

f=open("myfile.txt","a")
f.write(str)

f.close()