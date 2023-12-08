import re


# Example input
# Game 1: 4 green, 2 blue; 1 red

def min_req(text: str, color: str):
    return max(list(map(int, re.findall(f"(\\d+) {color}", text))))


with open('input.txt', 'r') as file:
    running_sum = 0
    for line in file.readlines():
        running_sum += min_req(line, "red") * min_req(line, "green") * min_req(line, "blue")
    print(running_sum)
