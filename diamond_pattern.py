
# diamond pattern program

list1 = ["*"]
rows = int(input("Enter number of rows: "))
list1 = ["*"]

space = rows - 1
while space >= 0:
 print(" "*space, *list1, sep = "")
 list1.append("*")
 list1.append("*")
 space = space - 1



'''i = 0
while i < rows*2-1:
 list1.append("*")
 i = i+1
print(*list1, sep = "")'''

temp = rows*2 - 1
while temp > 0:
 list1.insert(0," ")
 print(*list1[:temp-1], sep = "")
 temp = temp-1