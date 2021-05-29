


def is_Substring():
    i = 0
    while i < user_input_length + 1:
        j = i + 1
        counter = 1
        break_counter = 0
        while j < user_input_length:
            if user_input[i] != user_input[j]:
                counter = counter + 1
                pass
            elif user_input[i] == user_input[j]:
                break_counter = j
                counter = 0
                break
            j = j + 1
        i = i + 1







def isLongest(result, longest):
    if len(longest) > len(result): return longest
    else: return result




user_input_list = []
user_input = input("Enter the string: ")
user_input_length = len(user_input)
#print(user_input)

result = "a"
longest = str("1")


'''# To store the input string in list
user_input_length = len(user_input)
for i in range(user_input_length):
    user_input_list.append(user_input[i])
print(user_input_list)'''




#substring1 = user_input[counter - counter: break_counter]
#print(substring1)
