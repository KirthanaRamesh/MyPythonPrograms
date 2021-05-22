import datetime
import time



# Function to calculate age
def age_calculation():
    current_date = datetime.datetime.now()

# Calculation for years
    age_year = current_date.year - dob.tm_year
    string_age_year = str(age_year)

# Calculation for months
    if current_date.month < dob.tm_mon:
        temp_month = dob.tm_mon - current_date.month
    else:
        temp_month = current_date.month - dob.tm_mon
    x = temp_month + 1
    age_month = 12 - x
    string_age_month = str(age_month)

    print("Hello " + username + "! You are " + string_age_year + "years " + string_age_month + " months old.")
    print("You are Major.") if age_year > 17 else print("You are Minor.")

# User input
username = input("Enter your name: ")
string_dob = input("Enter Date of Birth (YYYY-MM-DD): ")
dob = time.strptime(string_dob,"%Y-%m-%d")

age_calculation()







