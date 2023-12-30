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

def check_limits(game_set, limits):
    # Checks if the game set exceeds the limits
    for key, value in game_set.items():
        if value > limits.get(key, float('inf')):
            return True #limit is exceeded
    return False    #limit is not exceeded

limits = {'r':12, 'g':13, 'b':14}
sum_of_games = 0
with open('input_day2.txt', 'r') as file:
    lines = file.readlines()    # Read the input file
    for line in lines:
        game_data = convert_input_string(line)  # Process each line using convert_input_string
        all_game_set_true = True    # Assume all game sets are true
        for game_set in game_data:  # Check each game set
            if check_limits(game_set, limits):  # If any game set exceeds the limits, set all_game_set_true to False and break
                all_game_set_true = False   
                break   
        if all_game_set_true:   # If all game sets are true, add the game number to sum_of_games
            sum_of_games += extract_game_number(line)
            
            
    print(sum_of_games)
        # Do something with the game_data   