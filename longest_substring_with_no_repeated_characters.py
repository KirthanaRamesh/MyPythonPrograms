
def is_longest(longest, sub_string):
    if len(longest) < len(sub_string):
        longest = sub_string
    return longest




def is_Substring(user_input_length, longest):
    #longest = "1"
    partial_result = "1"
    i = 0
    while i < user_input_length:
        j = i + 1
        flag = True

        while j < user_input_length:
            k = 1

            while k <= j:

                if k == j:
                    break

                if user_input_list[i] == user_input_list[i + 1]:
                    flag = False
                    break
                if user_input_list[i] == user_input_list[j]:
                    flag = False
                    break

                if user_input_list[i] != user_input_list[j]:

                    if user_input_list[k] == user_input_list[j]:
                        flag = False
                        break

                    elif user_input_list[k] != user_input_list[j]:
                        start = i
                        end = j
                        sub_string = ""
                        while start < end + 1:
                            sub_string = sub_string + "".join(user_input_list[start])
                            start = start + 1
                            partial_result = is_longest(partial_result, sub_string)

                            #if len(longest) < len(sub_string):
                              #  longest = sub_string
                        break

                k = k + 1

            if flag == False: break
            j = j + 1

        i = i + 1
    return(partial_result)



user_input = input("Enter a string: ")
#sub_string = ""
user_input_list = []

user_input_length = len(user_input)
longest = "1"
flag = True

for i in range(user_input_length):
    user_input_list.append(user_input[i])

result = is_Substring(user_input_length, longest)

if user_input == result: print("-1")
else: print(result)




