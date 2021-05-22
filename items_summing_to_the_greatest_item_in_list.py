


# Function to find out the pair that sums up to the largest item
def find_pair():
    i = 0
    while i < list_length:
        #flag = False
        j = 1
        while j < list_length - 1:
            if i == j: break
            temp = input_list[i] + input_list[j]
            if largest_item == temp:
                flag = True
                print_statement ="The pair of items that return the largest item is {} and {} "
                print(print_statement.format(input_list[i],input_list[j]))
                break
            j = j+1
        else: flag = False
        i = i+1
    if flag == False:
        print("No such pair exists in the list")

#User input
print("Returns the pair of items in a list that sums up to the greatest element in that list.")
input_list = input("\nEnter the items in the list separated by comma: ")
input_list = input_list.split(",")
input_list = [float(item) for item in input_list]

input_list.sort(reverse=True)
largest_item = input_list[0]
print_statement1 = "{} is the largest item in the list"
print(print_statement1.format(largest_item))
list_length = len(input_list)

find_pair()





