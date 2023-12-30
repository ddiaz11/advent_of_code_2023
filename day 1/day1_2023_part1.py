# If the line only has 1 digit, digits[0] = digits[-1]
def extract_number(string):
    digits = [char for char in string if char.isdigit()]
    return int(''.join([digits[0], digits[-1]]))

with open('input_part1.txt', 'r') as file:
    lines = (line.strip() for line in file)
    extracted_values = [extract_number(line) for line in lines]
    sum_of_values = sum(extracted_values)
print(sum_of_values)