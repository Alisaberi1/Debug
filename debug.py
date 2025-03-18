given_number = int(input())  # Input the number
given_number_string = str(given_number)  # Convert the number to a string

all_digits = []
for i in given_number_string:
    all_digits.append(int(i))  # Convert each digit to an integer and append

while len(all_digits) > 1:  # Repeat until there's only one digit
    sum_of_digits = 0  # Reset sum_of_digits to 0 for each iteration
    
    for i in all_digits:  # Sum all digits in the list
        sum_of_digits += i
    
    # Update all_digits with the digits of the new sum
    all_digits = [int(d) for d in str(sum_of_digits)]

# Print the final single-digit result
print(all_digits[0])
