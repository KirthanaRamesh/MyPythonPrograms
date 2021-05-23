rows = int(input("Enter the number of rows: "))
# version control software
#testing

list1 = ["*"]
i = 1
while i < rows:
    print(*list1, sep="")
    list1.append("*")
    i = i + 1

i = rows
while i > 0:
    print(*list1, sep = "")
    list1.pop()
    i = i - 1
