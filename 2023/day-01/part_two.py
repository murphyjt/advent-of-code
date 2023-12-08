table = {
    "0": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

with open('input.txt', 'r') as file:
    lines = file.readlines()
    running_sum = 0
    for line in lines:
        least = (len(line) + 1,)
        most = (0,)
        for key in table.keys():
            index = line.find(key)
            if index != -1 and index < least[0]:
                least = (index, key)
            index = line.rfind(key)
            if index != -1 and index >= most[0]:
                most = (index, key)
        running_sum += int(f"{table[least[1]]}{table[most[1]]}")
    print(running_sum)
