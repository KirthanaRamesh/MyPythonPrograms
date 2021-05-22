
# Function for separating the integer and fraction part from the input decimal number.
def separation_of_integer_and_fraction():
    global decimal_number, decimal_integer, decimal_fraction
    decimal_integer = int(decimal_number)
    decimal_fraction = decimal_integer - decimal_number


# Function to convert integer part to binary.
def integral_to_binary_calculation():
    global decimal_number, decimal_integer, decimal_fraction
    global binary_integral

    while decimal_integer >= 1:
        remainder = decimal_integer % 2
        decimal_integer = decimal_integer // 2
        binary_integral.append(remainder)
    binary_integral.reverse()


# Function to convert fraction part to binary
def fraction_to_binary_conversion():
    global decimal_fraction, temp1, temp2
    global binary_fraction
    i = 0
    temp1 = decimal_fraction * 2
    while i < precision :
        temp2 = int(temp1)
        temp1 = temp2 - temp1
        #temp1 = temp1 - temp2
        #temp1 = temp1 - int(temp1)
        binary_fraction.append(abs(temp2))
        temp1 = temp1 * 2
        i = i + 1


# Getting input from the user
print("\nConversion of decimal number N into equivalent binary number up-to K precision after decimal point. ")

decimal_number = float(input("\nEnter decimal number, N: "))
precision = int(input("Enter K: "))

binary_integral = []
binary_fraction = ["."]

separation_of_integer_and_fraction()
integral_to_binary_calculation()
fraction_to_binary_conversion()

print("The equivalent binary number is ", *binary_integral, *binary_fraction, sep = "")








