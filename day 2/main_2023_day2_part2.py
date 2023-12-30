import re

def extract_game_number(input_string):
    # Extracts the game number from the input string
    match = re.search(r'Game (\d+)', input_string)
    if match:
        return int(match.group(1))
    else:
        return None

def convert_input_string(input_string):
    # Converts the input string into a list of dictionaries
    game_data = input_string.split(': ')[1].split('; ')
    result = []
    for game in game_data:
        counts = {'r': 0, 'g': 0, 'b': 0}
        colors = re.findall(r'(\d+) (red|green|blue)', game)
        for count, color in colors:
            counts[color[0]] = int(count)
        result.append(counts)
    return result

def check_minimums(game_set, min_balls_needed):
    for color, count in game_set.items():
        if count > min_balls_needed[color]:
            min_balls_needed[color] = count
    return min_balls_needed

sum_of_products = 0
with open('input_day2_part1.txt', 'r') as file:
    lines = file.readlines()    # Read the input file
    for line in lines:
        min_balls_needed = {'r':0, 'g':0, 'b':0}    
        game_data = convert_input_string(line)  # Process each line using convert_input_string
        for game_set in game_data:  # Check each game set
            min_balls_needed = check_minimums(game_set, min_balls_needed)  # If any game set exceeds the limits, set all_game_set_true to False and break
        product = 1
        for count in min_balls_needed.values():
            product *= count
        sum_of_products += product
    print(sum_of_products)
        # Do something with the game_data   