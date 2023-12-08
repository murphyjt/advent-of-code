
with open('input.txt', 'r') as file:
    lines = file.readlines()
    running_sum = 0
    for line in lines:
        first = -1
        for char in line:
            if '0' <= char <= '9':
                if first == -1:
                    first = char
                last = char
        running_sum += int(f"{first}{last}")
    print(running_sum)
