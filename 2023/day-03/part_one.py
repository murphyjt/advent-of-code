class Node:
    def __init__(self, value: int, start: int, end: int):
        self.value = value
        self.start = start
        self.end = end
        self.visited = False

    def visit(self):
        self.visited = True


def print_info(node_list: list[list[Node]]):
    count = 0
    total = 0
    for row in node_list:
        elements = list(map(lambda x: x.value, row))
        # print(elements)
        for number in elements:
            count += 1
            total += number
    print(f"Sum of {count} numbers: {total}")


def build_node_list(lines: list[str]) -> list[list[Node]]:
    """
    Scan each line for numbers and add to node_list.
    Pretty certain this part works correctly.
    """
    node_list: list[list[Node]] = []
    for row, line in enumerate(lines):
        nodes = []
        value = ""
        start = -1
        end = -1  # Doesn't need to be reset, will always be updated
        for pos, char in enumerate(line):
            if char.isdigit():
                value += char
                if start == -1:
                    start = pos
                end = pos
            elif start != -1:  # char is not a digit and there's an uncommitted node
                nodes.append(Node(int(value), start, end))
                value = ""
                start = -1
        node_list.append(nodes)
    return node_list


class Color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


def visit_nodes(lines, node_list):
    # Scan symbols and visit adjacent numbers
    for row, line in enumerate(lines):
        for pos, char in enumerate(line):
            # UGH, took me forever to realize \n was being counted as a symbol :unamused:
            if (not char.isdigit()) and char != "." and char != "\n":
                if row > 0:
                    for node in node_list[row - 1]:
                        if node.start - 1 <= pos <= node.end + 1:
                            node.visit()
                for node in node_list[row]:
                    if pos == node.start - 1 or pos == node.end + 1:
                        node.visit()
                if row < len(lines) - 1:
                    for node in node_list[row + 1]:
                        if node.start - 1 <= pos <= node.end + 1:
                            node.visit()
        # print(f"{line_no + 1}: {[(node.value, node.visited) for node in row]}")


def debug(node_list, line_len):
    for line_no, row in enumerate(node_list):
        line_length = 0
        while line_length < line_len:
            for node in row:
                print("." * (node.start - line_length), end="")
                line_length += node.start - line_length
                line_length += node.end - node.start + 1
                if node.visited:
                    print(f"{Color.RED}{node.value}{Color.END}", end="")
                else:
                    print(node.value, end="")
            print("." * (line_len - line_length), end="")
            line_length += (line_len - line_length)
        print("")


def flatten(matrix: list[list[any]]):
    return [item for row in matrix for item in row]


def main():
    with open('input.txt', 'r') as file:
        lines = file.readlines()
    node_list = build_node_list(lines)
    # print_info(node_list)
    visit_nodes(lines, node_list)
    # Assumes a square grid
    debug(node_list, line_len=len(lines))
    running_sum = 0
    count = 0
    for node in flatten(node_list):
        if node.visited:
            count += 1
            running_sum += node.value
    print(f"Sum of {count} numbers: {running_sum}")


if __name__ == "__main__":
    main()
