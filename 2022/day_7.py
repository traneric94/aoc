class Directory:
    def __init__(self, name, parent=None):
        self.parent = parent  # Directory
        self.children_files = {}  # Files[]
        self.children_directories = {}  # Directories[]
        self.name = name
        self.size = 0

    # print current directory and children directories and files indented by level
    def __str__(self, level=0):
        ret = "\t" * level + f"{self.name}: {self.size}\n"
        for child in self.children_directories.values():
            ret += child.__str__(level + 1)
        for child in self.children_files.items():
            ret += "\t" * (level + 1) + f"{child[0]} {child[1]}\n"
        return ret


def create_dir_tree(lines):
    root = current = Directory('root')
    for line in lines:
        command = line.split()
        if command[0] == "$":
            # cd or ls
            if command[1] == "cd":
                if command[2] == "/":
                    current = root
                elif command[2] == "..":
                    current = current.parent
                else:
                    if command[2] in current.children_directories:
                        current = current.children_directories[command[2]]
                    else:
                        print('something went wrong, shouldve been caught at ls')

        elif command[0] == "dir":
            if command[1] not in current.children_directories:
                current.children_directories[command[1]] = Directory(
                    command[1], current)
            else:
                print('this should never happen')
        elif command[0].isdigit():
            current.children_files[command[1]] = int(command[0])

    return root


def day_one(directory_tree):
    dfs(directory_tree)
    result = count_directories(directory_tree)
    print(f"Day 1: {result}")


def dfs(node):
    result = 0

    if node is None:
        return 0

    for directory in node.children_directories.values():
        result += dfs(directory)

    for file in node.children_files.values():
        result += file

    node.size = result
    return result


def count_directories(node):
    result = 0
    if node is None:
        return 0
    for directory in node.children_directories.values():
        result += count_directories(directory)
        if directory.size < 100_000:
            result += directory.size
    return result


def day_two(directory_tree):
    file_system_size = 70000000
    free_space_required = 30000000
    current_space_used = directory_tree.size
    amount_to_delete = free_space_required - \
        (file_system_size - current_space_used)

    smallest = {'smallest': directory_tree}

    def find_smallest_directory(node):
        if node is None:
            return None

        for directory in node.children_directories.values():
            find_smallest_directory(directory)

        if node.size >= amount_to_delete and node.size < smallest['smallest'].size:
            smallest['smallest'] = node

    find_smallest_directory(directory_tree)
    print(f"Day 2: {smallest['smallest'].name}, {smallest['smallest'].size}")


if __name__ == "__main__":
    with open("day_7_input.txt") as f:
        lines = f.readlines()

    directory_tree = create_dir_tree(lines)
    day_one(directory_tree)
    print(directory_tree)
    day_two(directory_tree)
