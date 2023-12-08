import re


# Example input
# Game 1: 4 green, 2 blue; 1 red

def is_above_threshold(text: str, color: str, threshold: int):
    matches = list(map(int, re.findall(f"(\\d+) {color}", text)))
    return max(matches) > threshold


with open('input.txt', 'r') as file:
    running_sum = 0
    game_id_prefix_len = len("Game ")
    for line in file.readlines():
        game_id = int(line[game_id_prefix_len:line.find(":")])
        if is_above_threshold(line, "red", 12):
            continue
        if is_above_threshold(line, "green", 13):
            continue
        if is_above_threshold(line, "blue", 14):
            continue
        running_sum += game_id
    print(running_sum)
