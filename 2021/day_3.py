def get_common_bit_at_index(bit_strings, index, should_get_most_common=True):
    counter = 0
    for bit_string in bit_strings:
            if bit_string[index] == '1':
                counter += 1
            else:
                counter -= 1
    if counter >= 0 and should_get_most_common:
        return '1'
    elif counter >= 0:
        return '0'
    elif should_get_most_common:
        return '0'
    else:
        return '1'


def calculate_binary_gamma_result(bit_strings):
    bits = []
    bit_length = len(bit_strings[0])

    for bit_index in range(bit_length):
        bits.append(get_common_bit_at_index(bit_strings, bit_index))
    return ''.join(bits)

def calculate_life_support_rating(bit_strings, should_get_most_common=True):
    bit_length = len(bit_strings[0])

    for index in range(bit_length):
        # Determine most common bit in current place.
        for bit_string in bit_strings:
            most_common_bit = get_common_bit_at_index(
                bit_strings,
                index,
                should_get_most_common,
            )

        # Filter by that bit
        bit_strings = list(
            filter(lambda x: x[index] == most_common_bit, bit_strings)
        )
        if len(bit_strings) == 1:
            return bit_strings[0]



def get_result():
    with open('day_3_input.txt', 'r') as f:
        lines = f.readlines()
        for idx, line in enumerate(lines):
            lines[idx] = line.strip()

    gamma_bits_1 = calculate_binary_gamma_result(lines)
    gamma_bits_2 = ''.join(
        [ '1' if val == '0' else '0' for val in gamma_bits_1]
    )

    gamma_integer_1 = int(gamma_bits_1, 2)
    gamma_integer_2 = int(gamma_bits_2, 2)

    gamma_result = gamma_integer_1 * gamma_integer_2

    oxygen_rating = int(calculate_life_support_rating(lines, True), 2)
    c02_rating = int(calculate_life_support_rating(lines, False), 2)

    life_support_rating = oxygen_rating * c02_rating

    return f'''gamma_result: {gamma_result} + \
            life_support_rating: {life_support_rating}'''

if __name__ == '__main__':
    print(get_result())

