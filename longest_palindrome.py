# Program to find the longest Palindrome in the given string.

# Function to check palindrome
def isPalindrome(string, start, end):
    if string[start:end + 1] == string[end:start - 1:-1]:
        return True, string[start:end + 1]

# Function to find the longest palindrome
def isLongest(result, longest):
    if len(longest) > len(result): return longest
    else: return result



# Getting user input
print("Finding the longest Palindrome in the given string")
input_string = input("Enter string:")
string = "0" + input_string + "0"
length = len(string)
result = "a"
result = tuple(result)
longest = str("1")
start = 1
while start <= length - 2:
    end = length - 2
    while end >= start:
        if string[start] != string[end]:
            pass
        else:
            result = isPalindrome(string, start, end)
            if result:
                longest = isLongest(result[1], longest)

        end = end - 1
    start = start + 1
print(longest)
