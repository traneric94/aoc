class Directory:
    def __init__(self, parent=None):
        self.parent = parent  # Directory
        self.children_files = {}  # Files[]
        self.children_directories = {}  # Directories[]
        self.size = 0


def create_dir_tree(lines):
    root = current = Directory()
    for line in lines:
        command = line.split()
        if command[0] == "$":
            # cd or ls
            if command[1] == "cd":
                if command[2] == "/":
                    current = root
                if command[2] == "..":
                    current = current.parent
                else:
                    if command[2] not in current.children_directories:
                        current.children_directories[command[2]] = Directory(current)
                    else:
                        current = current.children_directories[command[2]]

        elif command[0] == "dir":
            if command[1] not in current.children_directories:
                current.children_directories[command[1]] = Directory(current)
        elif command[0].isdigit():
            current.children_files[command[1]] = int(command[0])

    return root


def day_one(directory_tree):
    def dfs(node):
        total = 0
        if node is None:
            return 0
        for directory in node.children_directories.values():
            total += dfs(directory)

        total += sum(node.children_files.values())

        node.size = total

        return total

    dfs(directory_tree)
    result = count_directories(directory_tree)
    print(f"Day 1: {result}")


def count_directories(node):
    result = 0

    if node is None:
        return 0

    for directory in directory_tree.children_directories.values():
        result += count_directories(directory)

    if directory.size > 100_000:
        result += 1

    return result


if __name__ == "__main__":
    with open("day_7_input.txt") as f:
        lines = f.readlines()

    directory_tree = create_dir_tree(lines)
    day_one(directory_tree)
