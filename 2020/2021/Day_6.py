class Group:
    def __init__(self, members):
        common_yes_answers = set(members[0])
        for member_answers in members[1:]:
           common_yes_answers.intersection_update(member_answers)

        self.group_yes = len(common_yes_answers)

        

    def accrue_yes_count(self):
        return self.group_yes.count(True)

groups = []
if __name__ == '__main__':
    # Process input
    with open('Day_6_input.txt', 'r') as f:
        lines = f.readlines();
        group_lines = []
        for idx, line in enumerate(lines):
            if line == '\n' or idx == len(lines) - 1:
                groups.append(Group(group_lines))
                group_lines = []
            else:
                group_lines.append(line.strip())

    yes_count = 0
    for group in groups:
        yes_count += group.group_yes
    print('Look mom I did it!', yes_count)
