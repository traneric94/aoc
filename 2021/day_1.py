import time

def get_result():
    with open('day_1_input.txt', 'r') as file:
        lines = file.readlines()
        result = 0
        i = 3
        while i < len(lines):
            current_sum = int(lines[i]) + int(lines[i-1]) + int(lines[i-2])
            previous_sum = int(lines[i-3]) + int(lines[i-1]) + int(lines[i-2])
            if current_sum > previous_sum:
                result += 1
            i += 1
    return result

if __name__ == '__main__':
    print(get_result())
