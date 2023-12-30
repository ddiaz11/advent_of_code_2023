import re

def extract_digits(input_string):
    # Mapping of number words to digits
    num_dict = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }

    digits = []
    temp = ''
    for char in input_string:
        if char.isdigit():
            # If the character is a digit, add it to the list
            digits.append(int(char))
        elif char.isalpha():
            # If the character is a letter, add it to the temporary string
            temp += char
            if re.fullmatch("|".join(num_dict.keys()), temp):
                num = num_dict[temp]
                
                
   
            for i in range(len(temp)):
                if temp[i:] in number_words:
                    # If a substrin0g is a number word, convert it to a digit and add it to the list
                    digits.append(number_words[temp[i:]])
                    temp = temp[:i]
    if digits:
        return join_list_elements([digits[0], digits[-1]]), None  # Return number and no error flag
    return None, "No digits found in the string"  # Return None for number and error message

def join_list_elements(list):
    # Convert the integers to strings and join them
    str_num = ''.join(map(str, list))
    # Convert the string back to an integer
    num = int(str_num)
    return num

def check_for_numbers(input_string):
    number_words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    # Check if any number word is present in the input string
    for word in number_words:
        if word in input_string:
            return True

    return False


try:
    with open('input_part2.txt', 'r') as file:
        lines = (line.strip() for line in file)
        extracted_values = [extract_digits(line) for line in lines]
        errors = [error for _, error in extracted_values if error]
        sum_of_values = sum(result for result, _ in extracted_values if not _)
    print(sum_of_values)

except FileNotFoundError:
    print("File not found.")
except ValueError as e:
    print(f"A value error occurred: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    file.close()  # Ensures file closure even if an exception occurs
