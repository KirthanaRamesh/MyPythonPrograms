
# To generate a random 4 digit code
import random
four_digit_code = ["0", "0", "0", "0" ]
temp = random.randint(1000, 100000)
string_temp = str(temp)

for index in range(4):
    four_digit_code[index] = string_temp[index]
    four_digit_code[index] = int(four_digit_code[index])
print(four_digit_code)

# Function to check if the guessed number matches the original 4 digit code
def calculate():
    always_right_list = ["R","R","R","R"]
    while True:
        try:
            guess_code = int(input("Enter your 4 digit guess code: "))
        except ValueError:
            print("Please enter a 4 digit number.")

        else:
            string_guess_code = str(guess_code)
            if len(string_guess_code) != 4:
                print("Please enter a 4 digit number.")
            else: break
    quotient = 1
    my_bool = False
    flag = 0
    # To store the user input in list
    while quotient > 0:
        quotient = guess_code // 10
        remainder = guess_code % 10
        list_guess_code.append(remainder)
        guess_code = quotient
    list_guess_code.reverse()

    # Logic for checking if the guess made by the user is correct
    # Logic to check - correct number, wrong position
    j = 0
    while j < 4:
        i = 0
        while i < 4:
            if list_guess_code[j] == four_digit_code[i] :
                temp_list[j] = "Y"
                break
            elif list_guess_code[j] != four_digit_code[i]:
                temp_list[j] = "B"
            i = i + 1
        j = j + 1

    # Logic to check - correct number, correct position
    k = 0
    while k < 4:
        if list_guess_code[k] == four_digit_code[k] :
            temp_list[k] = "R"
        k = k + 1

        if temp_list == always_right_list:
            print("Congrats!! You guessed the 4 digit code right.")
            my_bool = True
            break
    print(temp_list)
    return my_bool

# This function will be called when the user selects level easy
def level_easy(bool):
    check = 0
    for guess in range(1,16):
        print('\nChance ' + str(guess))
        my_output = calculate()
        if my_output == True:
            check = 1
            break
    if check == 0:
        print("Sorry! You weren't able to guess the 4 digit code")
        print("The 4 digit code is", end = " ")
        print(four_digit_code)

# This function will be called when the user selects level intermediate
def level_intermediate(bool):
    check = 0
    for guess in range(1,8):
        print('\nChance ' + str(guess))
        my_output = calculate()
        if my_output == True:
            check = 1
            break
    if check == 0:
        print("Sorry! You weren't able to guess the 4 digit code")
        print("The 4 digit code is", end=" ")
        print(four_digit_code)

# This function will be called when the user selects level hard
def level_hard(bool):
    check = 0
    for guess in range(1,6):
        print('\nChance ' + str(guess))
        my_output = calculate()
        if my_output == True:
            check = 1
            break
    if check == 0:
        print("\nSorry! You weren't able to guess the 4 digit code")
        print("The 4 digit code is", end=" ")
        print(four_digit_code)


# Main code
print("\nLow Level Implementation of Mastermind Game\n")

print("Instructions")
print("\t1) There are 3 levels of difficulty. ")
print("\t2)In each level of difficulty, you will have to guess the correct 4 digit code within the specified number of chances.")
print("\t3)Notations and their meaning")
print("\t\tR - Number is correct. Position is correct. ")
print("\t\tY - Number is correct. Position is wrong. ")
print("\t\tB - Number is wrong. Position is wrong. ")




list_guess_code = []
temp_list = ["B","B","B","B"]
bool = False

print("\nSelect Your Difficulty Level")
print("\t1. Easy (15 chances) \n \t2. Intermediate (7 chances) \n \t3. Hard (5 chances)\n")
while True:
    try:
        choice = int(input("Enter the difficulty level (corresponding serial number): "))
    except ValueError:
        print("Please enter valid option.")
        continue
    else:
        if choice > 3 or choice == 0: print("Please enter valid option.")
        else: break


if choice == 1: level_easy(bool)
elif choice == 2: level_intermediate(bool)
elif choice == 3: level_hard(bool)











