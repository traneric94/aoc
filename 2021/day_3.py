
def calculate_binary_gamma_result(is_most_frequent=False):
    with open('day_3_input.txt', 'r') as f:
        lines = f.readlines()
        counter = { index: 0 for index, _ in enumerate(lines[0].strip())}
        for line in lines:
            for index, bit in enumerate(line.strip()):
                if bit == '1':
                    counter[index] += 1
                else:
                    counter[index] -= 1
        print(counter)
        if is_most_frequent:
            gamma_rate = [ '1' if value > 0  else '0' for value in counter.values()]
        else:
            gamma_rate = [ '1' if value < 0  else '0' for value in counter.values()]
        return gamma_rate

def get_result():
    gamma_bits_1 = calculate_binary_gamma_result(True)
    gamma_bits_2 = calculate_binary_gamma_result(False)

    gamma_integer_1 = int(''.join(gamma_bits_1), 2)
    gamma_integer_2 = int(''.join(gamma_bits_2), 2)

    return gamma_integer_1 * gamma_integer_2

if __name__ == '__main__':
    print(get_result())

