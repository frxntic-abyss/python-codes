file = open("Codingal.txt", "r")
counter = 0

Content = file.read()
coList = Content.split("\n")


for i in coList:
    if i:
           counter+=1

print("this is the number of lines in the file")
print(counter)