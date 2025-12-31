file=open("file -1.txt","r")
content=file.read()
file.close()
print(content)

file=open("file-2.txt","w")
file.write("hiiiii")
file.write("hellooo")
file.write("\nheyyy")
file.close()

file=open("file-3.txt","a")
file.write("\nThis is a new line.")
file.close()


with open("file-2.txt","r")as file:
    data=file.read()
    print(data)
#no need to close here

with open("sample.txt","w")as f:
    f.write("welcome to file handeling!")
    
with open("sample.txt","r") as f:
    print(f.read())

with open("file-2.txt","r") as file:
    lines=file.readlines()
print(lines)
m=[line.strip() for line in lines] #strip - to remove new lines
print(m)

p=[line.strip() for line in lines]
print(p)

with open("file-2.txt","r") as file2:
    lines=file2.readlines()
print(lines)
m=[line.strip() for line in lines]
print(m)
